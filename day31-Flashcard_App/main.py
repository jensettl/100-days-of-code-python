from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("day30-Flashcard_App/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day30-Flashcard_App/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_back, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_back, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("day30-Flashcard_App/data/words_to_learn.csv", index=False)
    next_card()


# Window Element
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas Element
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="day30-Flashcard_App/images/card_front.png")
card_back_img = PhotoImage(file="day30-Flashcard_App/images/card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
card_back = canvas.create_image(400, 263, image=card_back_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 32, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button Element
cross_im = PhotoImage(file="day30-Flashcard_App/images/wrong.png")
cross_button = Button(image=cross_im, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="day30-Flashcard_App/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()

# Main Loop
window.mainloop()
