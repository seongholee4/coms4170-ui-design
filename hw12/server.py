from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, jsonify
from data import lessons, quiz_questions

app = Flask(__name__)

# Temporary storage for user answers
user_responses = {}


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson = lessons[lesson_id]
    return render_template('learn.html', lesson = lesson)

@app.route('/start_quiz')
def start_quiz():
    user_responses.clear()  # Reset answers at the start of a quiz
    return render_template('start_quiz.html')

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    question = quiz_questions.get(str(quiz_id))
    if question is None:
        return "Question not found", 404

    feedback = None
    show_next = False  # Controls the display of the "Next" button
    form_disabled = False  # Disable form after submission

    if request.method == 'POST':
        # Store user's choice in user_responses
        user_answer = request.form.get('answer')
        if user_answer:
            user_responses[quiz_id] = user_answer
            # Provide immediate feedback
            if user_answer == question['correct_answer']:
                feedback = 'Correct!'
            else:
                feedback = 'Incorrect!'
            show_next = True  # Show the "Next" button only after an answer is submitted.
            form_disabled = True  # Disable the form to prevent re-submission

    if question['next_question'] == "end" and show_next:
        return redirect(url_for('results')) # Redirect to results page

    return render_template('quiz.html', question=question, feedback=feedback, quiz_id=quiz_id, show_next=show_next, form_disabled=form_disabled)

@app.route('/quiz_results')
def results():
    score = 0
    for qid, ans in user_responses.items():
        correct_answer = quiz_questions[qid]['correct_answer']
        if ans == correct_answer:
            score += 1
    return render_template('quiz_results.html', score=score, total=len(quiz_questions))


if __name__ == '__main__':
    app.run(debug=True)
