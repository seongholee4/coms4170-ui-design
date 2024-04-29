# represent data in JSON
lessons = {
    "1": {
        "lesson_id": "1",
        "title": "Sichuan Hotpot",
        "image": "https://hotpotambassador.com/wp-content/uploads/2018/11/chongqing-min-1.jpg",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """Chongqing hotpots often feature a wide variety of different meats and ingredients """,
        "about": {
            "flavor": "Spicy and Numbing",
            "meat": "Thinly shaved beef or lamb",
            "seasoning": "Mala seasoning with chili pepper and sichuan pepper",
            "dipping sauce": "Sesame oil mixed with crushed fresh garlic, chopped scallions, and cilantro"
        },
        "next_lesson": "2"
    },
    "2": {
        "lesson_id": "2",
        "title": "Beijing Hotpot",
        "image": "https://via.placeholder.com/300",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """It is characterized by its simplicity and the use of copper Mongolian pots.""",
        "about": {
            "flavor": "Savory and aromatic",
            "meat": "lamb meat",
            "seasoning": "Chinese herbs and spices like goji berries, jujubes, and licorice root",
            "dipping sauce": "Sesame dipping sauce",
        },
        "next_lesson": "3"
    },
    "3": {
        "lesson_id": "3",
        "title": "Sundubu-jjigae",
        # blank image 300 width x 300 height url: https://via.placeholder.com/300
        "image": "https://m.mommindmall.com/web/product/big/202205/89ccf5a7ae0662fb28c0e7e259e0221a.jpg",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """Sundubu-jiggae is a Korean soup cooked with soft tofu and can be prepared in both meat and vegan options.""",
         "about": {
            "flavor": "savory, and choice of spicy or non-spicy broth",
            "meat": "beef, seafood, or pork",
            "seasoning": "kimchi, ham and cheese, dumplings, soysauce, gochugaru and sesame oil",
            "dipping sauce": "instead of dipping sauce, it is served with a bowl of rice and a raw egg to crack into the stew",
        },
        "next_lesson": "4"
    },
    "4": {
        "lesson_id": "4",
        "title": "Coconut Chicken Hotpot",
        "image": "https://hotpotambassador.com/wp-content/uploads/2018/11/chicken.jpg",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """The broth is not made with butter or fatty oils, making it one of the healthier hotpot options.""",
         "about": {
            "flavor": "Rich and creamy coconut flavor with a hint of spice",
            "meat": "Chicken, often served with seafood like shrimp and fish balls",
            "seasoning": "Coconut milk-based broth flavored with lemongrass, galangal, and kaffir lime leaves",
            "dipping sauce": "Soy Dipping Sauce",
        },
        "next_lesson": "5"
    },
    "5": {
        "lesson_id": "5",
        "title": "Sukiyaki Hotpot",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Sukiyaki_01.jpg/440px-Sukiyaki_01.jpg",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """It is a Japanese dish that is prepared and served in the nabemono (Japanese hot pot).""",
         "about": {
            "flavor": "sweet and savory",
            "meat": "Thinly sliced beef",
            "seasoning": "Sweet soy sauce-based broth with mirin, sugar, and sake",
            "dipping sauce": "raw egg dipping sauce",
        },
        "next_lesson": "6"
    },
    "6": {
        "lesson_id": "6",
        "title": "Fondue Hotpot",
        "image": "https://via.placeholder.com/300",
        "dipping_sauce_image": "https://via.placeholder.com/300",
        "text": """In Swiss cuisine, Fondue Chinoise is a local variation of the traditional Chinese hot pot.""",
         "about": {
            "flavor": "Rich and cheesy",
            "meat": "cubes of beef, chicken and pork",
            "seasoning": "Cheese fondue made with a combination of melted cheeses such as Swiss, Gruyère",
            "dipping sauce": "None, as the meat and vegetables are dipped directly into the cheese fondue",
        },
        "next_lesson": "end"
    }
}

quiz_questions = {
    "1": {
        "quiz_id": "1",
        "question": "Which one is Sichuan Hotpot?",
        "answers": {
            "A": "https://via.placeholder.com/300",
            "B": "https://via.placeholder.com/300",
            "C": "https://via.placeholder.com/300",
            "D": "https://via.placeholder.com/300"
        },
        "correct_answer": "A",
        "feedback": "Chongqing hotpots often feature a wide variety of different meats and ingredients",
        "prev_question": "start",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "question": "Which one is Sukiyaki Hotpot?",
        "answers": {
            "A": "https://via.placeholder.com/300",
            "B": "https://via.placeholder.com/300",
            "C": "https://via.placeholder.com/300",
            "D": "https://via.placeholder.com/300"
        },
        "correct_answer": "A",
        "hint": "",
        "feedback": "Sukiyaki is a Japanese dish that is prepared and served in the nabemono.",
        "prev_question": "1",
        "next_question": "3"
    },
    "3": {
        "quiz_id": "3",
        "question": "Which hotpot might be the healthiest one?",
        "answers": {
            "A": "Image1",
            "B": "Image2",
            "C": "Image3",
            "D": "Image4"
        },
        "correct_answer": "C",
        "feedback": "Coconut Chicken Hotpot is one of the healthier hotpot options.",
        "prev_question": "2",
        "next_question": "4"
    },
    "4": {
        "quiz_id": "4",
        "question": "Which dipping sauce should you choose if you are tasting Sichuan Hotpot?",
        "answers": {
            "A": "Sauce1",
            "B": "Sauce2",
            "C": "Sauce3",
            "D": "Sauce4"
        },
        "correct_answer": "D",
        "feedback": "Sichuan hotpot is often served with a dipping sauce made of sesame oil mixed with crushed fresh garlic, chopped scallions, and cilantro.",
        "prev_question": "3",
        "next_question": "5"
    },
    "5": {
        "quiz_id": "5",
        "question": "Which dipping sauce should you choose if you are tasting Sukiyaki Hotpot?",
        "answers": {
            "A": "Sauce1",
            "B": "Sauce2",
            "C": "Sauce3",
            "D": "Sauce4"
        },
        "correct_answer": "A",
        "feedback": "Sukiyaki hotpot is often served with a raw egg dipping sauce.",
        "prev_question": "4",
        "next_question": "6"
    },
    "6": {
        "quiz_id": "6",
        "question": "Which hotpot is soy sauce based?",
        "answers": {
            "A": "Hotpot1",
            "B": "Hotpot2",
            "C": "Hotpot3",
            "D": "Hotpot4"
        },
        "correct_answer": "A",
        "feedback": "Sukiyaki hotpot is a sweet soy sauce-based broth with mirin, sugar, and sake.",
        "prev_question": "5",
        "next_question": "7"
    },
    "7": {
        "quiz_id": "7",
        "question": "Lamb is the main meat in which hotpot?",
        "answers": {
            "A": "Hotpot1",
            "B": "Hotpot2",
            "C": "Hotpot3",
            "D": "Hotpot4"
        },
        "correct_answer": "C",
        "feedback": "Beijing hotpot is characterized by its simplicity and the use of copper Mongolian pots.",
        "prev_question": "6",
        "next_question": "8"
    },
    "8": {
        "quiz_id": "8",
        "question": "What is the name of the Swiss Hotpot?",
        "answers": {
            "A": "Fondue",
            "B": "Frando",
            "C": "Fundi",
            "D": "Funduo"
        },
        "correct_answer": "C",
        "feedback": "Fondue Chinoise is a local variation of the traditional Chinese hot pot.",
        "prev_question": "7",
        "next_question": "9"
    },
    "9": {
        "quiz_id": "9",
        "question": "What does the Korean hotpot Sundubu-jjigae mean?",
        "answers": {
            "A": "Soft tofu stew",
            "B": "chicken stew",
            "C": "beef stew",
            "D": "pork stew"
        },
        "correct_answer": "D",
        "feedback": "Sundubu-jiggae is a Korean soup cooked with soft tofu and can be prepared in both meat and vegan options.",
        "prev_question": "8",
        "next_question": "10"
    },
    "10": {
        "quiz_id": "10",
        "question": "How to pronounce this in Japanese?",
        "answers": {
            "A": "Sukiyaki",
            "B": "Chongqing",
            "C": "Pronounciation3",
            "D": "Pronounciation4"
        },
        "correct_answer": "D",
        "feedback": "Sukiyaki is a Japanese dish that is prepared and served in the nabemono.",
        "prev_question": "9",
        "next_question": "11"
    },
    "11": {
        "quiz_id": "11",
        "question": "What is the main ingredient in the Fondue Hotpot?",
        "answers": {
            "A": "Cheese",
            "B": "Beef",
            "C": "Chicken",
            "D": "Pork"
        },
        "correct_answer": "A",
        "hint": "",
        "prev_question": "10",
        "next_question": "end"
    }
}

