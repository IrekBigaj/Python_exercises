from turtle import Turtle
WIDTH = 5
HEIGHT = 1


class Paddle (Turtle):  # inherit from Turtle superclass
    def __init__(self, x_position, y_position):
        super().__init__()
        # self.penup()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.color("white")
        self.speed("fastest")
        self.x_position = x_position
        self.y_position = y_position
        self.goto(x_position, y_position)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)

    def move_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
