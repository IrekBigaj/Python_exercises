from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.back_to_start()
        self.left(90)
        self.FINISH_LINE = FINISH_LINE_Y

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def back_to_start(self):
        self.goto(STARTING_POSITION)
