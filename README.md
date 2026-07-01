# mSCoRe

Benchmark and evaluation code for **"mSCoRe: a Multilingual and Scalable Benchmark for Skill-based Commonsense Reasoning"** (LREC-COLING 2026).

[Paper](https://doi.org/10.63317/5kajwk9dj3j9) &nbsp;|&nbsp; [🤗 Dataset](https://huggingface.co/datasets/ngotrnghia1811/mSCORE)

## Overview

mSCoRe evaluates LLMs' commonsense reasoning across **5 languages** and **10 reasoning skills**, with a dynamic complexity scaling mechanism that progressively increases task difficulty. It consists of two subsets:

- **mSCoRe-G** — General commonsense reasoning (English, German, French, Chinese, Japanese), built on mCSQA.
- **mSCoRe-S** — Social/cultural commonsense reasoning, built on CultureBank (TikTok + Reddit sources).

Each question is a multiple-choice commonsense problem with structured atomic reasoning steps, where each step is labeled with a specific reasoning skill. Complexity scales from level 0 (original) to level 6 through context expansion, option adjustment, and commonsense implicitation.

**5,600 instances** total (4,000 general + 1,600 social) across 4 complexity levels in the main benchmark.

## 📦 Dataset

The mSCoRe benchmark is available on HuggingFace:

[![HuggingFace Dataset](https://img.shields.io/badge/🤗_HuggingFace-mSCORE-yellow)](https://huggingface.co/datasets/ngotrnghia1811/mSCORE)

### Load the dataset

```python
from datasets import load_dataset

# Load any language-level config combo
dataset = load_dataset("ngotrnghia1811/mSCORE", "mcsqa-en", split="mcsqa-en")
print(dataset[0])
```

Available configs:
- General: `mcsqa-en`, `mcsqa-de`, `mcsqa-fr`, `mcsqa-zh`, `mcsqa-ja` 
- Social: `culturebank-tiktok`, `culturebank-reddit`

Each config has 4 complexity levels (L0–L3), totaling 5,600 instances.

## 📦 Dataset

The mSCoRe benchmark is available on HuggingFace:

[![HuggingFace Dataset](https://img.shields.io/badge/🤗_HuggingFace-mSCORE-yellow)](https://huggingface.co/datasets/ngotrnghia1811/mSCORE)

```python
from datasets import load_dataset

# Load any language-level config
# General: mcsqa-en, mcsqa-de, mcsqa-fr, mcsqa-zh, mcsqa-ja
# Social: culturebank-tiktok, culturebank-reddit
dataset = load_dataset("ngotrnghia1811/mSCORE", "mcsqa-en", split="mcsqa-en")
print(dataset[0])
```

**5,600 instances** across 7 configs × 4 complexity levels (L0–L3). Each instance includes the question, answer, options, reasoning process, and reasoning skills used.

## Setup

```bash
git clone https://github.com/ngotrnghia1811/mSCORE.git
cd mSCoRe
pip install -r requirements.txt
```

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-key-here"
```

## Evaluation

Scripts are provided for four reasoning evaluation settings, each for both mCSQA and CultureBank:

| Script | Setting | Dataset |
|--------|---------|---------|
| `scripts/run_all_skills.py` | All 10 skills (proposed taxonomy) | mCSQA |
| `scripts/run_cot.py` | Chain-of-Thought | mCSQA |
| `scripts/run_logic.py` | Logical skills only | mCSQA |
| `scripts/run_general.py` | 3 general categories | mCSQA |
| `scripts/culbank_run_all_skills.py` | All 10 skills | CultureBank |
| `scripts/culbank_run_cot.py` | Chain-of-Thought | CultureBank |
| `scripts/culbank_run_logic.py` | Logical skills only | CultureBank |
| `scripts/culbank_run_general.py` | 3 general categories | CultureBank |

Run an evaluation:

```bash
python scripts/run_all_skills.py
```

Set the language by editing `run_lang` at the top of each script (`en`, `de`, `fr`, `zh`, `ja`).

## Reasoning Skill Taxonomy

| Category | Skills |
|----------|--------|
| Logical | Inductive, Deductive, Abductive |
| Contextual | Analogical, Counterfactual, Probabilistic, Temporal, Spatial |
| Social & Ethical | Social, Moral |

## Main Results

Accuracy on **mSCoRe-G** (average across 5 languages, complexity levels L0–L3):

| Model | L0 | L1 | L2 | L3 |
|-------|:--:|:--:|:--:|:--:|
| GPT-4o | **79.2** | 74.9 | **73.1** | 69.5 |
| o1 | 76.6 | 71.3 | 68.5 | 65.3 |
| LLaMA-3.3-70B | 78.9 | **75.9** | 70.2 | **70.4** |
| R1-70B | 77.3 | 71.8 | 67.8 | 68.4 |
| Aya-32B | 76.4 | 69.8 | 66.4 | 65.0 |
| R1-8B | 64.7 | 56.8 | 55.5 | 53.2 |
| LLaMA-3.1-8B | 48.6 | 43.9 | 40.4 | 39.0 |

Accuracy on **mSCoRe-S** (average across TikTok + Reddit):

| Model | L0 | L1 | L2 | L3 |
|-------|:--:|:--:|:--:|:--:|
| LLaMA-3.3-70B | **81.8** | **75.8** | **76.8** | **74.8** |
| GPT-4o | 73.0 | 68.0 | 65.5 | 66.5 |
| o1 | 73.3 | 70.0 | 65.5 | 65.3 |
| R1-70B | 71.0 | 66.3 | 64.8 | 65.0 |
| Aya-32B | 69.5 | 60.8 | 62.0 | 60.0 |

## Project Structure

```
mSCoRe/
├── config/prompt/          # Multilingual prompt templates (en, de, fr, zh, ja)
├── models/
│   ├── generators/         # LLM generation (OpenAI API + HuggingFace)
│   └── evaluators/         # LLM-as-judge evaluation
├── modules/
│   ├── skill_reason.py     # Core reasoning evaluation class
│   └── dataset_processor.py# Dataset loaders (mCSQA, CultureBank)
├── scripts/                # Ready-to-run evaluation scripts
├── main.py
└── requirements.txt
```

## Citation

```bibtex
@inproceedings{ngo2026mscore,
    title     = {m{SCoRe}: a Multilingual and Scalable Benchmark for
                 Skill-based Commonsense Reasoning},
    author    = {Ngo, Nghia Trung and Dernoncourt, Franck and
                 Nguyen, Thien Huu},
    booktitle = {Proceedings of the 2026 Joint International Conference
                 on Computational Linguistics, Language Resources and
                 Evaluation (LREC-COLING 2026)},
    year      = {2026},
    pages     = {5095--5115},
    doi       = {10.63317/5kajwk9dj3j9},
}
```

## License

MIT
