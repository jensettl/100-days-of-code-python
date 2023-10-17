# Hangman Game
# For / While Loops, If/Else, Lists, Strings, Range

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

CHOSEN_WORD = random.choice(word_list)
LIVES = 6

word_hidden = ["_" for _ in range(len(CHOSEN_WORD))]
print(f" ".join(word_hidden))

while "_" in word_hidden:
    guess = input("\nGuess a letter: ").lower()

    # check if letter already guessed
    if guess in word_hidden:
        print(f"You've already guessed {guess}")

    # evaluate guess and replace blanks
    for idx, letter in enumerate(CHOSEN_WORD):
        if letter == guess:
            word_hidden[idx] = letter

    # check if guess is not in CHOSEN_WORD
    if guess not in CHOSEN_WORD:
        LIVES -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if LIVES == 0:
            print(stages[LIVES])
            print(f"You lose! The word was {CHOSEN_WORD}")
            exit()

    # print the current state of the word
    print(f" ".join(word_hidden))
    print(stages[LIVES])

print("You win!")
