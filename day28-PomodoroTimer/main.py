from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

    # stop timer
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Canvas to layer widgets on top of each other
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="day28-PomodoroTimer/tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold"),
)
canvas.grid(column=1, row=1)

start_button = Button(
    text="Start",
    highlightthickness=0,
    width=10,
    font=(FONT_NAME, 10, "bold"),
    command=start_timer,
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    highlightthickness=0,
    width=10,
    font=(FONT_NAME, 10, "bold"),
    command=reset_timer,
)
reset_button.grid(column=2, row=2)


window.mainloop()
