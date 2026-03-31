import os, json, sys


#! mCSQA Rubrics

mcsqa_commonsenseness = {
    "task": "Evaluate the 'Commonsense-ness' of a multiple-choice commonsense question.",
    "evaluation_criteria": "Does answering the question rely solely on commonsense knowledge accessible to the general population, or does it require formal reasoning and specialized expertise beyond everyday understanding?",
    "rubric": {
        "1": "The question requires formal reasoning and specialized expertise to answer correctly. It demands advanced knowledge in a specific field, technical terminology, or in-depth understanding that goes beyond general life experience. The average person, relying only on commonsense knowledge, would find it challenging or impossible to select the correct answer without additional study or expertise.",
        "2": "The question can be addressed with some commonsense reasoning but may also require moderate specific knowledge or logical deduction. While not entirely dependent on formal expertise, it involves concepts or facts that are not universally known but can be reasoned through by an informed individual. The average person might answer correctly with thoughtful consideration but could also be misled without careful analysis.",
        "3": "The question is answerable using basic commonsense knowledge that is widely shared and understood by the general population. It does not rely on any specialized information or formal reasoning processes. The correct answer should be apparent to most people through everyday experience and general understanding of the world."
    }
}

mcsqa_complexity = {
    "task": "Evaluate the 'Hardness/Complexity' of a commonsense question.",
    "evaluation_criteria": "How difficult is the question to understand and answer? Does it require minimal reasoning or a complex, multi-step thought process to identify the correct answer?",
    "rubric": {
        "1": "The question is very easy to understand, and the correct answer can be quickly identified with a single, straightforward reasoning step. It requires minimal cognitive effort, and most individuals can arrive at the correct answer almost immediately without confusion.",
        "2": "The question is relatively easy to understand, requiring only a couple of straightforward reasoning steps to identify the correct answer. While the question may introduce one or two elements that require brief consideration, the overall context remains clear. Most people can find the correct answer with a small amount of thought.",
        "3": "The question is moderately challenging, necessitating several reasoning steps to accurately comprehend and resolve. It introduces multiple elements or scenarios that require a careful thought process to integrate and analyze. Many individuals will need to pause and deliberately work through the connections or implications before reaching the correct answer.",
        "4": "The question is hard to comprehend and necessitates a complex thought process with multiple reasoning steps. It may involve abstract concepts, less obvious relationships, or misleading information that requires careful analysis. Individuals must invest significant cognitive effort to work through the complexities and identify the correct answer.",
        "5": "The question is very hard to comprehend and requires a long reasoning process with multiple reasoning steps to find the right answer. It demands high-level critical thinking, problem-solving skills, and possibly specialized knowledge. Only with thorough analysis and persistence can individuals navigate the complexity to arrive at the correct answer."
    }
}

mcsqa_expandability = {
    "task": "Evaluate the 'Expandability' of a commonsense question.",
    "evaluation_criteria": "To what extent can the question be expanded or elaborated upon to introduce additional complexity or dimensions?",
    "rubric": {
        "1": "The question cannot be expanded. It is inherently simplistic and covers a very narrow topic or scenario. There is little to no room for introducing additional elements, dimensions, or complexity without altering the fundamental nature of the question. The question stands effectively as a self-contained unit with minimal potential for elaboration.",
        "2": "The question has some potential for expansion. While it currently covers its intended scope adequately, there is moderate room to add a few additional elements or explore related themes that could introduce more complexity. The question can be expanded moderately by incorporating extra conditions, perspectives, or related scenarios, but such additions are not numerous.",
        "3": "The question can be significantly expanded to become a more complex question. It has ample scope for adding new dimensions, scenarios, or layers of reasoning. By introducing additional variables, conditional information, or intricate details, the question can transform into a more challenging problem that requires advanced reasoning and deeper comprehension."
    }
}

#! CulBank Rubrics

culbank_multicultureness = {
	"task": "evaluate the 'Multicultural-ness' of a commonsense cultural situation",
	"evaluation_criteria": "Does the situation involve interactions between multiple distinct cultures, reflecting a blend of practices, norms, or etiquette from each?",
	"rubric": {
		"1": "The situation is primarily rooted in a single culture, without significant influence or interaction from other cultural norms or practices. The interactions and behaviors exhibited are almost exclusively aligned with one cultural tradition, lacking a blend of cultural elements or considerations from another distinct culture.",
		"2": "The situation involves elements from two cultures, showing some level of cross-cultural interaction. While both cultural influences are present, the interaction may largely reflect the dominance of one culture over the other, with limited integration or blending of unique practices, norms, or etiquette from both cultures.",
		"3": "The situation reflects a rich blend of cultural interactions involving more than two distinct cultures. It demonstrates a balanced integration of diverse cultural practices, norms, or etiquette. The interactions and behaviors of the parties involved show a deep understanding and appreciation of multiple cultural perspectives, leading to an enriching multicultural exchange."
	}
}

culbank_commonsenseness = {
	"task": "evaluate the 'Commonsense-ness' of a cultural situation",
	"evaluation_criteria": "To what extent can the situation be understood and addressed using basic commonsense knowledge, without requiring specialized or expert reasoning?",
	"rubric": {
		"1": "The situation requires formal reasoning and specialized expertise to understand and address appropriately. It involves complex cultural nuances or specific knowledge that goes beyond general commonsense understanding. Responding effectively necessitates familiarity with detailed cultural protocols or insider knowledge.",
		"2": "The situation can be partially addressed using commonsense knowledge, but some elements require a deeper understanding or contextual insights that may not be readily apparent to someone without specific cultural awareness. While general reasoning can guide some actions, certain aspects benefit from additional cultural knowledge or experience.",
		"3": "The situation can be appropriately addressed using basic commonsense reasoning. It involves straightforward cultural interactions that do not demand specialized knowledge. Commonsense understanding of general social norms and human interactions is sufficient to respond suitably and effectively in this context."
	}
}

culbank_complexity = {
    "task": "Evaluate the 'Complexity' of a cultural situation.",
    "evaluation_criteria": "How intricate is the cultural situation in terms of nuances, number of cultural elements, perspectives, social dynamics, and interactions, requiring varying depths of understanding to navigate appropriately?",
    "rubric": {
        "1": "The situation is very simple, involving a single cultural aspect with straightforward practices and minimal perspectives or interactions. Understanding and responding require little to no specialized knowledge or awareness of cultural nuances.",
        "2": "The situation has minor complexity, incorporating a couple of cultural elements or perspectives with basic interactions. There are some cultural nuances, but they are easily understood with general awareness. Navigating the situation may require modest cultural sensitivity but is generally manageable.",
        "3": "The situation is moderately complex, involving several cultural elements, multiple perspectives, and noticeable social dynamics. Understanding and responding appropriately require some cultural knowledge and sensitivity to nuances. There is potential for misunderstandings without a moderate level of cultural competence.",
        "4": "The situation is complex, featuring numerous cultural elements, diverse perspectives, intricate social dynamics, and significant interactions. Navigating the situation effectively necessitates considerable cultural competence, an awareness of subtle nuances, and an understanding of how different cultural norms might conflict or interact.",
        "5": "The situation is highly complex, encompassing a multitude of deeply intertwined cultural elements, perspectives, and interactions. It includes profound cultural nuances, ambiguous social cues, and a high potential for misunderstandings. Expert knowledge and significant experience are required to address it appropriately, as the situation may involve conflicting norms and requires advanced cultural navigation skills."
    }
}



culbank_expandability = {
    "task": "Evaluate the 'Expandability' of a cultural situation",
    "evaluation_criteria": "Assess the potential for the situation to be expanded by including additional cultural dimensions, participants, interactions, and its adaptability to different contexts.",
    "rubric": {
        "1": "The situation is tightly defined within a single cultural framework, offering little room for the addition of new cultural dimensions. It does not easily support additional participants or interactions, requiring significant adaptation for expansion. It is context-specific and struggles to adapt to different settings or applications.",
        "2": "The situation allows for the inclusion of some additional cultural dimensions without drastically altering the core context. It can accommodate more participants or interactions with some adjustments to existing dynamics. There is some flexibility for adaptation to similar contexts or applications, albeit with moderate effort needed.",
        "3": "The situation is flexible and open, easily incorporating multiple new cultural dimensions or elements. It naturally supports additional participants and interactions without losing coherence. It is broadly applicable and adaptable across varied contexts and applications, maintaining core effectiveness and relevance."
    }
}


