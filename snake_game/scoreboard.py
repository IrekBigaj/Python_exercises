from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 21, "bold")


class ScoreBoard (Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 270)
        self.no_of_points = 0
        self.update()

    def update(self):
        self.write(arg=f"Score: {self.no_of_points}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.no_of_points += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER :(", align=ALIGNMENT, font=FONT)
