# #100days of code - day 27 - Exercises

import tkinter
window = tkinter.Tk()
window.title("Window name!")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # dodaje ramkę wokół elementu - tu okna

def button_clicked():
    my_label["text"] = f"Clicked and write: {input_data.get()}!"


my_label = tkinter.Label(text="Label name", font=("Arial", 20, "bold"))
# my_label.pack(side="left")  # wyswietla na ekranie
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)  # dodaje ramkę wokół elementu - tu labelki

input_data = tkinter.Entry(width=10)
# input_data.pack()
input_data.grid(column=3, row=2)

button = tkinter.Button(text="New button", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New button2", command=button_clicked)
button2.grid(column=2, row=0)


window.mainloop()  # na koniec programu

# def add(*args):
#     sum_of_numbers = 0
#     for number in args:
#         sum_of_numbers += number
#     return sum_of_numbers
#
#
# print(add(7, 1, 5, 6, 7, 0, 4))
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(10, add=3, multiply=5)
#
#
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.colour = kwargs.get("colour")
#
#
# my_car = Car(make = "Nissan", model="GTR")
# print(my_car.model)