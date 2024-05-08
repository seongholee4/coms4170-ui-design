# represent data in JSON
from image_url import lessons, quiz_questions
lessons = {
    "1": {
        "lesson_id": "1",
        "title": "Sichuan Hotpot",
        "image": lessons["1"]["image"],
        "dipping_sauce_image": lessons["1"]["dipping_sauce_image"],
        "text": """Sichuan hotpots often feature a wide variety of different meats and ingredients. """,
        "about": {
            "flavor": "The heavily flavored broth and numbing hot spiciness (málà 麻辣) is what Sichuan hotpot is most known for",
            "meat": "Various kinds of meats such as beef, and fresh máodù (毛肚, cow stomach)",
            "seasoning": "The hotpot soup base uses premium butter as its special ingredient, giving the broth a very rich taste that perfectly matches the red hot chili and Sichuan pepper",
            "dipping sauce": "Sesame oil mixed with crushed fresh garlic, chopped scallions, and cilantro"
        },
        "next_lesson": "2"
    },
    "2": {
        "lesson_id": "2",
        "title": "Beijing Hotpot",
        "image": lessons["2"]["image"],
        "dipping_sauce_image": lessons["2"]["dipping_sauce_image"],
        "text": """It is characterized by its simplicity and the use of copper Mongolian pots.""",
        "about": {
            "flavor": "Savory and aromatic. This style of hotpot is very pure and focuses on the quality of the ingredients – tender and tasty meat and fresh and leafy vegetables, rather than on the broth",
            "meat": "Thinly-sliced mutton is one of the most important ingredients",
            "seasoning": "Ingredients are often cooked in clear water or lightly flavored broth, with some scallions, goji berries, and ginger",
            "dipping sauce": "Sesame-based dipping sauce Zhīmajiàng (芝麻酱), which tastes somewhat like Tahini sauce (but stronger and sweeter)",
        },
        "next_lesson": "3"
    },
    "3": {
        "lesson_id": "3",
        "title": "Sundubu-jjigae (Soft Tofu Stew)",
        "image": lessons["3"]["image"],
        "dipping_sauce_image": lessons["3"]["dipping_sauce_image"],
        "text": """Sundubu-jiggae is cooked with soft tofu with either meat or vegan options.""",
         "about": {
            "flavor": "Savory, and choice of spicy or non-spicy broth",
            "meat": "Beef, seafood, or pork",
            "seasoning": "Kimchi, ham and cheese, dumplings, soysauce, pepper-powder, and sesame oil",
            "dipping sauce": "Served with a bowl of rice and an egg on top",
        },
        "next_lesson": "4"
    },
    "4": {
        "lesson_id": "4",
        "title": "Coconut Chicken Hotpot",
        "image": lessons["4"]["image"],
        "dipping_sauce_image": lessons["4"]["dipping_sauce_image"],
        "text": """The broth is not made with butter or fatty oils, making it one of the healthier hotpot options.""",
         "about": {
            "flavor": "Rich and creamy coconut flavor.",
            "meat": "Chicken, often served with seafood like shrimp and fish balls",
            "seasoning": "Coconut milk-based broth flavored with lemongrass, galangal, and kaffir lime leaves",
            "dipping sauce": "Soy sauce and some freshly squeezed limejuice",
        },
        "next_lesson": "5"
    },
    "5": {
        "lesson_id": "5",
        "title": "Sukiyaki Hotpot",
        "image": lessons["5"]["image"],
        "dipping_sauce_image": lessons["5"]["dipping_sauce_image"],
        "text": """It is a Japanese dish served in a nabemono (Japanese hot pot).""",
         "about": {
            "flavor": "Sweet and savory",
            "meat": "Thinly sliced beef",
            "seasoning": "Sweet soy sauce-based broth with mirin, sugar, and sake",
            "dipping sauce": "Raw egg dipping sauce",
        },
        "next_lesson": "6"
    },
    "6": {
        "lesson_id": "6",
        "title": "Fondue Hotpot",
        "image": lessons["6"]["image"],
        "dipping_sauce_image": lessons["6"]["dipping_sauce_image"],
        "text": """In Swiss cuisine, Fondue Chinoise is a local variation of the traditional Chinese hot pot.""",
         "about": {
            "flavor": "Rich and cheesy",
            "meat": "Beef, chicken, or pork",
            "seasoning": "Cheese fondue made with a combination of melted cheese such as Swiss, Gruyère",
            "dipping sauce": "Melted cheese dipping sauce",
        },
        "next_lesson": "end"
    }
}
    
quiz_questions = {
    "1": {
        "quiz_id": "1",
        "question": "Which one is Sichuan Hotpot?",
        "answers": {
            "A": quiz_questions["1"]["answers"]["A"],
            "B": quiz_questions["1"]["answers"]["B"],
            "C": quiz_questions["1"]["answers"]["C"],
            "D": quiz_questions["1"]["answers"]["D"]
        },
        "correct_answer": "A",
        "feedback": "Sichuan hotpots often feature a wide variety of different meats and ingredients",
        "prev_question": "start",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "question": "Which one is Sukiyaki Hotpot?",
        "answers": {
            "A": quiz_questions["2"]["answers"]["A"],
            "B": quiz_questions["2"]["answers"]["B"],
            "C": quiz_questions["2"]["answers"]["C"],
            "D": quiz_questions["2"]["answers"]["D"]
        },
        "correct_answer": "A",
        "hint": "",
        "feedback": "Sukiyaki is a Japanese dish that is prepared and served in the nabemono.",
        "prev_question": "1",
        "next_question": "3"
    },
    "3": {
        "quiz_id": "3",
        "question": "Which hotpot is Coconut Chicken Hotpot?",
        "answers": {
            "A": quiz_questions["3"]["answers"]["A"],
            "B": quiz_questions["3"]["answers"]["B"],
            "C": quiz_questions["3"]["answers"]["C"],
            "D": quiz_questions["3"]["answers"]["D"]
        },
        "correct_answer": "C",
        "feedback": "Coconut Chicken Hotpot is one of the healthier hotpot options.",
        "prev_question": "2",
        "next_question": "4"
    },
    "4": {
        "quiz_id": "4",
        "question": "Which dipping sauce is for Sichuan Hotpot?",
        "answers": {
            "A": quiz_questions["4"]["answers"]["A"],
            "B": quiz_questions["4"]["answers"]["B"],
            "C": quiz_questions["4"]["answers"]["C"],
            "D": quiz_questions["4"]["answers"]["D"]
        },
        "correct_answer": "D",
        "feedback": "Sichuan hotpot is often served with a dipping sauce made of sesame oil mixed with crushed fresh garlic, chopped scallions, and cilantro.",
        "prev_question": "3",
        "next_question": "5"
    },
    "5": {
        "quiz_id": "5",
        "question": "Identify the dipping sauce for Beijing Hotpot.",
        "answers": {
            "A": quiz_questions["5"]["answers"]["A"],
            "B": quiz_questions["5"]["answers"]["B"],
            "C": quiz_questions["5"]["answers"]["C"],
            "D": quiz_questions["5"]["answers"]["D"]
        },
        "correct_answer": "D",
        "feedback": "Sesame-based dipping sauce is used for Beijing hotpot.",
        "prev_question": "4",
        "next_question": "6"
    },
    "6": {
        "quiz_id": "6",
        "question": "Which hotpot is a sweet soy sauce-based broth?",
        "answers": {
            "A": quiz_questions["6"]["answers"]["A"],
            "B": quiz_questions["6"]["answers"]["B"],
            "C": quiz_questions["6"]["answers"]["C"],
            "D": quiz_questions["6"]["answers"]["D"]
        },
        "correct_answer": "D",
        "feedback": "Sukiyaki hotpot is a sweet soy sauce-based broth with mirin, sugar, and sake.",
        "prev_question": "5",
        "next_question": "7"
    },
    "7": {
        "quiz_id": "7",
        "question": "Which hotpot uses a copper Mongolian pots?",
        "answers": {
            "A": quiz_questions["7"]["answers"]["A"],
            "B": quiz_questions["7"]["answers"]["B"],
            "C": quiz_questions["7"]["answers"]["C"],
            "D": quiz_questions["7"]["answers"]["D"]
        },
        "correct_answer": "D",
        "feedback": "Beijing hotpot is characterized by its simplicity and the use of copper Mongolian pots.",
        "prev_question": "6",
        "next_question": "8"
    },
    "8": {
        "quiz_id": "8",
        "question": "What is the name of the Swiss Hotpot?",
        "answers": {
            "A": "Fondue Hotpot",
            "B": "Sukiyaki Hotpot",
            "C": "Coconut Chicken Hotpot",
            "D": "Beijing Hotpot"
        },
        "correct_answer": "A",
        "feedback": "Fondue Chinoise is a local variation of the traditional Chinese hot pot.",
        "prev_question": "7",
        "next_question": "9"
    },
    "9": {
        "quiz_id": "9",
        "question": "Which hotpot is cooked with soft tofu?",
        "answers": {
            "A": "Sundubu-jjiggae",
            "B": "Sichuan Hotpot",
            "C": "Sukiyaki Hotpot",
            "D": "Fondue Hotpot"
        },
        "correct_answer": "A",
        "feedback": "Sundubu-jjiggae is a Korean soup cooked with soft tofu and can be prepared in both meat and vegan options.",
        "prev_question": "8",
        "next_question": "10"
    },
    "10": {
        "quiz_id": "10",
        "question": "Which hotpot is a Japanese dish?",
        "answers": {
            "A": "Sukiyaki Hotpot",
            "B": "Sichuan Hotpot",
            "C": "Beijing Hotpot",
            "D": "Sundubu-Jjigae"
        },
        "correct_answer": "A",
        "feedback": "Sukiyaki is a Japanese dish that is prepared and served in the nabemono.",
        "prev_question": "9",
        "next_question": "end"
    },
}

