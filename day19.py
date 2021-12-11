from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()

def move_forward():
    timmy.forward(10)

def turn_right():
    timmy.right(5)

def turn_left():
    timmy.left(5)

def move_backward():
    timmy.backward(10)

def change_color():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black', 'violet', 'brown']
    timmy.color(random.choice(colors))

def clean_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

my_screen.listen()
my_screen.onkey(change_color, "space")
my_screen.onkey(move_forward, "w")
my_screen.onkey(move_backward, "s")
my_screen.onkey(turn_right, "d")
my_screen.onkey(turn_left, "a")
my_screen.onkey(clean_screen, "c")

my_screen.exitonclick()
