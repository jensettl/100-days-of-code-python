from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def Up(self):
        self.goto(self.xcor(), self.ycor() + 40)

    def Down(self):
        self.goto(self.xcor(), self.ycor() - 40)
