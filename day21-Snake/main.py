# Creating the classic snake game with the turtle module in python

# Challenges:
# Level 1: Create a Snake Body, Move the snake, Create Snake Food
# Level 2: Detect Collision with food, Create a scoreboard, Detect collision with wall, Detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time


# Creating a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off animation

# Creating a snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# game is on
game_is_on = True

# key inputs
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()  # update the screen
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Exit the screen on click
screen.exitonclick()
