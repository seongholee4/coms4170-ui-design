from flask import Flask, redirect
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

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
        "next_lesson": "end"
    }
}
quiz_questions = {
    "1": {
        "quiz_id": "1",
        "question": "Question1",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "answer1",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "question": "Question2",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "answer3",
        "next_question": "end"
    }
}

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson = lessons[lesson_id]
    return render_template('learn.html', lesson = lesson)

@app.route('/quiz')
def start_quiz():
    return redirect('/quiz/1')

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    question = quiz_questions.get(str(quiz_id))
    if question is None:
        return "Question not found", 404
    return render_template('quiz.html', question=question, quiz_id=quiz_id)

# @app.route('/quiz/<quiz_id>')
# def quiz(quiz_id):
#     question = quiz_questions[quiz_id]
#     return render_template('quiz.html', question = question)

if __name__ == '__main__':
    app.run(debug=True)
