from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="day29-PasswordManagerTk/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


window.mainloop()
