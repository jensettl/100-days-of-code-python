# Randomisation and Python Lists

import random
import ascii

choices = ["rock", "paper", "scissors"]

user_choice = input("Do you want - rock, paper or scissors?\n").lower()


def print_ascii(choice):
    if choice == "rock":
        print(ascii.rock)
    elif choice == "paper":
        print(ascii.paper)
    elif choice == "scissors":
        print(ascii.scissors)
    else:
        print(f"{choice} is invalid")


computer_choice = random.choice(choices)

print("Computer chose:")
print_ascii(computer_choice)

print("You chose:")
print_ascii(user_choice)

# Game Logic
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
