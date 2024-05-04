from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, jsonify
from data import lessons, quiz_questions

app = Flask(__name__)

# Temporary storage for user answers
user_responses = {'answer': "", 'correct': "", 'second_attempt': ""}

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
    feedback = question.get('feedback', "")

    return render_template('quiz.html', question=question, quiz_id=quiz_id, total_questions=total_questions, feedback=feedback)

@app.route('/quiz/<quiz_id>/check_answer', methods=['POST'])
def check_answer(quiz_id):
    user_answer = request.form.get('answer')
    question = quiz_questions.get(str(quiz_id))
    if not user_answer:
        return jsonify(correct=False, message="No answer selected, please choose an option.")

    # Store answer and correctness in user_responses
    correct = user_answer == question['correct_answer']
    second_attempt = user_responses.get(quiz_id, {}).get('second_attempt')

    if correct or (second_attempt and second_attempt['correct'] == True):
        if second_attempt:
            user_responses[quiz_id]['second_attempt'] = {'correct': correct, 'answer': second_attempt}
        else:
            user_responses[quiz_id] = {'answer': user_answer, 'correct': correct}
        explanation = question.get('explanation', "Well done! Your answer is correct.")
        return jsonify(correct=True, message=explanation)
    else:
        # Check if it's the first attempt
        if 'second_attempt' not in user_responses.get(quiz_id, {}):
            # Store the first attempt
            user_responses[quiz_id] = {'answer': user_answer, 'correct': correct}
            feedback = question.get('feedback', "")
            return jsonify(correct=False, message="Incorrect! Here is a hint to help you choose the correct answer.", feedback=feedback)
        else:
            user_responses[quiz_id]['second_attempt'] = {'correct': False, 'answer': user_answer}
            feedback = question.get('feedback', "")
            return jsonify(correct=False, message="Incorrect! here is the feedback", feedback=feedback)

@app.route('/quiz_results')
def results():
    score = 0
    for quiz_id, response in user_responses.items():
        if quiz_id not in quiz_questions:
            continue
        correct = response['correct']
        if correct:
            score += 1
        else:
            second_attempt = response.get('second_attempt', {})
            if second_attempt and second_attempt.get('correct'):
                score += 1

   
    return render_template('quiz_results.html', score=score, total_questions=total_questions)




if __name__ == '__main__':
    app.run(debug=True)
