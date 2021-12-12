# #100days of code - day 20-21 - Snake Game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("                                ===> 🐍 Snake Game by Alien Software 🐍 <===")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)  # control snake's speed - you can choose level or speed up if score is higher
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_point()
        snake.extend_snake()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with snake's tail
    for segment in snake.snake_segments[1:]:  # choose elements from list from 1 to end (slice)
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()
