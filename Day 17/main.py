from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q) for q in question_data]
quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_questions_left():
    quiz_brain.ask_questions()

print(f"You scored {quiz_brain.score}/{len(quiz_brain.question_list)}")
