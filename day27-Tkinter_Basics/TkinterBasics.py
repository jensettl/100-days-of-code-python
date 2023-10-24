# Tkinter
# can be used to create GUI applications
# Tkinter is a built-in module in python

# Properties of Tkinter: https://tcl.tk/man/tcl8.6/TkCmd

# Mark Code BY SECTION below, SHIFT+Enter to start in interactive mode

# ======================================================================================================================

from tkinter import *

root = Tk()  # creates a blank window

# Title
root.title("Tkinter Basics!")

# Window Size
root.minsize(400, 400)  # width x height

# Label
myLabel = Label(root, text="Hello World!", font=("Helvetica", 24, "bold"))
myLabel.pack()


# Button
def button_click():
    button["text"] = "Clicked!"
    new_text = input.get()
    myLabel.config(text=new_text)
    # myLabel.config(text="Button Clicked!")


button = Button(text="Click Me!", command=button_click)
button.pack(side="top")


# Entry
input = Entry(width=50)
input.pack()

root.mainloop()  # keeps the window open

# Tkinter is a very basic GUI module
# It is not used for professional GUI applications
# It is used to make quick and easy GUI applications

# ======================================================================================================================
# Tkinter Grid

from tkinter import *

root = Tk()
root.title("Tkinter Grid")
root.geometry("400x400")

# creating a label widget
myLabel = Label(root, text="Hello World!", padx=50)
# shoving it onto the screen
myLabel.grid(row=0, column=0)

# button widget
myButton = Button(root, text="Click Me!")
myButton.grid(row=0, column=1)

root.mainloop()

# Tkinter uses a grid system to place widgets on the screen
# Each widget can use the grid system to specify which row and column to go in

# ======================================================================================================================
