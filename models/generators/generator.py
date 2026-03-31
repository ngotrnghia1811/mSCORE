import torch
import gc
from abc import ABC, abstractmethod
from torch.utils.data import DataLoader
from tqdm import tqdm
from jinja2.exceptions import TemplateError
from functools import partial


class Generator(ABC):
    def __init__(self,
                 model_name: str = None,
                 batch_size: int = 1,
                 max_new_tokens: int = 1,
                 max_length: int = None):
        self.model_name = model_name
        self.batch_size = batch_size
        self.max_new_tokens = max_new_tokens
        self.max_length = max_length

    @abstractmethod
    def generate(self, inp):
        pass
    
    @abstractmethod
    def collate_fn(self, inp):
        pass

    def eval(self, dataset):
        """
        Generate responses for a dataset.
        """
        with torch.no_grad():
            dataloader = DataLoader(
                dataset, 
                batch_size=self.batch_size, 
                collate_fn=partial(self.collate_fn, eval=True), 
                num_workers=4
            )
            
            responses, instructions, question_ids = [], [], []
            for data_dict in tqdm(dataloader, desc='Generating'):
                id_ = data_dict['q_id']
                instruction = data_dict['instruction']
                question_ids += id_
                instructions += instruction
                generated_response = self.generate(data_dict['model_input'])
                responses += generated_response
                
                torch.cuda.empty_cache()
                gc.collect()
                
            return question_ids, instructions, responses

    def get_response(self):
        """
        This replaces the 'generation_prompt' in case the generator does not have a chat_template.
        It's used to prompt and also to identify the label positions to mask prompt in training.
        """
        return '\nResponse:\n'

    def get_response_template_ids(self):
        response_template = self.get_response()
        return self.tokenizer.encode(response_template, add_special_tokens=False)
    
    def compile_prompt(self, system_prompt: str, user_prompt: str, question: str, label: str = None):
        """
        Applying the chat template if it exists.
        Returns:
        - the final prompt
        - if a label is provided, the position of the first label index within the tokenized sequence
        """
        add_generation_prompt = (label is None)
        label_start_index = None

        if self.tokenizer.chat_template is None:
            user_prompt_with_values = eval(user_prompt).replace(':\ ', ': ')
            prompt = f"{system_prompt}\n{user_prompt_with_values}" + self.get_response()
            if label is not None:
                label_start_index = len(self.tokenizer(prompt, add_special_tokens=False)['input_ids'])
                prompt += label + self.tokenizer.eos_token

        else:        
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": eval(user_prompt).replace(':\ ', ': ')}
            ]
            try:
                if label is not None:
                    label_start_index = len(self.tokenizer.apply_chat_template(
                        messages, 
                        tokenize=True, 
                        add_generation_prompt=True, 
                        add_special_tokens=False
                    ))
                    messages.append({"role": "assistant", "content": label})
                
                prompt = self.tokenizer.apply_chat_template(
                    messages,
                    add_generation_prompt=add_generation_prompt, 
                    tokenize=False
                )

            except TemplateError as e:
                if "System role not supported" in str(e):
                    messages = [{"role": "user", "content": messages[0]['content'] + '\n' + messages[1]['content']}]

                    if label is not None:
                        label_start_index = len(self.tokenizer.apply_chat_template(
                            messages,
                            tokenize=True,
                            add_generation_prompt=True,
                            add_special_tokens=False
                        ))
                        messages.append({"role": "assistant", "content": label})

                    prompt = self.tokenizer.apply_chat_template(
                        messages,
                        add_generation_prompt=add_generation_prompt,
                        tokenize=False
                    )
                else:
                    raise e
        
        if label is not None:
            assert label_start_index is not None
            if not prompt.endswith(self.tokenizer.eos_token):
                prompt += self.tokenizer.eos_token
            
        return prompt, label_start_index

    def format_instruction(self, sample: dict, eval: bool = True) -> (str, int):
        """
        Makes the actual prompt from the prompt template and the model chat template.
        Returns:
        - The formatted prompt
        - Start index of the label in that prompt if eval=False and a label is provided, None otherwise
        """
        question = sample['question']
        label = None if eval else sample['label']
        return self.compile_prompt(self.prompt.system, self.prompt.user, question, label=label) 