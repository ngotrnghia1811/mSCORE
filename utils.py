import datasets
import random 
import json
import shutil
import pytrec_eval
import os 
import torch
import time
import glob
import warnings
import numpy as np
import torch

from collections import defaultdict
from datasets.fingerprint import Hasher
from omegaconf import OmegaConf
from tqdm import tqdm


def print_generate_out(questions, instructions, predictions, query_ids, references, ranking_labels, n=5):
    """Print a sample of generated questions, instructions, predictions, query_ids, references, and ranking labels."""
    rand = random.sample(range(len(query_ids)), n)
    for i in rand:
        print('_'*50)


def write_generated(out_folder, out_filename, query_ids, questions, instructions, responses, labels, ranking_labels):
    """Write a list of generated questions, instructions, responses, labels, and ranking labels to a jsonl file."""
    jsonl_list = list()
    for i, (q_id, question, response, instruction, label, ranking_label) in enumerate(zip(query_ids, questions, responses, instructions, labels, ranking_labels)):
        jsonl = {}
        jsonl['q_id'] = q_id
        jsonl['response'] = response
        jsonl['instruction'] = instruction
        jsonl['label'] = label
        jsonl['question'] = question
        jsonl['ranking_label'] = ranking_label
        jsonl_list.append(jsonl)
    write_dict(out_folder, out_filename, jsonl_list)


def write_dict(out_folder, out_filename, dict_to_write):
    """Write a dictionary to a jsonl file."""
    with open(f'{out_folder}/{out_filename}', 'w') as fp:
        json.dump(dict_to_write, fp, indent=2)

def init_experiment(config, experiment_folder, runs_folder, run_name, overwrite_exp=False, continue_batch=None):
    """Initialize an experiment folder with a config file."""
    os.makedirs(experiment_folder, exist_ok=True)
    OmegaConf.save(config=config, f=f"{experiment_folder}/config.yaml")
