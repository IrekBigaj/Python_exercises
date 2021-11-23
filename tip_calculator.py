# Tip Calculator #100days of code - day 2

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill_amount = 0
tip_percent = 0
how_many_people = 0

try:
    bill_amount = float(input("What was the total bill? $"))
except TypeError:
    exit("Wrong input data! TypeError")
except ValueError:
    exit("Wrong input data! ValueError")


# What was the total bill? $124.56
try:
    tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
except TypeError:
    exit("Wrong input data! TypeError")
except ValueError:
    exit("Wrong input data! ValueError")

if tip_percent == 10 or tip_percent == 12 or tip_percent == 15:
    print("Good choice!")
else:
    print("Wrong percent but I try calculate it.")

try:
    how_many_people = int(input("How many people to split the bill? "))
except TypeError:
    exit("Wrong input data! TypeError")
except ValueError:
    exit("Wrong input data! ValueError")

# amount_per_person = round((bill_amount/how_many_people) * (1 + tip_percent/100), 2)
bill_with_tip = round(bill_amount * (1 + tip_percent/100), 2)
# amount_per_person = round(bill_with_tip/how_many_people, 2) # nie zapewnia poprawnej
# prezentacji - wyświetla się 1 miejsce po przecinku
amount_per_person = "{:.2f}".format(bill_with_tip/how_many_people)  # wymusza format dla liczby
# zmiennoprzecinkowej i konwertuje na string
# większy opis jest tutaj: https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

print(f"Each person should pay: ${amount_per_person}")
