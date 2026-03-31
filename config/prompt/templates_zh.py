
from liquid import Template
from .icl_examples import ZH_ICL_EXAMPLES as ICL_EXAMPLES


#SECTION: INPUT PROMPT

input_infer = Template('''
输入：
{{question}}

输出：
''')

input_gen = Template('''
输入：
{{question}}

输出：
''')


input_expand = Template('''
输入：
{{question}}

输出：
''')


input_implicit = Template('''
输入：
{{question}}

输出：
''')

#SECTION: ROLE PROMPT

llm_roles = {
    "commonsense_infer": 
      """
      您是一个具备高级常识推理技能的语言模型，能够进行逻辑和分析推理、启发式和直觉思维、比较和假设分析，以及情境和专业理解。
      """,
    "commonsense_gen": 
      """
      您是一个具备高级常识推理技能的语言模型，能够进行逻辑和分析推理、启发式和直觉思维、比较和假设分析，以及情境和专业理解。
      """,
    "culbank_gen": 
      """
      您是一个具备高级常识推理技能的语言模型，能够进行逻辑和分析推理、启发式和直觉思维、比较和假设分析，以及情境和专业理解。
      """, 
    "commonsense_expand": 
      """
      您是一个具备高级常识推理技能的语言模型，能够进行逻辑和分析推理、启发式和直觉思维、比较和假设分析，以及情境和专业理解。
      """,
    "commonsense_implicit": 
      """
      您是一个具备高级常识推理技能的语言模型，能够进行逻辑和分析推理、启发式和直觉思维、比较和假设分析，以及情境和专业理解。
      """,
}



#SECTION: TASK DESCRIPTION
task_descriptions = {
    "commonsense_infer": 
      """
      您的任务是通过提供详细的"推理过程"回答多项选择的常识问题，该过程涉及多个"推理步骤"。每个"推理步骤"应为"原子推理步骤"——一个主要运用一种推理技能的不可分割的推理单元。这是一个完整的、连贯的思维过程，不能被分解为更小的步骤，否则会失去意义。目标是使用最少数量的步骤，确保每个步骤都是不冗余的，且通过排除一个或多个答案选项来缩小可能的选项范围。
      """,
    "commonsense_gen": 
      """
      给定一个带有正确选项的多项选择常识问题，您的任务是提供"常识背景"以扩展给定的问题，并提供涉及多个"推理步骤"以得出正确答案的详细"推理过程"。
        + 问题的"常识背景"是指通常不需要专业知识就能理解的背景知识或附加细节，包括时间、地点、社会规范、文化影响及其他相关细节等。
        + 每个"推理步骤"应为"原子推理步骤"——一个主要运用一种推理技能的不可分割的推理单元。这是一个完整的、连贯的思维过程，不能被分解为更小的步骤，否则会失去意义。"推理过程"必须尽可能高效，仅使用必要的最少步骤，确保每个步骤都是不冗余的，并通过排除一个或多个答案选项来缩小可能的选项范围。
      """,
    "culbank_gen": 
      """
      您的任务是根据给定的文化情境创建一个多项选择的常识问题，格式如下：
      {
          "cultural_topic": "文化群体 - 主题 - 场景",
          "social_context": "行为发生的环境",
          "actor": "展示行为的人",
          "question": "关于该行为者行为的常识问题",
          "actor_behavior": "行为者的行为 - 高度一致同意（正确答案选项）",
          "recipient": "行为的受体",
          "relation": "行为者和受体之间的关系",
          "recipient_behavior": "受体的行为",
      }
      问题应该隐含地结合文化背景，挑战AI利用常识推理能力得出正确答案。目标是测试和增强AI对特定环境中的文化规范和行为的理解。
      提供详细的"推理过程"以得出正确答案选项，该过程包含多个"推理步骤"来得出正确答案。每个"推理步骤"应为"原子推理步骤"——一个主要运用一种推理技能的不可分割的推理单元。这是一个完整的、连贯的思维过程，不能被分解为更小的步骤，否则会失去意义。"推理过程"必须尽可能高效，仅使用必要的最少步骤，确保每个步骤都是不冗余的，并通过排除一个或多个答案选项来缩小可能的选项范围。
      """, 
    "commonsense_expand": 
      """
        给定一个具有多个选项的多项选择常识问题，您的任务是通过扩展其上下文、修改问题、调整答案选项，并添加一个额外的推理步骤，以创建一个更复杂的问题。您的输出应包括扩展后的背景、修改后的问题、修订的答案选项、正确答案以及详细的"推理过程"。
      """,
    "commonsense_implicit": 
      """
        给定一个具有多个选项的多项选择常识问题，您的任务是通过扩展其上下文、修改问题、调整答案选项，并添加一个额外的推理步骤，以创建一个更复杂的问题。您的输出应包括扩展后的背景、修改后的问题、修订的答案选项、正确答案以及详细的"推理过程"。
      """,
}


#SECTION: REASONING SKILL
reasoning_skills = {
    'inductive_reasoning': {
        "short_description": "从具体观察中得出一般结论。",
        "long_description": "归纳推理是一种从具体观察中得出一般结论的方法。不同于演绎推理从一般前提推导出具体结论，归纳推理从详细事实开始构建到更广泛的概括或理论。这种方法在科学研究中广泛使用，在重复实验和观察的基础上形成全面的原则或假设。",
        "abstract_example": "在观察到多个实例中事件A_1导致事件A_2后，你推断在未来的事件A_n也将类似地导致事件A_2。",
        "concrete_example": "在观察到几次天气预报预测下雨后，你推断未来很可能雨依旧会下。"
    },
    "deductive_reasoning": {
        "short_description": "从一般前提出发推导出具体结论。",
        "long_description": "演绎推理涉及从一般前提出发推导出具体结论。它确保如果前提是真实的且推理是有效的，那么结论也必须是真实的。演绎逻辑在需要严谨证明的领域至关重要，例如数学和形式科学。",
        "abstract_example": "鉴于前提是所有X都是Y，并且知道对象x₁是X，你推演出对象x₁也一定是Y。",
        "concrete_example": "所有鸟有羽毛。麻雀是鸟。因此麻雀有羽毛。"
    },
    "abductive_reasoning": {
        "short_description": "形成假设以解释观察。",
        "long_description": "溯因推理是形成假设以解释观察的过程。它从一个不完整的观察集开始，推断出最可能的解释。与演绎和归纳推理不同，溯因推理寻求给定一组事实的最简单和最合理的解释，常常带来新理论或假设的生成。",
        "abstract_example": "观察到事件B，你假设原因2是在几个可能原因中最合理的解释。",
        "concrete_example": "你醒来看见街道是湿的，最可能的解释是昨晚下雨了。"
    },
    "analogical_reasoning": {
        "short_description": "在类似情况下绘制平行关系以推断结论。",
        "long_description": "类比推理涉及在类似情况下绘制平行关系以推断结论。通过比较分享某些特征的两个对象或系统，可以推测它们可能分享额外的、未观察到的属性。这种推理形式在解决问题、科学发现和法律推理中广泛使用，以将已知领域（源域）的知识转移到未知领域（目标域）。类比推理在日常生活中也被用来对对象或情况之间的相似性做出推测。",
        "abstract_example": "看到组件C_1₁在情景C_a中与组件C_1_b互动，你推断组件C_2₁和组件C_2_a在情景C_b中将以类似方式互动。",
        "concrete_example": "就像园丁给植物浇水以帮助它们生长，老师提供知识和指导以帮助学生发展。"
    },
    "counterfactual_reasoning": {
        "short_description": "考虑没有发生的替代情景和结果。",
        "long_description": "反事实推理包括考虑未发生的替代情景和结果。它涉及想象在不同情况下“可能会发生什么”，对于理解因果关系、评估决策和规划未来行动非常有用。反事实推理常用于哲学、心理学和商业等领域，以探索不同选择或行动的潜在后果。",
        "abstract_example": "回顾没有发生的条件X，你想象如果它发生了，结果Y可能会替代结果Z。",
        "concrete_example": "如果你早点离开家五分钟，你本可以准时赶上公共汽车。"
    },
    "probabilistic_reasoning": {
        "short_description": "应用概率原理在不确定性下进行推断。",
        "long_description": "概率推理包括应用概率原理在不确定性下进行推断。它使个人能够评估不同结果的可能性，并根据各种事件发生的概率做出明智的决定。这种类型的推理在统计、风险评估和人工智能等领域至关重要。",
        "abstract_example": "评估选项A的成功概率（P(A) > P(B)）高于选项B，你决定选择选项A。",
        "concrete_example": "明天有70％的几率下雨，所以你决定出门时带把雨伞。"
    },
    "temporal_reasoning": {
        "short_description": "理解事件的顺序和持续时间。",
        "long_description": "时间推理是一种理解和推理事件在时间上的顺序和持续时间的能力。它涉及理解时间特定数据，例如事件顺序、事件持续时间和不同时间点之间的关系。时间推理在调度、规划和理解叙述方面至关重要。",
        "abstract_example": "规划你的一天，你安排事件T_1在事件T_2之前发生，以确保活动的正确顺序。",
        "concrete_example": "你观察到太阳将在上午升起并在晚上落山。你推测月亮将在同一时间升起和落下。"
    },
    "spatial_reasoning": {
        "short_description": "在空间中可视化和操纵对象。",
        "long_description": "空间推理涉及在空间中可视化和操纵对象。它涉及理解不同对象之间的关系，例如它们相对于彼此的位置、方向和移动。空间推理在工程、建筑、地理和各种形式的视觉艺术等领域是基础的，帮助个人解决与物体物理排列和移动相关的问题。",
        "abstract_example": "在排列家具时，你可视化对象S_1和对象S_2，以确定它们在房间内的最佳位置。",
        "concrete_example": "建筑师通过可视化窗户和周围的墙壁来确定最佳位置，从而决定窗户的最佳角度和高度。"
    },
    "social_reasoning": {
        "short_description": "理解社会互动和规范。",
        "long_description": "社会推理涉及理解社会互动和规范。它包括分析和解释社会情境的能力，识别适当和不当的行为，并预测他人的意图、情感和想法。有效的社交推理对于建立成功的人际关系和驾驭复杂的社交环境至关重要。",
        "abstract_example": "注意到人A在情境S中以某种方式表现，你调整自己的行为（行为B）以有效互动。",
        "concrete_example": "你注意到你的朋友在一次谈话后看起来不高兴，所以你决定问他们是否还好。"
    }, 
    "moral_reasoning": {
        "short_description": "根据伦理原则决定对错。",
        "long_description": "道德推理是指根据伦理原则决定对错的过程。它包括评估行动、意图和结果，以对道德问题做出判断。道德推理是伦理决策的核心，受各种因素影响，包括社会规范、个人价值观和哲学理论。",
        "abstract_example": "考虑到行动M可能会伤害人C，你决定这是道德上错误的，并选择一种尊重伦理原则的替代方案。",
        "concrete_example": "看到有人掉了钱包，你决定归还它而不是拿走里面的钱，因为这是正确的做法。"
    }
}

general_reasoning_skills = {
  "logical_reasoning": {
    "short_description": "用结构化的方法推导结论。",
    "long_description": "逻辑推理包括涉及结构化过程的推理形式，以从给定信息中推导结论。这包括演绎、归纳和溯因推理等方法，这些方法是科学和分析学科中的基础，以确保结论在逻辑上是合理的。"
  },
  "contextual_reasoning": {
    "short_description": "理解元素之间的关系和背景。",
    "long_description": "情境推理包括用于理解元素之间关系、背景和动态的技能。它涵盖了类比、反事实、概率、时间和空间等各种推理类型，用于评估场景、预测结果和解决不同背景下的问题。"
  },
  "social_and_ethical_reasoning": {
    "short_description": "与社会互动和道德原则相关的推理。",
    "long_description": "社会和道德推理包括专注于理解社会互动和评估道德原则的技能。它包括社会和道德推理，对解释行为、驾驭复杂的社会环境以及基于道德考量作出决策至关重要。"
  }
}


#SECTION: OUTPUT FORMAT
output_formats = {
    "with_skills": '''
    ```json
    {
      "commonsense_question": "问题文本",
      "options": {
          "A": "选项答案文本_A",
          ...
      },
      "correct_answer": ["答案选项", "答案文本"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "推理技能名称",
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "推理技能名称",
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          }
      }
    }
    ```
    ''',

    "with_context_and_skills": '''
    ```json
    {
      "commonsense_context": "背景文本",
      "commonsense_question": "问题文本",
      "options": {
          "A": "选项答案文本_A",
          ...
      },
      "correct_answer": ["答案选项", "答案文本"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "推理技能名称",
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "推理技能名称",
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          }
      }
    }
    ```
    ''',

    "without_skills": '''
    ```json
    {
      "commonsense_question": "问题文本",
      "options": {
          "A": "选项答案文本_A",
          ...
      },
      "correct_answer": ["答案选项", "答案文本"]
    }
    ```
    ''',

    "with_context_without_skills": '''
    ```json
    {
      "commonsense_context": "背景文本",
      "commonsense_question": "问题文本",
      "options": {
          "A": "选项答案文本_A",
          ...
      },
      "correct_answer": ["答案选项", "答案文本"]
    }
    ```
    ''',

    "cot_without_skills": '''
    ```json
    {
      "commonsense_question": "问题文本",
      "options": {
          "A": "选项答案文本_A",
          ...
      },
      "correct_answer": ["答案选项", "答案文本"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          },
          ...
          "reasoning_step_n": {
              "reasoning": "推理文本",
              "eliminated_options": [已排除选项列表],
              "possible_options": [剩余选项列表]
          }
      }
    }
    ```
    '''
}


#SECTION: INFERENCE

logical_inference = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	3.1. 选择一个如下的推理技能用于该REASONING STEP：
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}
	3.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或强化正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。
	3.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	3.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_logic_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_logic_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''

general_inference = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	3.1. 选择一个如下的推理技能用于该REASONING STEP：
    + logical_reasoning: {general_reasoning_skills["logical_reasoning"]["short_description"]}
    + contextual_reasoning: {general_reasoning_skills["contextual_reasoning"]["short_description"]}
    + social_and_ethical_reasoning: {general_reasoning_skills["social_and_ethical_reasoning"]["short_description"]}
	3.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或强化正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。
	3.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	3.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_general_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_general_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''

#NOTE: standard_inference_o1 is the same as standard_inference_4o for zh
standard_inference_o1 = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	3.1. 选择一个如下的推理技能用于该REASONING STEP：
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
	3.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或强化正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。
	3.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	3.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''

standard_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	3.1. 选择一个如下的推理技能用于该REASONING STEP：
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
	3.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或强化正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。
	3.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	3.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''

#! cot
cot_inference_o1 = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["cot_without_skills"]}

'''

cot_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 仔细阅读问题及所有提供的答案选项。
2. 通过选择正确的答案选项来回答问题。
3. 描述您到达答案的逐步"REASONING PROCESS"。
4. 生成您的输出，使用下列结构的JSON格式：
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
按照以下步骤逐步进行：
1. 问题理解：仔细阅读问题及所有提供的答案选项。
2. 添加"COMMONSENSE CONTEXT"：通过提供额外的"COMMONSENSE CONTEXT"来扩展原始问题。确保添加的背景相关且增强了对问题的理解。
3. 描述您的逐步"REASONING PROCESS"以得出正确答案。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	3.1. 选择一个如下的推理技能用于该REASONING STEP：
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
	3.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或强化正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。
	3.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	3.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
4. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT:
{ICL_EXAMPLES["mcsqa_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT:
{ICL_EXAMPLES["mcsqa_gen_1"]["output"]} \n
EXAMPLE 2 - INPUT:
{ICL_EXAMPLES["mcsqa_gen_2"]["input"]} \n
EXAMPLE 2 - OUTPUT:
{ICL_EXAMPLES["mcsqa_gen_2"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''


#! CultureBank
culbank_gen = f'''
### LLM ROLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["culbank_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 分析提供的文化情境：查看文化群体、情境、行为者行为和其他描述的细节，以理解情境的关键要素。
2. 添加"COMMONSENSE CONTEXT"：基于输入中给定的上下文，对问题的"COMMONSENSE CONTEXT"是指无需专业知识即可理解的背景知识或附加细节，包括时间、地点、社会规范、文化影响和其他塑造对主题理解的相关细节。
3. 创建"Commonsense Question"：结合文化背景和角色的询问，制定一个简洁的问题。确保问题隐含地融入原始上下文而不明确说明它。基于"actor_behavior"创建正确答案选项。
4. 提供其他答案选项：创建5个多项选择(包括上一步中的正确答案)。其中两个应该是合理的选项。 另外两个应该是与文化背景相关且合理但在文化背景下不正确的干扰选项。
5. 描述您的逐步"REASONING PROCESS"以得出正确答案。每个"ATOMIC REASONING STEP"必须遵循此顺序：
	5.1. 选择一个如下的推理技能用于该"REASONING STEP":
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
	5.2. 应用选择的"Reasoning Skill"：提供一个简明的解释，说明所选的"Reasoning Skill"如何用于排除某些答案选项或增强正确答案选项。确保推理清晰且不可进一步分割为更小的步骤。 
	5.3. 消除选项：列出在此步骤中基于您的推理被排除的选项。
	5.4. 更新可能的选项：提供此步骤后剩余可能选项的列表。
6. 生成您的输出，使用下列结构的JSON格式：
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT:
{ICL_EXAMPLES["culbank_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT:
{ICL_EXAMPLES["culbank_gen_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''


#! Complexity
expand_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_expand"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_expand"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 问题理解：仔细阅读给定的问题、背景及其答案选项。
2. 背景扩展：在"COMMONSENSE CONTEXT"中添加额外的背景或情境细节，以增加问题的深度和推理要求。
3. 问题修改：利用"EXPANDED COMMONSENSE CONTEXT"来设计一个更复杂的问题，同时保持其核心概念和常识。
4. 选项调整：
	+ 调整现有的答案选项以适应新的复杂问题
	+ 确保正确答案选项在语义上与原始选项相似
	+ 引入一个额外的合理但不正确的选项，以增加问题的复杂性
	+ 保持所有答案选项的简洁性与原始选项一致
5. 推理精炼：调整原始的"REASONING PROCESS"以适应新的背景。新增的"ATOMIC REASONING STEP"必须使用以下"Reasoning Skills"之一：
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
6. 使用以下结构以JSON格式生成输出：
 {output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT:
{ICL_EXAMPLES["expand_1"]["input"]} \n
EXAMPLE 1 - OUTPUT:
{ICL_EXAMPLES["expand_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''


#! Implicitation
implicit_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_implicit"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_implicit"]} \n
### STEP-BY-STEP INSTRUCTIONS
按照以下步骤逐步进行：
1. 分析提供的"commonsense_context"，以理解推理所需的潜在假设和隐含知识。
2. 检查"commonsense_question"及其相关的"options"，以识别回答问题所需的关键要素。
3. 通过结合原始上下文和问题重写"commonsense_question"，以创建一个带有"IMPLICITLY IMPLIED COMMONSENSE CONTEXT"的新"commonsense_question"。确保新问题仍然清晰可理解。
4. 验证在变换的问题中"REASONING PROCESS"保持不变，并确认正确答案与原始答案相同。
5. 确保所有答案选项在重写问题的上下文中是合理的、相关的，并保持其原意。
6. 保留"reasoning"部分的结构和内容，以反映支持正确答案的逻辑步骤。"ATOMIC REASONING STEP"必须使用以下"Reasoning Skills"之一：
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
EXAMPLE 1 - INPUT:
{ICL_EXAMPLES["implicit_1"]["input"]} \n
EXAMPLE 1 - OUTPUT:
{ICL_EXAMPLES["implicit_1"]["output"]} \n

### OUTPUT REMINDER
确保您的输出遵循指示和示范的上下文示例中的JSON结构。
'''