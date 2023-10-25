from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=40)

logo = PhotoImage(file="day29-PasswordManagerTk/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=52)
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

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

length_label = Label(text="Length:")
length_label.grid(column=0, row=4)


# Spinbox
length_spinbox = Spinbox(
    from_=12,
    to=25,
    width=5,
    command=spinbox_used,
)
length_spinbox.grid(column=1, row=4, sticky="W")

# Add
add_button = Button(width=30, text="Save Password to File")
add_button.grid(column=1, row=5, columnspan=2, pady=10)


window.mainloop()
