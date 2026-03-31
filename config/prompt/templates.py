
from liquid import Template
from .icl_examples import EN_ICL_EXAMPLES as ICL_EXAMPLES


#SECTION: INPUT PROMPT

input_infer = Template('''
INPUT:
{{question}}

OUTPUT:
''')

input_gen = Template('''
INPUT:
{{question}}

OUTPUT:
''')


input_expand = Template('''
INPUT:
{{question}}

OUTPUT:
''')


input_implicit = Template('''
INPUT:
{{question}}

OUTPUT:
''')

#SECTION: ROLE PROMPT

llm_roles = {
    "commonsense_infer": 
      """
      You are a language model with advanced commonsense reasoning skills, capable of logical and analytical reasoning, heuristic and intuitive thinking, comparative and hypothetical analysis, and contextual and specialized understanding. 
      """,
    "commonsense_gen": 
      """
      You are a language model with advanced commonsense reasoning skills, capable of logical and analytical reasoning, heuristic and intuitive thinking, comparative and hypothetical analysis, and contextual and specialized understanding. 
      """,
    "culbank_gen": 
      """
      You are a language model with advanced commonsense reasoning skills, capable of logical and analytical reasoning, heuristic and intuitive thinking, comparative and hypothetical analysis, and contextual and specialized understanding. 
      """, 
    "commonsense_expand": 
      """
      You are a language model with advanced commonsense reasoning skills, capable of logical and analytical reasoning, heuristic and intuitive thinking, comparative and hypothetical analysis, and contextual and specialized understanding. 
      """,
    "commonsense_implicit": 
      """
      You are a language model with advanced commonsense reasoning skills, capable of logical and analytical reasoning, heuristic and intuitive thinking, comparative and hypothetical analysis, and contextual and specialized understanding. 
      """,
}


#SECTION: TASK DESCRIPTION
task_descriptions = {
    "commonsense_infer": 
      """
      Your task is to answer multi-choice commonsense questions by providing a detailed "REASONING PROCESS" that involves multiple "REASONING STEPs". Each "REASONING STEP" should be an "ATOMIC REASONING STEP" — an indivisible unit of reasoning that predominantly utilizes one reasoning skill. It is a single, coherent thought process that cannot be broken down into smaller steps without losing its meaning. The goal is to use the minimum number of steps necessary, ensuring that each step is non-redundant and contributes to narrowing down the possible options by eliminating one or more answer choices.
      """,
    "commonsense_gen": 
      """
      Given a multi-choice commonsense questions with the correct option, you task is to provide a "COMMONSENSE CONTEXT" to expand on the given question and a detailed "REASONING PROCESS" that involves multiple "REASONING STEPs" to arrive at the correct answer. 
        + A "COMMONSENSE CONTEXT" to the question refers to the background knowledge or additional details that are generally understood without requiring specialized knowledge, including factors such as time, place, social norms, cultural influences, and other relevant details that shape the understanding of the topic.
        + Each "REASONING STEP" should be an "ATOMIC REASONING STEP" — an Indivisible Unit of reasoning that predominantly utilizes one reasoning skill. It is a single, coherent thought process that cannot be broken down into smaller steps without losing its meaning. The "REASONING PROCESS" must be as efficent as possible, only using the minimum number of steps necessary, ensuring that each step is non-redundant and contributes to narrowing down the possible options by eliminating one or more answer choices.,
      """,
    "culbank_gen": 
      """
      Your task is to create a multiple-choice commonsense question based on a given cultural situation in the following format:
      {
          "cultural_topic": "culture group - topic - scenario",
          "social_context": "settings the behavior takes place",
          "actor": "who exhibit the behavior",
          "question": "the commonsense question regarding the actor's behavior",
          "actor_behavior": "behavior of the actor - which are highly agreed upon (the correct answer option)",
          "recipient": "recipient of the action",
          "relation": "relation between the actor and the recipient",
          "recipient_behavior": "behavior of the recipient",
      }
      The question should implicitly incorporate the cultural context, challenging the AI's ability to utilize commonsense reasoning to arrive at the correct answer. The goal is to test and enhance the AI's understanding of cultural norms and behaviors in a specific setting.
      Provide the detailed "REASONING PROCESS" the arrive at the correct anwser option that involves multiple "REASONING STEPs" to arrive at the correct answer. Each "REASONING STEP" should be an "ATOMIC REASONING STEP" — an Indivisible Unit of reasoning that predominantly utilizes one reasoning skill. It is a single, coherent thought process that cannot be broken down into smaller steps without losing its meaning. The "REASONING PROCESS" must be as efficent as possible, only using the minimum number of steps necessary, ensuring that each step is non-redundant and contributes to narrowing down the possible options by eliminating one or more answer choices.
      """, 
    "commonsense_expand": 
      """
        Given a multi-choice commonsense question with its options, your task is to modify and expand it to create a more complex question by expanding its context, modifying the question, adjusting the answer options, and adding an additional REASONING STEP. Your output should include the expanded context, the modified question, revised answer options, the correct answer, and a detailed "REASONING PROCESS".
      """,
    # "commonsense_implicit": 
    #   """
    #     Given a multi-choice commonsense question with its options, your task is to modify and expand it to create a more complex question by expanding its context, modifying the question, adjusting the answer options, and adding an additional REASONING STEP. Your output should include the expanded context, the modified question, revised answer options, the correct answer, and a detailed "REASONING PROCESS".
    #   """,
    "commonsense_implicit": 
      """
        Your task is to perform "Commonsense Implicitation," which involves combining a given "commonsense_context" with a "question" to generate a new, concise commonsense question that implicitly incorporates the original context. This process aims to evaluate the commonsense reasoning abilities of LLMs by ensuring that the implicit context preserves the original reasoning process and maintains the correctness of the answer.
      """,
}

#SECTION: REASONING SKILL
reasoning_skills = {
    'inductive_reasoning': {
        "short_description": "Drawing general conclusions from specific observations.",
        "long_description": "Inductive reasoning is a method of drawing general conclusions from specific observations. Unlike deductive reasoning, which starts with general premises to reach specific conclusions, inductive reasoning begins with detailed facts and builds up to broader generalizations or theories. This approach is commonly used in scientific research, where repeated experiments and observations lead to the formulation of overarching principles or hypotheses ",
        "abstract_example": "After witnessing several instances where Event A_1 leads to Event A_2, you infer that Event A_n will similarly result in Event A₂ in future occurrences",
        "concrete_example": "After witnessing several instances where the weather forecast predicts rain, you infer that rain will likely continue to fall in the future",
    },
    "deductive_reasoning": {
        "short_description": "Deriving specific conclusions from general premises.",
        "long_description": "Deductive reasoning involves deriving specific conclusions from general premises. It ensures that if the premises are true and the reasoning is valid, the conclusion must also be true. Deductive logic is fundamental in fields that require rigorous proof, such as mathematics and formal sciences.",
        "abstract_example": "Given the premise that All X are Y, and knowing that Object x₁ is an X, you deduce that Object x₁ must also be a Y.",
        "concrete_example": "Given All birds have feathers. A sparrow is a bird. Therefore, a sparrow has feathers"
    },
    "abductive_reasoning": {
        "short_description": "Forming hypotheses to explain observations.",
        "long_description": "Abductive reasoning is the process of forming hypotheses to explain observations. It starts with an incomplete set of observations and proceeds to the likeliest possible explanation. Unlike deductive and inductive reasoning, abductive reasoning seeks the simplest and most plausible explanation for a given set of facts, often leading to the generation of new theories or hypotheses.",
        "abstract_example": "Observing Event B, you hypothesize that Reason 2 is the most plausible explanation among several possible causes.",
        "concrete_example": "You wake up and see that the street is wet. The most likely explanation is that it rained last night."
    },
    "analogical_reasoning": {
        "short_description": "Drawing parallels between similar situations to infer conclusions.",
        "long_description": "Analogical reasoning involves drawing parallels between similar situations to infer conclusions. By comparing two objects or systems that share certain characteristics, one can infer that they may share additional, unobserved properties. This form of reasoning is widely used in problem-solving, scientific discovery, and legal reasoning to transfer knowledge from a known domain (source) to an unknown domain (target). Analogical reasoning is also used in everyday life to make inferences about the similarities between objects or situations.",
        "abstract_example": "Seeing that Component C_1₁ interacts with Component C_1_b in Situation C_a, you infer that Component C_2₁ and Component C_2_a will interact similarly in Situation C_b.",
        "abstract_example": "Think of Situation C_a, where Component C_a_1₁ interacts with Component C_a_2 in a specific way. You encounter Situation C_b with Component C_b_1 and Component C_b_2, and infer that Component C_b_1 and Component C_b_2 will interact similarly in Situation C_a.",
        "concrete_example": "Just as a gardener waters plants to help them grow, a teacher provides knowledge and guidance to help students develop."
    },
    "counterfactual_reasoning": {
        "short_description": "Considering alternative scenarios and outcomes that did not happen.",
        "long_description": "Counterfactual reasoning entails considering alternative scenarios and outcomes that did not occur. It involves imagining 'what might have happened' under different circumstances, which is useful for understanding causality, evaluating decisions, and planning future actions. Counterfactual reasoning is often used in fields such as philosophy, psychology, and business to explore the potential consequences of different choices or actions.",
        "abstract_example": "Reflecting on Condition X that didn’t occur, you imagine that if it had, Outcome Y might have replaced Outcome Z.",
        "concerte_example": "If you had left the house five minutes earlier, you would have caught the bus on time.",
    },
    "probabilistic_reasoning": {
        "short_description": "Applying principles of probability to make inferences under uncertainty.",
        "long_description": "Probabilistic reasoning involves applying principles of probability to make inferences under uncertainty. It enables individuals to assess the likelihood of different outcomes and make informed decisions based on the probability of various events occurring. This type of reasoning is crucial in fields like statistics, risk assessment, and artificial intelligence.",
        "abstract_example": "Evaluating that Option A has a higher probability (P(A) > P(B)) of success than Option B, you decide to choose Option A.",
        "concrete_example": "There’s a 70% chance of rain tomorrow, so you decide to carry an umbrella when you go out."
    },
    "temporal_reasoning": {
        "short_description": "Understanding sequences and durations of events.",
        "long_description": "Temporal reasoning is the ability to understand and reason about the sequence and duration of events over time. It involves comprehending time-specific data, such as the order of events, how long events last, and the relationships between different time points. Temporal reasoning is essential in areas like scheduling, planning, and understanding narratives.",
        "abstract_example": "Planning your day, you schedule Event T_1 to occur before Event T_2, ensuring the correct sequence of activities.",
        "concrete_example": "You observe that the sun will rise in the morning and set in the evening. You infer that the moon will rise and set at the same time."
    },
    "spatial_reasoning": {
        "short_description": "Visualizing and manipulating objects in space.",
        "long_description": "Spatial reasoning entails visualizing and manipulating objects in space. It involves understanding the relationships between different objects, such as their position, orientation, and movement relative to each other. Spatial reasoning is fundamental in fields like engineering, architecture, geography, and various forms of visual arts, enabling individuals to solve problems related to the physical arrangement and movement of object.",
        "abstract_example": "While arranging furniture, you visualize Object S_1 and Object S_2 to determine their optimal placement within the room.",
        "concrete_example": "A architect determining the best location for a window by visualizing the window and the surrounding walls to determine the optimal angle and height."
    },
    "social_reasoning": {
        "short_description": "Understanding social interactions and norms.",
        "long_description": "Social reasoning involves understanding social interactions and norms. It encompasses the ability to analyze and interpret social situations, recognize appropriate and inappropriate behaviors, and predict others' intentions, emotions, and thoughts. Effective social reasoning is crucial for building successful interpersonal relationships and navigating complex social environments.",
        "abstract_example": "Noticing that Person A behaves a certain way in Situation S, you adjust your own behavior (Behavior B) to interact effectively.",
        "concrete_example": "You notice that your friend looks upset after a conversation, so you decide to ask them if they’re okay."
    }, 
    "moral_reasoning": {
        "short_description": "Deciding what is right or wrong based on ethical principles.",
        "long_description": "Moral reasoning is the process of deciding what is right or wrong based on ethical principles. It involves evaluating actions, intentions, and consequences to make judgments about moral issues. Moral reasoning is central to ethical decision-making and is influenced by various factors, including societal norms, personal values, and philosophical theories.",
        "abstract_example": "Considering that Action M could harm Person C, you decide it is morally wrong and choose an alternative that respects ethical principles.",
        "concrete_example": "Seeing someone drop their wallet, you decide to return it instead of keeping the money inside because it’s the right thing to do."
    }
}

general_reasoning_skills = {
  "logical_reasoning": {
    "short_description": "Structured reasoning forms to derive conclusions.",
    "long_description": "Logical reasoning encompasses forms of reasoning that involve structured processes to derive conclusions from given information. This includes methodologies like deductive, inductive, and abductive reasoning, which are foundational in scientific and analytical disciplines to ensure conclusions are logically sound."
  },
  "contextual_reasoning": {
    "short_description": "Understanding relationships and contexts between elements.",
    "long_description": "Contextual reasoning includes skills used to understand relationships, contexts, and dynamics between elements. It covers various types of reasoning such as analogical, counterfactual, probabilistic, temporal, and spatial, used to evaluate scenarios, predict outcomes, and solve problems across different contexts."
  },
  "social_and_ethical_reasoning": {
    "short_description": "Reasoning related to social interactions and ethical principles.",
    "long_description": "Social and ethical reasoning involves skills focused on understanding social interactions and evaluating ethical principles. It includes social and moral reasoning, essential for interpreting behaviors, navigating complex social environments, and making decisions based on ethical considerations."
  }
}


#SECTION: OUTPUT FORMAT
output_formats = {
    "with_skills": '''
    ```json
    {
      "commonsense_question": "question_text",
      "options": {
          "A": "option_answer_text_A",
          ...
      },
      "correct_answer": ["answer_option", "answer_text"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "reasoning_skill_name",
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "reasoning_skill_name",
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          }
      }
    }
    ```
    ''',

    "with_context_and_skills": '''
    ```json
    {
      "commonsense_context": "context_text",
      "commonsense_question": "question_text",
      "options": {
          "A": "option_answer_text_A",
          ...
      },
      "correct_answer": ["answer_option", "answer_text"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "reasoning_skill_name",
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "reasoning_skill_name",
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          }
      }
    }
    ```
    ''',

    "without_skills": '''
    ```json
    {
      "commonsense_question": "question_text",
      "options": {
          "A": "option_answer_text_A",
          ...
      },
      "correct_answer": ["answer_option", "answer_text"]
    }
    ```
    ''',

    "with_context_without_skills": '''
    ```json
    {
      "commonsense_context": "context_text",
      "commonsense_question": "question_text",
      "options": {
          "A": "option_answer_text_A",
          ...
      },
      "correct_answer": ["answer_option", "answer_text"]
    }
    ```
    ''',
    "cot_without_skills": '''
    ```json
    {
      "commonsense_question": "question_text",
      "options": {
          "A": "option_answer_text_A",
          ...
      },
      "correct_answer": ["answer_option", "answer_text"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          },
          ...
          "reasoning_step_n": {
              "reasoning": "reasoning_text",
              "eliminated_options": [list_of_eliminated_options],
              "possible_options": [list_of_remaining_options]
          }
      }
    }
    ```
    '''
}

#SECTION: INFERENCE

logical_inference = f'''
Your task is to answer multi-choice commonsense questions. Provide your reasoning process using the following "REASONING SKILLS":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_logic_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_logic_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

general_inference = f'''
Your task is to answer multi-choice commonsense questions. Provide your reasoning process using the following "REASONING SKILLS":
    + logical_reasoning: {general_reasoning_skills["logical_reasoning"]["short_description"]}
    + contextual_reasoning: {general_reasoning_skills["contextual_reasoning"]["short_description"]}
    + social_and_ethical_reasoning: {general_reasoning_skills["social_and_ethical_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_general_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_general_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

standard_inference_o1 = f'''
Your task is to answer multi-choice commonsense questions. Provide your reasoning process using the following "REASONING SKILLS":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

standard_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Read the question carefully along with all the provided answer options.
2. Answer the question by choosing the correct answer option. 
3. Describe your step-by-step "REASONING PROCESS" to arrive at your answer. Each "ATOMIC REASONING STEP" must following this sequence:
	3.1. Choose a "REASONING SKILL" below to be used by the REASONING STEP:
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}
	3.2. Apply the choosen "REASONING SKILL": provide a concise explanation of how the chosen "REASONING SKILL" is applied to eliminate certain answer options or reinforce the correct answer option. Ensure the reasoning is clear and cannot be further divided into smaller steps.
	3.3. Eliminate Options: List the options eliminated in this step based on your reasoning.
	3.4. Update Possible Options: Provide the list of remaining possible options after this step.
4. Generate your output in the JSON format with the following structure:
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''


#! cot
cot_inference_o1 = f'''
Your task is to answer multi-choice commonsense questions and provide your reasoning process to find the correct answer. Generate your output in the JSON format with the following structure:
{output_formats["cot_without_skills"]}

'''

cot_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Read the question carefully along with all the provided answer options.
2. Answer the question by choosing the correct answer option. 
3. Describe your step-by-step "REASONING PROCESS" to arrive at your answer.
4. Generate your output in the JSON format with the following structure:
{output_formats["cot_without_skills"]}

'''

#SECTION: GENERATE

#! mCSQA
mcsqa_gen = f'''
### LLM ROLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Question Comprehension: Read the question carefully along with all the provided answer options.
2. Adding The "COMMONSENSE CONTEXT": Expand on the original question by providing an additional "COMMONSENSE CONTEXT". Ensure that the added context is relevant and enriches the understanding of the question.
3. Describe your Step-by-Step "REASONING PROCESS" to arrive at the correct answer. Each "ATOMIC REASONING STEP" must following this sequence:
	3.1. Choose a REASONING SKILL below to be used by the REASONING STEP:
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}
	3.2. Apply the choosen "REASONING SKILL": provide a concise explanation of how the chosen "REASONING SKILL" is applied to eliminate certain answer options or reinforce the correct answer option. Ensure the reasoning is clear and cannot be further divided into smaller steps.
	3.3. Eliminate Options: List the options eliminated in this step based on your reasoning.
	3.4. Update Possible Options: Provide the list of remaining possible options after this step.
4. Generate your output in the JSON format with the following structure:
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["mcsqa_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["mcsqa_gen_1"]["output"]} \n
EXAMPLE 2 - INPUT :
{ICL_EXAMPLES["mcsqa_gen_2"]["input"]} \n
EXAMPLE 2 - OUTPUT :
{ICL_EXAMPLES["mcsqa_gen_2"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

#! CultureBank
culbank_gen = f'''
### LLM ROLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["culbank_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Analyze the Provided Cultural Situation: Review the details of the cultural group, context, actor behaviors, and other descriptions to understand the key elements of the situation.
2. Adding The "COMMONSENSE CONTEXT": Based on the context given in the input, A "COMMONSENSE CONTEXT" to the question refers to the background knowledge or additional details that are generally understood without requiring specialized knowledge, including factors such as time, place, social norms, cultural influences, and other relevant details that shape the understanding of the topic.
3. Create the "Commonsense Question": Combine the cultural context and the persona's inquiry to formulate a concise question. Ensure the question IMPLICITLY incorporates the original context without explicitly stating it. Create the correct answer option based on the "actor_behavior"
4. Provide Other Answer Options: Create 5 multiple-choice options (including the correct answer from the previous step). Two of which should be plausible options. The other two should be distractors that are relevant and reasonable but incorrect based on the cultural context.
5. Describe your Step-by-Step "REASONING PROCESS" to arrive at the correct answer. Each "ATOMIC REASONING STEP" must following this sequence:
	5.1. Choose a "REASONING SKILL" below to be used by the "REASONING STEP":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}
	5.2. Apply the choosen "REASONING SKILL": provide a concise explanation of how the chosen "REASONING SKILL" is applied to eliminate certain answer options or reinforce the correct answer option. Ensure the reasoning is clear and cannot be further divided into smaller steps.  
	5.3. Eliminate Options: List the options eliminated in this step based on your reasoning.
	5.4. Update Possible Options: Provide the list of remaining possible options after this step.
6. Generate your output in the JSON format with the following structure:
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["culbank_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["culbank_gen_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

#! Complexity
expand_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_expand"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_expand"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Question Comprehension: Carefully read the given question and the context, and its answer options.
2. Context Expansion: adding additional backgound or situaltional details to the "COMMONSENSE CONTEXT" to add depth and reasoning requirements to the question.
3. Question Modificatioin:  Utilize the "EXPANDED COMMONSENSE CONTEXT" to craft a more complex question while maintaining its core concept and commonsense.
4. Option Adjustments: 
	+ Adjust the existing answer options to align with the new complex question
	+ Ensure the correct answer option remains semantically similar to the original
	+ Introduce an additional plausible but incorrect option to increase the complexity of the question
	+ Keep all answer options as concise as the originals
5. Reasoning Refinements: Refine the original "REASONING PROCESS" to fit the new context. The additional "ATOMIC REASONING STEP" must use one of the following "REASONING SKILLs":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}
6. Format the Output using JSON format with the following structure:
 {output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["expand_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["expand_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''

#! Implicitation
implicit_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_implicit"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_implicit"]} \n
### STEP-BY-STEP INSTRUCTIONS
Following these Step-by-Step Instructions:
1. Analyze the provided "commonsense_context" to understand the underlying assumptions and implicit knowledge required for reasoning
2. Examine the "commonsense_question" and its associated "options" to identify key elements essential for answering the question
3. Rewrite the "commonsense_question" by combining the original context and question to create a more new "commonsense_question" with an "IMPLICITLY IMPLIED COMMONSENSE CONTEXT". Ensure that the new question remains clear and understandable
4. Verify that the "REASONING PROCESS" remains unchanged in the transformed question, and confirm that the correct answer remains the same as in the original
5. Ensure that all answer options are reasonable, relevant, and maintain their original intent in the context of the rewritten question
6. Retain the structure and content of the "reasoning" section to reflect the logical steps supporting the correct answer. The  "ATOMIC REASONING STEP" must use one of the following "REASONING SKILLs":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
    + analogical_reasoning: {reasoning_skills["analogical_reasoning"]["short_description"]}
    + counterfactual_reasoning: {reasoning_skills["counterfactual_reasoning"]["short_description"]}
    + probabilistic_reasoning: {reasoning_skills["probabilistic_reasoning"]["short_description"]}
    + temporal_reasoning: {reasoning_skills["temporal_reasoning"]["short_description"]}
    + spatial_reasoning: {reasoning_skills["spatial_reasoning"]["short_description"]}
    + social_reasoning: {reasoning_skills["social_reasoning"]["short_description"]}
    + moral_reasoning: {reasoning_skills["moral_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["implicit_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["implicit_1"]["output"]} \n

### OUTPUT REMINDER
Ensure that your output follows the JSON structure as instructed and demonstrated in the in-context example.
'''


#SECTION: EVALUATE

#! QA Evaluation

#! Reason Evaluation

step_wise_eval = {

}

process_wise_eval = {

}


