# Classic Pong Game created with the Turtle Module

# Challenges:
# Create a Screen
# Create and move a paddle
# Create another player
# Create the ball and make it move
# Detect collision with the wall and bounce
# Detect collision with paddle
# Detect whenn paddle misses
# Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = False
prompt = "Who do you wanna face? Type 'player' or 'computer'"

# Creating a screen Object
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
player_settings = screen.textinput(title="Player Settings", prompt=prompt)

# Create objects
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

# Track Keystroke
screen.listen()
screen.onkey(key="Up", fun=r_paddle.Up)
screen.onkey(key="Down", fun=r_paddle.Down)
screen.onkey(key="w", fun=l_paddle.Up)
screen.onkey(key="s", fun=l_paddle.Down)

if player_settings:
    game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # computer plays right paddle, comment out to deactivate
    if player_settings == "computer" and ball.xcor() > 0:
        if r_paddle.ycor() < ball.ycor():
            r_paddle.Up()
        elif r_paddle.ycor() > ball.ycor():
            r_paddle.Down()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 330
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -330
    ):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

# Exit on click
screen.exitonclick()
