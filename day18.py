from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
my_screen = Screen()

#timmy.shape("turtle")
#timmy.color("red")

# draw square
# for i in range(4):
#     timmy.forward((100))
#     timmy.right(90)

# modul generacji imion superbohaterow
# import heroes

# rysuje przerywana linie
# for i in range (8):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# rysuje zestaw figur geometrycznych o losowych koloarach
# for no_side in range(3, 11):  # jakie figury ma rysowac (od trojkata do dziesiaciokata
#     colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#     timmy.pencolor(random.choice(colors))
#     for times in range(no_side):  # tyle razy co ma boki
#         timmy.forward(100)
#         timmy.right(360 / no_side)

# rysuje linię w losowym kierunku o losowym kolorze

timmy.speed(10)
pensize = 1
colormode(255)


def random_color():
    """Funkcja zwraca skladniki r,g,b koloru"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

# rysuje coraz grubszą kreskę poruszając sie w losowym kierunku
# while True:
#     colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black', 'violet', 'brown']
#     #timmy.pencolor(random.choice(colors))
#     timmy.pencolor(random_color())
#     timmy.pensize(pensize)
#     for i in range(1, random.randint(1, 5)):
#         timmy.right(90)
#     timmy.forward(30)
#     pensize += 1


timmy.speed(0)

# spirograf
def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(size_of_gap)


draw_spirograph(5)
my_screen.exitonclick()
