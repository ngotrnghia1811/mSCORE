run_lang = 'zh'

import os, sys, json
import pandas as pd
import numpy as np
import tqdm

import openai
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

from datasets import load_dataset

from config.prompt.templates import (
    mcsqa_gen as en_mcsqa_gen,
    culbank_gen as en_culbank_gen,
    expand_prompt as en_expand_prompt,
    implicit_prompt as en_implicit_prompt,
    # standard_inference as en_standard_inference,
    logical_inference as en_logical_inference,
    task_descriptions as en_task_descriptions,
    reasoning_skills as en_reasoning_skills,
)

from config.prompt.templates_de import (
    mcsqa_gen as de_mcsqa_gen,
    expand_prompt as de_expand_prompt,
    implicit_prompt as de_implicit_prompt,
    # standard_inference as de_standard_inference,
    logical_inference as de_logical_inference,
    task_descriptions as de_task_descriptions,
    reasoning_skills as de_reasoning_skills,
)

from config.prompt.templates_fr import (
    mcsqa_gen as fr_mcsqa_gen,
    expand_prompt as fr_expand_prompt,
    implicit_prompt as fr_implicit_prompt,
    # standard_inference as fr_standard_inference,
    logical_inference as fr_logical_inference,
    task_descriptions as fr_task_descriptions,
    reasoning_skills as fr_reasoning_skills,
)

from config.prompt.templates_zh import (
    mcsqa_gen as zh_mcsqa_gen,
    expand_prompt as zh_expand_prompt,
    implicit_prompt as zh_implicit_prompt,
    # standard_inference as zh_standard_inference,
    logical_inference as zh_logical_inference,
    task_descriptions as zh_task_descriptions,
    reasoning_skills as zh_reasoning_skills,
)

from config.prompt.templates_ja import (
    mcsqa_gen as ja_mcsqa_gen,
    expand_prompt as ja_expand_prompt,
    implicit_prompt as ja_implicit_prompt,
    # standard_inference as ja_standard_inference,
    logical_inference as ja_logical_inference,
    task_descriptions as ja_task_descriptions,
    reasoning_skills as ja_reasoning_skills,
)

all_prompts = {}

all_prompts['en'] = {
    'mcsqa_gen': en_mcsqa_gen,
    'expand_prompt': en_expand_prompt,
    'implicit_prompt': en_implicit_prompt,
    # 'standard_inference': en_standard_inference,
    'logical_inference': en_logical_inference,
}

all_prompts['ja'] = {
    'mcsqa_gen': ja_mcsqa_gen,
    'expand_prompt': ja_expand_prompt,
    'implicit_prompt': ja_implicit_prompt,
    # 'standard_inference': ja_standard_inference,
    'logical_inference': ja_logical_inference,
}

all_prompts['zh'] = {
    'mcsqa_gen': zh_mcsqa_gen,
    'expand_prompt': zh_expand_prompt,
    'implicit_prompt': zh_implicit_prompt,
    # 'standard_inference': zh_standard_inference,
    'logical_inference': zh_logical_inference,
}

all_prompts['de'] = {
    'mcsqa_gen': de_mcsqa_gen,
    'expand_prompt': de_expand_prompt,
    'implicit_prompt': de_implicit_prompt,
    # 'standard_inference': de_standard_inference,
    'logical_inference': de_logical_inference,
}

all_prompts['fr'] = {
    'mcsqa_gen': fr_mcsqa_gen,
    'expand_prompt': fr_expand_prompt,
    'implicit_prompt': fr_implicit_prompt,
    # 'standard_inference': fr_standard_inference,
    'logical_inference': fr_logical_inference,
}

# ds = load_dataset("yusuke1997/mCSQA")

openai_cli = openai.OpenAI(api_key=openai.api_key)

langs = ['en', 'ja', 'zh', 'de', 'fr']

mcsqa_datasets = {l: load_dataset("yusuke1997/mCSQA", l) for l in langs}

# langs = ['en', 'ja', 'zh', 'de', 'fr']
# run_lang = 'fr'
print('running ', run_lang)


selected_index = {
    'en': [6, 17, 18, 28, 43, 49, 63, 67, 76, 84, 91, 96, 105, 109, 110, 120, 128, 130, 138, 142, 143, 146, 154, 157, 159, 163, 166, 167, 169, 180, 188, 192, 195, 197, 206, 217, 225, 229, 233, 234, 235, 262, 265, 280, 291, 293, 296, 298, 302, 304, 308, 311, 331, 336, 339, 343, 348, 352, 359, 382, 383, 387, 394, 400, 411, 413, 420, 429, 431, 443, 462, 476, 479, 485, 508, 511, 521, 526, 527, 534, 539, 543, 544, 551, 557, 562, 567, 574, 580, 581, 587, 591, 609, 611, 624, 631, 634, 635, 639, 640, 650, 658, 682, 684, 691, 692, 699, 704, 707, 710, 717, 723, 725, 729, 735, 741, 751, 762, 765, 768, 769, 771, 774, 776, 777, 779, 780, 782, 785, 808, 816, 820, 826, 840, 851, 858, 861, 862, 865, 866, 878, 882, 887, 889, 891, 893, 895, 898, 900, 907, 910, 943, 947, 948, 949, 954, 959, 964, 968, 973, 975, 978, 979, 981, 1004, 1008, 1014, 1023, 1032, 1036, 1040, 1042, 1044, 1045, 1048, 1051, 1062, 1067, 1071, 1081, 1092, 1098, 1105, 1125, 1132, 1157, 1213, 1223, 1234, 1263, 1272, 1273, 1274, 1293, 1301, 1323, 1325, 1337, 1340, 1346],
    'ja': [41, 144, 166, 366, 536, 686, 1063, 1132, 1198, 1211, 23, 24, 79, 80, 94, 98, 120, 133, 149, 157, 167, 188, 194, 212, 227, 249, 257, 297, 300, 329, 358, 380, 386, 410, 440, 441, 454, 458, 488, 492, 494, 506, 533, 537, 559, 579, 589, 600, 607, 646, 671, 680, 682, 690, 700, 712, 739, 770, 798, 806, 814, 857, 943, 977, 1000, 1005, 1007, 1015, 1027, 1032, 1046, 1048, 1086, 1122, 1128, 1133, 1139, 1177, 1184, 1200, 1218, 1221, 1225, 1246, 1251, 1263, 1264, 1323, 1350, 1408, 1448, 1452, 2, 3, 6, 21, 25, 46, 66, 71, 86, 89, 95, 103, 108, 124, 130, 137, 142, 143, 145, 146, 151, 152, 155, 159, 171, 181, 187, 190, 196, 204, 221, 279, 281, 285, 287, 288, 290, 307, 312, 315, 332, 333, 339, 362, 363, 370, 378, 381, 403, 414, 424, 437, 438, 453, 477, 483, 495, 502, 528, 535, 553, 577, 619, 648, 653, 665, 673, 675, 681, 709, 734, 745, 757, 763, 782, 785, 792, 809, 820, 832, 833, 836, 839, 845, 882, 883, 894, 897, 903, 925, 960, 964, 968, 972, 1003, 1040, 1044, 1050, 1064, 1065, 1107, 1116, 1125, 1127, 1148, 1179, 1192, 1193],
    'zh': [179, 508, 535, 600, 777, 858, 974, 1220, 1268, 1403, 1422, 1467, 5, 16, 50, 56, 60, 89, 125, 134, 190, 208, 217, 234, 253, 257, 265, 311, 322, 324, 329, 358, 365, 426, 445, 485, 534, 575, 611, 613, 625, 630, 647, 657, 667, 674, 675, 686, 705, 721, 725, 736, 788, 797, 816, 840, 859, 883, 897, 910, 919, 949, 956, 1002, 1022, 1027, 1039, 1065, 1081, 1088, 1135, 1137, 1142, 1168, 1182, 1193, 1196, 1247, 1295, 1308, 1340, 1351, 1365, 1371, 1396, 1398, 1401, 1421, 1429, 1437, 1440, 1461, 1466, 1483, 1507, 1511, 1512, 8, 22, 27, 30, 58, 73, 87, 88, 96, 97, 124, 126, 127, 136, 137, 138, 161, 167, 174, 181, 192, 194, 196, 201, 209, 210, 219, 227, 233, 246, 255, 267, 284, 295, 339, 354, 356, 372, 385, 392, 400, 403, 411, 424, 430, 431, 456, 457, 469, 487, 501, 538, 540, 548, 549, 551, 563, 614, 634, 636, 639, 640, 665, 677, 687, 701, 726, 738, 744, 746, 754, 761, 763, 765, 768, 770, 778, 779, 782, 807, 809, 810, 814, 818, 819, 822, 828, 839, 841, 853, 874, 875, 879, 880, 885, 899, 909, 921, 950, 951, 959, 981, 986],
    'de': [1471, 16, 41, 45, 89, 97, 132, 133, 161, 170, 202, 206, 207, 225, 226, 234, 239, 240, 315, 323, 353, 366, 388, 390, 407, 458, 470, 483, 525, 526, 547, 554, 598, 641, 674, 682, 688, 749, 751, 781, 787, 824, 847, 852, 878, 903, 938, 977, 1026, 1067, 1117, 1129, 1140, 1166, 1176, 1185, 1188, 1192, 1216, 1221, 1223, 1238, 1239, 1245, 1253, 1276, 1280, 1282, 1286, 1313, 1339, 1349, 1353, 1391, 1410, 1412, 1423, 1433, 1451, 1457, 1475, 1496, 1539, 10, 20, 24, 32, 47, 61, 65, 73, 76, 83, 94, 95, 96, 98, 99, 100, 102, 106, 119, 123, 124, 131, 135, 145, 146, 149, 150, 158, 159, 160, 167, 174, 177, 180, 188, 195, 197, 200, 203, 213, 214, 224, 227, 230, 243, 244, 250, 257, 258, 260, 264, 267, 269, 275, 278, 283, 284, 287, 288, 296, 297, 303, 306, 308, 317, 327, 335, 338, 341, 347, 351, 352, 354, 356, 357, 361, 364, 370, 384, 387, 389, 394, 396, 398, 399, 400, 404, 405, 418, 419, 426, 427, 428, 431, 432, 437, 439, 440, 441, 449, 452, 454, 461, 464, 469, 471, 474, 477, 485, 496, 500, 503, 505, 507, 508, 509, 510],
    'fr': [326, 1, 5, 45, 47, 52, 55, 64, 68, 69, 78, 92, 94, 97, 104, 107, 112, 116, 117, 166, 172, 174, 176, 178, 182, 196, 197, 231, 236, 253, 261, 264, 278, 280, 281, 283, 286, 294, 295, 304, 312, 315, 319, 327, 341, 352, 359, 367, 379, 384, 389, 399, 408, 411, 415, 421, 424, 431, 444, 453, 458, 467, 470, 515, 528, 539, 553, 589, 603, 606, 636, 669, 690, 698, 717, 733, 734, 753, 767, 769, 781, 786, 806, 809, 812, 819, 837, 853, 854, 855, 871, 882, 886, 919, 923, 931, 938, 939, 974, 978, 981, 988, 1001, 0, 4, 7, 18, 19, 20, 23, 26, 27, 31, 42, 44, 54, 57, 59, 70, 73, 74, 75, 76, 83, 85, 89, 93, 103, 118, 125, 127, 131, 142, 144, 147, 159, 160, 169, 180, 183, 187, 188, 199, 201, 208, 209, 213, 215, 224, 227, 229, 237, 238, 239, 241, 244, 251, 254, 255, 257, 259, 260, 262, 263, 269, 272, 273, 274, 275, 277, 284, 290, 296, 301, 306, 307, 310, 311, 317, 320, 331, 334, 335, 338, 348, 349, 354, 361, 363, 364, 365, 366, 369, 374, 377, 383, 387, 390, 391, 392],
}

selected_index = {k: sorted(v) for k, v in selected_index.items()}

data_json = {}
for l in ['en', 'ja', 'zh', 'de', 'fr']:
    data_json[l] = []
    for i, d in enumerate(mcsqa_datasets[l]['test']):
        if i not in selected_index[l]:
            continue
        key_pos = d['choices']['label'].index(d['answerKey'])
        inp = \
        {
            "question": d['question'],
            "options": {
                "A": d['choices']['text'][0],
                "B": d['choices']['text'][1],
                "C": d['choices']['text'][2],
                "D": d['choices']['text'][3],
                "E": d['choices']['text'][4],
                },
            "correct_answer": (d['answerKey'], d['choices']['text'][key_pos]),
        }
        json_inp = json.dumps(inp, indent=4) 
        data_json[l].append(json_inp)
    

print(len(data_json[run_lang]))


import json
from ast import literal_eval


openai_cli = openai.OpenAI(api_key=openai.api_key)


def run_mcsqa_gen(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_gen.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """
    
    messages = [
        {"role": "system", "content": all_prompts[run_lang]['mcsqa_gen']},
        {"role": "user", "content": input_prompt}
    ]

    # print(messages[0])
    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        # model="gpt-3.5-turbo",
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
    
    # json_dict = {
        # "search_queries": {}
    # }
    # json_data = json.loads(response)
    # result = json.loads(result)
    # result.update(literal_eval(question))

    return result, messages


def run_expand(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_gen.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """
    
    messages = [
        {"role": "system", "content": all_prompts[run_lang]['expand_prompt']},
        {"role": "user", "content": input_prompt}
    ]

    # print(messages[0])
    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        # model="gpt-3.5-turbo",
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
    
    # json_dict = {
        # "search_queries": {}
    # }
    # json_data = json.loads(response)
    # result = json.loads(result)
    # result.update(literal_eval(question))

    return result, messages


#! IMPLCITATION
def run_implicit(inp, api_model="gpt-4o", seed=1000):
    # Construct the messages for the OpenAI API
    
    # input_prompt =input_implicit.render(question=inp)
    input_prompt = f"""
    INPUT:
    {inp}

    OUTPUT:
    """
    
    messages = [
        {"role": "system", "content": all_prompts[run_lang]['implicit_prompt']},
        {"role": "user", "content": input_prompt}
    ]

    # print(messages[0])
    # Call the OpenAI API
    response = openai_cli.chat.completions.create(
        model=api_model,
        # model="gpt-3.5-turbo",
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
    
    # json_dict = {
        # "search_queries": {}
    # }
    # json_data = json.loads(response)
    # result = json.loads(result)
    # result.update(literal_eval(question))

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

    sys_prompt = all_prompts[run_lang]['logical_inference']
    
    
    # Call the OpenAI API
    if api_model == 'o1-mini' or api_model == 'o1-preview':
        messages = [
            {"role": "user", "content": sys_prompt},
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
            {"role": "developer", "content": sys_prompt},
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
            {"role": "system", "content": sys_prompt},
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

seed = 10001

# Whole pipeline
start = 0
end = 200

# redo_id = [120]
# redo_id = [23, 46, 75, 80]  # [82, 90 , 107]

print(f'Running from {start} to {end}')
input_data = data_json[run_lang]
api_model = "gpt-4o"
# api_model = "o1-mini"
# api_model = "o1-preview"
level = 4

mcsqa_gen_data = []
mcsqa_expand_data = []
mcsqa_implicit_data = []
mcsqa_infer_data = []

data_dir = '/projects/uonlp/nghian/projects/optim/mRAG/skill_reason/datasets/mCSQA'
os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_gen_data', exist_ok=True)
for l in range(level):
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_expand_data_{l}', exist_ok=True)
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_implicit_data_{l}', exist_ok=True)
    os.makedirs(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_infer_data_{l}', exist_ok=True)

# os.makedirs(f'results/{api_model}/mcsqa_gen_data', exist_ok=True)
# for l in range(level):
    # os.makedirs(f'results/{api_model}/mcsqa_expand_data_{l}', exist_ok=True)
    # os.makedirs(f'results/{api_model}/mcsqa_implicit_data_{l}', exist_ok=True)
    # os.makedirs(f'results/{api_model}/mcsqa_infer_data_{l}', exist_ok=True)

# for i in tqdm.tqdm(range(len(input_data), start, end)):
for i in tqdm.tqdm(range(start, end)):
    # Convert: mcsqa -> gen

    if i in redo_id:
        gen_ret_gen = run_mcsqa_gen(input_data[i], api_model=api_model, seed=seed)
        mcsqa_gen_data.append(gen_ret_gen)
        save_data = {
            "system": gen_ret_gen[1][0]['content'],
            "input": gen_ret_gen[1][1]['content'],
            "output": gen_ret_gen[0],
        }
        # Save
        save_path = f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_gen_data/{run_lang}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)
    else:
        continue

    if os.path.exists(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_gen_data/{run_lang}_{i}.json'):
        gen_ret_gen = json.load(open(f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_gen_data/{run_lang}_{i}.json', 'r'))
        gen_ret_gen = [gen_ret_gen['output'], gen_ret_gen['system'], gen_ret_gen['input']]
    else:
        gen_ret_gen = run_mcsqa_gen(input_data[i], api_model=api_model, seed=seed)
        mcsqa_gen_data.append(gen_ret_gen)
        save_data = {
            "system": gen_ret_gen[1][0]['content'],
            "input": gen_ret_gen[1][1]['content'],
            "output": gen_ret_gen[0],
        }
        # Save
        save_path = f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_gen_data/{run_lang}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)
        
    # Expand: gen -> expand
    for l in range(level):
        if l == 0:
            expand_inp = gen_ret_gen[0]
        else:
            expand_inp = gen_ret_expand[0]
        # gen_ret_expand = run_expand(gen_ret_gen[0])
        gen_ret_expand = run_expand(expand_inp, api_model=api_model, seed=seed)
        mcsqa_expand_data.append(gen_ret_expand)
        save_data = {
            "system": gen_ret_expand[1][0]['content'],
            "input": gen_ret_expand[1][1]['content'],
            "output": gen_ret_expand[0],
        }
        # Save
        save_path = f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_expand_data_{l}/{run_lang}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)
    
        # Implicit: expand -> implicit
        gen_ret_implicit = run_implicit(gen_ret_expand[0], api_model=api_model, seed=seed)
        mcsqa_implicit_data.append(gen_ret_implicit)
        save_data = {
            "system": gen_ret_implicit[1][0]['content'],
            "input": gen_ret_implicit[1][1]['content'],
            "output": gen_ret_implicit[0],
        }
        # Save
        save_path = f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_implicit_data_{l}/{run_lang}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)
        
        # Infer: implicit -> infer
        gen_ret_infer = run_infer(gen_ret_implicit[0], api_model=api_model, seed=seed)
        mcsqa_infer_data.append(gen_ret_infer)
        save_data = {
            "system": gen_ret_infer[1][0]['content'],
            "input": gen_ret_infer[1][1]['content'],
            "output": gen_ret_infer[0],
        }
        # Save  
        save_path = f'{data_dir}/generated_results/{api_model}/{run_lang}/mcsqa_infer_data_{l}/{run_lang}_{i}.json'
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=4)



# SECTION:
# SECTION: o1 Infer
# SECTION:
import traceback
seed = 10000

# Whole pipeline
# run_lang = 'fr'
start = 0
end = 200

input_data = data_json[run_lang]    
api_model = "o1-mini"
print(f'Running {api_model} Logic Infer for {run_lang} from {start} to {end} for {len(input_data)} samples')
# api_model = "gpt-4o"
# api_model = "o1"
# api_model = "o1-mini"
# api_model = "o1-preview"
level = 4

# mcsqa_gen_data = []
# mcsqa_expand_data = []
# mcsqa_implicit_data = []
# mcsqa_infer_data = []

data_dir = '/projects/uonlp/nghian/projects/optim/mRAG/skill_reason/datasets/mCSQA'
# os.makedirs(f'{data_dir}/generated_results/{api_model}/mcsqa_gen_data', exist_ok=True)
for l in range(level):
    # os.makedirs(f'{data_dir}/generated_results/{api_model}/mcsqa_expand_data_{l}', exist_ok=True)
    # os.makedirs(f'{data_dir}/generated_results/{api_model}/mcsqa_implicit_data_{l}', exist_ok=True)
    os.makedirs(f'{data_dir}/logic_generated_results/{api_model}/{run_lang}/mcsqa_infer_data_{l}', exist_ok=True)

# os.makedirs(f'results/{api_model}/mcsqa_gen_data', exist_ok=True)
# for l in range(level):
    # os.makedirs(f'results/{api_model}/mcsqa_expand_data_{l}', exist_ok=True)
    # os.makedirs(f'results/{api_model}/mcsqa_implicit_data_{l}', exist_ok=True)
    # os.makedirs(f'results/{api_model}/mcsqa_infer_data_{l}', exist_ok=True)

error_o1 = []
error_o1_preview = []
preview_cnt = 0
for i in tqdm.tqdm(range(start, end)):
    for l in range(level):

        save_path = f'{data_dir}/logic_generated_results/{api_model}/{run_lang}/mcsqa_infer_data_{l}/{run_lang}_{i}.json'
        # if file exists, skip
        if os.path.exists(save_path):
            continue

        # try and except    
        try:
            # Infer: implicit -> infer
            # load gpt-4o implicit
            # gen_ret_implicit = json.load(open(f'{data_dir}/generated_results/gpt-4o/{run_lang}/mcsqa_implicit_data_{l}/{run_lang}_{i}.json', 'r'))
            gen_ret_implicit = json.load(open(f'{data_dir}/generated_results/gpt-4o/{run_lang}_fix/mcsqa_implicit_data_{l}/{run_lang}_{i}.json', 'r'))
            gen_ret_implicit = [gen_ret_implicit['output'], gen_ret_implicit['system'], gen_ret_implicit['input']]

            gen_ret_infer = run_infer(gen_ret_implicit[0], api_model=api_model, seed=seed)
            # mcsqa_infer_data.append(gen_ret_infer)
            save_data = {
                "system": gen_ret_infer[1][0]['content'],
                "input": gen_ret_infer[1][1]['content'],
                "output": gen_ret_infer[0],
                "save_id": selected_index[run_lang][i],
            }
            # Save  
            with open(save_path, 'w') as f:
                json.dump(save_data, f, indent=4)
        except Exception as e1:
            # try again with api_model = o1-preview

            # print(f'Error o1: {traceback.format_exc()} at {run_lang}_{i} {l} level; Try o1-preview')
            print(f'Error o1: {e1} at {run_lang}_{i} {l} level')
            error_o1.append([save_path, e1])
            # try:
            #     gen_ret_infer = run_infer(gen_ret_implicit[0], api_model="o1-preview", seed=seed)
            #     mcsqa_infer_data.append(gen_ret_infer)
            #     save_data = {
            #         "system": gen_ret_infer[1][0]['content'],
            #         "input": gen_ret_infer[1][1]['content'],
            #         "output": gen_ret_infer[0],
            #         "save_id": selected_index[run_lang][i],
            #     }
            #     preview_cnt += 1
            #     print(f'Preview cnt: {preview_cnt}')
            #     with open(save_path, 'w') as f:
            #         json.dump(save_data, f, indent=4)
            # except Exception as e2:
            #     print(f'Error o1-preview: {traceback.format_exc()} at {run_lang}_{i} {l} level')
            #     error_o1_preview.append([save_path, e2])
            continue

print(f'Preview cnt: {preview_cnt}')
print(f'Error o1: {len(error_o1)}')
print(f'Error o1-preview: {len(error_o1_preview)}')