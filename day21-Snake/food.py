from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-27, 27) * 10
        random_y = random.randint(-27, 27) * 10
        self.goto(random_x, random_y)
