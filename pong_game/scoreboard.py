from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, "bold")
WIDTH = 1
HEIGHT = 0.2


class ScoreBoard (Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 270)
        self.no_of_points_left = 0
        self.no_of_points_right = 0
        self.update()

    def update(self):
        self.write(arg=f"{self.no_of_points_left} 👽 SCORE 👽 {self.no_of_points_right}", align=ALIGNMENT, font=FONT)

    def add_point_left(self):
        self.clear()
        self.no_of_points_left += 1
        self.update()

    def add_point_right(self):
        self.clear()
        self.no_of_points_right += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)


class Line (Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.pensize(5)
        self.goto(0, -260)
        self.left(90)

        for i in range(-260, 260, 40):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
