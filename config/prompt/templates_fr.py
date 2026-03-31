
from liquid import Template
from .icl_examples import FR_ICL_EXAMPLES as ICL_EXAMPLES

#SECTION: INPUT PROMPT

input_infer = Template('''
ENTRÉE :
{{question}}

SORTIE :
''')

input_gen = Template('''
ENTRÉE :
{{question}}

SORTIE :
''')

input_expand = Template('''
ENTRÉE :
{{question}}

SORTIE :
''')

input_implicit = Template('''
ENTRÉE :
{{question}}

SORTIE :
''')

#SECTION: ROLE PROMPT

llm_roles = {
    "commonsense_infer": 
      """
      Vous êtes un modèle linguistique doté de compétences avancées en raisonnement de bon sens, capable de raisonnement logique et analytique, de pensée heuristique et intuitive, d'analyse comparative et hypothétique, et de compréhension contextuelle et spécialisée.
      """,
    "commonsense_gen": 
      """
      Vous êtes un modèle linguistique doté de compétences avancées en raisonnement de bon sens, capable de raisonnement logique et analytique, de pensée heuristique et intuitive, d'analyse comparative et hypothétique, et de compréhension contextuelle et spécialisée.
      """,
    "culbank_gen": 
      """
      Vous êtes un modèle linguistique doté de compétences avancées en raisonnement de bon sens, capable de raisonnement logique et analytique, de pensée heuristique et intuitive, d'analyse comparative et hypothétique, et de compréhension contextuelle et spécialisée.
      """, 
    "commonsense_expand": 
      """
      Vous êtes un modèle linguistique doté de compétences avancées en raisonnement de bon sens, capable de raisonnement logique et analytique, de pensée heuristique et intuitive, d'analyse comparative et hypothétique, et de compréhension contextuelle et spécialisée.
      """,
    "commonsense_implicit": 
      """
      Vous êtes un modèle linguistique doté de compétences avancées en raisonnement de bon sens, capable de raisonnement logique et analytique, de pensée heuristique et intuitive, d'analyse comparative et hypothétique, et de compréhension contextuelle et spécialisée.
      """,
}


#SECTION: TASK DESCRIPTION
task_descriptions = {
    "commonsense_infer": 
      """
      Votre tâche est de répondre aux questions à choix multiples sur le bon sens en fournissant un "REASONING PROCESS" détaillé impliquant plusieurs "REASONING STEPs". Chaque "REASONING STEP" doit être un "ATOMIC REASONING STEP" — une unité indivisible de raisonnement qui utilise principalement une compétence de raisonnement. C'est un processus de pensée unique et cohérent qui ne peut pas être décomposé en étapes plus petites sans en perdre le sens. L'objectif est d'utiliser le nombre minimum d'étapes nécessaires, en veillant à ce que chaque étape soit non redondante et contribue à réduire les options possibles en éliminant un ou plusieurs choix de réponse.
      """,
    "commonsense_gen": 
      """
      Étant donné une question à choix multiples sur le bon sens avec l'option correcte, votre tâche est de fournir un "COMMONSENSE CONTEXT" pour développer la question donnée et un "REASONING PROCESS" détaillé impliquant plusieurs "REASONING STEPs" pour arriver à la réponse correcte. 
        + Un "COMMONSENSE CONTEXT" de la question fait référence aux connaissances de base ou aux détails supplémentaires qui sont généralement compris sans nécessiter de connaissances spécialisées, y compris des facteurs tels que le temps, le lieu, les normes sociales, les influences culturelles et d'autres détails pertinents qui façonnent la compréhension du sujet.
        + Chaque "REASONING STEP" doit être un "ATOMIC REASONING STEP" — une unité indivisible de raisonnement qui utilise principalement une compétence de raisonnement. C'est un processus de pensée unique et cohérent qui ne peut pas être décomposé en étapes plus petites sans en perdre le sens. Le "REASONING PROCESS" doit être aussi efficace que possible, n'utilisant que le nombre minimum d'étapes nécessaires, en veillant à ce que chaque étape soit non redondante et contribue à réduire les options possibles en éliminant un ou plusieurs choix de réponse.,
      """,
    "culbank_gen": 
      """
      Votre tâche est de créer une question à choix multiples sur le bon sens basée sur une situation culturelle donnée dans le format suivant :
      {
          "cultural_topic": "groupe culturel - sujet - scénario",
          "social_context": "contextes où le comportement a lieu",
          "actor": "qui exhibe le comportement",
          "question": "la question sur le bon sens concernant le comportement de l'acteur",
          "actor_behavior": "comportement de l'acteur - qui est largement convenu (l'option de réponse correcte)",
          "recipient": "destinataire de l'action",
          "relation": "relation entre l'acteur et le destinataire",
          "recipient_behavior": "comportement du destinataire",
      }
      La question doit implicitement incorporer le contexte culturel, mettant à l'épreuve la capacité de l'IA à utiliser le raisonnement de bon sens pour arriver à la réponse correcte. L'objectif est de tester et d'améliorer la compréhension des normes et des comportements culturels de l'IA dans un cadre spécifique.
      Fournissez le "REASONING PROCESS" détaillé pour arriver à l'option de réponse correcte impliquant plusieurs "REASONING STEPs" pour arriver à la réponse correcte. Chaque "REASONING STEP" doit être un "ATOMIC REASONING STEP" — une unité indivisible de raisonnement qui utilise principalement une compétence de raisonnement. C'est un processus de pensée unique et cohérent qui ne peut pas être décomposé en étapes plus petites sans en perdre le sens. Le "REASONING PROCESS" doit être aussi efficace que possible, n'utilisant que le nombre minimum d'étapes nécessaires, en veillant à ce que chaque étape soit non redondante et contribue à réduire les options possibles en éliminant un ou plusieurs choix de réponse.
      """, 
    "commonsense_expand": 
      """
        Étant donné une question à choix multiples sur le bon sens avec ses options, votre tâche est de la modifier et de l'élargir pour créer une question plus complexe en élargissant son contexte, en modifiant la question, en ajustant les options de réponse et en ajoutant une étape de raisonnement supplémentaire. Votre sortie doit inclure le contexte élargi, la question modifiée, les options de réponse révisées, la réponse correcte et un "REASONING PROCESS" détaillé.
      """,
    "commonsense_implicit": 
      """
        Étant donné une question à choix multiples sur le bon sens avec ses options, votre tâche est de la modifier et de l'élargir pour créer une question plus complexe en élargissant son contexte, en modifiant la question, en ajustant les options de réponse et en ajoutant une étape de raisonnement supplémentaire. Votre sortie doit inclure le contexte élargi, la question modifiée, les options de réponse révisées, la réponse correcte et un "REASONING PROCESS" détaillé.
      """,
}


#SECTION: REASONING SKILL
reasoning_skills = {
    'inductive_reasoning': {
        "short_description": "Tirer des conclusions générales à partir d'observations spécifiques.",
        "long_description": "Le raisonnement inductif est une méthode de tirage de conclusions générales à partir d'observations spécifiques. Contrairement au raisonnement déductif, qui part de prémisses générales pour atteindre des conclusions spécifiques, le raisonnement inductif commence par des faits détaillés et aboutit à des généralisations ou théories plus larges. Cette approche est couramment utilisée dans la recherche scientifique, où des expériences et observations répétées conduisent à la formulation de principes ou hypothèses généraux.",
        "abstract_example": "Après avoir été témoin de plusieurs instants où l'Événement A_1 conduit à l'Événement A_2, vous en déduisez que l'Événement A_n résultera de manière similaire en Événement A₂ dans les occurrences futures.",
        "concrete_example": "Après avoir été témoin de plusieurs occasions où la prévision météorologique prévoit de la pluie, vous en déduisez que la pluie continuera probablement à tomber à l'avenir.",
    },
    "deductive_reasoning": {
        "short_description": "Dériver des conclusions spécifiques à partir de prémisses générales.",
        "long_description": "Le raisonnement déductif consiste à dériver des conclusions spécifiques à partir de prémisses générales. Il garantit que si les prémisses sont vraies et que le raisonnement est valide, la conclusion doit également être vraie. La logique déductive est fondamentale dans des domaines nécessitant une preuve rigoureuse, comme les mathématiques et les sciences formelles.",
        "abstract_example": "Étant donné la prémisse que Tous les X sont Y, et sachant que l'Objet x₁ est un X, vous déduisez que l'Objet x₁ doit aussi être un Y.",
        "concrete_example": "Étant donné que Tous les oiseaux ont des plumes. Un moineau est un oiseau. Par conséquent, un moineau a des plumes."
    },
    "abductive_reasoning": {
        "short_description": "Formuler des hypothèses pour expliquer les observations.",
        "long_description": "Le raisonnement abductif est le processus de formuler des hypothèses pour expliquer les observations. Il commence par un ensemble incomplet d'observations et procède à l'explication la plus probable possible. Contrairement au raisonnement déductif et inductif, le raisonnement abductif cherche l'explication la plus simple et la plus plausible pour un ensemble donné de faits, conduisant souvent à la génération de nouvelles théories ou hypothèses.",
        "abstract_example": "Observant l'Événement B, vous émettez l'hypothèse que la Raison 2 est l'explication la plus plausible parmi plusieurs causes possibles.",
        "concrete_example": "Vous vous réveillez et voyez que la rue est mouillée. L'explication la plus probable est qu'il a plu la nuit dernière."
    },
    "analogical_reasoning": {
        "short_description": "Établir des parallèles entre des situations similaires pour en tirer des conclusions.",
        "long_description": "Le raisonnement analogique implique de tirer des parallèles entre des situations similaires pour en déduire des conclusions. En comparant deux objets ou systèmes qui partagent certaines caractéristiques, on peut en déduire qu'ils peuvent partager d'autres propriétés non observées. Cette forme de raisonnement est largement utilisée pour résoudre des problèmes, faire des découvertes scientifiques et raisonnements juridiques afin de transférer des connaissances d'un domaine connu (source) à un domaine inconnu (cible). Le raisonnement analogique est également utilisé dans la vie quotidienne pour faire des inférences sur les similitudes entre objets ou situations.",
        "abstract_example": "Voyant que le Composant C_1₁ interagit avec le Composant C_1_b dans la Situation C_a, vous en déduisez que le Composant C_2₁ et le Composant C_2_a interagiront de manière similaire dans la Situation C_b.",
        "concrete_example": "Tout comme un jardinier arrose les plantes pour les aider à pousser, un enseignant fournit des connaissances et des conseils pour aider les élèves à se développer."
    },
    "counterfactual_reasoning": {
        "short_description": "Considérer des scénarios et résultats alternatifs qui ne se sont pas produits.",
        "long_description": "Le raisonnement contrefactuel implique de considérer des scénarios et résultats alternatifs qui ne se sont pas produits. Il consiste à imaginer 'ce qui aurait pu arriver' dans des circonstances différentes, ce qui est utile pour comprendre la causalité, évaluer les décisions et planifier des actions futures. Le raisonnement contrefactuel est souvent utilisé dans des domaines comme la philosophie, la psychologie et le commerce pour explorer les conséquences potentielles de différents choix ou actions.",
        "abstract_example": "En réfléchissant à la Condition X qui ne s'est pas produite, vous imaginez que si cela avait eu lieu, le Résultat Y aurait pu remplacer le Résultat Z.",
        "concrete_example": "Si vous aviez quitté la maison cinq minutes plus tôt, vous auriez pris le bus à l'heure."
    },
    "probabilistic_reasoning": {
        "short_description": "Appliquer les principes de probabilité pour faire des inférences en situation d'incertitude.",
        "long_description": "Le raisonnement probabiliste implique d'appliquer les principes de probabilité pour faire des inférences en situation d'incertitude. Il permet aux individus d'évaluer la probabilité de différents résultats et de prendre des décisions éclairées en fonction de la probabilité de divers événements. Ce type de raisonnement est crucial dans des domaines comme les statistiques, l'évaluation des risques et l'intelligence artificielle.",
        "abstract_example": "Évaluant que l'Option A a une probabilité plus élevée (P(A) > P(B)) de succès que l'Option B, vous décidez de choisir l'Option A.",
        "concrete_example": "Il y a 70% de chances de pluie demain, donc vous décidez de prendre un parapluie lorsque vous sortez."
    },
    "temporal_reasoning": {
        "short_description": "Comprendre les séquences et durées des événements.",
        "long_description": "Le raisonnement temporel est la capacité de comprendre et de raisonner sur la séquence et la durée des événements dans le temps. Il implique de comprendre les données spécifiques au temps, telles que l'ordre des événements, leur durée et les relations entre différents points dans le temps. Le raisonnement temporel est essentiel dans des domaines comme la planification, l'organisation et la compréhension de récits.",
        "abstract_example": "En planifiant votre journée, vous programmez l'Événement T_1 pour se produire avant l'Événement T_2, garantissant la bonne séquence des activités.",
        "concrete_example": "Vous observez que le soleil se lèvera le matin et se couchera le soir. Vous en déduisez que la lune se lèvera et se couchera au même moment."
    },
    "spatial_reasoning": {
        "short_description": "Visualiser et manipuler des objets dans l'espace.",
        "long_description": "Le raisonnement spatial implique de visualiser et manipuler des objets dans l'espace. Il consiste à comprendre les relations entre différents objets, tels que leur position, leur orientation et leur mouvement les uns par rapport aux autres. Le raisonnement spatial est fondamental dans les domaines tels que l'ingénierie, l'architecture, la géographie et diverses formes d'arts visuels, permettant aux individus de résoudre des problèmes liés à l'agencement physique et au mouvement des objets.",
        "abstract_example": "Lors de l'organisation des meubles, vous visualisez l'Objet S_1 et l'Objet S_2 pour déterminer leur placement optimal au sein de la pièce.",
        "concrete_example": "Un architecte déterminant le meilleur emplacement pour une fenêtre en visualisant la fenêtre et les murs environnants pour déterminer l'angle et la hauteur optimaux."
    },
    "social_reasoning": {
        "short_description": "Comprendre les interactions et normes sociales.",
        "long_description": "Le raisonnement social implique de comprendre les interactions et normes sociales. Il englobe la capacité à analyser et interpréter les situations sociales, reconnaître les comportements appropriés et inappropriés et prédire les intentions, émotions et pensées des autres. Un raisonnement social efficace est crucial pour bâtir des relations interpersonnelles réussies et naviguer dans des environnements sociaux complexes.",
        "abstract_example": "Remarquant que la Personne A se comporte d'une certaine façon dans la Situation S, vous ajustez votre propre comportement (Comportement B) pour interagir efficacement.",
        "concrete_example": "Vous remarquez que votre ami a l'air contrarié après une conversation, alors vous décidez de lui demander si tout va bien."
    }, 
    "moral_reasoning": {
        "short_description": "Décider ce qui est bien ou mal en fonction de principes éthiques.",
        "long_description": "Le raisonnement moral est le processus de décider ce qui est bien ou mal en fonction de principes éthiques. Il implique d'évaluer les actions, intentions et conséquences pour porter des jugements sur des questions morales. Le raisonnement moral est central à la prise de décision éthique et est influencé par divers facteurs, y compris les normes sociétales, les valeurs personnelles et les théories philosophiques.",
        "abstract_example": "Considérant que l'Action M pourrait nuire à la Personne C, vous décidez qu'il est moralement incorrect et choisissez une alternative qui respecte les principes éthiques.",
        "concrete_example": "En voyant quelqu'un laisser tomber son portefeuille, vous décidez de le lui rendre plutôt que de garder l'argent qu'il contient parce que c'est la bonne chose à faire."
    }
}

general_reasoning_skills = {
  "logical_reasoning": {
    "short_description": "Approches structurées pour déduire des conclusions.",
    "long_description": "Le raisonnement logique comprend des formes de raisonnement impliquant des processus structurés pour déduire des conclusions à partir d'informations données. Cela inclut des méthodologies comme le raisonnement déductif, inductif et abductif, qui sont fondamentales dans les disciplines scientifiques et analytiques pour garantir que les conclusions sont logiquement valides."
  },
  "contextual_reasoning": {
    "short_description": "Compréhension des relations et contextes entre les éléments.",
    "long_description": "Le raisonnement contextuel inclut des compétences utilisées pour comprendre les relations, les contextes et les dynamiques entre les éléments. Il couvre divers types de raisonnement tels que l'analogique, le contrefactuel, le probabiliste, le temporel et le spatial, utilisés pour évaluer des scénarios, prédire des résultats et résoudre des problèmes dans divers contextes."
  },
  "social_and_ethical_reasoning": {
    "short_description": "Raisonnement lié aux interactions sociales et aux principes éthiques.",
    "long_description": "Le raisonnement social et éthique implique des compétences centrées sur la compréhension des interactions sociales et l'évaluation des principes éthiques. Il inclut le raisonnement social et moral, essentiel pour interpréter les comportements, naviguer dans des environnements sociaux complexes et prendre des décisions basées sur des considérations éthiques."
  }
}

#SECTION: OUTPUT FORMAT
output_formats = {
    "with_skills": '''
    ```json
    {
      "commonsense_question": "texte_de_la_question",
      "options": {
          "A": "texte_option_réponse_A",
          ...
      },
      "correct_answer": ["option_réponse", "texte_réponse"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "nom_de_la_compétence_de_raisonnement",
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "nom_de_la_compétence_de_raisonnement",
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          }
      }
    }
    ```
    ''',

    "with_context_and_skills": '''
    ```json
    {
      "commonsense_context": "texte_contexte",
      "commonsense_question": "texte_de_la_question",
      "options": {
          "A": "texte_option_réponse_A",
          ...
      },
      "correct_answer": ["option_réponse", "texte_réponse"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "nom_de_la_compétence_de_raisonnement",
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "nom_de_la_compétence_de_raisonnement",
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          }
      }
    }
    ```
    ''',

    "without_skills": '''
    ```json
    {
      "commonsense_question": "texte_de_la_question",
      "options": {
          "A": "texte_option_réponse_A",
          ...
      },
      "correct_answer": ["option_réponse", "texte_réponse"]
    }
    ```
    ''',

    "with_context_without_skills": '''
    ```json
    {
      "commonsense_context": "texte_contexte",
      "commonsense_question": "texte_de_la_question",
      "options": {
          "A": "texte_option_réponse_A",
          ...
      },
      "correct_answer": ["option_réponse", "texte_réponse"]
    }
    ```
    ''',

    'cot_without_skills': '''
    ```json
    {
      "commonsense_question": "texte_de_la_question",
      "options": {
          "A": "texte_option_réponse_A",
          ...
      },
      "correct_answer": ["option_réponse", "texte_réponse"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          },
          ...
          "reasoning_step_n": {
              "reasoning": "texte_de_raisonnement",
              "eliminated_options": [liste_des_options_éliminées],
              "possible_options": [liste_des_options_restantes]
          }
      }
    }
    ```
    '''
}



#SECTION: INFERENCE
logical_inference = f'''
Votre tâche consiste à répondre à des questions à choix multiples de bon sens. Fournissez votre processus de raisonnement en utilisant les "REASONING SKILLS" suivantes:
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_logic_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_logic_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''

general_inference = f'''
Votre tâche consiste à répondre à des questions à choix multiples de bon sens. Fournissez votre processus de raisonnement en utilisant les "REASONING SKILLS" suivantes:
    + logical_reasoning: {general_reasoning_skills["logical_reasoning"]["short_description"]}
    + contextual_reasoning: {general_reasoning_skills["contextual_reasoning"]["short_description"]}
    + social_and_ethical_reasoning: {general_reasoning_skills["social_and_ethical_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_general_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_general_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''

standard_inference_o1 = f'''
Votre tâche consiste à répondre à des questions à choix multiples de bon sens. Fournissez votre processus de raisonnement en utilisant les "REASONING SKILLS" suivantes:
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

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''

standard_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Suivez ces instructions étape par étape :
1. Lisez attentivement la question ainsi que toutes les options de réponse fournies.
2. Répondez à la question en choisissant la bonne option de réponse. 
3. Décrivez votre "REASONING PROCESS" étape par étape pour arriver à votre réponse. Chaque "ATOMIC REASONING STEP" doit suivre cette séquence :
	3.1. Choisissez une compétence de raisonnement ci-dessous à utiliser par le REASONING STEP :
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
	3.2. Appliquez la "Reasoning Skill" choisie : fournissez une explication concise de la façon dont la "Reasoning Skill" choisie est appliquée pour éliminer certaines options de réponse ou renforcer l'option de réponse correcte. Assurez-vous que le raisonnement est clair et ne peut pas être divisé en étapes plus petites.
	3.3. Éliminez les options : énumérez les options éliminées à cette étape en fonction de votre raisonnement.
	3.4. Mettez à jour les Options Possibles : fournissez la liste des options possibles restantes après cette étape.
4. Générez votre sortie au format JSON avec la structure suivante :
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''


#! cot
cot_inference_o1 = f'''
Votre tâche consiste à répondre à des questions de bon sens à choix multiples et à fournir votre processus de raisonnement pour trouver la bonne réponse.
Générez votre sortie au format JSON avec la structure suivante :
{output_formats["cot_without_skills"]}

'''

cot_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Suivez ces instructions étape par étape :
1. Lisez la question attentivement, ainsi que toutes les options de réponse fournies.
2. Répondez à la question en choisissant la bonne option de réponse. 
3. Décrivez votre "REASONING PROCESS" étape par étape pour arriver à votre réponse.
4. Générez votre sortie au format JSON avec la structure suivante :
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
Suivez ces instructions étape par étape :
1. Compréhension de la question : Lisez attentivement la question ainsi que toutes les options de réponse fournies.
2. Ajout du "COMMONSENSE CONTEXT" : Développez la question originale en fournissant un "COMMONSENSE CONTEXT" supplémentaire. Assurez-vous que le contexte ajouté est pertinent et enrichit la compréhension de la question.
3. Décrivez votre "REASONING PROCESS" étape par étape pour arriver à la bonne réponse. Chaque "ATOMIC REASONING STEP" doit suivre cette séquence :
	3.1. Choisissez parmi les compétences de raisonnement ci-dessous celle qui sera utilisée par le REASONING STEP :
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
	3.2. Appliquez la "Reasoning Skill" choisie : fournissez une explication concise de la façon dont la "Reasoning Skill" choisie est appliquée pour éliminer certaines options de réponse ou renforcer l'option de réponse correcte. Assurez-vous que le raisonnement est clair et ne peut pas être divisé en étapes plus petites.
	3.3. Éliminez les options : énumérez les options éliminées à cette étape en fonction de votre raisonnement.
	3.4. Mettez à jour les Options Possibles : fournissez la liste des options possibles restantes après cette étape.
4. Générez votre sortie au format JSON avec la structure suivante :
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["mcsqa_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["mcsqa_gen_1"]["output"]} \n
EXAMPLE 2 - INPUT :
{ICL_EXAMPLES["mcsqa_gen_2"]["input"]} \n
EXAMPLE 2 - OUTPUT :
{ICL_EXAMPLES["mcsqa_gen_2"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''


#! CultureBank
culbank_gen = f'''
### LLM ROLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["culbank_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
Suivez ces instructions étape par étape :
1. Analyse de la Situuation Culturelle Fournie : Consultez les détails du groupe culturel, du contexte, des comportements des acteurs et d'autres descriptions pour comprendre les éléments clés de la situation.
2. Ajoutez le "COMMONSENSE CONTEXT" : En fonction du contexte donné en entrée, un "COMMONSENSE CONTEXT" de la question fait référence aux connaissances de base ou aux détails supplémentaires qui sont généralement compris sans nécessiter de connaissances spécialisées, y compris des facteurs tels que le temps, le lieu, les normes sociales, les influences culturelles et d'autres détails pertinents qui façonnent la compréhension du sujet.
3. Créez la "Commonsense Question" : Combinez le contexte culturel et la question de la persona pour formuler une question concise. Assurez-vous que la question intègre IMPLICITEMENT le contexte d'origine sans le déclarer explicitement. Créez l'option de réponse correcte basée sur le "actor_behavior".
4. Fournissez d'autres options de réponse : Créez 5 options à choix multiples (y compris la réponse correcte de l'étape précédente). Deux d'entre elles doivent être des options plausibles. Les deux autres doivent être des leurres qui sont pertinents et raisonnables mais incorrects selon le contexte culturel.
5. Décrivez votre "REASONING PROCESS" étape par étape pour arriver à la bonne réponse. Chaque "ATOMIC REASONING STEP" doit suivre cette séquence :
	5.1. Choisissez une "Reasoning Skill" ci-dessous à utiliser par le "REASONING STEP" :
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
	5.2. Appliquez la "Reasoning Skill" choisie : fournissez une explication concise de la façon dont la "Reasoning Skill" choisie est appliquée pour éliminer certaines options de réponse ou renforcer l'option de réponse correcte. Assurez-vous que le raisonnement est clair et ne peut pas être divisé en étapes plus petites.  
	5.3. Éliminez les options : énumérez les options éliminées à cette étape en fonction de votre raisonnement.
	5.4. Mettez à jour les Options Possibles : fournissez la liste des options possibles restantes après cette étape.
6. Générez votre sortie au format JSON avec la structure suivante :
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["culbank_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["culbank_gen_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''


#! Complexity
expand_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_expand"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_expand"]} \n
### STEP-BY-STEP INSTRUCTIONS
Suivez ces instructions étape par étape :
1. Compréhension de la Question : Lisez attentivement la question donnée, le contexte et ses options de réponse.
2. Expansion du Contexte : Ajoutez des détails supplémentaires sur le contexte ou la situation au "COMMONSENSE CONTEXT" pour ajouter de la profondeur et des exigences de raisonnement à la question.
3. Modification de la Question : Utilisez le "EXPANDED COMMONSENSE CONTEXT" pour créer une question plus complexe tout en conservant son concept central et son bon sens.
4. Ajustements des Options : 
	+ Ajustez les options de réponse existantes pour les aligner avec la nouvelle question complexe
	+ Assurez-vous que l'option de réponse correcte reste sémantiquement similaire à l'original
	+ Introduisez une option supplémentaire plausible mais incorrecte pour augmenter la complexité de la question
	+ Gardez toutes les options de réponse aussi concises que celles d'origine
5. Affinements du Raisonnement : Affinez le "REASONING PROCESS" original pour l'adapter au nouveau contexte. L'"ATOMIC REASONING STEP" supplémentaire doit utiliser l'une des "Reasoning Skills" suivantes :
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
6. Formatez la sortie en utilisant le format JSON avec la structure suivante :
 {output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["expand_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["expand_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''


#! Implicitation
implicit_prompt = f'''
### LLM ROLE
{llm_roles["commonsense_implicit"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_implicit"]} \n
### STEP-BY-STEP INSTRUCTIONS
Suivez ces instructions étape par étape :
1. Analysez le "commonsense_context" fourni pour comprendre les hypothèses sous-jacentes et les connaissances implicites requises pour le raisonnement.
2. Examinez la "commonsense_question" et ses "options" associées pour identifier les éléments clés essentiels pour répondre à la question.
3. Réécrivez la "commonsense_question" en combinant le contexte et la question originale pour créer une nouvelle "commonsense_question" avec un "IMPLICITLY IMPLIED COMMONSENSE CONTEXT". Assurez-vous que la nouvelle question reste claire et compréhensible.
4. Vérifiez que le "REASONING PROCESS" reste inchangé dans la question transformée et confirmez que la bonne réponse reste la même que dans l'original.
5. Assurez-vous que toutes les options de réponse sont raisonnables, pertinentes et conservent leur intention originale dans le contexte de la question réécrite.
6. Conservez la structure et le contenu de la section "reasoning" pour refléter les étapes logiques soutenant la bonne réponse. L'"ATOMIC REASONING STEP" doit utiliser l'une des "Reasoning Skills" suivantes :
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

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["implicit_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["implicit_1"]["output"]} \n

### OUTPUT REMINDER
Assurez-vous que votre sortie respecte la structure JSON comme indiqué et démontré dans l'exemple en contexte.
'''
