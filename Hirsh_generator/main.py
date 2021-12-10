# #100days of code - day 18 - Hirsh dot painting generator
import random

import colorgram
from turtle import Turtle, Screen, colormode

timmy = Turtle()
my_screen = Screen()


def extract_colors(file):
    """Function extracts list of RGB colors from picture in input parameter"""
    rgb_list = []
    colors = colorgram.extract(file, 100)
    # print(len(colors))
    for i in range(0, len(colors)):
        color_rgb = colors[i].rgb
        # print(color_rgb)
        r = color_rgb.r  # r = color_rgb[0]
        g = color_rgb.g
        b = color_rgb.b
        color_tuple = (r, g, b)
        # print(color_tuple)
        rgb_list.append(color_tuple)
    return rgb_list


# print(extract_colors("image.jpg"))

color_list = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35),
              (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64),
              (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79),
              (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90),
              (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204),
              (78, 66, 42), (23, 99, 96)]

# 10 x 10 dots
# radius 20
# space betwwen 50

timmy.speed(10)
pensize = 1
colormode(255)

timmy.penup()
timmy.hideturtle()
timmy.goto(-200, -200)


for i in range(0, 10):
    for j in range(0, 10):
        # timmy.pendown()
        random_color = random.choice(color_list)
        timmy.dot(20, random_color)
        # timmy.penup()
        timmy.forward(50)
    timmy.goto(timmy.xcor() - 10*50, timmy.ycor() + 50)


my_screen.exitonclick()
