# represent data in JSON
lessons = {
    "1": {
        "lesson_id": "1",
        "title": "Sichuan Hotpot",
        "image": "https://hotpotambassador.com/wp-content/uploads/2018/11/chongqing-min-1.jpg",
        "text": """It uses mala seasoning flavored with chilli peppers and Sichuan pepper for a spicy and numbing flavor. Chongqing hotpots often feature a wide variety of different meats and ingredients, and offer many saucesand condiments to flavor the meat. The typical dipping sauce contains sesame oil and is mixed with crushed fresh garlic and chopped scallions and cilantros. """,
        "next_lesson": "2"
    },
    "2": {
        "lesson_id": "2",
        "title": "Sukiyaki Hotpot",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Sukiyaki_01.jpg/440px-Sukiyaki_01.jpg",
        "text": """It is a Japanese dish that is prepared and served in the nabemono (Japanese hot pot) style. It consists of meat (usually thinly sliced beef) which is slowly cooked or simmered at the table, alongside vegetables and other ingredients, in a shallow iron pot in a mixture of soy sauce, sugar, and mirin. The ingredients are usually dipped in a small bowl of raw, beaten eggs after being cooked in the pot, and then eaten.""",
        "next_lesson": "3"
    },
    "3": {
        "lesson_id": "3",
        "title": "Budae Jjigae Hotpot",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Budae_jjigae_%2828587380901%29.jpg/440px-Budae_jjigae_%2828587380901%29.jpg",
        "text": """ It also goes by the English name: army stew. It is a type of spicy kimchi based hotpot (Korean stew) from South Korea that is made with a variety of ingredients, often canned or processed. Common ingredients include ham, sausage, Spam, baked beans, kimchi, instant noodles, gochujang and American cheese. No certain dipping sauce but many people eat with kimchi or cheese.""",
        "next_lesson": "end"
    },
    "end": {
        "lesson_id": "end",
        "title": "End of lessons",
        "image": "",
        "text": "End of lessons",
        "next_lesson": ""
    }
}

quiz_questions = {
    "1": {
        "quiz_id": "1",
        "question": "Which one is Sichuan Hotpot?",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "answer1",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "question": "Question2",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "answer3",
        "next_question": "3"
    },
    "3": {
        "quiz_id": "3",
        "question": "Question3",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "answer4",
        "next_question": "end"
    }
}
