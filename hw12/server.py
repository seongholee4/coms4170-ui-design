from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, jsonify
from data import lessons, quiz_questions

app = Flask(__name__)

# Temporary storage for user answers
user_responses = {'answer': "", 'correct': "", 'second_attempt': "", 'bonus': ""}

total_lessons = len(lessons)
total_questions = len(quiz_questions)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson = lessons[lesson_id]
    return render_template('learn.html', lesson = lesson, total_lessons = total_lessons)

@app.route('/start_quiz')
def start_quiz():
    user_responses.clear()  # Reset answers at the start of a quiz
    return render_template('start_quiz.html')

@app.route('/quiz/<quiz_id>', methods=['GET'])
def quiz(quiz_id):
    question = quiz_questions.get(str(quiz_id))
    if question is None:
        return "Question not found", 404

    # Ensure feedback and button states are reset each time the page is loaded
    feedback = user_responses.get(quiz_id, {}).get('feedback', None)
    print(feedback)

    return render_template('quiz.html', question=question, quiz_id=quiz_id, total_questions=total_questions, feedback=feedback)

@app.route('/quiz/<quiz_id>/check_answer', methods=['POST'])
def check_answer(quiz_id):
    user_answer = request.form.get('answer')
    question = quiz_questions.get(str(quiz_id))
    if not user_answer:
        return jsonify(correct=False, message="No answer selected, please choose an option.")

    # Store answer and correctness in user_responses
    correct = user_answer == question['correct_answer']
    user_responses[quiz_id] = {'answer': user_answer, 'correct': correct}
    if quiz_id == '11' and correct:
        user_responses[quiz_id]['bonus'] = True

    if correct:
        return jsonify(correct=True)
        # return jsonify(correct=True, explanation=question['explanation'])
    else:
        hint = question.get('hint', "")
        return jsonify(correct=False, message="Incorrect! Try again or request a hint.", hint=hint)

@app.route('/quiz_results')
def results():
    score = 0
    for quiz_id, response in user_responses.items():
        if quiz_id not in quiz_questions:
            continue
        ans = response['answer']
        correct = response['correct']
        if correct:
            score += 1
    bonus = user_responses.get('11', {}).get('bonus', False)
    if bonus == True:
        score += 1
    return render_template('quiz_results.html', score=score, total_questions=total_questions)


if __name__ == '__main__':
    app.run(debug=True)
