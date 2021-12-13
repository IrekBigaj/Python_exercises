# #100days of code - day 22 - Pong Game
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, Line
import time

POINTS_TO_WIN = 10

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("                                                                  "
                "         ===> 👽 Pong Game by Alien Software 👽 <===")
my_screen.tracer(0)

scoreboard = ScoreBoard()
line = Line()
ball = Ball()
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

my_screen.listen()
my_screen.onkey(r_paddle.move_up, "Up")
my_screen.onkey(r_paddle.move_down, "Down")

my_screen.onkey(l_paddle.move_up, "w")
my_screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.xcor() > 380:
        scoreboard.add_point_left()
        ball.refresh()
        ball.move_speed *= 0.9

    # Detect collision with right paddle
    if ball.xcor() < -380:
        scoreboard.add_point_right()
        ball.refresh()
        ball.move_speed *= 0.9

    if scoreboard.no_of_points_left >= POINTS_TO_WIN or scoreboard.no_of_points_right >= POINTS_TO_WIN:
        ball.hideturtle()
        scoreboard.game_over()
        game_is_on = False

    my_screen.update()

my_screen.exitonclick()
