from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
import random

topic = input("What Quiz Set would you like to play 'Computers' or 'Mathematics'?: ")

question_bank_filtered = [
    item for item in question_data if item["category"] == f"Science: {topic}"
]

question_bank = [
    Question(item["question"], item["correct_answer"])
    for item in question_bank_filtered
]

# for question in question_data:
#     new_question = Question(question["text"], question["answer"])
#     question_bank.append(new_question)

random.shuffle(question_bank)

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
