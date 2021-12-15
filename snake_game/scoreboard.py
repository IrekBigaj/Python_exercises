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
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.no_of_points} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.no_of_points += 1
        self.update()

    def reset(self):
        if self.no_of_points > self.high_score:
            self.high_score = self.no_of_points
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.no_of_points = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER :(", align=ALIGNMENT, font=FONT)
