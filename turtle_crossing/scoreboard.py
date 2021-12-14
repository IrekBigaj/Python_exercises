from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard (Turtle):  # inherit from Turtle superclass
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"👽 Level: {self.level}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
