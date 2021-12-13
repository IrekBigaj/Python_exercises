from turtle import Turtle
WIDTH = 1
HEIGHT = 1


class Ball (Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
