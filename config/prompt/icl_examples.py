

EN_ICL_EXAMPLES = {
    "infer_1": 
    {
        "input": '''\
        ```json
        {
            "question": "What household appliance is used to keep food cold and prevent it from spoiling?",
            "options": {
                "A": "Oven",
                "B": "Refrigerator",
                "C": "Dishwasher",
                "D": "Microwave",
                "E": "Toaster"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
        "question": "What household appliance is used to keep food cold and prevent it from spoiling?",
        "options": {
            "A": "Oven",
            "B": "Refrigerator",
            "C": "Dishwasher",
            "D": "Microwave",
            "E": "Toaster"
        },
        "correct_answer": ["B", "Refrigerator"],
        "reasoning_process": {
            "reasoning_step_1": {
            "reasoning_skill": "causal_reasoning",
            "reasoning": "An oven heats food, which does not align with keeping food cold.",
            "eliminated_options": ["A"],
            "possible_options": ["B", "C", "D", "E"]
            },
            "reasoning_step_2": {
            "reasoning_skill": "deductive_reasoning",
            "reasoning": "A dishwasher cleans dishes; it is not used for storing or cooling food.",
            "eliminated_options": ["C"],
            "possible_options": ["B", "D", "E"]
            },
            "reasoning_step_3": {
            "reasoning_skill": "inductive_reasoning",
            "reasoning": "Microwaves and toasters are appliances that heat or toast food, not cool it.",
            "eliminated_options": ["D", "E"],
            "possible_options": ["B"]
            }
        }
        ```'''
    },
    "infer_logic_1":
    {
        "input": '''\
        ```json
        {
            "question": "What household appliance is used to keep food cold and prevent it from spoiling?",
            "options": {
                "A": "Oven",
                "B": "Refrigerator",
                "C": "Dishwasher",
                "D": "Microwave",
                "E": "Toaster"
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "What household appliance is used to keep food cold and prevent it from spoiling?",
            "options": {
                "A": "Oven",
                "B": "Refrigerator",
                "C": "Dishwasher",
                "D": "Microwave",
                "E": "Toaster"
            },
            "correct_answer": ["B", "Refrigerator"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "inductive_reasoning",
                    "reasoning": "From multiple observations, an oven, a microwave, and a toaster all heat food. None of these keep items cold.",
                    "eliminated_options": ["A", "D", "E"],
                    "possible_options": ["B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "If an appliance’s primary function is to preserve food by cooling, it must be a refrigerator.",
                    "eliminated_options": ["C"],
                    "possible_options": ["B"]
                }
            }
        }
        ```''',
    },
    "infer_general_1":
    {
        "input": '''\
        ```json
        {
            "question": "Which action is most likely to promote a healthy work-life balance?",
            "options": {
                "A": "Regularly working late hours",
                "B": "Setting clear work boundaries",
                "C": "Constantly checking work emails during personal time",
                "D": "Skipping lunch to get more work done",
                "E": "Taking short breaks throughout the day"
            },
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "Which action is most likely to promote a healthy work-life balance?",
            "options": {
                "A": "Regularly working late hours",
                "B": "Setting clear work boundaries",
                "C": "Constantly checking work emails during personal time",
                "D": "Skipping lunch to get more work done",
                "E": "Taking short breaks throughout the day"
            },
            "correct_answer": ["B", "Setting clear work boundaries"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "logical_reasoning",
                    "reasoning": "Promoting a healthy work-life balance typically requires practices that differentiate and manage time effectively between work and personal life. Regularly working late and checking work emails during personal time blend these boundaries.",
                    "eliminated_options": ["A", "C", "D"],
                    "possible_options": ["B", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_and_ethical_reasoning",
                    "reasoning": "Setting clear work boundaries respects both personal needs and professional responsibilities. While taking short breaks is beneficial, it doesn’t directly establish a strong boundary between work and life.",
                    "eliminated_options": ["E"],
                    "possible_options": ["B"]
                }
            }
        }
        ```''',
    },
    #! mcsqa_gen
    "mcsqa_gen_1":
    {
        "input": '''\
        ```json
        {
            "question": "What is the most practical and time-efficient method for a person to travel from New York City to London?",
            "options": {
                "A": "Taking a direct flight",
                "B": "Driving a car",
                "C": "Hitchhiking",
                "D": "Taking a train",
                "E": "Sailing on a private yacht",
            },
            "correct_answer": ["A", "Taking a direct flight"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "A person planning an international trip needs to consider factors such as distance, geography, time efficiency, and available modes of transportation. Traveling from New York City to London involves crossing the Atlantic Ocean. The most practical methods would involve air or sea travel, considering the vast oceanic distance and the impracticality of land travel in this context.",
            "commonsense_question": "What is the most practical and time-efficient method for a person to travel from New York City to London?",
            "options": {
                "A": "Taking a direct flight",
                "B": "Driving a car",
                "C": "Hitchhiking",
                "D": "Taking a train",
                "E": "Sailing on a private yacht",
            },
            "correct_answer": ["A", "Taking a direct flight"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "spatial_reasoning",
                    "reasoning": "There is an ocean between New York City and London, making it impossible to drive a car or take a train directly from one city to the other.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Hitchhiking across the Atlantic would rely on finding vessels willing to take a passenger without prior arrangement, which is highly unlikely and unpredictable.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "temporal_reasoning",
                    "reasoning": "Sailing on a private yacht is possible but significantly slower than flying, taking several days or weeks compared to hours.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ''',
    },
    "mcsqa_gen_2":
    {
        "input": '''\
        ```json
        {
            "question": "What is a common beverage that is often served at parties?",
            "options": {
                "A": "water",
                "B": "soda",
                "C": "tomato juice",
                "D": "milk",
                "E": "broth"
            },
            "correct_answer": ("B","soda"),
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "In many social settings, such as parties or social gatherings, certain foods and beverages are commonly served to guests as refreshments. Finger foods and drinks are particularly popular because they are easy to consume while socializing, do not require utensils, and often appeal to a wide range of tastes.",
            "commonsense_question": "What is a common beverage that is often served at parties?",
            "options": {
                "A": "water",
                "B": "soda",
                "C": "tomato juice",
                "D": "milk",
                "E": "broth"
            },
            "correct_answer": ["B","soda"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Milk are generally available in most settings but are not always seen as 'party drinks.' Tomato juice and broth are less commonly chosen for parties, where refreshments are intended to be casual and widely appealing.",
                    "eliminated_options": ["C", "D", "E"],
                    "possible_options": ["A","B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Soda is a popular beverage choice for parties due to its variety, carbonation, and appeal to all ages, making it more likely to be found at social events compared to water, which is often a default but not featured beverage.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B"]
                }
            }
        }
        ''',
    },
    #! culbank_gen
    "culbank_gen_1":
    {
        "input": '''\
        ```json
        {
            "cultural_topic": "Japanese culture - Gift Giving - Etiquette and Practices",
            "social_context": "During a business meeting in Japan, a visiting executive from a Western country wants to express gratitude to their hosts.",
            "actor": "Visiting executive",
            "question": "I am attending a business meeting in Japan and would like to give a small gift to my Japanese hosts. What should I consider to ensure my gesture is well-received?",
            "actor_behavior": "Offer a gift wrapped in traditional Japanese style as a gesture of appreciation",
            "recipient": "Japanese business hosts",
            "relation": "Business partners",
            "recipient_behavior": "Receive the gift with both hands and show appreciation"
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "In Japanese business culture, gift-giving is a common practice used to express gratitude and strengthen relationships. It's important to present gifts elegantly, often wrapped in specific ways that show respect and thoughtfulness. The act of giving is often more significant than the gift itself, demonstrating mutual respect.",
            "commonsense_question": "What is an important consideration for a Western executive when presenting a gift to their Japanese counterparts during a business meeting?",
            "options": {
                "A": "Ensure the gift is wrapped neatly and elegantly in traditional Japanese style.",
                "B": "Choose a very expensive gift to show the value of the relationship.",
                "C": "Present the gift before the meeting starts to set a positive tone.",
                "D": "Avoid gift giving as it might be seen as a bribe.",
                "E": "Only present gifts that are locally sourced from the executive's home country."
            },
            "answer": ["A", "Ensure the gift is wrapped neatly and elegantly in traditional Japanese style."],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Understanding that in Japan, the presentation of a gift is just as important as the gift itself, reflecting the giver's respect and thoughtfulness.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Consideration for timing suggests presenting a gift is not necessarily supposed to precede the meeting but is better given after to cement relationship progress.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "abductive_reasoning",
                    "reasoning": "While sourcing gifts locally can add personal touch, the key focus in Japanese culture is on presentation to signify respect and careful thought.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! expand_complexity
    "expand_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "When driving in rainy weather, visibility can be significantly reduced.",
            "commonsense_question": "Why should you turn on your headlights when it's raining?",
            "options": {
                "A": "To see better",
                "B": "To dry the headlights",
                "C": "To signal other drivers",
                "D": "To save battery",
                "E": "To warm up the car"
            },
            "correct_answer": ["A", "To see better"],
            "reasoning_process": {
                "reasoning_step_1": {
                "reasoning_skill": "deductive_reasoning",
                "reasoning": "In rainy weather, reduced visibility makes it harder to see the road and other vehicles. Turning on headlights improves visibility.",
                "eliminated_options": ["B", "D", "E"],
                "possible_options": ["A", "C"]
                },
                "reasoning_step_2": {
                "reasoning_skill": "social_reasoning",
                "reasoning": "Headlights also help other drivers see your vehicle, reducing the risk of accidents.",
                "eliminated_options": ["C"],
                "possible_options": ["A"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "When driving in rainy weather, visibility can be significantly reduced. Rain can obscure road markings and make it difficult to see other vehicles, pedestrians, and obstacles. Using headlights not only helps you see better but also makes your vehicle more visible to others. This is crucial for safety, especially during heavy rain or in low-light conditions.",
            "commonsense_question": "On a dark, rainy evening with heavy traffic, why is it essential to turn on your car's headlights?",
            "options": {
                "A": "To enhance visibility for yourself and make your car visible to others",
                "B": "To dry off the headlights quickly",
                "C": "To signal that you are stopping soon",
                "D": "To conserve energy in the vehicle",
                "E": "To heat the car interior faster",
                "F": "Because it's legally required in many areas"
            },
            "correct_answer": ["A", "To enhance visibility for yourself and make your car visible to others"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "In dark and rainy conditions, visibility is compromised. Headlights illuminate the road ahead and make your vehicle visible to others, which is essential for safe driving.",
                    "eliminated_options": ["B", "D", "E"],
                    "possible_options": ["A", "C", "F"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "'Signaling' typically involves using turn signals or brake lights. Headlights are primarily for visibility rather than signaling specific actions like stopping.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "F"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "moral_reasoning",
                    "reasoning": "'Legal requirements' (option F) support safety measures but are not the primary reason for turning on headlights. The key reason is safety—ensuring you can see and be seen.",
                    "eliminated_options": ["F"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! context_implicit
    "implicit_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "You are on an adventure trip in a remote area of a foreign country. During the trip, a member of your group experiences severe discomfort with symptoms like dizziness and shortness of breath, but language barriers and limited access to local healthcare make it difficult to seek immediate help. Additionally, there is limited internet connectivity, complicating communication with external resources.",
            "commonsense_question": "What is the most effective initial action to assess a group member’s health status during an adventure trip in a foreign country?",
            "options": {
                "A": "use a multilingual travel health app",
                "B": "seek local guide assistance",
                "C": "initiate emergency protocol",
                "D": "set up a telehealth call",
                "E": "consult a healthcare professional through offline support tools"
            },
            "correct_answer": ["E", "consult a healthcare professional through offline support tools"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Using a multilingual travel health app (option A) provides information but is insufficient for serious health concerns that need professional input.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Seeking local guide assistance (option B) may help with logistics but does not replace professional advice. Setting up a telehealth call (option D) is affected by limited internet connectivity and thus unreliable.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Initiating an emergency protocol (option C) could result in unnecessary escalation without confirming the severity through professional assessment.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_question": "During an adventure trip in a remote area of a foreign country where language barriers and internet connectivity are issues, what action should you take when a group member experiences severe discomfort with symptoms like dizziness and shortness of breath?",
            "options": {
                "A": "use a multilingual travel health app",
                "B": "seek local guide assistance",
                "C": "initiate emergency protocol",
                "D": "set up a telehealth call",
                "E": "consult a healthcare professional through offline support tools"
            },
            "correct_answer": ["E", "consult a healthcare professional through offline support tools"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Using a multilingual travel health app (option A) provides information but is insufficient for serious health concerns that need professional input.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Seeking local guide assistance (option B) may help with logistics but does not replace professional advice. Setting up a telehealth call (option D) is affected by limited internet connectivity and thus unreliable.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Initiating an emergency protocol (option C) could result in unnecessary escalation without confirming the severity through professional assessment.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```'''
    },
}







#SECTION:
#SECTION: ZH
#SECTION:

ZH_ICL_EXAMPLES = {
    "infer_1": 
    {
        "input": '''\
        ```json
        {
            "question": "哪种家用电器用于保持食物冷藏并防止其变质?",
            "options": {
                "A": "烤箱",
                "B": "冰箱",
                "C": "洗碗机",
                "D": "微波炉",
                "E": "烤面包机"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
        "question": "哪种家用电器用于保持食物冷藏并防止其变质?",
        "options": {
            "A": "烤箱",
            "B": "冰箱",
            "C": "洗碗机",
            "D": "微波炉",
            "E": "烤面包机"
        },
        "correct_answer": ["B", "冰箱"],
        "reasoning_process": {
            "reasoning_step_1": {
            "reasoning_skill": "causal_reasoning",
            "reasoning": "烤箱加热食物，这与保持食物冷藏不符。",
            "eliminated_options": ["A"],
            "possible_options": ["B", "C", "D", "E"]
            },
            "reasoning_step_2": {
            "reasoning_skill": "deductive_reasoning",
            "reasoning": "洗碗机清洗餐具；它不用于储存或冷藏食物。",
            "eliminated_options": ["C"],
            "possible_options": ["B", "D", "E"]
            },
            "reasoning_step_3": {
            "reasoning_skill": "intuitive_reasoning",
            "reasoning": "微波炉和烤面包机是加热或烘烤食物的电器，而不是用来冷藏食物。",
            "eliminated_options": ["D", "E"],
            "possible_options": ["B"]
            }
        }
        ```'''
    },
    "infer_logic_1":
    {
        "input": '''\
        ```json
        {
            "question": "哪种家用电器用于保持食物冷藏并防止其变质?",
            "options": {
                "A": "烤箱",
                "B": "冰箱",
                "C": "洗碗机",
                "D": "微波炉",
                "E": "烤面包机"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "哪种家用电器用于保持食物冷藏并防止其变质?",
            "options": {
                "A": "烤箱",
                "B": "冰箱",
                "C": "洗碗机",
                "D": "微波炉",
                "E": "烤面包机"
            },
            "correct_answer": ["B", "冰箱"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "inductive_reasoning",
                    "reasoning": "从多个观察来看，烤箱、微波炉和烤面包机都用于加热食物。这些都不保持物品冷冻。",
                    "eliminated_options": ["A", "D", "E"],
                    "possible_options": ["B", "C"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "如果电器的主要功能是通过冷冻来保存食物，那它必须是冰箱。",
                    "eliminated_options": ["C"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    "infer_general_1":
    {
        "input": '''\
        ```json
        {
            "question": "哪一种行为最可能促进健康的工作与生活平衡？",
            "options": {
                "A": "经常加班",
                "B": "设定明确的工作界限",
                "C": "在个人时间不断查看工作邮件",
                "D": "跳过午餐以完成更多工作",
                "E": "全天适时休息"
            },
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "哪一种行为最可能促进健康的工作与生活平衡？",
            "options": {
                "A": "经常加班",
                "B": "设定明确的工作界限",
                "C": "在个人时间不断查看工作邮件",
                "D": "跳过午餐以完成更多工作",
                "E": "全天适时休息"
            },
            "correct_answer": ["B", "设定明确的工作界限"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "logical_reasoning",
                    "reasoning": "促进健康的工作与生活平衡通常需要有效区分和管理工作和个人生活之间的时间。经常加班和在个人时间查看工作邮件会模糊这些界限。",
                    "eliminated_options": ["A", "C", "D"],
                    "possible_options": ["B", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_and_ethical_reasoning",
                    "reasoning": "设定明确的工作界限既尊重个人需求又顾及职业责任。虽然适时休息是有益的，但它并不能直接在工作与生活之间建立强有力的界限。",
                    "eliminated_options": ["E"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    #! mcsqa_gen
    "mcsqa_gen_1":
    {
        "input": '''\
        ```json
        {
            "question": "从纽约市到伦敦最实用和节省时间的旅行方法是什么?",
            "options": {
                "A": "搭乘直飞航班",
                "B": "开车",
                "C": "搭便车",
                "D": "乘火车",
                "E": "乘坐私人游艇",
            },
            "correct_answer": ["A", "搭乘直飞航班"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "计划国际旅行时需要考虑因素如距离、地理、时间效率和可用的交通方式。 从纽约市到伦敦的旅行需要跨过大西洋。考虑到广阔的海洋距离以及陆地旅行的不切实际，最实用的方法将涉及空中或海上旅行。",
            "commonsense_question": "从纽约市到伦敦最实用和节省时间的旅行方法是什么?",
            "options": {
                "A": "搭乘直飞航班",
                "B": "开车",
                "C": "搭便车",
                "D": "乘火车",
                "E": "乘坐私人游艇",
            },
            "correct_answer": ["A", "搭乘直飞航班"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "spatial_reasoning",
                    "reasoning": "纽约市和伦敦之间有一片大洋，使得无法直接从一个城市开车或乘火车到另一个城市。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "通过大西洋搭便车需要在没有预先安排下寻找愿意带乘客的船只，这种可能性极低且不可预测。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "temporal_reasoning",
                    "reasoning": "乘坐私人游艇是可能的，但比飞行要慢得多，要花费几天或几周，而飞行只需几个小时。",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ''',
    },
    "mcsqa_gen_2":
    {
        "input": '''\
        ```json
        {
            "question": "聚会上一种常见的饮品是什么?",
            "options": {
                "A": "水",
                "B": "苏打水",
                "C": "番茄汁",
                "D": "牛奶",
                "E": "肉汤"
            },
            "correct_answer": ["B","苏打水"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "在许多社交环境中，例如聚会或社交聚会，某些食物和饮料通常作为款待提供给客人。手指食物和饮料特别受欢迎，因为它们可以在社交时轻松食用，不需要餐具，且通常能吸引广泛的口味。",
            "commonsense_question": "聚会上一种常见的饮品是什么?",
            "options": {
                "A": "水",
                "B": "苏打水",
                "C": "番茄汁",
                "D": "牛奶",
                "E": "肉汤"
            },
            "correct_answer": ["B","苏打水"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "牛奶一般在大多数环境中都是可用的，但并不总是被视为‘派对饮料’。番茄汁和肉汤不太可能选择用于派对，在派对中，款待是为了轻松且广泛吸引。",
                    "eliminated_options": ["C", "D", "E"],
                    "possible_options": ["A","B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "苏打水由于其多样性、碳酸化和吸引所有年龄段的人的特性，是聚会的流行饮品选择，与水相比，它更可能出现在社交场合中，水通常是一种默认但不是特色饮料。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B"]
                }
            }
        }
        ''',
    },
    #! culbank_gen
    "culbank_gen_1":
    {
        "input": '''\
        ```json
        {
            "cultural_topic": "日本文化 - 礼物赠送 - 礼节和做法",
            "social_context": "在日本举行的商务会议期间，一位来自西方国家的访问执行者希望向他们的东道主表达谢意。",
            "actor": "访问执行者",
            "question": "我正在参加日本的商务会议，想给我的日本东道主送个小礼物。我应该考虑什么以确保我的举动被善意接受?",
            "actor_behavior": "以感谢的姿态赠送一个包裹在传统日本风格的礼物",
            "recipient": "日本商业东道主",
            "relation": "业务合作伙伴",
            "recipient_behavior": "双手接过礼物并表现出感激"
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "在日本商业文化中，赠送礼物是表达感谢和加强关系的常见做法。重要的是要优雅地赠送礼物，通常用显示尊重和体贴的方式进行包裹。赠礼的行为往往比礼物本身更重要，体现相互尊重。",
            "commonsense_question": "在商务会议期间，西方执行者向他们的日本同事赠送礼物时的一个重要考虑是什么?",
            "options": {
                "A": "确保礼物以传统日本风格整齐优雅地包装。",
                "B": "选择非常昂贵的礼物以显示关系的价值。",
                "C": "在会议开始之前赠送礼物以营造积极氛围。",
                "D": "避免赠送礼物，因为可能会被视为贿赂。",
                "E": "仅赠送执行者本国当地产的礼物。"
            },
            "answer": ["A", "确保礼物以传统日本风格整齐优雅地包装。"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "理解在日本，礼物的展示与礼物本身同样重要，反映了赠送者的尊重和细致思考。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "对时间的考虑表明赠送礼物不一定需要在会议之前，而最好在会后赠送以巩固关系进展。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "abductive_reasoning",
                    "reasoning": "虽然从本地采购礼物可以增加个人色彩，但日本文化中的关键关注点在于通过展示来表示尊重和细心思考。",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! expand_complexity
    "expand_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "在下雨天驾驶时，可见度可能会显著降低。",
            "commonsense_question": "为什么下雨时你应该打开车灯?",
            "options": {
                "A": "看得更清楚",
                "B": "晾干车灯",
                "C": "向其他驾驶员发出信号",
                "D": "节省电池",
                "E": "加热汽车"
            },
            "correct_answer": ["A", "看得更清楚"],
            "reasoning_process": {
                "reasoning_step_1": {
                "reasoning_skill": "deductive_reasoning",
                "reasoning": "在下雨天气中，由于可见度降低，使得看清道路和其他车辆变得困难。打开车灯可以改善可见度。",
                "eliminated_options": ["B", "D", "E"],
                "possible_options": ["A", "C"]
                },
                "reasoning_step_2": {
                "reasoning_skill": "social_reasoning",
                "reasoning": "车灯也有助于其他驾驶员看到你的车辆，减少事故风险。",
                "eliminated_options": ["C"],
                "possible_options": ["A"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "在下雨天驾驶时，可见度可能会显著降低。雨水会遮挡路面标记，使得看清其他车辆、行人和障碍变得困难。使用车灯不仅可以帮助你更好地看清道路，还使你的车辆对其他人更可见。在大雨或低光照条件下，这对安全非常重要。",
            "commonsense_question": "在一个黑暗、雨夜的高峰交通中，为什么必须打开你汽车的头灯?",
            "options": {
                "A": "提高自己的可见度，并让其他人看到你的车",
                "B": "快速晾干车灯",
                "C": "发出即将停车的信号",
                "D": "节约车辆能源",
                "E": "更快加热车厢内",
                "F": "在许多地区是法律要求"
            },
            "correct_answer": ["A", "提高自己的可见度，并让其他人看到你的车"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "在黑暗和下雨的条件下，可见度受损。头灯照亮前方道路，使你的车辆对他人可见，这对安全驾驶至关重要。",
                    "eliminated_options": ["B", "D", "E"],
                    "possible_options": ["A", "C", "F"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "‘信号’通常使用转向灯或刹车灯。车灯主要用于提高可见度，而不是指示特定动作如停车。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "F"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "moral_reasoning",
                    "reasoning": "‘法律要求’（选项F）支持安全措施，但不是打开头灯的主要原因。关键原因是安全——确保你可以看得到和被看见。",
                    "eliminated_options": ["F"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! context_implicit
    "implicit_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "您正在一个外国偏远地区进行冒险旅行。在旅行中，您小组中的成员出现了严重不适，症状包括头晕和呼吸急促，但语言障碍和有限的当地医疗保健限制使得很难立即寻求帮助。此外，有限的互联网连接使得与外部资源的沟通更加复杂。",
            "commonsense_question": "在外国的冒险旅行中，评估小组成员健康状况的最有效初始行动是什么?",
            "options": {
                "A": "使用多语言旅行健康应用",
                "B": "寻求当地导游协助",
                "C": "启动紧急协议",
                "D": "发起远程医疗通话",
                "E": "通过离线支持工具咨询医疗专业人士"
            },
            "correct_answer": ["E", "通过离线支持工具咨询医疗专业人士"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "使用多语言旅行健康应用（选项A）可以提供信息，但对于需要专业意见的严重健康问题则不足。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "寻求当地导游协助（选项B）可能有助于后勤，但不能替代专业建议。由于有限的互联网连接，远程医疗通话（选项D）不可靠。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "没有通过专业评估确认严重性，启动紧急协议（选项C）可能导致不必要的升级。",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_question": "在一个偏远地区的外国冒险旅行中，当小组成员感觉严重不适并伴有头晕和呼吸急促等症状时该怎么办，而此时语言障碍和网络连接是个问题?",
            "options": {
                "A": "使用多语言旅行健康应用",
                "B": "寻求当地导游协助",
                "C": "启动紧急协议",
                "D": "发起远程医疗通话",
                "E": "通过离线支持工具咨询医疗专业人士"
            },
            "correct_answer": ["E", "通过离线支持工具咨询医疗专业人士"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "使用多语言旅行健康应用（选项A）可以提供信息，但对于需要专业意见的严重健康问题则不足。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "寻求当地导游协助（选项B）可能有助于后勤，但不能替代专业建议。由于有限的互联网连接，远程医疗通话（选项D）不可靠。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "没有通过专业评估确认严重性，启动紧急协议（选项C）可能导致不必要的升级。",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```'''
    },
}







#SECTION:
#SECTION: JA
#SECTION:
JA_ICL_EXAMPLES = {
    "infer_1": 
    {
        "input": '''\
        ```json
        {
            "question": "食品を冷たく保ち、腐らせないようにするために使用される家電製品はどれですか？",
            "options": {
                "A": "オーブン",
                "B": "冷蔵庫",
                "C": "食器洗い機",
                "D": "電子レンジ",
                "E": "トースター"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
        "question": "食品を冷たく保ち、腐らせないようにするために使用される家電製品はどれですか？",
        "options": {
            "A": "オーブン",
            "B": "冷蔵庫",
            "C": "食器洗い機",
            "D": "電子レンジ",
            "E": "トースター"
        },
        "correct_answer": ["B", "冷蔵庫"],
        "reasoning_process": {
            "reasoning_step_1": {
            "reasoning_skill": "causal_reasoning",
            "reasoning": "オーブンは食べ物を加熱しますが、冷やすことにはなりません。",
            "eliminated_options": ["A"],
            "possible_options": ["B", "C", "D", "E"]
            },
            "reasoning_step_2": {
            "reasoning_skill": "deductive_reasoning",
            "reasoning": "食器洗い機は食器を洗浄します；食物の冷蔵や保存には使われません。",
            "eliminated_options": ["C"],
            "possible_options": ["B", "D", "E"]
            },
            "reasoning_step_3": {
            "reasoning_skill": "intuitive_reasoning",
            "reasoning": "電子レンジとトースターは食べ物を加熱または焼くためのもので、冷却には使われません。",
            "eliminated_options": ["D", "E"],
            "possible_options": ["B"]
            }
        }
        ```'''
    },
    "infer_logic_1":
    {
        "input": '''\
        ```json
        {
            "question": "どの家庭用電化製品が食べ物を冷やして腐らないようにするために使用されますか？",
            "options": {
                "A": "オーブン",
                "B": "冷蔵庫",
                "C": "食器洗い機",
                "D": "電子レンジ",
                "E": "トースター"
            },
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "どの家庭用電化製品が食べ物を冷やして腐らないようにするために使用されますか？",
            "options": {
                "A": "オーブン",
                "B": "冷蔵庫",
                "C": "食器洗い機",
                "D": "電子レンジ",
                "E": "トースター"
            },
            "correct_answer": ["B", "冷蔵庫"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "inductive_reasoning",
                    "reasoning": "複数の観察から、オーブン、電子レンジ、トースターはすべて食べ物を加熱します。これらはどれも物を冷やしません。",
                    "eliminated_options": ["A", "D", "E"],
                    "possible_options": ["B", "C"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "電化製品の主な機能が冷やして食品を保存することであれば、それは冷蔵庫でなければなりません。",
                    "eliminated_options": ["C"],
                    "possible_options": ["B"]
                }
            }
        }
        ```''',
    },
    "infer_general_1":
    {
        "input": '''\
        ```json
        {
            "question": "どの行動が健康的な仕事と生活のバランスを促進する可能性が最も高いですか？",
            "options": {
                "A": "定期的に遅くまで働く",
                "B": "明確な仕事の境界を設定する",
                "C": "個人の時間に常に仕事のメールをチェックする",
                "D": "より多くの仕事を終わらせるために昼食を抜く",
                "E": "短い休憩を一日中取る"
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "どの行動が健康的な仕事と生活のバランスを促進する可能性が最も高いですか？",
            "options": {
                "A": "定期的に遅くまで働く",
                "B": "明確な仕事の境界を設定する",
                "C": "個人の時間に常に仕事のメールをチェックする",
                "D": "より多くの仕事を終わらせるために昼食を抜く",
                "E": "短い休憩を一日中取る"
            },
            "correct_answer": ["B", "明確な仕事の境界を設定する"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "logical_reasoning",
                    "reasoning": "健康的な仕事と生活のバランスを促進するためには、仕事と個人生活の間の時間を効果的に区別し管理することが必要です。定期的に遅くまで働くことや個人の時間に仕事のメールをチェックすることは、これらの境界を曖昧にします。",
                    "eliminated_options": ["A", "C", "D"],
                    "possible_options": ["B", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_and_ethical_reasoning",
                    "reasoning": "明確な仕事の境界を設定することは、個人のニーズと職業上の責任の両方を尊重します。短い休憩を取ることは有益ですが、それは仕事と生活の間に強力な境界を直接的に確立するものではありません。",
                    "eliminated_options": ["E"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    #! mcsqa_gen
    "mcsqa_gen_1":
    {
        "input": '''\
        ```json
        {
            "question": "ニューヨークからロンドンへの最も現実的で時間効率の良い移動方法は何ですか？",
            "options": {
                "A": "直行便を利用する",
                "B": "車で行く",
                "C": "ヒッチハイクする",
                "D": "電車を使う",
                "E": "プライベートヨットで航海する",
            },
            "correct_answer": ["A", "直行便を利用する"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "国際旅行の計画では、距離、地理、時間効率、および利用可能な移動手段を考慮する必要があります。ニューヨークからロンドンへの旅には、大西洋を越える必要があります。広大な海洋距離と地上移動の非現実性を考慮すると、最も実用的な方法は空路または海路の移動となります。",
            "commonsense_question": "ニューヨークからロンドンへの最も現実的で時間効率の良い移動方法は何ですか？",
            "options": {
                "A": "直行便を利用する",
                "B": "車で行く",
                "C": "ヒッチハイクする",
                "D": "電車を使う",
                "E": "プライベートヨットで航海する",
            },
            "correct_answer": ["A", "直行便を利用する"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "spatial_reasoning",
                    "reasoning": "ニューヨークとロンドンの間には海があるため、車や電車で直接行くことはできません。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "大西洋をヒッチハイクするには、乗客を乗せる準備のある船を見つける必要があるが、それは非常に不可能で予測できません。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "temporal_reasoning",
                    "reasoning": "プライベートヨットでの航海は可能ですが、飛行機での移動よりもはるかに遅く、数日または数週間かかりますが、飛行機なら数時間で済みます。",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ''',
    },
    "mcsqa_gen_2":
    {
        "input": '''\
        ```json
        {
            "question": "パーティーでよく出される一般的な飲み物は何ですか？",
            "options": {
                "A": "水",
                "B": "ソーダ",
                "C": "トマトジュース",
                "D": "牛乳",
                "E": "ブロス"
            },
            "correct_answer": ["B","ソーダ"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "多くの社交場では、パーティーや社交の場で特定の食べ物や飲み物がリフレッシュメントとしてゲストに提供されます。フィンガーフードや飲み物は特に人気があります、それらは社交しながら簡単に消費でき、カトラリーを必要とせず、幅広い味に対応します。",
            "commonsense_question": "パーティーでよく出される一般的な飲み物は何ですか？",
            "options": {
                "A": "水",
                "B": "ソーダ",
                "C": "トマトジュース",
                "D": "牛乳",
                "E": "ブロス"
            },
            "correct_answer": ["B","ソーダ"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "牛乳は一般的にほとんどの環境で利用可能ですが、常に「パーティードリンク」とは見なされません。トマトジュースやブロスはパーティーで選ばれることは少ないですが、リフレッシュメントはカジュアルで広く受け入れられなければなりません。",
                    "eliminated_options": ["C", "D", "E"],
                    "possible_options": ["A","B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "ソーダは多様性、炭酸、自分の魅力によりパーティーでの飲み物の人気選択肢であり、年齢層にかかわらず、基本飲料ではなく、際立った飲み物ではない水と比較して、より社交的な場に見つかりやすいです。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B"]
                }
            }
        }
        ''',
    },
    #! culbank_gen
    "culbank_gen_1":
    {
        "input": '''\
        ```json
        {
            "cultural_topic": "日本文化 - 贈り物 - エチケットと慣習",
            "social_context": "日本でのビジネスミーティング中、西洋からの訪問しているエグゼクティブがホストへの感謝の気持ちを表したいと望んでいます。",
            "actor": "訪問するエグゼクティブ",
            "question": "私は日本でのビジネスミーティングに参加しており、日本のホストに小さな贈り物をしたいです。気持ちをよく受け入れられることを確認するために何を考慮すべきですか？",
            "actor_behavior": "感謝の意を表すために伝統的な日本のスタイルで包んだ贈り物を提供する",
            "recipient": "日本のビジネスホスト",
            "relation": "ビジネスパートナー",
            "recipient_behavior": "両手で贈り物を受け取り、感謝の意を示す"
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "日本のビジネス文化では、贈り物を贈ることは感謝の意を表し、関係を強化する一般的な慣習です。贈り物はエレガントに提示されることが重要であり、しばしば敬意と慎重さを示す特定の方法で包まれます。贈り物を贈る行為はしばしば贈り物そのものよりも重要であり、相互尊重を示しています。",
            "commonsense_question": "西洋のエグゼクティブがビジネスミーティング中に日本のカウンターパートに贈り物をする際の重要な考慮事項は何ですか？",
            "options": {
                "A": "伝統的な日本のスタイルで整然とエレガントに贈り物を包むことを保証する。",
                "B": "関係の価値を示すために非常に高価な贈り物を選ぶ。",
                "C": "積極的なムードを設定するために、会議が始まる前に贈り物を渡す。",
                "D": "贈り物が賄賂として見なされる可能性があるため、贈り物を回避する。",
                "E": "エグゼクティブの出身国からのみ地元製品を贈り物として提供する。",
            },
            "answer": ["A", "伝統的な日本のスタイルで整然とエレガントに贈り物を包むことを保証する。"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "日本では、贈り物の手渡しと贈り物そのものが同じくらい重要であり、贈り主の敬意と慎重な考慮を反映するためです。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "タイミングの考慮は贈り物を渡すことが必ずしも会議の前に行われるわけではなく、その進展をしっかりとするために会議の後に贈るほうが望ましいと示唆しています。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "abductive_reasoning",
                    "reasoning": "地元で調達した贈り物が個人的なタッチを加えることができる場合でも、日本文化の主な重点は敬意と慎重さを示すことにあります。",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! expand_complexity
    "expand_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "雨天時の運転では、視界が大きく制限されることがあります。",
            "commonsense_question": "雨が降っているときはなぜヘッドライトを点けるべきですか？",
            "options": {
                "A": "よりよく見えるように",
                "B": "ヘッドライトを乾かすために",
                "C": "他の運転者に信号を送るために",
                "D": "バッテリーを節約するために",
                "E": "車を暖めるために"
            },
            "correct_answer": ["A", "よりよく見えるように"],
            "reasoning_process": {
                "reasoning_step_1": {
                "reasoning_skill": "deductive_reasoning",
                "reasoning": "雨天時、視界が低下し、道路や他の車両が見えにくくなります。ヘッドライトを点けることで、視界が向上します。",
                "eliminated_options": ["B", "D", "E"],
                "possible_options": ["A", "C"]
                },
                "reasoning_step_2": {
                "reasoning_skill": "social_reasoning",
                "reasoning": "ヘッドライトは、他の運転者があなたの車両を見るのにも役立ち、事故のリスクを減らします。",
                "eliminated_options": ["C"],
                "possible_options": ["A"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "雨天時の運転では、視界が大きく制限されることがあります。雨は道路標識をぼやかし、他の車両、歩行者、障害物を見るのを困難にします。ヘッドライトの使用は、単にあなたがより良く見えるようにするだけでなく、他の人にあなたの車をもっと見てもらうことも助けます。これは特に激しい雨や暗い条件での安全に重要です。",
            "commonsense_question": "暗く、雨が降りしきる夕方、交通渋滞の中で、なぜ車のヘッドライトをつけることが重要ですか？",
            "options": {
                "A": "自分の視認性を高め、他の人にあなたの車を見えるようにするために",
                "B": "ヘッドライトを早く乾かすために",
                "C": "まもなく停止することを知らせるために",
                "D": "車のエネルギーを節約するために",
                "E": "車内を早く温めるために",
                "F": "多くの地域で法的に要求されるため"
            },
            "correct_answer": ["A", "自分の視認性を高め、他の人にあなたの車を見えるようにするために"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "暗くて雨の多い条件では、可視性が損なわれます。ヘッドライトは前方の道路を照らし、あなたの車両を他の車両に見えるようにし、安全な運転に不可欠です。",
                    "eliminated_options": ["B", "D", "E"],
                    "possible_options": ["A", "C", "F"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "'信号'は通常、ターンシグナルやブレーキライトの使用を含んでいます。ヘッドライトは、特定の行動（例えば停止）を信号するのではなく、主に視認性のために使用されます。",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "F"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "moral_reasoning",
                    "reasoning": "'法的要求'（選択肢F）は安全対策を支持しますが、ヘッドライトを点ける主な理由ではありません。主な理由は安全です - あなたが見えて、見られることを確実にすることです。",
                    "eliminated_options": ["F"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! context_implicit
    "implicit_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "あなたは外国の遠隔地で冒険旅行をしています。旅行中に、あなたのグループのメンバーがめまいや息切れなどの症状でひどい不快感を感じていますが、言語の壁と地元医療へのアクセス制限がすぐに助けを求めるのを困難にします。さらに、インターネット接続が限られているため、外部リソースとのコミュニケーションが複雑になります。",
            "commonsense_question": "外国での冒険旅行中にグループメンバーの健康状態を評価する最も効果的な初期行動は何ですか？",
            "options": {
                "A": "多言語トラベルヘルスアプリを使用する",
                "B": "現地ガイドの助けを求める",
                "C": "緊急プロトコルを開始する",
                "D": "遠隔医療通話を準備する",
                "E": "オフラインサポートツールを使用して医療専門家に相談する"
            },
            "correct_answer": ["E", "オフラインサポートツールを使用して医療専門家に相談する"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "多言語トラベルヘルスアプリ（選択肢A）の使用は情報を提供しますが、専門家の意見を必要とする深刻な健康問題には不十分です。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "現地ガイドの助けを求める（選択肢B）は物流を助けることができますが、専門家のアドバイスに代わるものではありません。インターネット接続の制限のため、遠隔医療通話（選択肢D）は信頼性が低いです。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "専門家の評価を受けずに緊急プロトコルを開始する（選択肢C）は、不必要なエスカレーションを引き起こす可能性があります。",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_question": "言語障害やインターネット接続が問題である外国の遠隔地での冒険旅行中に、グループメンバーがめまいや息切れなどの症状で強い不快感を感じたとき、どのような行動をすべきですか？",
            "options": {
                "A": "多言語トラベルヘルスアプリを使用する",
                "B": "現地ガイドの助けを求める",
                "C": "緊急プロトコルを開始する",
                "D": "遠隔医療通話を準備する",
                "E": "オフラインサポートツールを使用して医療専門家に相談する"
            },
            "correct_answer": ["E", "オフラインサポートツールを使用して医療専門家に相談する"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "多言語トラベルヘルスアプリ（選択肢A）の使用は情報を提供しますが、専門家の意見を必要とする深刻な健康問題には不十分です。",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "現地ガイドの助けを求める（選択肢B）は物流を助けることができますが、専門家のアドバイスに代わるものではありません。インターネット接続の制限のため、遠隔医療通話（選択肢D）は信頼性が低いです。",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "専門家の評価を受けずに緊急プロトコルを開始する（選択肢C）は、不必要なエスカレーションを引き起こす可能性があります。",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```'''
    },
}









#SECTION:
#SECTION: FR
#SECTION:
FR_ICL_EXAMPLES = {
    "infer_1": 
    {
        "input": '''\
        ```json
        {
            "question": "Quel appareil ménager est utilisé pour garder les aliments au frais et les empêcher de se gâter?",
            "options": {
                "A": "Four",
                "B": "Réfrigérateur",
                "C": "Lave-vaisselle",
                "D": "Micro-ondes",
                "E": "Grille-pain"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
        "question": "Quel appareil ménager est utilisé pour garder les aliments au frais et les empêcher de se gâter?",
        "options": {
            "A": "Four",
            "B": "Réfrigérateur",
            "C": "Lave-vaisselle",
            "D": "Micro-ondes",
            "E": "Grille-pain"
        },
        "correct_answer": ["B", "Réfrigérateur"],
        "reasoning_process": {
            "reasoning_step_1": {
            "reasoning_skill": "causal_reasoning",
            "reasoning": "Un four chauffe les aliments, ce qui ne correspond pas à leur refroidissement.",
            "eliminated_options": ["A"],
            "possible_options": ["B", "C", "D", "E"]
            },
            "reasoning_step_2": {
            "reasoning_skill": "deductive_reasoning",
            "reasoning": "Un lave-vaisselle nettoie la vaisselle, il n'est pas utilisé pour stocker ou refroidir les aliments.",
            "eliminated_options": ["C"],
            "possible_options": ["B", "D", "E"]
            },
            "reasoning_step_3": {
            "reasoning_skill": "intuitive_reasoning",
            "reasoning": "Les micro-ondes et les grille-pains sont des appareils qui chauffent ou grillent les aliments, pas qui les refroidissent.",
            "eliminated_options": ["D", "E"],
            "possible_options": ["B"]
            }
        }
        ```'''
    },
    "infer_logic_1":
    {
        "input": '''\
        ```json
        {
            "question": "Quel appareil ménager est utilisé pour garder les aliments au frais et éviter qu'ils ne se gâtent ?",
            "options": {
                "A": "Four",
                "B": "Réfrigérateur",
                "C": "Lave-vaisselle",
                "D": "Micro-ondes",
                "E": "Grille-pain"
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "Quel appareil ménager est utilisé pour garder les aliments au frais et éviter qu'ils ne se gâtent ?",
            "options": {
                "A": "Four",
                "B": "Réfrigérateur",
                "C": "Lave-vaisselle",
                "D": "Micro-ondes",
                "E": "Grille-pain"
            },
            "correct_answer": ["B", "Réfrigérateur"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "inductive_reasoning",
                    "reasoning": "À partir de plusieurs observations, un four, un micro-ondes, et un grille-pain chauffent tous les aliments. Aucun de ceux-ci ne garde les objets froids.",
                    "eliminated_options": ["A", "D", "E"],
                    "possible_options": ["B", "C"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Si la fonction principale d'un appareil est de conserver les aliments en les refroidissant, il doit s'agir d'un réfrigérateur.",
                    "eliminated_options": ["C"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    "infer_general_1":
    {
        "input": '''\
        ```json
        {
            "question": "Quelle action est la plus susceptible de promouvoir un équilibre sain entre le travail et la vie personnelle ?",
            "options": {
                "A": "Travailler régulièrement tard le soir",
                "B": "Établir des limites claires pour le travail",
                "C": "Vérifier constamment les emails professionnels pendant le temps personnel",
                "D": "Sauter le déjeuner pour avancer davantage dans le travail",
                "E": "Faire de courtes pauses tout au long de la journée"
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "Quelle action est la plus susceptible de promouvoir un équilibre sain entre le travail et la vie personnelle ?",
            "options": {
                "A": "Travailler régulièrement tard le soir",
                "B": "Établir des limites claires pour le travail",
                "C": "Vérifier constamment les emails professionnels pendant le temps personnel",
                "D": "Sauter le déjeuner pour avancer davantage dans le travail",
                "E": "Faire de courtes pauses tout au long de la journée"
            },
            "correct_answer": ["B", "Établir des limites claires pour le travail"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "logical_reasoning",
                    "reasoning": "Promouvoir un équilibre sain entre le travail et la vie personnelle nécessite généralement de différencier et de gérer efficacement le temps entre travail et vie privée. Travailler régulièrement tard et vérifier les emails professionnels pendant le temps personnel brouillent ces frontières.",
                    "eliminated_options": ["A", "C", "D"],
                    "possible_options": ["B", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_and_ethical_reasoning",
                    "reasoning": "Établir des limites claires pour le travail respecte à la fois les besoins personnels et les responsabilités professionnelles. Même si faire de courtes pauses est bénéfique, cela n'établit pas directement une frontière solide entre le travail et la vie personnelle.",
                    "eliminated_options": ["E"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },  
    #! mcsqa_gen
    "mcsqa_gen_1":
    {
        "input": '''\
        ```json
        {
            "question": "Quelle est la méthode la plus pratique et efficace en termes de temps pour voyager de New York à Londres?",
            "options": {
                "A": "Prendre un vol direct",
                "B": "Conduire une voiture",
                "C": "Faire de l'auto-stop",
                "D": "Prendre le train",
                "E": "Naviguer sur un yacht privé",
            },
            "correct_answer": ["A", "Prendre un vol direct"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Lors de la planification d'un voyage international, il est nécessaire de prendre en compte des facteurs tels que la distance, la géographie, l'efficacité du temps et les modes de transport disponibles. Voyager de New York à Londres implique de traverser l'océan Atlantique. Les méthodes les plus pratiques consisteraient à utiliser des voyages aériens ou maritimes, compte tenu de la grande distance océanique et de l'impraticabilité des voyages terrestres dans ce contexte.",
            "commonsense_question": "Quelle est la méthode la plus pratique et efficace en termes de temps pour voyager de New York à Londres?",
            "options": {
                "A": "Prendre un vol direct",
                "B": "Conduire une voiture",
                "C": "Faire de l'auto-stop",
                "D": "Prendre le train",
                "E": "Naviguer sur un yacht privé",
            },
            "correct_answer": ["A", "Prendre un vol direct"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "spatial_reasoning",
                    "reasoning": "Il y a un océan entre New York et Londres, ce qui rend impossible de conduire une voiture ou de prendre un train directement d'une ville à l'autre.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Faire de l'auto-stop à travers l'Atlantique nécessiterait de trouver des navires prêts à prendre un passager sans arrangement préalable, ce qui est hautement improbable et imprévisible.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "temporal_reasoning",
                    "reasoning": "Naviguer sur un yacht privé est possible mais considérablement plus lent qu'un vol, prenant plusieurs jours ou semaines comparé à quelques heures.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ''',
    },
    "mcsqa_gen_2":
    {
        "input": '''\
        ```json
        {
            "question": "Quelle est une boisson courante souvent servie lors de fêtes?",
            "options": {
                "A": "eau",
                "B": "soda",
                "C": "jus de tomate",
                "D": "lait",
                "E": "bouillon"
            },
            "correct_answer": ["B","soda"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Dans de nombreux contextes sociaux, comme les fêtes ou les rassemblements sociaux, certains aliments et boissons sont couramment servis aux invités comme rafraîchissements. Les mets à grignoter et les boissons sont particulièrement populaires car ils sont faciles à consommer tout en socialisant, ne nécessitent pas d'ustensiles, et plaisent souvent à un large éventail de goûts.",
            "commonsense_question": "Quelle est une boisson courante souvent servie lors de fêtes?",
            "options": {
                "A": "eau",
                "B": "soda",
                "C": "jus de tomate",
                "D": "lait",
                "E": "bouillon"
            },
            "correct_answer": ["B","soda"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Le lait est généralement disponible dans la plupart des contextes mais n'est pas toujours considéré comme une 'boisson de fête'. Le jus de tomate et le bouillon sont moins souvent choisis pour les fêtes, où les rafraîchissements sont destinés à être décontractés et largement attrayants.",
                    "eliminated_options": ["C", "D", "E"],
                    "possible_options": ["A","B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Le soda est un choix de boisson populaire pour les fêtes en raison de sa variété, de sa carbonatation et de son attrait pour tous les âges, ce qui le rend plus susceptible d'être trouvé lors d'événements sociaux comparé à l'eau, qui est souvent une boisson de base mais pas mise en avant.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B"]
                }
            }
        }
        ''',
    },
    #! culbank_gen
    "culbank_gen_1":
    {
        "input": '''\
        ```json
        {
            "cultural_topic": "Culture japonaise - Offrir des cadeaux - Étiquette et pratiques",
            "social_context": "Lors d'une réunion d'affaires au Japon, un cadre occidental en visite souhaite exprimer sa gratitude envers ses hôtes.",
            "actor": "Cadre en visite",
            "question": "Je participe à une réunion d'affaires au Japon et j'aimerais offrir un petit cadeau à mes hôtes japonais. Que dois-je prendre en compte pour m'assurer que mon geste est bien reçu?",
            "actor_behavior": "Offrir un cadeau emballé selon le style traditionnel japonais en signe de reconnaissance",
            "recipient": "Hôtes d'affaires japonais",
            "relation": "Partenaires commerciaux",
            "recipient_behavior": "Recevoir le cadeau à deux mains et montrer de l'appréciation"
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Dans la culture d'affaires japonaise, offrir des cadeaux est une pratique courante pour exprimer de la gratitude et renforcer les relations. Il est important de présenter les cadeaux avec élégance, souvent emballés d'une manière qui montre du respect et de la réflexion. L'acte d'offrir est souvent plus significatif que le cadeau lui-même, démontrant un respect mutuel.",
            "commonsense_question": "Quelle est une considération importante pour un cadre occidental lorsqu'il offre un cadeau à ses homologues japonais lors d'une réunion d'affaires?",
            "options": {
                "A": "Assurer que le cadeau est emballé de manière soignée et élégante dans le style traditionnel japonais.",
                "B": "Choisir un cadeau très cher pour montrer la valeur de la relation.",
                "C": "Présenter le cadeau avant le début de la réunion pour donner un ton positif.",
                "D": "Éviter d'offrir des cadeaux car cela pourrait être perçu comme un pot-de-vin.",
                "E": "Ne présenter que des cadeaux provenant de la région d'origine du cadre.",
            },
            "answer": ["A", "Assurer que le cadeau est emballé de manière soignée et élégante dans le style traditionnel japonais."],
            "reasoning": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Comprendre qu'au Japon, la présentation d'un cadeau est aussi importante que le cadeau lui-même, reflétant le respect et la réflexion du donneur.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "La prise en compte du moment suggère que présenter un cadeau ne doit pas nécessairement précéder la réunion mais est mieux donné après pour renforcer les progrès de la relation.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "abductive_reasoning",
                    "reasoning": "Bien que les cadeaux locaux puissent apporter une touche personnelle, l'accent principal de la culture japonaise est mis sur la présentation pour signifier le respect et la réflexion soignée.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! expand_complexity
    "expand_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "Lorsque vous conduisez sous la pluie, la visibilité peut être considérablement réduite.",
            "commonsense_question": "Pourquoi devriez-vous allumer vos phares quand il pleut?",
            "options": {
                "A": "Pour mieux voir",
                "B": "Pour sécher les phares",
                "C": "Pour signaler aux autres conducteurs",
                "D": "Pour économiser la batterie",
                "E": "Pour chauffer la voiture"
            },
            "correct_answer": ["A", "Pour mieux voir"],
            "reasoning_process": {
                "reasoning_step_1": {
                "reasoning_skill": "deductive_reasoning",
                "reasoning": "Par temps de pluie, la visibilité réduite rend la route et les autres véhicules plus difficiles à voir. Allumer les phares améliore la visibilité.",
                "eliminated_options": ["B", "D", "E"],
                "possible_options": ["A", "C"]
                },
                "reasoning_step_2": {
                "reasoning_skill": "social_reasoning",
                "reasoning": "Les phares aident aussi les autres conducteurs à voir votre véhicule, réduisant le risque d'accidents.",
                "eliminated_options": ["C"],
                "possible_options": ["A"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Lorsque vous conduisez sous la pluie, la visibilité peut être considérablement réduite. La pluie peut obscurcir les marquages routiers et rendre difficile la vision des autres véhicules, piétons et obstacles. Utiliser les phares non seulement vous aide à mieux voir mais rend également votre véhicule plus visible pour les autres. Ceci est crucial pour la sécurité, surtout lors de fortes pluies ou dans des conditions de faible luminosité.",
            "commonsense_question": "Par une soirée pluvieuse et sombre avec beaucoup de circulation, pourquoi est-il essentiel d'allumer les phares de votre voiture?",
            "options": {
                "A": "Pour améliorer la visibilité pour vous-même et rendre votre voiture visible pour les autres",
                "B": "Pour sécher rapidement les phares",
                "C": "Pour signaler que vous allez bientôt vous arrêter",
                "D": "Pour économiser l'énergie du véhicule",
                "E": "Pour chauffer l'intérieur de la voiture plus rapidement",
                "F": "Parce que c'est légalement requis dans de nombreuses régions"
            },
            "correct_answer": ["A", "Pour améliorer la visibilité pour vous-même et rendre votre voiture visible pour les autres"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Dans des conditions sombres et pluvieuses, la visibilité est compromise. Les phares éclairent la route à venir et rendent votre véhicule visible aux autres, ce qui est essentiel pour une conduite en toute sécurité.",
                    "eliminated_options": ["B", "D", "E"],
                    "possible_options": ["A", "C", "F"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "'Signaler' implique généralement l'utilisation de clignotants ou de feux de stop. Les phares sont principalement utilisés pour la visibilité plutôt que pour signaler des actions spécifiques comme s'arrêter.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "F"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "moral_reasoning",
                    "reasoning": "'Obligations légales' (option F) soutiennent les mesures de sécurité mais ne sont pas la principale raison d'allumer les phares. La raison principale est la sécurité - s'assurer que vous pouvez voir et être vu.",
                    "eliminated_options": ["F"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! context_implicit
    "implicit_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "Vous êtes en voyage d'aventure dans une région éloignée d'un pays étranger. Pendant le voyage, un membre de votre groupe ressent un grave inconfort avec des symptômes comme des étourdissements et un essoufflement, mais les barrières linguistiques et un accès limité aux soins de santé locale compliquent la recherche d'aide immédiate. De plus, la connexion Internet limitée complique la communication avec les ressources externes.",
            "commonsense_question": "Quelle est l'action initiale la plus efficace pour évaluer l'état de santé d'un membre du groupe lors d'un voyage d'aventure dans un pays étranger?",
            "options": {
                "A": "utiliser une application de santé de voyage multilingue",
                "B": "demander l'assistance d'un guide local",
                "C": "initier un protocole d'urgence",
                "D": "mettre en place une consultation télé-médicale",
                "E": "consulter un professionnel de la santé grâce à des outils de soutien hors ligne"
            },
            "correct_answer": ["E", "consulter un professionnel de la santé grâce à des outils de soutien hors ligne"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Utiliser une application de santé de voyage multilingue (option A) fournit des informations mais est insuffisant pour les préoccupations de santé graves nécessitant un avis professionnel.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Demander l'assistance d'un guide local (option B) peut aider avec la logistique mais ne remplace pas un avis professionnel. Mettre en place une consultation télé-médicale (option D) est affectée par la connectivité Internet limitée et donc peu fiable.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Initier un protocole d'urgence (option C) pourrait conduire à une escalade inutile sans confirmer la gravité par une évaluation professionnelle.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_question": "Lors d'un voyage d'aventure dans une région éloignée d'un pays étranger où les barrières linguistiques et la connectivité Internet sont des problèmes, quelle action devez-vous entreprendre si un membre du groupe ressent un grave inconfort avec des symptômes comme des étourdissements et un essoufflement?",
            "options": {
                "A": "utiliser une application de santé de voyage multilingue",
                "B": "demander l'assistance d'un guide local",
                "C": "initier un protocole d'urgence",
                "D": "mettre en place une consultation télé-médicale",
                "E": "consulter un professionnel de la santé grâce à des outils de soutien hors ligne"
            },
            "correct_answer": ["E", "consulter un professionnel de la santé grâce à des outils de soutien hors ligne"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Utiliser une application de santé de voyage multilingue (option A) fournit des informations mais est insuffisant pour les préoccupations de santé graves nécessitant un avis professionnel.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Demander l'assistance d'un guide local (option B) peut aider avec la logistique mais ne remplace pas un avis professionnel. Mettre en place une consultation télé-médicale (option D) est affectée par la connectivité Internet limitée et donc peu fiable.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Initier un protocole d'urgence (option C) pourrait conduire à une escalade inutile sans confirmer la gravité par une évaluation professionnelle.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```'''
    },
}







#SECTION:
#SECTION: DE
#SECTION:
DE_ICL_EXAMPLES = {
    "infer_1": 
    {
        "input": '''\
        ```json
        {
            "question": "Welches Haushaltsgerät wird verwendet, um Lebensmittel kühl zu halten und vor dem Verderben zu bewahren?",
            "options": {
                "A": "Backofen",
                "B": "Kühlschrank",
                "C": "Geschirrspüler",
                "D": "Mikrowelle",
                "E": "Toaster"
                }
        }
        ```''',
        "output": '''\
        ```json
        {
        "question": "Welches Haushaltsgerät wird verwendet, um Lebensmittel kühl zu halten und vor dem Verderben zu bewahren?",
        "options": {
            "A": "Backofen",
            "B": "Kühlschrank",
            "C": "Geschirrspüler",
            "D": "Mikrowelle",
            "E": "Toaster"
        },
        "correct_answer": ["B", "Kühlschrank"],
        "reasoning_process": {
            "reasoning_step_1": {
            "reasoning_skill": "causal_reasoning",
            "reasoning": "Ein Ofen erhitzt Lebensmittel, was nicht mit dem Kühlhalten von Lebensmitteln übereinstimmt.",
            "eliminated_options": ["A"],
            "possible_options": ["B", "C", "D", "E"]
            },
            "reasoning_step_2": {
            "reasoning_skill": "deductive_reasoning",
            "reasoning": "Ein Geschirrspüler reinigt Geschirr; er wird nicht zum Lagern oder Kühlen von Lebensmitteln verwendet.",
            "eliminated_options": ["C"],
            "possible_options": ["B", "D", "E"]
            },
            "reasoning_step_3": {
            "reasoning_skill": "intuitive_reasoning",
            "reasoning": "Mikrowellen und Toaster sind Geräte, die Lebensmittel erhitzen oder rösten, nicht kühlen.",
            "eliminated_options": ["D", "E"],
            "possible_options": ["B"]
            }
        }
        ```'''
    },
    "infer_logic_1":
    {
        "input": '''\
        ```json
        {
            "question": "Welches Haushaltsgerät wird verwendet, um Lebensmittel kühl zu halten und zu verhindern, dass sie verderben?",
            "options": {
                "A": "Ofen",
                "B": "Kühlschrank",
                "C": "Geschirrspüler",
                "D": "Mikrowelle",
                "E": "Toaster"
            },
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "Welches Haushaltsgerät wird verwendet, um Lebensmittel kühl zu halten und zu verhindern, dass sie verderben?",
            "options": {
                "A": "Ofen",
                "B": "Kühlschrank",
                "C": "Geschirrspüler",
                "D": "Mikrowelle",
                "E": "Toaster"
            },
            "correct_answer": ["B", "Kühlschrank"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "inductive_reasoning",
                    "reasoning": "Aus mehreren Beobachtungen geht hervor, dass ein Ofen, eine Mikrowelle und ein Toaster alle Lebensmittel erhitzen. Keines davon hält Dinge kühl.",
                    "eliminated_options": ["A", "D", "E"],
                    "possible_options": ["B", "C"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Wenn die Hauptfunktion eines Geräts darin besteht, Lebensmittel durch Kühlen zu konservieren, muss es sich um einen Kühlschrank handeln.",
                    "eliminated_options": ["C"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    "infer_general_1":
    {
        "input": '''\
        ```json
        {
            "question": "Welche Maßnahme fördert am ehesten eine gesunde Work-Life-Balance?",
            "options": {
                "A": "Regelmäßig lange arbeiten",
                "B": "Klare Grenzen für die Arbeit setzen",
                "C": "Ständig dienstliche E-Mails in der Freizeit checken",
                "D": "Mittagessen auslassen, um mehr Arbeit zu erledigen",
                "E": "Den ganzen Tag über kurze Pausen einlegen"
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "question": "Welche Maßnahme fördert am ehesten eine gesunde Work-Life-Balance?",
            "options": {
                "A": "Regelmäßig lange arbeiten",
                "B": "Klare Grenzen für die Arbeit setzen",
                "C": "Ständig dienstliche E-Mails in der Freizeit checken",
                "D": "Mittagessen auslassen, um mehr Arbeit zu erledigen",
                "E": "Den ganzen Tag über kurze Pausen einlegen"
            },
            "correct_answer": ["B", "Klare Grenzen für die Arbeit setzen"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "logical_reasoning",
                    "reasoning": "Um eine gesunde Work-Life-Balance zu fördern, ist es in der Regel notwendig, die Zeit zwischen Arbeit und Privatleben effektiv zu unterscheiden und zu verwalten. Regelmäßig lange zu arbeiten und dienstliche E-Mails in der Freizeit zu checken, verwischt diese Grenzen.",
                    "eliminated_options": ["A", "C", "D"],
                    "possible_options": ["B", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_and_ethical_reasoning",
                    "reasoning": "Klare Grenzen für die Arbeit zu setzen, respektiert sowohl persönliche Bedürfnisse als auch berufliche Verpflichtungen. Obwohl es vorteilhaft ist, kurze Pausen einzulegen, schafft dies nicht direkt eine starke Grenze zwischen Arbeit und Leben.",
                    "eliminated_options": ["E"],
                    "possible_options": ["B"]
                }
            }
        }
        ```'''
    },
    #! mcsqa_gen
    "mcsqa_gen_1":
    {
        "input": '''\
        ```json
        {
            "question": "Was ist die praktischste und zeiteffizienteste Methode, um von New York nach London zu reisen?",
            "options": {
                "A": "Direktflug nehmen",
                "B": "Mit dem Auto fahren",
                "C": "Trampen",
                "D": "Zug nehmen",
                "E": "Mit einer privaten Yacht segeln",
            },
            "correct_answer": ["A", "Direktflug nehmen"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Bei der Planung einer internationalen Reise müssen Faktoren wie Distanz, Geografie, Zeitersparnis und verfügbare Verkehrsmittel berücksichtigt werden. Die Reise von New York nach London erfordert die Überquerung des Atlantiks. Die praktischsten Methoden wären Luft- oder Seereisen, angesichts der großen ozeanischen Entfernung und der Unpraktikabilität von Landreisen in diesem Zusammenhang.",
            "commonsense_question": "Was ist die praktischste und zeiteffizienteste Methode, um von New York nach London zu reisen?",
            "options": {
                "A": "Direktflug nehmen",
                "B": "Mit dem Auto fahren",
                "C": "Trampen",
                "D": "Zug nehmen",
                "E": "Mit einer privaten Yacht segeln",
            },
            "correct_answer": ["A", "Direktflug nehmen"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "spatial_reasoning",
                    "reasoning": "Es gibt einen Ozean zwischen New York und London, sodass es unmöglich ist, mit dem Auto oder Zug direkt von einer Stadt zur anderen zu reisen.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Trampen über den Atlantik würde erfordern, dass man Schiffe findet, die bereit sind, einen Passagier ohne vorherige Vereinbarung mitzunehmen, was sehr unwahrscheinlich und unvorhersehbar ist.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "temporal_reasoning",
                    "reasoning": "Mit einer privaten Yacht zu segeln ist möglich, aber erheblich langsamer als zu fliegen, da es mehrere Tage oder Wochen dauert im Vergleich zu Stunden.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ''',
    },
    "mcsqa_gen_2":
    {
        "input": '''\
        ```json
        {
            "question": "Welches ist ein gängiges Getränk, das oft auf Partys serviert wird?",
            "options": {
                "A": "Wasser",
                "B": "Limonade",
                "C": "Tomatensaft",
                "D": "Milch",
                "E": "Brühe"
            },
            "correct_answer": ["B","Limonade"],
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "In vielen sozialen Umgebungen, wie Partys oder gesellschaftlichen Zusammenkünften, werden bestimmte Speisen und Getränke den Gästen als Erfrischungen serviert. Fingerfood und Getränke sind besonders beliebt, da sie leicht beim Geselligsein konsumiert werden können, keine Utensilien erfordern und oft eine breite Geschmackspalette ansprechen.",
            "commonsense_question": "Welches ist ein gängiges Getränk, das oft auf Partys serviert wird?",
            "options": {
                "A": "Wasser",
                "B": "Limonade",
                "C": "Tomatensaft",
                "D": "Milch",
                "E": "Brühe"
            },
            "correct_answer": ["B","Limonade"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Milch ist allgemein in den meisten Umgebungen erhältlich, wird aber nicht immer als ‚Partygetränk‘ angesehen. Tomatensaft und Brühe sind weniger häufig gewählt für Partys, wo Erfrischungen locker und breit ansprechend sein sollen.",
                    "eliminated_options": ["C", "D", "E"],
                    "possible_options": ["A","B"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "probabilistic_reasoning",
                    "reasoning": "Limonade ist eine beliebte Getränkeauswahl für Partys aufgrund ihrer Vielfalt, Kohlensäure und ihrer Attraktivität für alle Altersgruppen, was sie bei gesellschaftlichen Veranstaltungen wahrscheinlicher macht als Wasser, das oft als Standard-, aber nicht als vorgestelltes Getränk gilt.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B"]
                }
            }
        }
        ''',
    },
    #! culbank_gen
    "culbank_gen_1":
    {
        "input": '''\
        ```json
        {
            "cultural_topic": "Japanische Kultur - Geschenkgeben - Etikette und Praktiken",
            "social_context": "Während eines Geschäftstreffens in Japan möchte ein westlicher Führungskraft, der zu Besuch ist, seine Dankbarkeit gegenüber seinen Gastgebern ausdrücken.",
            "actor": "Besuchender Führungskraft",
            "question": "Ich besuche ein Geschäftstreffen in Japan und möchte meinen japanischen Gastgebern ein kleines Geschenk machen. Was sollte ich berücksichtigen, um sicherzustellen, dass meine Geste gut aufgenommen wird?",
            "actor_behavior": "Ein Geschenk im traditionellen japanischen Stil als Zeichen der Anerkennung überreichen",
            "recipient": "Japanische Geschäftsgastgeber",
            "relation": "Geschäftspartner",
            "recipient_behavior": "Das Geschenk mit beiden Händen entgegennehmen und Dankbarkeit zeigen"
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "In der japanischen Geschäftskultur ist das Geschenkgeben eine übliche Praxis, um Dankbarkeit auszudrücken und Beziehungen zu stärken. Es ist wichtig, Geschenke elegant zu präsentieren, oft auf eine Art und Weise verpackt, die Respekt und Nachdenklichkeit zeigt. Der Akt des Schenkens ist oft bedeutsamer als das Geschenk selbst und demonstriert gegenseitigen Respekt.",
            "commonsense_question": "Was ist eine wichtige Überlegung für einen westlichen Führungskraft, wenn er während eines Geschäftstreffens ein Geschenk seinen japanischen Kollegen überreicht?",
            "options": {
                "A": "Sicherstellen, dass das Geschenk ordentlich und elegant im traditionellen japanischen Stil verpackt ist.",
                "B": "Ein sehr teures Geschenk wählen, um den Wert der Beziehung zu zeigen.",
                "C": "Das Geschenk vor Beginn des Treffens überreichen, um eine positive Stimmung zu setzen.",
                "D": "Vermeiden, Geschenke zu machen, da es als Bestechung angesehen werden könnte.",
                "E": "Nur Geschenke präsentieren, die aus der Heimatregion des Führungskraft stammen.",
            },
            "answer": ["A", "Sicherstellen, dass das Geschenk ordentlich und elegant im traditionellen japanischen Stil verpackt ist."],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Verstehen, dass in Japan die Präsentation eines Geschenks genauso wichtig ist wie das Geschenk selbst, da sie den Respekt und die Nachdenklichkeit des Gebers widerspiegelt.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["A", "C", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Die Berücksichtigung des Timings legt nahe, dass die Übergabe eines Geschenks nicht unbedingt vor dem Treffen erfolgen muss, sondern besser danach, um den Fortschritt der Beziehung zu festigen.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "abductive_reasoning",
                    "reasoning": "Während lokal bezogene Geschenke eine persönliche Note hinzufügen können, liegt der Hauptfokus in der japanischen Kultur auf der Präsentation, um Respekt und sorgfältige Überlegung zu signalisieren.",
                    "eliminated_options": ["E"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! expand_complexity
    "expand_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "Beim Fahren bei Regenwetter kann die Sicht erheblich eingeschränkt sein.",
            "commonsense_question": "Warum sollten Sie Ihre Scheinwerfer einschalten, wenn es regnet?",
            "options": {
                "A": "Um besser zu sehen",
                "B": "Um die Scheinwerfer zu trocknen",
                "C": "Um anderen Fahrern zu signalisieren",
                "D": "Um Batterie zu sparen",
                "E": "Um das Auto aufzuwärmen"
            },
            "correct_answer": ["A", "Um besser zu sehen"],
            "reasoning_process": {
                "reasoning_step_1": {
                "reasoning_skill": "deductive_reasoning",
                "reasoning": "Bei Regenwetter macht die reduzierte Sicht das Sehen der Straße und anderer Fahrzeuge schwieriger. Das Einschalten der Scheinwerfer verbessert die Sicht.",
                "eliminated_options": ["B", "D", "E"],
                "possible_options": ["A", "C"]
                },
                "reasoning_step_2": {
                "reasoning_skill": "social_reasoning",
                "reasoning": "Scheinwerfer helfen auch anderen Fahrern, Ihr Fahrzeug zu sehen und das Unfallrisiko zu verringern.",
                "eliminated_options": ["C"],
                "possible_options": ["A"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_context": "Beim Fahren bei Regenwetter kann die Sicht erheblich eingeschränkt sein. Regen kann Fahrbahnmarkierungen verdecken und es schwierig machen, andere Fahrzeuge, Fußgänger und Hindernisse zu sehen. Die Verwendung von Scheinwerfern hilft nicht nur, besser zu sehen, sondern macht Ihr Fahrzeug auch für andere sichtbarer. Dies ist entscheidend für die Sicherheit, insbesondere bei starkem Regen oder bei schlechten Lichtverhältnissen.",
            "commonsense_question": "Warum ist es unverzichtbar, bei starkem Verkehr an einem dunklen, regnerischen Abend die Scheinwerfer des Autos einzuschalten?",
            "options": {
                "A": "Um die Sichtbarkeit für sich selbst zu verbessern und Ihr Auto für andere sichtbar zu machen",
                "B": "Um die Scheinwerfer schneller zu trocknen",
                "C": "Um anzuzeigen, dass Sie bald anhalten",
                "D": "Um Energie im Fahrzeug zu sparen",
                "E": "Um den Innenraum des Autos schneller zu heizen",
                "F": "Weil es in vielen Gebieten gesetzlich vorgeschrieben ist"
            },
            "correct_answer": ["A", "Um die Sichtbarkeit für sich selbst zu verbessern und Ihr Auto für andere sichtbar zu machen"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Bei dunklen und regnerischen Bedingungen ist die Sicht eingeschränkt. Scheinwerfer beleuchten die Straße voraus und machen Ihr Fahrzeug für andere sichtbar, was entscheidend für sicheres Fahren ist.",
                    "eliminated_options": ["B", "D", "E"],
                    "possible_options": ["A", "C", "F"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "'Signalisieren' umfasst in der Regel die Verwendung von Blinkern oder Bremslichtern. Scheinwerfer werden primär zur Sichtbarkeit genutzt, nicht um spezifische Aktionen wie Anhalten anzuzeigen.",
                    "eliminated_options": ["C"],
                    "possible_options": ["A", "F"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "moral_reasoning",
                    "reasoning": "'Gesetzliche Anforderungen' (Option F) unterstützen Sicherheitsmaßnahmen, sind aber nicht der Hauptgrund für das Einschalten von Scheinwerfern. Der Hauptgrund ist Sicherheit - Sicherzustellen, dass Sie sehen können und gesehen werden.",
                    "eliminated_options": ["F"],
                    "possible_options": ["A"]
                }
            }
        }
        ```'''
    },
    #! context_implicit
    "implicit_1":
    {
        "input": '''\
        ```json
        {
            "commonsense_context": "Sie befinden sich auf einem Abenteuertrip in einem abgelegenen Gebiet eines fremden Landes. Während der Reise verspürt ein Mitglied Ihrer Gruppe starke Beschwerden mit Symptomen wie Schwindel und Atemnot, aber Sprachbarrieren und eingeschränkter Zugang zu lokalen Gesundheitsdiensten erschweren es, unmittelbare Hilfe zu suchen. Außerdem erschwert eingeschränkte Internetverbindung die Kommunikation mit externen Ressourcen.",
            "commonsense_question": "Welche ist die effektivste Anfangsmaßnahme, um den Gesundheitszustand eines Gruppenmitglieds während eines Abenteuertrips in einem fremden Land zu beurteilen?",
            "options": {
                "A": "eine mehrsprachige Reisegesundheits-App verwenden",
                "B": "Hilfe bei einem lokalen Führer suchen",
                "C": "Notfallprotokoll einleiten",
                "D": "einen Telemedizin-Anruf einrichten",
                "E": "einen Gesundheitsdienstleister über Offline-Support-Tools konsultieren"
            },
            "correct_answer": ["E", "einen Gesundheitsdienstleister über Offline-Support-Tools konsultieren"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Die Verwendung einer mehrsprachigen Reisegesundheits-App (Option A) liefert Informationen, ist jedoch unzureichend bei ernsthaften Gesundheitsproblemen, die professionellen Input erfordern.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Die Suche nach Hilfe bei einem lokalen Führer (Option B) kann bei der Logistik helfen, ersetzt jedoch nicht professionelle Beratung. Die Einrichtung eines Telemedizin-Anrufs (Option D) wird durch eingeschränkte Internetverbindung beeinträchtigt und ist daher unzuverlässig.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Ein Notfallprotokoll einzuleiten (Option C) könnte ohne Bestätigung der Schwere durch professionelle Beurteilung zu unnötiger Eskalation führen.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```''',
        "output": '''\
        ```json
        {
            "commonsense_question": "Während eines Abenteuertrips in einem abgelegenen Gebiet eines fremden Landes, wo Sprachbarrieren und Internetverbindung ein Problem sind, welche Maßnahme sollten Sie ergreifen, wenn ein Gruppenmitglied schwere Beschwerden mit Symptomen wie Schwindel und Atemnot verspürt?",
            "options": {
                "A": "eine mehrsprachige Reisegesundheits-App verwenden",
                "B": "Hilfe bei einem lokalen Führer suchen",
                "C": "Notfallprotokoll einleiten",
                "D": "einen Telemedizin-Anruf einrichten",
                "E": "einen Gesundheitsdienstleister über Offline-Support-Tools konsultieren"
            },
            "correct_answer": ["E", "einen Gesundheitsdienstleister über Offline-Support-Tools konsultieren"],
            "reasoning_process": {
                "reasoning_step_1": {
                    "reasoning_skill": "deductive_reasoning",
                    "reasoning": "Die Verwendung einer mehrsprachigen Reisegesundheits-App (Option A) liefert Informationen, ist jedoch unzureichend bei ernsthaften Gesundheitsproblemen, die professionellen Input erfordern.",
                    "eliminated_options": ["A"],
                    "possible_options": ["B", "C", "D", "E"]
                },
                "reasoning_step_2": {
                    "reasoning_skill": "analogical_reasoning",
                    "reasoning": "Die Suche nach Hilfe bei einem lokalen Führer (Option B) kann bei der Logistik helfen, ersetzt jedoch nicht professionelle Beratung. Die Einrichtung eines Telemedizin-Anrufs (Option D) wird durch eingeschränkte Internetverbindung beeinträchtigt und ist daher unzuverlässig.",
                    "eliminated_options": ["B", "D"],
                    "possible_options": ["C", "E"]
                },
                "reasoning_step_3": {
                    "reasoning_skill": "social_reasoning",
                    "reasoning": "Ein Notfallprotokoll einzuleiten (Option C) könnte ohne Bestätigung der Schwere durch professionelle Beurteilung zu unnötiger Eskalation führen.",
                    "eliminated_options": ["C"],
                    "possible_options": ["E"]
                }
            }
        }
        ```'''
    },
}
