from liquid import Template
from .icl_examples import JA_ICL_EXAMPLES as ICL_EXAMPLES


#SECTION: INPUT PROMPT

input_infer = Template('''
入力:
{{question}}

出力:
''')

input_gen = Template('''
入力:
{{question}}

出力:
''')

input_expand = Template('''
入力:
{{question}}

出力:
''')

input_implicit = Template('''
入力:
{{question}}

出力:
''')

#SECTION: ROLE PROMPT

llm_roles = {
    "commonsense_infer": 
      """
      あなたは高度な常識的推論能力を備えた言語モデルです。論理的かつ分析的な推論、ヒューリスティックかつ直感的な思考、比較および仮説的な分析、そして文脈に基づいた専門的理解が可能です。 
      """,
    "commonsense_gen": 
      """
      あなたは高度な常識的推論能力を備えた言語モデルです。論理的かつ分析的な推論、ヒューリスティックかつ直感的な思考、比較および仮説的な分析、そして文脈に基づいた専門的理解が可能です。 
      """,
    "culbank_gen": 
      """
      あなたは高度な常識的推論能力を備えた言語モデルです。論理的かつ分析的な推論、ヒューリスティックかつ直感的な思考、比較および仮説的な分析、そして文脈に基づいた専門的理解が可能です。 
      """, 
    "commonsense_expand": 
      """
      あなたは高度な常識的推論能力を備えた言語モデルです。論理的かつ分析的な推論、ヒューリスティックかつ直感的な思考、比較および仮説的な分析、そして文脈に基づいた専門的理解が可能です。 
      """,
    "commonsense_implicit": 
      """
      あなたは高度な常識的推論能力を備えた言語モデルです。論理的かつ分析的な推論、ヒューリスティックかつ直感的な思考、比較および仮説的な分析、そして文脈に基づいた専門的理解が可能です。 
      """,
}


#SECTION: TASK DESCRIPTION
task_descriptions = {
    "commonsense_infer": 
      """
      あなたのタスクは、詳細な"REASONING PROCESS"を提供し、複数の"REASONING STEP"を伴うことで、マルチチョイスの常識的な質問に答えることです。各"REASONING STEP"は"ATOMIC REASONING STEP"であるべきです — 主に1つの推論スキルを利用する不可分な推論単位。それは意味を失うことなく小さなステップに分解できない単一の、一貫した思考過程です。目的は、必要最小限のステップを使用し、各ステップが冗長でないことを保証し、1つまたは複数の選択肢を排除することによって可能な選択肢が絞り込まれるようにすることです。
      """,
    "commonsense_gen": 
      """
      正しい選択肢があるマルチチョイスの常識的な質問に基づいて、与えられた質問を拡充するための"COMMONSENSE CONTEXT"と、正しい答えに到達するために複数の"REASONING STEP"を伴う詳細な"REASONING PROCESS"を提供することがあなたのタスクです。
        + 質問に対する"COMMONSENSE CONTEXT"とは、一般に専門知識を必要とせずに理解される背景知識や追加の詳細を指し、時間、場所、社会的規範、文化的影響、その他のトピックの理解を形成する関連詳細を含みます。
        + 各"REASONING STEP"は"ATOMIC REASONING STEP"であるべきです — 主に1つの推論スキルを利用する不可分な推論単位。それは意味を失うことなく小さなステップに分解できない単一の、一貫した思考過程です。"REASONING PROCESS"は可能な限り効率的でなければならず、必要最小限のステップを使用し、各ステップが冗長でないことを保証し、1つまたは複数の選択肢を排除することによって可能な選択肢を絞り込むことに寄与します。
      """,
    "culbank_gen": 
      """
      あなたのタスクは、次の形式で与えられた文化的状況に基づいてマルチチョイスの常識的な質問を作成することです：
      {
          "cultural_topic": "文化グループ - トピック - シナリオ",
          "social_context": "行動が行われる環境",
          "actor": "行動を示す人",
          "question": "行動者の行動に関する常識的な質問",
          "actor_behavior": "行動者の行動 - 高く同意されたもの（正しい答えの選択肢）",
          "recipient": "行動の受取人",
          "relation": "行動者と受取人の関係",
          "recipient_behavior": "受取人の行動",
      }
      質問は文化的背景を暗に取り入れ、AIが常識的な推論を活用して正しい答えを出す能力を試すものであるべきです。目的は、特定の状況における文化的規範や行動に関するAIの理解をテストし、強化することです。正しい回答選択肢に至るための詳細な"REASONING PROCESS"を提供し、それには複数の"REASONING STEP"が含まれているべきです。各"REASONING STEP"は"ATOMIC REASONING STEP"であるべきです — 主に1つの推論スキルを利用する不可分な推論単位。それは意味を失うことなく小さなステップに分解できない単一の、一貫した思考過程です。"REASONING PROCESS"は可能な限り効率的でなければならず、必要最小限のステップを使用し、各ステップが冗長でないことを保証し、1つまたは複数の選択肢を排除することによって可能な選択肢を絞り込むことに寄与します。
      """, 
    "commonsense_expand":
      """
        選択肢とともに与えられたマルチチョイスの常識的な質問を基に、より複雑な質問を作成するためにその文脈を拡張し、質問を修正し、回答選択肢を調整し、追加のREASONING STEPを追加してください。出力には、展開された文脈、修正された質問、修正された選択肢、正しい答え、および詳細な"REASONING PROCESS"が含まれているべきです。
      """,
    "commonsense_implicit": 
      """
        選択肢とともに与えられたマルチチョイスの常識的な質問を基に、より複雑な質問を作成するためにその文脈を拡張し、質問を修正し、回答選択肢を調整し、追加のREASONING STEPを追加してください。出力には、展開された文脈、修正された質問、修正された選択肢、正しい答え、および詳細な"REASONING PROCESS"が含まれているべきです。
      """,
}


#SECTION: REASONING SKILL
reasoning_skills = {
    'inductive_reasoning': {
        "short_description": "特定の観察から一般的な結論を導く。",
        "long_description": "帰納的推論は、特定の観察から一般的な結論を導く方法です。演繹的推論と異なり、一般的な前提から具体的な結論を導くのではなく、詳細な事実から広い一般化や理論へと築き上げていきます。このアプローチは科学的研究でよく使用され、繰り返される実験や観察が包括的な原則や仮説の形成に繋がります。",
        "abstract_example": "Event A_1がEvent A_2を引き起こした事例をいくつか目撃した後、将来的にはEvent A_nもEvent A₂を引き起こすと推論します",
        "concrete_example": "天気予報が雨を予測した事例をいくつか目撃した後、将来的にも雨が降り続く可能性が高いと推論します",
    },
    "deductive_reasoning": {
        "short_description": "一般的な前提から具体的な結論を導き出す。",
        "long_description": "演繹的推論は、一般的な前提から具体的な結論を導き出します。前提が真であり、推論が有効であれば、結論もまた必ず真であることを保証します。演繹的ロジックは、数学や形式科学のような厳密な証明を必要とする分野で基本的なものです。",
        "abstract_example": "すべてのXがYであるという前提、およびObject x₁がXであることを知っている場合、Object x₁もまたYでなければならないと推測します。",
        "concrete_example": "すべての鳥は羽を持っています。スズメは鳥です。したがって、スズメには羽があります。"
    },
    "abductive_reasoning": {
        "short_description": "観察を説明する仮説を形成する。",
        "long_description": "仮説形成は、観察を説明するための仮説を形成するプロセスです。これにより、観察の不完全なセットから最も可能性の高い説明へと進みます。演繹的および帰納的推論とは異なり、仮説形成は、与えられた事実のセットに対して最も単純で最も合理的な説明を求め、新しい理論や仮説の生成にしばしば繋がります。",
        "abstract_example": "Event Bを観察し、いくつかの可能性のある原因の中で、Reason 2が最も妥当な説明であると仮説します。",
        "concrete_example": "起きてみると、通りが濡れています。最も可能性が高い説明は、昨夜雨が降ったということです。"
    },
    "analogical_reasoning": {
        "short_description": "似た状況間で類似性を見つけて結論を引き出す。",
        "long_description": "類推的推論は、似た状況間で類似性を見つけて結論を引き出すことです。ある特徴を共有する2つの対象またはシステムを比較することで、彼らが追加の観察されていない特性を共有する可能性を推測します。この形の推論は、問題解決、科学的発見、法律上の推論で広く使用されており、既知の領域（ソース）から未知の領域（ターゲット）に知識を移転するのに役立ちます。日常生活でも、物体や状況の間の類似性に基づいて推測するために使用されます。",
        "abstract_example": "状況C_aでComponent C_1₁がComponent C_1_bと相互作用しているのを見て、状況C_bでもComponent C_2₁とComponent C_2_aが同様に相互作用すると推測します。",
        "abstract_example": "Component C_a_1₁が状況C_aでComponent C_a_2と特定の方法で相互作用しているのを考えます。状況C_bでComponent C_b_1とComponent C_b_2に遭遇し、Component C_b_1とComponent C_b_2が状況C_aで同様に相互作用すると推測します。",
        "concrete_example": "植物が成長するのを助けるために水やりをする庭師のように、教師は知識とガイダンスを提供して生徒を発展させます。"
    },
    "counterfactual_reasoning": {
        "short_description": "起こらなかった代替シナリオや結果を考慮する。",
        "long_description": "反事実の推論は、起こらなかった代替シナリオや結果を考慮することを含みます。異なる状況下で『何が起こったかもしれないか』を想像することにより、因果関係を理解し、意思決定を評価し、将来の行動を計画するのに役立ちます。哲学、心理学、ビジネスなどの分野で、異なる選択や行動の潜在的な結果を探るためにしばしば使用されます。",
        "abstract_example": "起こらなかった条件Xを考え、その場合には結果Yが結果Zに置き換わったかもしれないと想像します。",
        "concrete_example": "もし5分早く家を出ていたら、バスに間に合っていたでしょう。"
    },
    "probabilistic_reasoning": {
        "short_description": "不確実性の中で推測するために確率の原則を適用する。",
        "long_description": "確率的推論は、不確実性の中で推測するために確率の原則を適用します。異なる結果の可能性を評価し、さまざまなイベントが発生する確率に基づいて情報に基づいた決定を下すことができます。この種類の推論は、統計、リスク評価、人工知能などの分野で重要です。",
        "abstract_example": "Option Aの成功の確率がOption Bよりも高い（P(A) > P(B)）と評価した場合、Option Aを選択することに決めます。",
        "concrete_example": "明日の降雨確率が70%なので、外出時には傘を持って出かけることにします。"
    },
    "temporal_reasoning": {
        "short_description": "イベントの順序と期間を理解する。",
        "long_description": "時間的推論は、時間内でのイベントの順序や期間を理解・推論する能力です。特定の時間データを理解し、イベントの順序、イベントの持続時間、および異なる時間点間の関係を解釈します。スケジューリング、計画、物語の理解などの分野で重要です。",
        "abstract_example": "日中の計画を立てて、イベントT_1をイベントT_2の前にスケジュールし、アクティビティの正しい順序を確保します。",
        "concrete_example": "太陽が朝に昇り、夕方に沈むことを観察します。同様に、月も同じ時間に昇り沈むと推測します。"
    },
    "spatial_reasoning": {
        "short_description": "空間内で物体を視覚化・操作する。",
        "long_description": "空間推論は、空間内で物体を視覚化・操作することを含みます。異なる物体群の間の位置関係、向き、動きなどを理解します。空間推論は、エンジニアリング、建築、地理学、視覚芸術のさまざまな分野で基本的で、物体の物理的配置や動きに関する問題解決を可能にします。",
        "abstract_example": "家具の配置中に、部屋内でのObject S_1とObject S_2の最適な配置を視覚化します。",
        "concrete_example": "建築家が窓と周囲の壁を視覚化し、最適な角度と高さを決定するために窓を最適な位置にすることを決定する。"
    },
    "social_reasoning": {
        "short_description": "社会的相互作用と規範を理解する。",
        "long_description": "社会的推論は、社会的相互作用と規範を理解することを含みます。社会的状況を分析し、適切な行動と不適切な行動を認識し、他者の意図、感情、考えを予測する能力を包括します。効果的な社会的推論は、成功する対人的関係を構築し、複雑な社会環境をうまく乗り越えるのに重要です。",
        "abstract_example": "状況SでPerson Aがある行動をしているのに気づき、効果的に相互作用できるように自分の行動（Behavior B）を調整します。",
        "concrete_example": "友達が話した後にうつむいている様子に気づいたため、彼らが大丈夫かどうか尋ねます。"
    }, 
    "moral_reasoning": {
        "short_description": "倫理原則に基づいて何が正しいか間違っているかを決定する。",
        "long_description": "道徳的推論は、倫理原則に基づいて何が正しいか間違っているかを決定する過程です。行動、意図、結果を評価し、道徳的問題について判断を下すことを含みます。道徳的推論は、倫理的意思決定の要であり、社会的規範、個人的価値観、哲学的理論などのさまざまな要因から影響を受けます。",
        "abstract_example": "行動MがPerson Cを害する可能性を考え、倫理原則を尊重するために代替案を選び、それが道徳的に間違っていると判断します。",
        "concrete_example": "誰かが財布を落とすのを見て、その中のお金を保持するのではなく、財布を返すことに決定します。それが正しいことだからです。"
    }
}

general_reasoning_skills = {
  "logical_reasoning": {
    "short_description": "構造化された方法で結論を導き出す。",
    "long_description": "論理的推論には、与えられた情報から結論を導き出すための構造化されたプロセスを含む推論形式が含まれます。これは、結論が論理的に妥当であることを保証するために科学的および分析的分野で基礎とされる演繹、帰納、仮説推論などの方法を含みます。"
  },
  "contextual_reasoning": {
    "short_description": "要素間の関係と文脈を理解する。",
    "long_description": "文脈的推論には、要素間の関係、文脈、およびダイナミクスを理解するためのスキルが含まれます。これは、さまざまな状況でシナリオを評価し、結果を予測し、問題を解決するために使用される類推、反事実、確率、時間的、および空間的推論をカバーしています。"
  },
  "social_and_ethical_reasoning": {
    "short_description": "社会的相互作用と倫理的原則に関連する推論。",
    "long_description": "社会的および倫理的推論は、社会的相互作用を理解し、倫理原則を評価することに重点を置いたスキルを含みます。これは、行動を解釈し、複雑な社会環境を乗り切り、倫理的配慮に基づいて意思決定を行うために不可欠な社会的および倫理的推論を含みます。"
  }
}

#SECTION: OUTPUT FORMAT
output_formats = {
    "with_skills": '''
    ```json
    {
      "commonsense_question": "質問文",
      "options": {
          "A": "選択肢のテキスト_A",
          ...
      },
      "correct_answer": ["正しい選択肢", "選択肢のテキスト"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "推論スキル名",
              "reasoning": "推論のテキスト",
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "推論スキル名",
              "reasoning": "推論のテキスト",
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          }
      }
    }
    ```
    ''',

    "with_context_and_skills": '''
    ```json
    {
      "commonsense_context": "コンテキストテキスト",
      "commonsense_question": "質問文",
      "options": {
          "A": "選択肢のテキスト_A",
          ...
      },
      "correct_answer": ["正しい選択肢", "選択肢のテキスト"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "推論スキル名",
              "reasoning": "推論のテキスト",
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "推論スキル名",
              "reasoning": "推論のテキスト",
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          }
      }
    }
    ```
    ''',

    "without_skills": '''
    ```json
    {
      "commonsense_question": "質問文",
      "options": {
          "A": "選択肢のテキスト_A",
          ...
      },
      "correct_answer": ["正しい選択肢", "選択肢のテキスト"]
    }
    ```
    ''',

    "with_context_without_skills": '''
    ```json
    {
      "commonsense_context": "コンテキストテキスト",
      "commonsense_question": "質問文",
      "options": {
          "A": "選択肢のテキスト_A",
          ...
      },
      "correct_answer": ["正しい選択肢", "選択肢のテキスト"]
    }
    ```
    ''',

    "cot_without_skills": '''
    ```json
    {
      "commonsense_question": "質問文",
      "options": {
          "A": "選択肢のテキスト_A",
          ...
      },
      "correct_answer": ["正しい選択肢", "選択肢のテキスト"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning": "推論のテキスト",  
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          },
          ...
          "reasoning_step_n": {
              "reasoning": "推論のテキスト",
              "eliminated_options": [排除された選択肢のリスト],
              "possible_options": [残された選択肢のリスト]
          }
      }
    }
    ```
    '''
}


#SECTION: INFERENCE

logical_inference = f'''
あなたの課題は、多肢選択式の常識的な質問に答えることです。次の「推論スキル」を使用して推論プロセスを提供してください。
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_logic_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_logic_1"]["output"]} \n

### OUTPUT REMINDER
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''

general_inference = f'''
あなたの課題は、多肢選択式の常識的な質問に答えることです。次の「推論スキル」を使用して推論プロセスを提供してください。
    + logical_reasoning: {general_reasoning_skills["logical_reasoning"]["short_description"]}
    + contextual_reasoning: {general_reasoning_skills["contextual_reasoning"]["short_description"]}
    + social_and_ethical_reasoning: {general_reasoning_skills["social_and_ethical_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_general_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_general_1"]["output"]} \n

### OUTPUT REMINDER
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''

standard_inference_o1 = f'''
あなたの課題は、多肢選択式の常識的な質問に答えることです。次の「推論スキル」を使用して推論プロセスを提供してください。
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
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''

standard_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
次のステップバイステップの指示に従います:
1. 問題文とすべての提供された回答選択肢を注意深く読みます。
2. 正しい回答選択肢を選んで質問に答えます。
3. 回答に至るまでの「REASONING PROCESS」を段階的に説明します。各「ATOMIC REASONING STEP」は以下のシーケンスに従う必要があります:
	3.1. 以下の推論スキルのうち1つを選び、REASONING STEPで使用します:
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
	3.2. 選択した「REASONING SKILL」を適用します: 選択された「REASONING SKILL」が特定の選択肢を排除するのにどのように適用されたか、または正しい選択肢を強化するのにどのように適用されたかについて、簡潔に説明します。推論が明確であり、さらに小さなステップに分解できないことを保証します。
	3.3. オプションを排除します: このステップで推論に基づいて排除されたオプションを列挙します。
	3.4. 残りの選択肢を更新します: このステップ後の残りの選択肢のリストを提供します。
4. 次の構造を持つJSON形式で出力を生成します:
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
INPUT:
{ICL_EXAMPLES["infer_1"]["input"]} \n
OUTPUT:
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''

#! cot
cot_inference_o1 = f'''
あなたの仕事は、多肢選択式の常識的な質問に答え、正しい答えを見つけるための推論プロセスを提供することです。
次の構造を持つJSON形式で出力を生成します:
{output_formats["cot_without_skills"]}

'''

cot_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
次のステップバイステップの指示に従います:
1. 問題文とすべての提供された回答選択肢を注意深く読みます。
2. 正しい回答選択肢を選んで質問に答えます。
3. 回答に至るまでの「REASONING PROCESS」を段階的に説明します。
4. 次の構造を持つJSON形式で出力を生成します:
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
次のステップバイステップの指示に従います:
1. 質問の理解: 問題文とすべての提供された回答選択肢を注意深く読みます。
2. "COMMONSENSE CONTEXT" の追加: 元の質問を拡充するために、追加の "COMMONSENSE CONTEXT" を提供します。追加コンテキストが関連性を持ち、質問の理解を豊かにすることを確認してください。
3. 正しい回答に至るまでの「REASONING PROCESS」を段階的に説明します。各「ATOMIC REASONING STEP」は以下のシーケンスに従う必要があります:
	3.1. 以下の推論スキルのうち1つを選び、REASONING STEPで使用します:
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
	3.2. 選択した「REASONING SKILL」を適用します: 選択された「REASONING SKILL」が特定の選択肢を排除するのにどのように適用されたか、または正しい選択肢を強化するのにどのように適用されたかについて、簡潔に説明します。推論が明確であり、さらに小さなステップに分解できないことを保証します。
	3.3. オプションを排除します: このステップで推論に基づいて排除されたオプションを列挙します。
	3.4. 残りの選択肢を更新します: このステップ後の残りの選択肢のリストを提供します。
4. 次の構造を持つJSON形式で出力を生成します:
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
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''


#! CultureBank
culbank_gen = f'''
### LLM ROLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["culbank_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
次のステップバイステップの指示に従います:
1. 提供された文化的状況を分析: 文化グループ、コンテキスト、アクターの行動、およびその他の説明の詳細を確認し、状況の重要な要素を理解します。
2. "COMMONSENSE CONTEXT" の追加: 入力で与えられたコンテキストに基づいて、質問に対する "COMMONSENSE CONTEXT" とは、時間、場所、社会的規範、文化的影響、およびトピックの理解を形成する関連する詳細を含む、特別な知識を必要とせずに一般に理解される背景知識や追加の詳細を指します。
3. "Commonsense Question" を作成: 文化的コンテキストとキャラクターの質問を組み合わせて簡潔な質問を作成します。質問が元のコンテキストを明示的に述べることなく含意していることを確認してください。"actor_behavior" に基づいて正しい回答オプションを作成します。
4. 他の回答オプションを提供: 5つの選択肢問題（前のステップの正しい答えを含む）を作成します。そのうちの2つは妥当なオプションであるべきです。他の2つは関連性があり合理的ですが、文化的コンテキストに基づいて不正解な誘惑選択肢であるべきです。
5. 正しい回答に至るまでの「REASONING PROCESS」を段階的に説明します。各「ATOMIC REASONING STEP」は以下のシーケンスに従う必要があります:
	5.1. 以下の「REASONING SKILL」から1つを選び、「REASONING STEP」で使用します:
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
	5.2. 選択した「REASONING SKILL」を適用します: 選択された「REASONING SKILL」が特定の選択肢を排除するのにどのように適用されたか、または正しい選択肢を強化するのにどのように適用されたかについて、簡潔に説明します。推論が明確であり、さらに小さなステップに分解できないことを保証します。
	5.3. オプションを排除します: このステップで推論に基づいて排除されたオプションを列挙します。
	5.4. 残りの選択肢を更新します: このステップ後の残りの選択肢のリストを提供します。
6. 次の構造を持つJSON形式で出力を生成します:
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["culbank_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["culbank_gen_1"]["output"]} \n

### OUTPUT REMINDER
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''


#! Complexity

expand_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_expand"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_expand"]} \n
### STEP-BY-STEP INSTRUCTIONS
次のステップバイステップの指示に従います:
1. 質問の理解: 提供された質問、コンテキスト、およびその回答オプションを注意深く読みます。
2. コンテキストの拡張: 質問に深みを持たせ、推論要求を追加するために、"COMMONSENSE CONTEXT"に追加の背景情報や状況的な詳細を追加します。
3. 質問の修正: "EXPANDED COMMONSENSE CONTEXT"を利用して、核心的概念と常識を維持しながらさらに複雑な質問を作成します。
4. オプションの調整:
	+ 新しい複雑な質問に合わせて既存の回答選択肢を調整します
	+ 正しい回答選択が元の文意に似たものであることを保証します
	+ 質問の複雑さを増すために、妥当だが不正確な選択肢を追加します
	+ オプションをすべて元と同様に簡潔に保ちます
5. 推論の洗練: 元の"REASONING PROCESS"を新しいコンテキストに合わせて洗練します。追加の"ATOMIC REASONING STEP"は以下の"REASONING SKILLs"のいずれかを使用する必要があります:
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
6. 次の構造でJSON形式を使用して出力をフォーマットします:
 {output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["expand_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["expand_1"]["output"]} \n

### OUTPUT REMINDER
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''


#! Implicitation
implicit_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_implicit"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_implicit"]} \n
### STEP-BY-STEP INSTRUCTIONS
次のステップバイステップの指示に従います:
1. 提供された「commonsense_context」を分析し、推論に必要な基本的な仮定や暗黙の知識を理解します。
2. 「commonsense_question」とその関連する「options」を調べて、質問に回答するために必要な重要な要素を特定します。
3. 元のコンテキストと質問を組み合わせて「IMPLICITLY IMPLIED COMMONSENSE CONTEXT」を含む新しい「commonsense_question」を作成することで、質問を書き直します。新しい質問が明確で理解しやすいことを確認します。
4. 変換された質問でも「REASONING PROCESS」が変更されないことを確認し、正しい回答が元のものと同じであることを確認します。
5. すべての回答オプションが合理的で関連性があり、書き直された質問の文脈で元の意図を維持することを保証します。
6. 「reasoning」セクションの構造と内容を保持し、正しい回答を支える論理ステップを反映します。「ATOMIC REASONING STEP」は次の「REASONING SKILLs」のいずれかを使用する必要があります:
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
出力が指示されたJSON構造およびコンテキスト例で示されている内容に従うことを確認します。
'''
