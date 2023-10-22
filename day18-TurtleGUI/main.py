# https://docs.python.org/3/library/turtle.html
# colors: https://trinket.io/docs/colors

from turtle import Turtle, Screen
import random

COLORS = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

# Creating a turtle object
t = Turtle()

# Creating the screen object
screen = Screen()

# Setting the screen color-mode
screen.colormode(255)


def random_color() -> ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# CHALLENGE 3 - Draw Shapes
# draw different shapes with turtle
# num_sides = 5
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.fd(100)
#         t.rt(angle)


# for shape_side_n in range(3, 11):
# draw_shape(shape_side_n)

# CHALLENGE 4 - Random Walk
# walk randomly with turtle (https://en.wikipedia.org/wiki/Random_walk)
# directions = [0, 90, 180, 270]

# t.pensize(15)
# t.speed("fastest")

# for _ in range(200):
#     t.color(random.choice(COLORS))
#     t.forward(30)
#     t.setheading(random.choice(directions))


# CHALLENGE 5 - Spirograph
# draw spirograph with turtle (https://en.wikipedia.org/wiki/Spirograph)
# t.speed("fastest")
# DENSITY = 5

# for _ in range(int(360 / DENSITY)):
#     t.color(random.choice(COLORS))
#     t.circle(100)
#     t.setheading(t.heading() + DENSITY)


# CHALLENGE 6 - HIRST PAINTING

# Step1: Extract Colors from Image to build a new color set
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("day18-TurtleGUI\image.png", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb_colors.append((r, g, b))

# print(rgb_colors)

COLORS = [
    (212, 154, 97),
    (52, 107, 131),
    (180, 78, 31),
    (199, 143, 34),
    (123, 80, 97),
    (117, 154, 170),
    (122, 176, 158),
    (233, 239, 243),
    (229, 197, 127),
    (193, 86, 106),
    (55, 38, 20),
    (11, 51, 65),
    (194, 122, 142),
    (43, 169, 125),
    (53, 121, 116),
    (167, 22, 30),
    (226, 93, 79),
]

# Set turtle shape, penup and hideturtle
t.shape("circle")
t.penup()
t.hideturtle()
t.speed("fastest")

# Move to Starting Position
t.setpos(-300, 300)

# Loop through rows and columns to create the dots
for _ in range(10):  # y axis
    for _ in range(10):  # x axis
        t.color(random.choice(COLORS))
        t.stamp()
        # t.dot(20, random.choice(COLORS))
        t.forward(50)
    t.setpos(-300, t.ycor() - 50)

# Exit on click
screen.exitonclick()
