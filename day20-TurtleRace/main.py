# In this chapter: Event Listeners, States and Higher Order Functions

# Higher Order Functions: Functions that can be passed as arguments to other functions
# Event Listeners: Functions that can detect key presses, mouse clicks, etc.
# Object States: Objects that can remember things about themselves

from turtle import Turtle, Screen
import random

# Variables & Constants
is_race_on = False
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COORDINATES = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# Creating a screen object
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

# Create 6 turtles objects
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(COLORS[turtle_index])
    new_turtle.goto(x=-230, y=Y_COORDINATES[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# Exits the program when the user clicks on the screen
screen.exitonclick()
