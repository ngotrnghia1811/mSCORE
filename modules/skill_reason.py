import os, sys, json
import argparse
import time
import tqdm
import numpy as np
import pandas as pd

import torch
import transformers

from utils import *
from config.prompt.templates import *

if openai.api_key is None:
    from config import config
    openai.api_key = config['api_key']



import os
import re
import json
import torch
import openai
import tiktoken
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
from config.prompt.templates import *

# Load OpenAI API configuration
from config import config

if openai.api_key is None:
    openai.api_key = config['api_key']

class SkillReason:
    def __init__(self, **kwargs):
        self.llm = _SkillReason(**kwargs)

    def eval(self, dataset_split):
        pass

    def process_context(self, gen_dataset, dataset_split):

    def generate(self, question, options, template_name="standard_inference", return_messages=False):
        
        gen_dataset = prepare_dataset_from_ids(gen_dataset, dataset_split)
    
        generation_start = time.time()

        questions, instructions, predictions, references = self.llm.generate(gen_dataset)  

        self.generator.eval(gen_dataset)

        # Log generation time
        generation_time = time.time() - generation_start
        write_generated(
            self.experiment_folder, 
            f"eval_{dataset_split}_out.json", 
            questions, 
            instructions, 
            predictions, 
            references
        )

        print_generate_out(
            questions,
            instructions,
            predictions,
            query_ids, 
            references,
            ranking_labels,
        )

        if hasattr(self.generator,"total_cost"):
            print(self.generator.total_cost,self.generator.prompt_cost, self.generator.completion_cost)
            write_dict(self.experiment_folder, f"eval_{dataset_split}_generation_cost.json", 
                {"total_cost": self.generator.total_cost,
                 "prompt_cost": self.generator.prompt_cost,
                 "completion_cost": self.generator.completion_cost})    

    def eval_metrics(self, questions, predictions, references):
        pass

    def train(self):
        pass


class _SkillReason:
    def __init__(self, llm_name="openai/gpt-3.5-turbo-16k", cache_dir=None, device="cpu"):
        """
        Initializes the SkillReason class.

        Args:
            llm_name (str): The name of the language model to use.
            cache_dir (str): Directory to cache models and tokenizers.
            device (str): Device to run the model on ('cpu' or 'cuda').
        """
        self.llm_name = llm_name
        self.cache_dir = cache_dir
        self.device = device
        self.templates = {
            "standard_inference": standard_inference,
            "expand_prompt": expand_prompt,
            "implicit_prompt": implicit_prompt,
            # Add more templates here as needed
        }

        if self.llm_name.split('/')[0].lower() == "openai":
            self.model = self.llm_name.split('/')[-1]
            if "gpt-3.5" in self.model or "gpt-35" in self.model:
                self.max_length = 16384
                self.context_length = 15000
            elif "gpt-4" in self.model:
                self.max_length = 32768
                self.context_length = 30000
            self.tokenizer = tiktoken.get_encoding("cl100k_base")
        else:
            # Load an AutoModel for causal language modeling
            self.tokenizer = AutoTokenizer.from_pretrained(self.llm_name, cache_dir=self.cache_dir)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.llm_name,
                cache_dir=self.cache_dir,
                torch_dtype=torch.float16,
                device_map='auto',
            )
            self.model.to(self.device)
            # Set maximum context and generation lengths based on the model
            self.max_length = self.model.config.max_position_embeddings
            self.context_length = int(self.max_length * 0.8)  # Reserve some tokens for generation

    def answer(self, question, options=None, template_name="standard_inference", return_messages=False):
        """
        Generates an answer for the given question using the specified template.

        Args:
            question (str): The commonsense question to answer.
            options (dict): A dictionary of answer options.
            template_name (str): The name of the template to use.
            return_messages (bool): Whether to return the messages used in the API call.

        Returns:
            response (str): The generated response from the language model.
            messages (list, optional): The messages used in the API call.
        """
        # Prepare the options string
        if options is not None:
            options_str = '\n'.join([f"{key}. {value}" for key, value in options.items()])
        else:
            options_str = ''

        # Prepare the input prompt using the selected template and liquid rendering
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found in the templates.")
        prompt_template = self.templates[template_name]
        prompt = prompt_template

        # Prepare the full prompt with the question and options
        input_prompt = f"Here is the question:\n{question}\n\nHere are the potential choices:\n{options_str}\n\nPlease think step-by-step and generate your output in JSON format as instructed."

        # Create the messages for the OpenAI API
        messages = [
            {"role": "system", "content": prompt.strip()},
            {"role": "user", "content": input_prompt.strip()}
        ]

        # Generate the response
        response = self.generate(messages)

        if return_messages:
            return response, messages
        else:
            return response

    def generate(self, messages):
        """
        Generates a response from the language model given a list of messages.

        Args:
            messages (list): A list of messages in the format required by the model.

        Returns:
            ans (str): The generated response from the language model.
        """
        if "openai" in self.llm_name.lower():
            # OpenAI API call
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.5,
            )
            ans = response.choices[0].message['content']
        else:
            # For other models using transformers
            prompt = self.format_prompt(messages)
            input_ids = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)
            max_new_tokens = self.max_length - input_ids.size(1)
            stopping_criteria = self.custom_stopping_criteria(input_ids.size(1))

            outputs = self.model.generate(
                input_ids=input_ids,
                max_length=self.max_length,
                temperature=0.7,
                do_sample=True,
                stopping_criteria=stopping_criteria,
            )
            ans = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            ans = ans[len(prompt):].strip()
        return ans

    def format_prompt(self, messages):
        """
        Formats the messages into a single prompt string for models that don't support messages.

        Args:
            messages (list): A list of messages.

        Returns:
            prompt (str): The formatted prompt string.
        """
        prompt = ""
        for message in messages:
            role = message['role'].capitalize()
            content = message['content']
            prompt += f"{role}:\n{content}\n\n"
        return prompt

    def custom_stopping_criteria(self, input_length):
        """
        Defines custom stopping criteria for the generation.

        Args:
            input_length (int): The length of the input prompt.

        Returns:
            stopping_criteria (StoppingCriteriaList): Custom stopping criteria.
        """
        stop_sequences = ["User:", "Assistant:", "System:"]
        return StoppingCriteriaList([StopOnTokens(stop_sequences, self.tokenizer, input_length)])

class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_sequences, tokenizer, start_length):
        """
        Initializes the stopping criteria.

        Args:
            stop_sequences (list): A list of stop sequences.
            tokenizer (transformers.PreTrainedTokenizer): The tokenizer used for encoding.
            start_length (int): The length to start looking for stop sequences.
        """
        super().__init__()
        self.stop_sequences = stop_sequences
        self.tokenizer = tokenizer
        self.start_length = start_length

    def __call__(self, input_ids, scores, **kwargs):
        """
        Checks if generation should stop based on the presence of stop sequences.

        Args:
            input_ids (torch.Tensor): The generated token IDs.
            scores (torch.Tensor): The scores of the generated tokens.

        Returns:
            stop (bool): True if generation should stop, False otherwise.
        """
        generated_tokens = input_ids[0][self.start_length:]
        generated_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        for stop_sequence in self.stop_sequences:
            if stop_sequence in generated_text:
                return True
        return False

# Example Usage
if __name__ == "__main__":
    # Initialize SkillReason with your model name and device
    skill_reason = SkillReason(llm_name="openai/gpt-3.5-turbo", device="cpu")

    # Prepare your question and options
    question = "What household appliance is used to keep food cold and prevent it from spoiling?"
    options = {
        "A": "Oven",
        "B": "Refrigerator",
        "C": "Dishwasher",
        "D": "Microwave",
        "E": "Toaster"
    }

    # Get the answer using the standard inference template
    response = skill_reason.answer(question, options, template_name="standard_inference")
    print(response)