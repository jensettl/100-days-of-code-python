# Local Scope - Variables created in functions
# Global Scope - Variables created outside of functions

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssht the answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attemps remaining to guess the number")

    while turns:
        guess = int(input("Make a guess: "))
        if guess < answer:
            print("Too low.")
            turns -= 1
            print(f"You have {turns} attemps remaining.")
        elif guess > answer:
            print("Too high.")
            turns -= 1
            print(f"You have {turns} attemps remaining.")
        else:
            print(f"You guessed correctly with {turns} tries remaining!")
            return


game()
