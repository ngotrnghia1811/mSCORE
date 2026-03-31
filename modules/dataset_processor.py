'''
Defines the base class for dataset processors and specific processors for general-domain datasets.
The processors are used to load and preprocess datasets for training and evaluation.
When called, the processors are called for every split.

The process() method returns a datasets.Dataset object with the following features:

- id: str, unique identifier for the example
- content: str, for example questions for QA datasets
- label: List[str] (optional, for query datasets)
    List of acceptable answers for the given question. Note that elements of the list are assumed to be synonyms / acceptable answers for the same question.
'''

import datasets
from datasets import Dataset
import os
from collections import defaultdict
import csv
from tqdm import tqdm
import pickle
from hydra.utils import instantiate
import json
from functools import partial
import random
from typing import Dict


# Base class that every processor inherits from
class Processor(object):
    """
    Base dataset processor class.
    """
    def __init__(self,
                 dataset_name: str,
                 split: str,
                 out_folder: str,
                 num_proc: int,
                 overwrite: bool,
                 debug: bool,
                 oracle_provenance: bool,
                 shuffle_labels: bool
                ) -> None:
        self.dataset_name = dataset_name
        self.split = split
        self.out_folder = out_folder
        self.num_proc = num_proc
        self.overwrite = overwrite
        self.debug = debug
        self.oracle_provenance = oracle_provenance
        self.shuffle_labels = shuffle_labels

    def process(self) -> Dataset:
        raise NotImplementedError()

    def add_index(self, dataset: Dataset) -> Dataset:
        """
        Add an index column to the dataset.
        """
        dataset = dataset.add_column("index", range(len(dataset)))
        return dataset

    def get_index_to_id(self, dataset: Dataset) -> Dict[str, int]:
        if 'index' not in dataset.features:
            dataset = self.add_index(dataset)
        return dict(zip(dataset["id"], dataset["index"]))

    def shuffled_labels_as_content(self, dataset: Dataset) -> Dataset:
        random.seed(42)
        col = dataset['label']
        random.shuffle(col)
        dataset_dict = dataset.to_dict()
        dataset_dict['ranking_label'] = [el[0] for el in col]
        return datasets.Dataset.from_dict(dataset_dict)
    
    def get_dataset(self) -> Dataset:
        pass

    def dict_to_tsv(self, id_to_index: Dict[str, int], file_path: str) -> None:
        pass

    def tsv_to_dict(self, file_path: str) -> Dict[str, int]:
        pass


# ---------------------------------------- #
# query processors
# ---------------------------------------- #

class mCSQA(Processor):
    def __init__(self, lang, *args, **kwargs):
        dataset_name = 'mcsqa'
        super().__init__(*args, **kwargs, dataset_name=dataset_name)
        self.lang = lang

    def process(self) -> Dataset:
        hf_name = 'yusuke1997/mCSQA'
        dataset = datasets.load_dataset(hf_name, self.lang, num_proc=self.num_proc)[self.lang][self.split]


        # Only keep hard questions
        dataset = dataset.filter(lambda d: d['hard'] == True)


        # Each data instance is a multiple-choice commonsense question
        # which an additional commonsense_context will be added to
        # by 'mcsqa_gen_prompt' together with gold (gpt-4o) reasoning steps
        questions = [d['question'] for d in dataset]
        options = [
            {
                "A": d['choices']['text'][0],
                "B": d['choices']['text'][1],
                "C": d['choices']['text'][2],
                "D": d['choices']['text'][3],
                "E": d['choices']['text'][4],
            } 
            for d in dataset
        ]
        correct_option_answers = [
            [
                d['answerKey'],  # correct option
                d['choices']['text'][d['choices']['label'].index(d['answerKey'])]  # correct answer text
            ]
            for d in dataset
        ]
        
        dataset = datasets.Dataset.from_dict(
            {
                'question': questions,
                'options': options,
                'correct_option_answer': correct_option_answers
            }
        )

        return dataset


class CultureBank(Processor):
    def __init__(self, *args, **kwargs):
        dataset_name = 'culturebank'
        super().__init__(*args, **kwargs, dataset_name=dataset_name)
        if self.split not in ['tiktok', 'reddit']:
            raise ValueError(f"Split {self.split} not supported for CultureBank, only 'tiktok' and 'reddit' are supported")

    def process(self) -> Dataset:
        hf_name = 'SALT-NLP/CultureBank'
        dataset = datasets.load_dataset(hf_name, self.split, num_proc=self.num_proc)[self.split]

        # Filter out data instances that do not have high agreement and no recipient
        dataset = dataset.filter(lambda d: d['agreement'] > 0.9 and d['recipient'] is not None)
        

        # each data instance is an cultural context
        # which will be transformd into a multiple-choice commonsense question
        # through culbank_gen_prompt

        cultural_topics = [f"{d['cultural group']} culture - {d['topic']} - {d['eval_scenario']}" for d in dataset]
        social_contexts = [d['eval_whole_desc'] for d in dataset]
        actors = [f"{d['actor']} - {d['eval_persona']}" for d in dataset]
        questions = [d['eval_question'] for d in dataset]
        actor_behaviors = [d['actor_behavior'] for d in dataset]
        recipients = [d['recipient'] for d in dataset]
        relations = [d['relation'] for d in dataset]
        recipient_behaviors = [d['recipient_behavior'] for d in dataset]

        dataset = datasets.Dataset.from_dict(
            {
                'cultural_topic': cultural_topics,
                'social_context': social_contexts,
                'actor': actors,
                'question': questions,
                'actor_behavior': actor_behaviors,
                'recipient': recipients,
                'relation': relations,
                'recipient_behavior': recipient_behaviors,
            }
        )
        return dataset
    
    
    def _filter_by_judge(self, judge_name):
        
        pass
