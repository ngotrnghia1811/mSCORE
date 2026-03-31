from liquid import Template
from .icl_examples import DE_ICL_EXAMPLES as ICL_EXAMPLES


#SECTION: INPUT PROMPT

input_infer = Template('''
EINGABE:
{{question}}

AUSGABE:
''')

input_gen = Template('''
EINGABE:
{{question}}

AUSGABE:
''')


input_expand = Template('''
EINGABE:
{{question}}

AUSGABE:
''')


input_implicit = Template('''
EINGABE:
{{question}}

AUSGABE:
''')

#SECTION: ROLE PROMPT

llm_roles = {
    "commonsense_infer": 
      """
      Sie sind ein Sprachmodell mit fortgeschrittenen Fähigkeiten im Bereich des gesunden Menschenverstands, fähig zu logischem und analytischem Denken, heuristischem und intuitivem Denken, vergleichender und hypothetischer Analyse sowie kontextuellem und spezialisiertem Verständnis.
      """,
    "commonsense_gen": 
      """
      Sie sind ein Sprachmodell mit fortgeschrittenen Fähigkeiten im Bereich des gesunden Menschenverstands, fähig zu logischem und analytischem Denken, heuristischem und intuitivem Denken, vergleichender und hypothetischer Analyse sowie kontextuellem und spezialisiertem Verständnis.
      """,
    "culbank_gen": 
      """
      Sie sind ein Sprachmodell mit fortgeschrittenen Fähigkeiten im Bereich des gesunden Menschenverstands, fähig zu logischem und analytischem Denken, heuristischem und intuitivem Denken, vergleichender und hypothetischer Analyse sowie kontextuellem und spezialisiertem Verständnis.
      """, 
    "commonsense_expand": 
      """
      Sie sind ein Sprachmodell mit fortgeschrittenen Fähigkeiten im Bereich des gesunden Menschenverstands, fähig zu logischem und analytischem Denken, heuristischem und intuitivem Denken, vergleichender und hypothetischer Analyse sowie kontextuellem und spezialisiertem Verständnis.
      """,
    "commonsense_implicit": 
      """
      Sie sind ein Sprachmodell mit fortgeschrittenen Fähigkeiten im Bereich des gesunden Menschenverstands, fähig zu logischem und analytischem Denken, heuristischem und intuitivem Denken, vergleichender und hypothetischer Analyse sowie kontextuellem und spezialisiertem Verständnis.
      """,
}



#SECTION: TASK DESCRIPTION
task_descriptions = {
    "commonsense_infer": 
      """
      Ihre Aufgabe ist es, Mehrfachauswahl-Fragen zum gesunden Menschenverstand zu beantworten, indem Sie einen detaillierten "REASONING PROCESS" bereitstellen, der mehrere "REASONING STEPs" umfasst. Jeder "REASONING STEP" sollte ein "ATOMIC REASONING STEP" sein — eine unteilbare Einheit des Denkens, die überwiegend eine Denktechnik nutzt. Es handelt sich um einen einzigen, zusammenhängenden Gedankengang, der nicht in kleinere Schritte zerlegt werden kann, ohne seine Bedeutung zu verlieren. Das Ziel ist es, die minimale Anzahl an Schritten zu verwenden, wobei sichergestellt wird, dass jeder Schritt nicht redundant ist und dazu beiträgt, die möglichen Optionen einzugrenzen, indem eine oder mehrere Antwortmöglichkeiten ausgeschlossen werden.
      """,
    "commonsense_gen": 
      """
      Bei vorgegebenen Mehrfachauswahl-Fragen zum gesunden Menschenverstand mit der richtigen Option besteht Ihre Aufgabe darin, einen "COMMONSENSE CONTEXT" bereitzustellen, um die gegebene Frage zu erweitern, und einen detaillierten "REASONING PROCESS" zu liefern, der mehrere "REASONING STEPs" umfasst, um zur korrekten Antwort zu gelangen. 
        + Ein "COMMONSENSE CONTEXT" zur Frage bezieht sich auf das Hintergrundwissen oder zusätzliche Details, die allgemein verstanden werden, ohne dass spezielles Wissen erforderlich ist, einschließlich Faktoren wie Zeit, Ort, soziale Normen, kulturelle Einflüsse und andere relevante Details, die das Verständnis des Themas formen.
        + Jeder "REASONING STEP" sollte ein "ATOMIC REASONING STEP" sein — eine unteilbare Einheit des Denkens, die überwiegend eine Denktechnik nutzt. Es handelt sich um einen einzigen, zusammenhängenden Gedankengang, der nicht in kleinere Schritte zerlegt werden kann, ohne seine Bedeutung zu verlieren. Der "REASONING PROCESS" muss so effizient wie möglich sein, indem nur die minimal notwendige Anzahl von Schritten verwendet wird, und es muss sichergestellt werden, dass jeder Schritt nicht redundant ist und dazu beiträgt, die möglichen Optionen einzugrenzen, indem eine oder mehrere Antwortmöglichkeiten ausgeschlossen werden.
      """,
    "culbank_gen": 
      """
      Ihre Aufgabe ist es, eine Mehrfachauswahl-Frage zum gesunden Menschenverstand zu erstellen, die auf einer bestimmten kulturellen Situation im folgenden Format basiert:
      {
          "cultural_topic": "Kulturgruppe - Thema - Szenario",
          "social_context": "Einstellungen, in denen das Verhalten stattfindet",
          "actor": "wer das Verhalten zeigt",
          "question": "die Frage zum gesunden Menschenverstand bezüglich des Verhaltens des Akteurs",
          "actor_behavior": "Verhalten des Akteurs - auf das stark geeinigt wurde (die korrekte Antwortoption)",
          "recipient": "Empfänger der Handlung",
          "relation": "Beziehung zwischen dem Akteur und dem Empfänger",
          "recipient_behavior": "Verhalten des Empfängers",
      }
      Die Frage sollte den kulturellen Kontext implizit einbeziehen und die Fähigkeit der KI herausfordern, gesunden Menschenverstand zu nutzen, um zur richtigen Antwort zu gelangen. Das Ziel ist es, das Verständnis der KI für kulturelle Normen und Verhaltensweisen in einem bestimmten Umfeld zu testen und zu verbessern.
      Liefern Sie den detaillierten "REASONING PROCESS", um zur richtigen Antwortoption zu gelangen, der mehrere "REASONING STEPs" umfasst, um zur richtigen Antwort zu gelangen. Jeder "REASONING STEP" sollte ein "ATOMIC REASONING STEP" sein — eine unteilbare Einheit des Denkens, die überwiegend eine Denktechnik nutzt. Es handelt sich um einen einzigen, zusammenhängenden Gedankengang, der nicht in kleinere Schritte zerlegt werden kann, ohne seine Bedeutung zu verlieren. Der "REASONING PROCESS" muss so effizient wie möglich sein, indem nur die minimal notwendige Anzahl von Schritten verwendet wird, und es muss sichergestellt werden, dass jeder Schritt nicht redundant ist und dazu beiträgt, die möglichen Optionen einzugrenzen, indem eine oder mehrere Antwortmöglichkeiten ausgeschlossen werden.
      """, 
    "commonsense_expand": 
      """
        Bei einer vorgegebenen Mehrfachauswahl-Frage zum gesunden Menschenverstand mit ihren Optionen besteht Ihre Aufgabe darin, sie zu ändern und zu erweitern, um eine komplexere Frage zu schaffen, indem ihr Kontext erweitert, die Frage modifiziert, die Antwortmöglichkeiten angepasst und ein zusätzlicher REASONING STEP hinzugefügt werden. Ihr Ergebnis sollte den erweiterten Kontext, die modifizierte Frage, die überarbeiteten Antwortmöglichkeiten, die richtige Antwort und einen detaillierten "REASONING PROCESS" enthalten.
      """,
    "commonsense_implicit": 
      """
        Bei einer vorgegebenen Mehrfachauswahl-Frage zum gesunden Menschenverstand mit ihren Optionen besteht Ihre Aufgabe darin, sie zu ändern und zu erweitern, um eine komplexere Frage zu schaffen, indem ihr Kontext erweitert, die Frage modifiziert, die Antwortmöglichkeiten angepasst und ein zusätzlicher REASONING STEP hinzugefügt wird. Ihr Ergebnis sollte den erweiterten Kontext, die modifizierte Frage, die überarbeiteten Antwortmöglichkeiten, die richtige Antwort und einen detaillierten "REASONING PROCESS" enthalten.
      """,
}



#SECTION: REASONING SKILL
reasoning_skills = {
    'inductive_reasoning': {
        "short_description": "Allgemeine Schlussfolgerungen aus spezifischen Beobachtungen ziehen.",
        "long_description": "Induktives Denken ist eine Methode, um allgemeine Schlussfolgerungen aus spezifischen Beobachtungen zu ziehen. Im Gegensatz zum deduktiven Denken, das mit allgemeinen Prämissen beginnt, um zu spezifischen Schlussfolgerungen zu gelangen, beginnt das induktive Denken mit detaillierten Fakten und baut auf diese Weise breitere Verallgemeinerungen oder Theorien auf. Dieser Ansatz wird häufig in der wissenschaftlichen Forschung verwendet, bei der wiederholte Experimente und Beobachtungen zur Formulierung übergreifender Prinzipien oder Hypothesen führen.",
        "abstract_example": "Nachdem Sie mehrere Fälle beobachtet haben, in denen Ereignis A_1 zu Ereignis A_2 führt, folgern Sie, dass Ereignis A_n in zukünftigen Vorkommen ebenfalls zu Ereignis A_2 führen wird.",
        "concrete_example": "Nachdem Sie mehrmals beobachtet haben, dass die Wettervorhersage Regen ankündigt, folgern Sie, dass es wahrscheinlich weiterhin regnen wird.",
    },
    "deductive_reasoning": {
        "short_description": "Spezifische Schlussfolgerungen aus allgemeinen Prämissen ableiten.",
        "long_description": "Deduktives Denken beinhaltet die Ableitung spezifischer Schlussfolgerungen aus allgemeinen Prämissen. Es stellt sicher, dass, wenn die Prämissen wahr sind und das Denken gültig ist, die Schlussfolgerung ebenfalls wahr sein muss. Deduktive Logik ist grundlegend für Bereiche, die einen rigorosen Beweis erfordern, wie Mathematik und formale Wissenschaften.",
        "abstract_example": "Angesichts der Prämisse, dass alle X Y sind, und der Tatsache, dass Objekt x₁ ein X ist, folgern Sie, dass Objekt x₁ ebenfalls ein Y sein muss.",
        "concrete_example": "Da alle Vögel Federn haben und ein Spatz ein Vogel ist, hat ein Spatz daher Federn."
    },
    "abductive_reasoning": {
        "short_description": "Bildung von Hypothesen zur Erklärung von Beobachtungen.",
        "long_description": "Abduktives Denken ist der Prozess der Bildung von Hypothesen zur Erklärung von Beobachtungen. Es beginnt mit einem unvollständigen Satz von Beobachtungen und geht zur wahrscheinlichsten möglichen Erklärung über. Im Gegensatz zu deduktivem und induktivem Denken sucht das abduktive Denken nach der einfachsten und plausibelsten Erklärung für einen gegebenen Sachverhalt, was oft zur Generierung neuer Theorien oder Hypothesen führt.",
        "abstract_example": "Beobachtend, dass Ereignis B stattfindet, stellen Sie die Hypothese auf, dass Ursache 2 die wahrscheinlichste Erklärung unter mehreren möglichen Ursachen ist.",
        "concrete_example": "Sie wachen auf und sehen, dass die Straße nass ist. Die wahrscheinlichste Erklärung ist, dass es letzte Nacht geregnet hat.",
    },
    "analogical_reasoning": {
        "short_description": "Ziehung von Parallelen zwischen ähnlichen Situationen, um Schlussfolgerungen abzuleiten.",
        "long_description": "Analogisches Denken beinhaltet das Ziehen von Parallelen zwischen ähnlichen Situationen, um Schlüsse zu ziehen. Durch den Vergleich zweier Objekte oder Systeme, die bestimmte Eigenschaften teilen, kann man darauf schließen, dass sie zusätzliche, unbemerkte Eigenschaften teilen könnten. Diese Denkweise wird häufig in der Problemlösung, wissenschaftlichen Entdeckung und in der juristischen Argumentation verwendet, um Wissen von einem bekannten Bereich (Quelle) auf einen unbekannten Bereich (Ziel) zu übertragen.",
        "abstract_example": "Nachdem Sie beobachtet haben, dass Komponente C_1₁ in Situation C_a mit Komponente C_1_b interagiert, folgern Sie, dass Komponente C_2₁ und Komponente C_2_a in Situation C_b ähnlich interagieren werden.",
        "concrete_example": "So wie ein Gärtner Pflanzen gießt, um ihr Wachstum zu fördern, stellt ein Lehrer Wissen und Anleitung zur Verfügung, um die Entwicklung der Schüler zu unterstützen."
    },
    "counterfactual_reasoning": {
        "short_description": "Betrachtung alternativer Szenarien und Ergebnisse, die nicht eingetreten sind.",
        "long_description": "Kontrafaktisches Denken bezieht das Nachdenken über alternative Szenarien und Ergebnisse ein, die nicht eingetreten sind. Es beinhaltet das Vorstellen von 'was passiert wäre', unter anderen Umständen, was nützlich ist, um Kausalität zu verstehen, Entscheidungen zu bewerten und zukünftige Handlungen zu planen.",
        "abstract_example": "Indem Sie über die Bedingung X nachdenken, die nicht eingetreten ist, stellen Sie sich vor, dass, wenn sie eingetreten wäre, Outcome Y das Outcome Z ersetzt hätte.",
        "concrete_example": "Wenn Sie das Haus fünf Minuten früher verlassen hätten, hätten Sie den Bus rechtzeitig erwischt.",
    },
    "probabilistic_reasoning": {
        "short_description": "Anwendung von Wahrscheinlichkeitsprinzipien, um Schlussfolgerungen unter Unsicherheit zu ziehen.",
        "long_description": "Probabilistisches Denken beinhaltet die Anwendung von Wahrscheinlichkeitsprinzipien, um Schlüsse unter Unsicherheit zu ziehen. Es ermöglicht es, die Wahrscheinlichkeit verschiedener Ergebnisse zu bewerten und informierte Entscheidungen basierend auf der Wahrscheinlichkeit verschiedener Ereignisse zu treffen.",
        "abstract_example": "Indem Sie bewerten, dass Option A eine höhere Wahrscheinlichkeit (P(A) > P(B)) auf Erfolg hat als Option B, entscheiden Sie, Option A zu wählen.",
        "concrete_example": "Da es eine 70%ige Chancen auf Regen gibt, entscheiden Sie sich dafür, einen Regenschirm mitzunehmen, wenn Sie das Haus verlassen."
    },
    "temporal_reasoning": {
        "short_description": "Verständnis von Abfolgen und Dauern von Ereignissen.",
        "long_description": "Temporales Denken ist die Fähigkeit, die Abfolge und Dauer von Ereignissen über die Zeit hinweg zu verstehen und zu verarbeiten. Es umfasst das Verständnis zeitlich spezifischer Daten, wie der Reihenfolge von Ereignissen, wie lange sie dauern und die Beziehungen zwischen verschiedenen Zeitpunkten.",
        "abstract_example": "Bei der Tagesplanung organisieren Sie Ereignis T_1 so, dass es vor Ereignis T_2 stattfindet, um die richtige Abfolge der Aktivitäten sicherzustellen.",
        "concrete_example": "Sie beobachten, dass die Sonne am Morgen aufgeht und am Abend untergeht. Sie schließen daraus, dass der Mond zur gleichen Zeit auf- und untergeht."
    },
    "spatial_reasoning": {
        "short_description": "Visualisierung und Manipulation von Objekten im Raum.",
        "long_description": "Räumliches Denken beinhaltet die Visualisierung und Manipulation von Objekten im Raum. Es umfasst das Verständnis der Beziehungen zwischen verschiedenen Objekten, wie deren Position, Orientierung und Bewegung zueinander.",
        "abstract_example": "Beim Möbelarrangement visualisieren Sie Objekt S_1 und Objekt S_2, um ihre optimale Platzierung im Raum zu bestimmen.",
        "concrete_example": "Ein Architekt bestimmt den besten Standort für ein Fenster, indem er das Fenster und die umgebenden Wände visualisiert, um den optimalen Winkel und die optimale Höhe festzulegen."
    },
    "social_reasoning": {
        "short_description": "Verständnis sozialer Interaktionen und Normen.",
        "long_description": "Soziales Denken umfasst das Verständnis sozialer Interaktionen und Normen. Es beinhaltet die Fähigkeit, soziale Situationen zu analysieren und zu interpretieren, angemessene und unangemessene Verhaltensweisen zu erkennen und die Absichten, Emotionen und Gedanken anderer vorherzusagen.",
        "abstract_example": "Indem Sie bemerken, wie sich Person A in Situation S verhält, passen Sie Ihr eigenes Verhalten (Verhalten B) an, um effektiv zu interagieren.",
        "concrete_example": "Sie bemerken, dass Ihr Freund nach einem Gespräch niedergeschlagen aussieht und fragen ihn, ob alles in Ordnung ist.",
    }, 
    "moral_reasoning": {
        "short_description": "Entscheidungen darüber treffen, was richtig oder falsch ist, basierend auf ethischen Prinzipien.",
        "long_description": "Moralisches Denken ist der Prozess der Entscheidung darüber, was richtig oder falsch ist, basierend auf ethischen Prinzipien. Es beinhaltet die Bewertung von Handlungen, Absichten und Konsequenzen zur Beurteilung moralischer Fragestellungen.",
        "abstract_example": "Indem Sie in Erwägung ziehen, dass Handlung M der Person C schaden könnte, kommen Sie zu dem Schluss, dass sie moralisch falsch ist und entscheiden sich für eine alternative Handlung, die ethische Prinzipien respektiert.",
        "concrete_example": "Wenn Sie jemanden sehen, der seine Geldbörse fallen lässt, entscheiden Sie sich, sie zurückzugeben, anstatt das Geld zu behalten, weil es das Richtige ist."
    }
}

general_reasoning_skills = {
  "logical_reasoning": {
    "short_description": "Strukturierte Ansätze zur Ableitung von Schlussfolgerungen.",
    "long_description": "Das logische Denken umfasst Formen des logischen Schließens, die strukturierte Prozesse verwenden, um aus gegebenen Informationen Schlussfolgerungen zu ziehen. Dazu gehören Methoden wie das deduktive, induktive und abduktive Schließen, die in wissenschaftlichen und analytischen Disziplinen grundlegend sind, um sicherzustellen, dass Schlussfolgerungen logisch stichhaltig sind."
  },
  "contextual_reasoning": {
    "short_description": "Verständnis von Beziehungen und Kontexten zwischen Elementen.",
    "long_description": "Das kontextuelle Denken umfasst Fähigkeiten, die eingesetzt werden, um Beziehungen, Kontexte und Dynamiken zwischen Elementen zu verstehen. Es deckt verschiedene Arten des Schließens ab, wie das analoge, kontrafaktische, probabilistische, temporale und räumliche Denken, die verwendet werden, um Szenarien zu bewerten, Ergebnisse vorherzusagen und Probleme in unterschiedlichen Kontexten zu lösen."
  },
  "social_and_ethical_reasoning": {
    "short_description": "Denken im Zusammenhang mit sozialen Interaktionen und ethischen Prinzipien.",
    "long_description": "Das soziale und ethische Denken beinhaltet Fähigkeiten, die darauf abzielen, soziale Interaktionen zu verstehen und ethische Prinzipien zu bewerten. Es umfasst soziales und moralisches Denken, das entscheidend ist, um Verhaltensweisen zu interpretieren, in komplexen sozialen Umfeldern zu navigieren und Entscheidungen auf der Grundlage ethischer Überlegungen zu treffen."
  }
}


#SECTION: OUTPUT FORMAT
output_formats = {
    "with_skills": '''
    ```json
    {
      "commonsense_question": "Fragetext",
      "options": {
          "A": "Antworttext_Option_A",
          ...
      },
      "correct_answer": ["Antwortoption", "Antworttext"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "Name_der_Denkfertigkeit",
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "Name_der_Denkfertigkeit",
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          }
      }
    }
    ```
    ''',

    "with_context_and_skills": '''
    ```json
    {
      "commonsense_context": "Kontext_Text",
      "commonsense_question": "Fragetext",
      "options": {
          "A": "Antworttext_Option_A",
          ...
      },
      "correct_answer": ["Antwortoption", "Antworttext"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning_skill": "Name_der_Denkfertigkeit",
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          },
          ...
          "reasoning_step_n": {
              "reasoning_skill": "Name_der_Denkfertigkeit",
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          }
      }
    }
    ```
    ''',

    "without_skills": '''
    ```json
    {
      "commonsense_question": "Fragetext",
      "options": {
          "A": "Antworttext_Option_A",
          ...
      },
      "correct_answer": ["Antwortoption", "Antworttext"]
    }
    ```
    ''',

    "with_context_without_skills": '''
    ```json
    {
      "commonsense_context": "Kontext_Text",
      "commonsense_question": "Fragetext",
      "options": {
          "A": "Antworttext_Option_A",
          ...
      },
      "correct_answer": ["Antwortoption", "Antworttext"]
    }
    ```
    ''',

    'cot_without_skills': '''
    ```json
    {
      "commonsense_question": "Fragetext",
      "options": {
          "A": "Antworttext_Option_A",
          ...
      },
      "correct_answer": ["Antwortoption", "Antworttext"],
      "reasoning_process": {
          "reasoning_step_1": {
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          },
          ...
          "reasoning_step_n": {
              "reasoning": "Denken_Text",
              "eliminated_options": [Liste_der_ausgeschlossenen_Optionen],
              "possible_options": [Liste_der_verbleibenden_Optionen]
          }
      }
    }
    ```
    '''
}


#SECTION: INFERENCE
logical_inference = f'''
Ihre Aufgabe besteht darin, Multiple-Choice-Fragen zum Allgemeinwissen zu beantworten. Erklären Sie Ihren Denkprozess unter Verwendung der folgenden "DENKFÄHIGKEITEN":
    + inductive_reasoning: {reasoning_skills["inductive_reasoning"]["short_description"]}
    + deductive_reasoning: {reasoning_skills["deductive_reasoning"]["short_description"]}
    + abductive_reasoning: {reasoning_skills["abductive_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_logic_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_logic_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''

general_inference = f'''
Ihre Aufgabe besteht darin, Multiple-Choice-Fragen zum Allgemeinwissen zu beantworten. Erklären Sie Ihren Denkprozess unter Verwendung der folgenden "DENKFÄHIGKEITEN":
    + logical_reasoning: {general_reasoning_skills["logical_reasoning"]["short_description"]}
    + contextual_reasoning: {general_reasoning_skills["contextual_reasoning"]["short_description"]}
    + social_and_ethical_reasoning: {general_reasoning_skills["social_and_ethical_reasoning"]["short_description"]}

### IN-CONTEXT EXAMPLES
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_general_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_general_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''


standard_inference_o1 = f'''
Ihre Aufgabe besteht darin, Multiple-Choice-Fragen zum Allgemeinwissen zu beantworten. Erklären Sie Ihren Denkprozess unter Verwendung der folgenden "DENKFÄHIGKEITEN":
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
{ICL_EXAMPLES["infer_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''  

standard_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Lesen Sie die Frage sorgfältig zusammen mit allen bereitgestellten Antwortoptionen.
2. Beantworten Sie die Frage, indem Sie die richtige Antwortoption wählen.
3. Beschreiben Sie Ihren schrittweisen "REASONING PROCESS", um zu Ihrer Antwort zu gelangen. Jeder "ATOMIC REASONING STEP" muss dieser Reihenfolge folgen:
	3.1. Wählen Sie eine Denkskala aus der folgenden Liste aus, die für den REASONING STEP verwendet werden soll:
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
	3.2. Anwenden der ausgewählten "REASONING SKILL": Geben Sie eine kurze Erklärung, wie die ausgewählte "REASONING SKILL" angewendet wird, um bestimmte Antwortoptionen auszuschließen oder die richtige Antwortoption zu verstärken. Stellen Sie sicher, dass das Denken klar ist und nicht weiter in kleinere Schritte unterteilt werden kann.
	3.3. Ausschluss von Optionen: Listen Sie die Optionen auf, die basierend auf Ihrem Denken in diesem Schritt ausgeschlossen wurden.
	3.4. Aktualisieren Sie die möglichen Optionen: Geben Sie die Liste der verbleibenden möglichen Optionen nach diesem Schritt an.
4. Erstellen Sie Ihren Output im JSON-Format mit der folgenden Struktur:
{output_formats["with_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["infer_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["infer_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''

#! cot
cot_inference_o1 = f'''
Ihre Aufgabe besteht darin, Multiple-Choice-Fragen zum allgemeinen Sinn zu beantworten und Ihren Denkprozess darzulegen, um die richtige Antwort zu finden.
Erstellen Sie Ihren Output im JSON-Format mit der folgenden Struktur:
{output_formats["cot_without_skills"]}

'''

cot_inference_4o = f'''
### LLM ROLE
{llm_roles["commonsense_infer"]} \n 
### TASK DESCRIPTION
{task_descriptions["commonsense_infer"]} \n
### STEP-BY-STEP INSTRUCTIONS
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Lesen Sie die Frage sorgfältig zusammen mit allen bereitgestellten Antwortoptionen.
2. Beantworten Sie die Frage, indem Sie die richtige Antwortoption wählen.
3. Beschreiben Sie Ihren schrittweisen "REASONING PROCESS", um zu Ihrer Antwort zu gelangen.
4. Erstellen Sie Ihren Output im JSON-Format mit der folgenden Struktur:
{output_formats["cot_without_skills"]}


'''


#SECTION: GENERATE

#! mCSQA
mcsqa_gen = f'''
### LLM ROLLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_gen"]} \n
### SCHRITT-FÜR-SCHRITT ANLEITUNG
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Verständnis der Frage: Lesen Sie die Frage sorgfältig zusammen mit allen bereitgestellten Antwortoptionen.
2. Hinzufügen des "COMMONSENSE CONTEXT": Erweitern Sie die ursprüngliche Frage, indem Sie einen zusätzlichen "COMMONSENSE CONTEXT" bereitstellen. Stellen Sie sicher, dass der hinzugefügte Kontext relevant ist und das Verständnis der Frage bereichert.
3. Beschreiben Sie Ihren schrittweisen "REASONING PROCESS", um zur richtigen Antwort zu gelangen. Jeder "ATOMIC REASONING STEP" muss dieser Reihenfolge folgen:
	3.1. Wählen Sie eine Denkskala aus der folgenden Liste aus, die für den REASONING STEP verwendet werden soll:
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
	3.2. Anwenden der ausgewählten "REASONING SKILL": Geben Sie eine kurze Erklärung, wie die ausgewählte "REASONING SKILL" angewendet wird, um bestimmte Antwortoptionen auszuschließen oder die richtige Antwortoption zu verstärken. Stellen Sie sicher, dass das Denken klar ist und nicht weiter in kleinere Schritte unterteilt werden kann.
	3.3. Ausschluss von Optionen: Listen Sie die Optionen auf, die basierend auf Ihrem Denken in diesem Schritt ausgeschlossen wurden.
	3.4. Aktualisieren Sie die möglichen Optionen: Geben Sie die Liste der verbleibenden möglichen Optionen nach diesem Schritt an.
4. Erstellen Sie Ihren Output im JSON-Format mit der folgenden Struktur:
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
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''


#! CultureBank
culbank_gen = f'''
### LLM ROLLE
{llm_roles["commonsense_gen"]} \n
### TASK DESCRIPTION
{task_descriptions["culbank_gen"]} \n
### STEP-BY-STEP INSTRUCTIONS
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Analysieren Sie die gegebene kulturelle Situation: Überprüfen Sie die Details der Kulturgruppe, den Kontext, das Verhalten der Akteure und andere Beschreibungen, um die Schlüsselelemente der Situation zu verstehen.
2. Hinzufügen des "COMMONSENSE CONTEXT": Basierend auf dem im Input gegebenen Kontext bezieht sich ein "COMMONSENSE CONTEXT" zur Frage auf das Hintergrundwissen oder zusätzliche Details, die allgemein verstanden werden, ohne dass spezielles Wissen erforderlich ist, einschließlich Faktoren wie Zeit, Ort, soziale Normen, kulturelle Einflüsse und andere relevante Details, die das Verständnis des Themas prägen.
3. Erstellen Sie die "Commonsense Question": Kombinieren Sie den kulturellen Kontext und die Anfrage der Person, um eine prägnante Frage zu formulieren. Stellen Sie sicher, dass die Frage den ursprünglichen Kontext IMPLIZIT einbezieht, ohne ihn explizit zu nennen. Erstellen Sie die richtige Antwortoption basierend auf dem "actor_behavior".
4. Erstellen Sie andere Antwortoptionen: Erstellen Sie 5 Antwortmöglichkeiten, von denen zwei plausible Optionen sein sollten. Die anderen beiden sollten Ablenkungen sein, die relevant und sinnvoll, aber basierend auf dem kulturellen Kontext falsch sind.
5. Beschreiben Sie Ihren schrittweisen "REASONING PROCESS", um zur richtigen Antwort zu gelangen. Jeder "ATOMIC REASONING STEP" muss dieser Reihenfolge folgen:
	5.1. Wählen Sie eine "REASONING SKILL" aus der folgenden Liste aus, die für den "REASONING STEP" verwendet werden soll:
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
	5.2. Anwenden der ausgewählten "REASONING SKILL": Geben Sie eine kurze Erklärung, wie die ausgewählte "REASONING SKILL" angewendet wird, um bestimmte Antwortoptionen auszuschließen oder die richtige Antwortoption zu verstärken. Stellen Sie sicher, dass das Denken klar ist und nicht weiter in kleinere Schritte unterteilt werden kann.  
	5.3. Ausschluss von Optionen: Listen Sie die Optionen auf, die basierend auf Ihrem Denken in diesem Schritt ausgeschlossen wurden.
	5.4. Aktualisieren Sie die möglichen Optionen: Geben Sie die Liste der verbleibenden möglichen Optionen nach diesem Schritt an.
6. Erstellen Sie Ihren Output im JSON-Format mit der folgenden Struktur:
{output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["culbank_gen_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["culbank_gen_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''


#! Complexity
expand_prompt = f'''
### LLM ROLLE
{llm_roles["commonsense_expand"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_expand"]} \n
### STEP-BY-STEP INSTRUCTIONS
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Verständnis der Frage: Lesen Sie die gegebene Frage und den Kontext sowie die Antwortoptionen sorgfältig durch.
2. Erweiterung des Kontexts: Fügen Sie zusätzliche Hintergrund- oder Situationsdetails zum "COMMONSENSE CONTEXT" hinzu, um der Frage mehr Tiefe und Denknotwendigkeiten zu verleihen.
3. Modifizierung der Frage: Nutzen Sie den "ERWEITERTEN COMMONSENSE CONTEXT", um eine komplexere Frage zu formulieren, während ihr Kerngedanke und der gesunde Menschenverstand beibehalten werden.
4. Anpassungen der Optionen:
    + Passen Sie die vorhandenen Antwortmöglichkeiten an, um mit der neuen, komplexen Frage übereinzustimmen.
    + Stellen Sie sicher, dass die richtige Antwortoption semantisch der ursprünglichen ähnlich bleibt.
    + Fügen Sie eine zusätzliche plausible, aber fehlerhafte Option hinzu, um die Komplexität der Frage zu erhöhen.
    + Halten Sie alle Antwortoptionen so prägnant wie die Originale.
5. Verfeinerung des Denkprozesses: Verfeinern Sie den ursprünglichen "REASONING PROCESS", um in den neuen Kontext zu passen. Der zusätzliche "ATOMIC REASONING STEP" muss eine der folgenden "REASONING SKILLs" verwenden:
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
6. Formatieren Sie den Output mithilfe des JSON-Formats mit der folgenden Struktur:
 {output_formats["with_context_and_skills"]}

### IN-CONTEXT EXAMPLE:
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["expand_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["expand_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''


#! Implicitation
implicit_prompt = f'''
### LLM ROLLE
{llm_roles["commonsense_implicit"]} \n
### TASK DESCRIPTION
{task_descriptions["commonsense_implicit"]} \n
### STEP-BY-STEP INSTRUCTIONS
Befolgen Sie diese Schritt-für-Schritt-Anleitung:
1. Analysieren Sie den bereitgestellten "commonsense_context", um die zugrunde liegenden Annahmen und das implizite Wissen zu verstehen, das für das logische Denken erforderlich ist.
2. Untersuchen Sie die "commonsense_question" und die zugehörigen "options", um die Schlüsselelemente zu identifizieren, die zum Beantworten der Frage erforderlich sind.
3. Umschreiben der "commonsense_question", indem Sie den ursprünglichen Kontext und die Frage kombinieren, um eine neue "commonsense_question" mit einem "IMPLIZITEN COMMONSENSE CONTEXT" zu erstellen. Stellen Sie sicher, dass die neue Frage klar und verständlich bleibt.
4. Überprüfen Sie, dass der "REASONING PROCESS" in der umgestalteten Frage unverändert bleibt, und bestätigen Sie, dass die richtige Antwort dieselbe ist wie im Original.
5. Stellen Sie sicher, dass alle Antwortoptionen vernünftig, relevant sind und ihren ursprünglichen Zweck im Kontext der umgeschriebenen Frage beibehalten.
6. Behalten Sie die Struktur und den Inhalt des "reasoning"-Abschnitts bei, um die logischen Schritte zu widerspiegeln, die die richtige Antwort unterstützen. Der "ATOMIC REASONING STEP" muss eine der folgenden "REASONING SKILLs" verwenden:
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

### IN-CONTEXT EXAMPLE
EXAMPLE 1 - INPUT :
{ICL_EXAMPLES["implicit_1"]["input"]} \n
EXAMPLE 1 - OUTPUT :
{ICL_EXAMPLES["implicit_1"]["output"]} \n

### OUTPUT REMINDER
Stellen Sie sicher, dass Ihr Output der JSON-Struktur folgt, wie im Beispiel und in der Anleitung beschrieben.
'''