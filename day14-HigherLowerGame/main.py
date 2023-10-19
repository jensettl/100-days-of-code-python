from game_data import data
from art import logo, vs
import random
import os


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(data):
    """Takes the data and returns the printable format."""
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f"{name}\n({description}, from {country})"


def check_winner(option1, option2):
    return option1 if option1["follower_count"] > option2["follower_count"] else option2


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "A"  # True if a is correct, False if b is correct
    else:
        return guess == "B"  # True if b is correct, False if a is correct


def game():
    print(logo)
    failed = False
    score = 0

    # Random Choices from game_data
    option1 = get_random_account()

    while not failed:
        option2 = get_random_account()
        # Reroll if options are the same
        while option1 == option2:
            option2 = get_random_account()

        # print options
        print(f"Compare A: {format_data(option1)}")
        print(vs)
        print(f"Against B: {format_data(option2)}")

        # User input
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        is_correct = check_answer(
            guess, option1["follower_count"], option2["follower_count"]
        )

        os.system("cls")
        print(logo)

        if is_correct:
            score += 1
            option1 = option2
            print(f"You're right! Current score: {score}")
        else:
            failed = True
            os.system("cls")
            print(f"Sorry, that's wrong. Final score: {score}")


game()
