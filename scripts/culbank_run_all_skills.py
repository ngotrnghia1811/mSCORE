run_type = 'tiktok'

import os, sys, json
import pandas as pd
import numpy as np
import tqdm

import openai
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

from datasets import load_dataset

from config.prompt.templates import (
    culbank_gen as culbank_gen,
    expand_prompt as expand_prompt,
    implicit_prompt as implicit_prompt,
    standard_inference_4o as standard_inference_4o,
    standard_inference_o1 as standard_inference_o1,
    task_descriptions as task_descriptions,
    reasoning_skills as reasoning_skills,
)

openai_cli = openai.OpenAI(api_key=openai.api_key)

culbank_datasets = load_dataset("SALT-NLP/CultureBank")

data_type = ['reddit', 'tiktok']

selected_idx = {
    'reddit': [35, 37, 44, 52, 67, 72, 73, 81, 90, 94, 139, 143, 154, 161, 164, 168, 174, 195, 198, 225, 226, 246, 259, 269, 307, 309, 318, 321, 342, 380, 414, 447, 451, 464, 479, 557, 592, 598, 602, 607, 609, 610, 616, 619, 646, 699, 725, 744, 797, 799, 824, 834, 861, 872, 877, 880, 886, 905, 907, 921, 927, 937, 962, 986, 987, 1001, 1002, 1010, 1013, 1033, 1039, 1045, 1052, 1127, 1157, 1172, 1199, 1214, 1238, 1254, 1261, 1267, 1274, 1282, 1294, 1295, 1302, 1338, 1355, 1362, 1366, 1377, 1384, 1386, 1424, 1425, 1432, 1442, 1448, 1451, 1457, 1463, 1498, 1509, 1516, 1519, 1534, 1546, 1566, 1581, 1582, 1584, 1587, 1603, 1664, 1685, 1713, 1732, 1750, 1769, 1794, 1795, 1800, 1804, 1810, 1813, 1814, 1816, 1845, 1865, 1876, 1884, 1899, 1926, 1936, 1958, 1963, 1977, 1983, 1991, 2007, 2015, 2037, 2042, 2045, 2050, 2087, 2107, 2140, 2150, 2163, 2198, 2202, 2219, 2222, 2243, 2247, 2256, 2282, 2294, 2313, 2337, 2350, 2368, 2376, 2377, 2382, 2390, 2393, 2404, 2410, 2413, 2424, 2427, 2431, 2471, 2493, 2502, 2506, 2509, 2519, 2524, 2533, 2552, 2553, 2560, 2575, 2576, 2577, 2580, 2585, 2595, 2598, 2618, 2624, 2626, 2629, 2636, 2643, 2666],
    'tiktok': [0, 2, 4, 5, 9, 10, 11, 15, 16, 22, 23, 27, 29, 30, 31, 33, 49, 51, 53, 55, 68, 70, 78, 79, 80, 82, 83, 85, 87, 88, 91, 92, 99, 103, 110, 112, 118, 119, 120, 135, 139, 143, 145, 148, 153, 154, 155, 161, 165, 168, 169, 170, 173, 177, 180, 184, 192, 211, 214, 215, 218, 220, 224, 225, 228, 230, 234, 235, 241, 242, 245, 262, 266, 270, 280, 283, 289, 297, 301, 305, 316, 318, 324, 329, 339, 340, 347, 349, 356, 357, 358, 359, 365, 366, 368, 369, 371, 373, 374, 383, 405, 407, 413, 415, 418, 420, 428, 430, 431, 434, 437, 447, 448, 449, 461, 462, 463, 465, 474, 475, 487, 491, 493, 499, 501, 502, 503, 506, 511, 517, 518, 521, 524, 526, 529, 530, 532, 536, 538, 542, 549, 550, 551, 552, 557, 559, 561, 562, 563, 564, 567, 571, 573, 577, 579, 580, 581, 582, 587, 588, 595, 599, 600, 601, 604, 607, 609, 611, 619, 629, 630, 633, 634, 635, 636, 639, 640, 643, 646, 648, 657, 658, 660, 663, 664, 673, 675, 676, 677, 682, 685, 688, 692, 696, 699, 702, 704, 706, 708, 714]
}

data_json = {}
for data_type in ['reddit', 'tiktok']:
    data_json[data_type] = []
    for i in range(0, len(culbank_datasets[data_type])):
        if i not in selected_idx[data_type]:
            continue
        d = culbank_datasets[data_type][i]
        ctx = {
            'cultural_topic': f"{d['cultural group']} culture - {d['topic']} - {d['eval_scenario']}",
            'social_context': f"{d['eval_whole_desc']}",
            'actor': f"{d['actor']} - {d['eval_persona']}",
            'question': f"{d['eval_question']}",
            'actor_behavior': f"{d['actor_behavior']}",
            'recipient': f"{d['recipient']}",
            'relation': f"{d['relation']}",
            'recipient_behavior': f"{d['recipient_behavior']}",
        }
        d = json.dumps(ctx, indent=4)
        data_json[data_type].append(d)

print(len(data_json[run_type]))



#! CULBANK GEN
import json
from ast import literal_eval


def run_culbank_gen(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_gen.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """
    
    messages = [
        {"role": "system", "content": culbank_gen},
        {"role": "user", "content": input_prompt}
    ]

    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        messages=messages,
        max_tokens=10000,
        n=1,
        stop=None,
        temperature=0,
        seed=seed,
        response_format={ "type": "json_object" },
    )

    # Extract the response text
    result = response.choices[0].message.content
    
    return result, messages


#! EXPAND
def run_expand(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_gen.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """

    messages = [
        {"role": "system", "content": expand_prompt},
        {"role": "user", "content": input_prompt}
    ]

    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        messages=messages,
        max_tokens=10000,
        n=1,
        stop=None,
        temperature=0,
        seed=seed,
    )

    # Extract the response text
    result = response.choices[0].message.content
    
    return result, messages

#! IMPLICIT
def run_implicit(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_implicit.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """

    messages = [
        {"role": "system", "content": implicit_prompt},
        {"role": "user", "content": input_prompt}
    ]

    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        messages=messages,
        max_tokens=10000,
        n=1,
        stop=None,
        temperature=0,
        seed=seed,
        response_format={ "type": "json_object" },
    )
    # Extract the response text
    result = response.choices[0].message.content
    return result, messages

#! INFER
def run_infer(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_implicit.render(question=inp)
    inp = inp.replace('INPUT:', '').replace('OUTPUT:', '').strip()
    inp = inp.replace(inp[inp.find("correct_answer")-1:], '') + '\n}'
    inp = inp.replace('},', '}')
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """

    # Call the OpenAI API
    if api_model == 'o1-mini' or api_model == 'o1-preview':
        messages = [
            {"role": "user", "content": standard_inference_o1},
            {"role": "user", "content": input_prompt}
        ]

        # print(messages[0])
        response = openai_cli.chat.completions.create(
            model=api_model,
            # model="gpt-3.5-turbo",
            messages=messages,
            max_completion_tokens=10000,
            n=1,
            # stop=None,
            # temperature=0,
            seed=seed,
            # response_format={ "type": "json_object" },
        )
    elif 'o1' in api_model:
        messages = [
            {"role": "developer", "content": standard_inference_o1},
            {"role": "user", "content": input_prompt}
        ]

        # print(messages[0])
        response = openai_cli.chat.completions.create(
            model=api_model,
            # model="gpt-3.5-turbo",
            messages=messages,
            max_completion_tokens=10000,
            n=1,
            # stop=None,
            # temperature=0,
            seed=seed,
            response_format={ "type": "json_object" },
        )
    else:
        messages = [
            {"role": "system", "content": standard_inference_4o},
            {"role": "user", "content": input_prompt}
        ]

        # print(messages[0])
        response = openai_cli.chat.completions.create(
            model=api_model,
            messages=messages,
            max_tokens=10000,
            n=1,
            # stop=None,
            temperature=0,
            seed=seed,
            response_format={ "type": "json_object" },
        )

    # Extract the response text
    result = response.choices[0].message.content
    
    # json_dict = {
        # "search_queries": {}
    # }
    # json_data = json.loads(response)
    # result = json.loads(result)
    # result.update(literal_eval(question))

    return result, messages


#SECTION:
#SECTION: 4o Gen
#SECTION:

seed = 10000

# Whole pipeline
start = 0
end = 100

# redo_id = [120]
# redo_id = [23, 46, 75, 80]  # [82, 90 , 107]

print(f'Running full pipeline for {run_type} from {start} to {end}')
input_data = data_json[run_type]
api_model = "gpt-4o"
# api_model = "o1-mini"
# api_model = "o1-preview"

level = 7

culbank_gen_data = []
culbank_expand_data = []
culbank_implicit_data = []
culbank_infer_data = []

data_dir = '/projects/uonlp/nghian/projects/optim/mRAG/skill_reason/datasets/CultureBank'
os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_gen_data', exist_ok=True)
for l in range(level):
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_expand_data_{l}', exist_ok=True)
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_implicit_data_{l}', exist_ok=True)
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_infer_data_{l}', exist_ok=True)


for i in tqdm.tqdm(range(start, end)):
    # Convert: culbank -> gen

    # if i in redo_id:
    #     gen_ret_gen = run_culbank_gen(input_data[i], api_model=api_model, seed=seed)
    #     culbank_gen_data.append(gen_ret_gen)
    #     save_data = {
    #         "system": gen_ret_gen[1][0]['content'],
    #         "input": gen_ret_gen[1][1]['content'],
    #         "output": gen_ret_gen[0],
    #     }
    #     # Save
    #     save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_gen_data/{run_type}_{i}.json'
    #     with open(save_path, 'w') as f:
    #         json.dump(save_data, f, indent=4)

    if os.path.exists(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_gen_data/{run_type}_{i}.json'):
        gen_ret_gen = json.load(open(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_gen_data/{run_type}_{i}.json', 'r'))
        gen_ret_gen = [gen_ret_gen['output'], gen_ret_gen['system'], gen_ret_gen['input']]
    else:
        gen_ret_gen = run_culbank_gen(input_data[i], api_model=api_model, seed=seed)
        culbank_gen_data.append(gen_ret_gen)
        save_data = {
            "system": gen_ret_gen[1][0]['content'],
            "input": gen_ret_gen[1][1]['content'],
            "output": gen_ret_gen[0],
            "save_id": selected_idx[run_type][i],
        }
        save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_gen_data/{run_type}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)

    # Expand: gen -> expand
    for l in range(level):
        if l == 0:
            expand_inp = gen_ret_gen[0]
        else:
            expand_inp = gen_ret_expand[0]

        gen_ret_expand = run_expand(expand_inp, api_model=api_model, seed=seed)
        culbank_expand_data.append(gen_ret_expand)
        save_data = {
            "system": gen_ret_expand[1][0]['content'],
            "input": gen_ret_expand[1][1]['content'],
            "output": gen_ret_expand[0],
            "save_id": selected_idx[run_type][i],
        }
        save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_expand_data_{l}/{run_type}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)

        # Implicit: expand -> implicit
        gen_ret_implicit = run_implicit(gen_ret_expand[0], api_model=api_model, seed=seed)
        culbank_implicit_data.append(gen_ret_implicit)
        save_data = {
            "system": gen_ret_implicit[1][0]['content'],
            "input": gen_ret_implicit[1][1]['content'],
            "output": gen_ret_implicit[0],
            "save_id": selected_idx[run_type][i],
        }
        save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_implicit_data_{l}/{run_type}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)

        # Infer: implicit -> infer
        gen_ret_infer = run_infer(gen_ret_implicit[0], api_model=api_model, seed=seed)
        culbank_infer_data.append(gen_ret_infer)
        save_data = {
            "system": gen_ret_infer[1][0]['content'],
            "input": gen_ret_infer[1][1]['content'],
            "output": gen_ret_infer[0],
            "save_id": selected_idx[run_type][i],
        }
        save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_infer_data_{l}/{run_type}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)


#SECTION:
#SECTION: o1 Infer
#SECTION:

import traceback
seed = 10000

# Whole pipeline
# run_lang = 'fr'
start = 0
end = 100

input_data = data_json[run_type]    
api_model = "o1-mini"
# api_model = "o1"
print(f'Running {api_model} Infer for {run_type} from {start} to {end} for {len(input_data)} samples')

level = 7

data_dir = '/projects/uonlp/nghian/projects/optim/mRAG/skill_reason/datasets/CultureBank'
for l in range(level):
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_infer_data_{l}', exist_ok=True)

error_o1 = []

for i in tqdm.tqdm(range(start, end)):
    for l in range(level):

        save_path = f'{data_dir}/generated_results/{api_model}/{run_type}/culbank_infer_data_{l}/{run_type}_{i}.json'
        # if file exists, skip
        if os.path.exists(save_path):
            continue

        # try and except    
        try:
            # Infer: implicit -> infer
            # load gpt-4o implicit
            gen_ret_implicit = json.load(open(f'{data_dir}/generated_results/gpt-4o/{run_type}/culbank_implicit_data_{l}/{run_type}_{i}.json', 'r'))
            gen_ret_implicit = [gen_ret_implicit['output'], gen_ret_implicit['system'], gen_ret_implicit['input']]

            gen_ret_infer = run_infer(gen_ret_implicit[0], api_model=api_model, seed=seed)
            # mcsqa_infer_data.append(gen_ret_infer)
            save_data = {
                "system": gen_ret_infer[1][0]['content'],
                "input": gen_ret_infer[1][1]['content'],
                "output": gen_ret_infer[0],
                "save_id": selected_idx[run_type][i],
            }
            # Save  
            with open(save_path, 'w') as f:
                json.dump(save_data, f, indent=4)
        except Exception as e1:
            # try again with api_model = o1-preview

            # print(f'Error o1: {traceback.format_exc()} at {run_lang}_{i} {l} level; Try o1-preview')
            print(f'Error o1: {e1} at {run_type}_{i} {l} level')
            error_o1.append([save_path, e1])
            continue

print(f'Error o1: {len(error_o1)}')

