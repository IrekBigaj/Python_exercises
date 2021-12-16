from turtle import Turtle
FONT = ("Courier", 10, "normal")
ALIGNMENT = "center"


class Publish(Turtle):
    def __init__(self, answer_state, name_x_pos, name_y_pos):
        super().__init__()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.goto(name_x_pos, name_y_pos)
        self.write(arg=answer_state, align=ALIGNMENT, font=FONT)



