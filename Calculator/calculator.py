# #100days of code - day 10 - Calculator
from art import logo


def add(number1, number2):
    """Function add first and second parameters
    and return sum of them"""
    return number1 + number2


def subtract(number1, number2):
    """Function subtract first and second parameters
    and return result of subtraction"""
    return number1 - number2


def multiply(number1, number2):
    """Function multiply first and second parameters
    and return result of multiplication"""
    return number1 * number2


def divide(number1, number2):
    """Function divide first and second parameters
        and return result of division.
        If second parameter is zero returns zero."""
    if number2 == 0:
        return 0
    else:
        return number1 / number2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


def calculator():
    """
    Main function to calculate operations
    """
    print(logo)
    number1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)

    to_continue = True
    while to_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            number1 = answer
        else:
            to_continue = False
            calculator()


calculator()
