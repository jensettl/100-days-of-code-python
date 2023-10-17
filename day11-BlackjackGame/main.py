from logo import logo
import random
import os
from typing import List


CARD_VALUES = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}


def deal_card() -> str:
    """Returns a random card from the deck."""
    return random.choice(list(CARD_VALUES.keys()))


def calculate_score(cards: List[str]) -> int:
    """Take a list of cards and return the score calculated from the cards"""
    score = 0
    for card in cards:
        score += CARD_VALUES[card]
    if score == 21 and len(cards) == 2:
        return 0
    if "Ace" in cards and score > 21:
        score -= 10
    return score


def compare(user_score: int, computer_score: int) -> str:
    """Compares user's and computer's scores and returns the result of the game.

    Args:
        user_score (int): sum of values of user's cards
        computer_score (int): sum of values of computer's cards

    Returns:
        str: result of the game
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game() -> None:
    """Plays a game of Blackjack."""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the user and computer 2 cards each using deal_card()
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your cards: {user_cards}")
        print(f"  Computer's First Card: [{computer_cards[0]}]\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: \n"
            )
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"> Your final hand: {user_cards}, final score: {user_score}")
    print(f"> Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()
