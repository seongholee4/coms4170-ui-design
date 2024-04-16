# represent data in JSON
lessons = {
    "1": {
        "lesson_id": "1",
        "title": "Lesson 1",
        "image": "This is the first lesson",
        "text": "This is the first lesson",
        "next_lesson": "2"
    },
    "2": {
        "lesson_id": "2",
        "title": "Lesson 2",
        "image": "This is the second lesson",
        "text": "This is the second lesson",
        "next_lesson": "3"
    },
    "3": {
        "lesson_id": "3",
        "title": "Lesson 3",
        "image": "This is the third lesson",
        "text": "This is the third lesson",
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