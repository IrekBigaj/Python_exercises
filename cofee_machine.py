# #100days of code - day 15 - Coffee Machine

LOGO = """
  #####  ####### ####### ####### #######    #     #    #     #####  #     # ### #     # ####### 
 #     # #     # #       #       #          ##   ##   # #   #     # #     #  #  ##    # #       
 #       #     # #       #       #          # # # #  #   #  #       #     #  #  # #   # #       
 #       #     # #####   #####   #####      #  #  # #     # #       #######  #  #  #  # #####   
 #       #     # #       #       #          #     # ####### #       #     #  #  #   # # #       
 #     # #     # #       #       #          #     # #     # #     # #     #  #  #    ## #       
  #####  ####### #       #       #######    #     # #     #  #####  #     # ### #     # ####### 
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0


def print_report():
    """ Print status of resources in coffee machine. No return"""
    print("     => 📄 RESOURCES IN MACHINE REPORT: 📄")
    print("     => Water: " + str(resources["water"]) + " ml")
    if resources["water"] == 0:
        print("     => !!!! You should add some water!")
    print("     => Milk: " + str(resources["milk"]) + " ml")
    if resources["milk"] == 0:
        print("     => !!!! You should add some milk!")
    print("     => Coffee: " + str(resources["coffee"]) + " g")
    if resources["coffee"] == 0:
        print("     => !!!! You should add some coffee!")
    print(f"     => Money: $" + "%.2f" % money_in_machine + "\n")
    return


def check_resources(drink):
    """Function is checking sufficient resources to prepare drink in input
    Return: 1 if there are sufficient resources, 0 otherwise"""
    # print("Drink cost: " + str(MENU[drink]["cost"]))
    need_water = MENU.get(drink).get("ingredients").get("water", 0)
    need_milk = MENU.get(drink).get("ingredients").get("milk", 0)
    need_coffee = MENU.get(drink).get("ingredients").get("coffee", 0)
    # print(f"We need: Water: {need_water}, milk: {need_milk} and coffee: {need_coffee}")
    existing_water = resources["water"]
    existing_milk = resources["milk"]
    existing_coffee = resources["coffee"]
    # print(f"We have: Water: {existing_water}, milk: {existing_milk} and coffee: {existing_coffee}")
    if existing_water >= need_water and existing_milk >= need_milk and existing_coffee >= need_coffee:
        # print("We have all ingredients")
        return 1
    elif existing_water < need_water:
        print("! ⚠️Sorry there is not enough water. :( Choose another drink.")
        return 0
    elif existing_milk < need_milk:
        print("! ⚠️Sorry there is not enough milk. :( Choose another drink.")
        return 0
    elif existing_coffee < need_coffee:
        print("! ⚠️Sorry there is not enough coffee. :( Choose another drink.")
        return 0
    else:
        return 0


def payment_for_drink(drink):
    """Process payment for drink in input.
    Returns: 1 if paid, 0 - otherwise"""
    global money_in_machine
    to_pay = MENU.get(drink).get("cost", 0)
    print(f"Amount to pay for {drink}: $" + "%.2f" % to_pay)  # formatted like a price
    print("Please insert coins:")
    try:
        quarters = int(input("How many quarters?: "))  # quarter = $0.25
    except ValueError:
        print("! ⚠️Wrong number. Count as 0.")
        quarters = 0
    try:
        dimes = int(input("How many dimes?: "))  # dime = $0.1
    except ValueError:
        print("! ⚠️Wrong number. Count as 0.")
        dimes = 0
    try:
        nickles = int(input("How many nickles?: "))  # nickel = $0.05
    except ValueError:
        print("! ⚠️Wrong number. Count as 0.")
        nickles = 0
    try:
        pennies = int(input("How many pennies?: "))  # penny = $0.01
    except ValueError:
        print("! ⚠️Wrong number. Count as 0.")
        pennies = 0
    user_inserted = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    print(f"You inserted $" + "%.2f" % user_inserted + " in coins.")
    if user_inserted == to_pay:
        money_in_machine += to_pay
        return 1
    elif user_inserted > to_pay:
        money_in_machine += to_pay
        print(f"Here is ${round(user_inserted-to_pay,2)} in change.")
        return 1
    else:
        print("! ⚠️Sorry that's not enough money. Money refunded.")
        return 0


def prepare_drink(drink):
    # existing_water = resources["water"]
    # existing_milk = resources["milk"]
    # existing_coffee = resources["coffee"]
    need_water = MENU.get(drink).get("ingredients").get("water", 0)
    need_milk = MENU.get(drink).get("ingredients").get("milk", 0)
    need_coffee = MENU.get(drink).get("ingredients").get("coffee", 0)
    resources["water"] -= need_water
    resources["milk"] -= need_milk
    resources["coffee"] -= need_coffee

    print(f"☕ Here is your {drink}. Enjoy!")
    return


def ask_user():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("🚧 🔧 Maintenance - machine turned off 🔧 🚧")
        exit()
    elif user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "e":
        if check_resources("espresso") == 1:
            if payment_for_drink("espresso") == 1:
                prepare_drink("espresso")
    elif user_choice == "latte" or user_choice == "l":
        if check_resources("latte") == 1:
            if payment_for_drink("latte") == 1:
                prepare_drink("latte")
    elif user_choice == "cappuccino" or user_choice == "c":
        if check_resources("cappuccino") == 1:
            if payment_for_drink("cappuccino") == 1:
                prepare_drink("cappuccino")
    else:
        print("! ⚠️Sorry. We don't have such drink!")
    return


while True:
    print(LOGO)
    ask_user()
