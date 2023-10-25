from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def generate_password():
    password = ""
    password_length = int(length_spinbox.get())

    ascii_chars = [char for char in range(33, 123)]
    exclude_chars = [34, 39, 42, 44, 46, 64, 96]

    password_chars = [char for char in ascii_chars if char not in exclude_chars]

    for _ in range(password_length):
        password += chr(random.choice(password_chars))

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = password_entry.get()

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    with open("day29-PasswordManagerTk\passwords.txt", "a") as file:
        file.write(f"{website} | {email} | {pwd}\n")

        success_label.config(text=f"Password for {website} Saved!")
        window.after(2000, clear_success_label)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


def clear_success_label():
    success_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=40)

logo = PhotoImage(file="day29-PasswordManagerTk/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", pady=5)
website_label.grid(column=0, row=1)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email
email_label = Label(text="Email/Username:", pady=5)
email_label.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.insert(0, "example@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:", pady=5)
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

length_label = Label(text="Length:")
length_label.grid(column=0, row=4)


# Spinbox
length_spinbox = Spinbox(
    from_=12,
    to=25,
    width=5,
)
length_spinbox.grid(column=1, row=4, sticky="W")

# Add
add_button = Button(width=30, text="Save Password to File", command=save)
add_button.grid(column=1, row=5, columnspan=2, pady=10)

# Successful Transaction
success_label = Label(text="")
success_label.grid(column=1, row=6)

window.mainloop()
