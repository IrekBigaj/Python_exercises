# import turtle
from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy_turtle = Turtle()
# timmy_turtle.shape("turtle")
# timmy_turtle.color("blue")
# my_screen = Screen()
# # my_screen.canvheight
# timmy_turtle.forward(100)
#
# jack_turtle = Turtle()
# jack_turtle.shape("turtle")
# jack_turtle.color("red")
# jack_turtle.backward(300)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon", ["electric", "water", "fire"])
table.align = "l"
print(table)
