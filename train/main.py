from model import Question
from train_data import data
from quiz import Train
from ui1 import interface

question_bank = []

for question in data:
    question_name = question["name"]
    question_seats = question["seats"]
    question_fare = question["fare"]

    # print(question_name)

    new_question = Question(question_name, question_seats, question_fare)
    
    # print(new_question)

    # print(f"{new_question.name} {new_question.seats} {new_question.fare}")

    question_bank.append(new_question)

# print(question_bank[0].name, question_bank[0].seats, question_bank[0].fare)

quiz = Train(question_bank[0].seats,question_bank[1].seats,  question_bank)

quiz_ui = interface(quiz)
# quiz.train_name()
# while quiz.booking_continue():
#     quiz.bookTicket()
#     restart=input("Type 'yes' if you want to book a ticket again. Otherwise type 'no'.\n")

#     if restart=="no":
#         print("Thank you")
#         break
