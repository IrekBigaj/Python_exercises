# #100days of code - day 16 - Coffee Machine - OOP

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine_menu = Menu()
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()

is_on = True

while is_on:
    options = my_machine_menu.get_items()
    user_choice = input("What would you like? (" + options + "): ").lower()
    if user_choice == "off":
        print("🚧 🔧 Maintenance - machine turned off 🔧 🚧")
        is_on = False
    elif user_choice == "report" or user_choice == "r":
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        ordered_drink = my_machine_menu.find_drink(user_choice)
        if my_coffee_machine.is_resource_sufficient(ordered_drink) and my_money_machine.make_payment(ordered_drink.cost):
            my_coffee_machine.make_coffee(ordered_drink)
