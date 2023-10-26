from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Window Element
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Element
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="day30-Flashcard_App/images/card_front.png")
card_back_img = PhotoImage(file="day30-Flashcard_App/images/card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 32, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button Element
wrong_img = PhotoImage(file="day30-Flashcard_App/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command="")
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="day30-Flashcard_App/images/right.png")
right_button = Button(
    image=right_img,
    highlightthickness=0,
    fg=BACKGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    command="",
)
right_button.grid(column=1, row=1)


# Main Loop
window.mainloop()
