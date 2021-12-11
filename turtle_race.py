# #100days of code - day 19 - Turtle Race Game
from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

user_choice = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []
start_position = -100

start_line_drawer = Turtle()
start_line_drawer.hideturtle()
start_line_drawer.penup()
start_line_drawer.goto(x=-230+20, y=start_position-30)
start_line_drawer.pendown()
start_line_drawer.left(90)
start_line_drawer.forward(200)
start_line_drawer.write("Start")

finish_line_drawer = Turtle()
finish_line_drawer.hideturtle()
finish_line_drawer.penup()
finish_line_drawer.goto(x=200, y=start_position - 30)
finish_line_drawer.pendown()
finish_line_drawer.left(90)
finish_line_drawer.forward(200)
finish_line_drawer.write("Finish")

user = Turtle(shape="turtle")
# user.hideturtle()
user.penup()
user.goto(x=-100, y=170)
user.pendown()
user.color(user_choice)
user.write("         Your choice: " + str(user_choice).upper() + " turtle will win.")


def print_winner_name(wining_turtle, user_bet):
    printer = wining_turtle.clone()
    printer.goto(x=-100, y=130)
    printer.pencolor("black")
    win_color = wining_turtle.pencolor()
    if win_color == user_bet:
        printer.write("         YOU'VE WON :) ! The " + str(wining_turtle.pencolor().upper()) +
                      " turtle is the winner!")
    else:
        printer.write("         YOU'VE LOST :( ! The " + str(wining_turtle.pencolor().upper()) +
                      " turtle is the winner!")


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_position)
    start_position += 30
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 176:
            is_race_on = False
            winning_color = turtle.pencolor()
            print_winner_name(turtle, user_choice)
            # if winning_color == user_choice:
            #     print(f"You've won! The {winning_color} turtle is the winner!")
            # else:
            #     print(f"You've lost! The {winning_color} turtle is the winner!")


my_screen.exitonclick()
