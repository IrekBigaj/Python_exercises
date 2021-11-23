# Day 2 - #100Days Of Code

# funkcja type() - zwraca typ zmiennej

print(type(123))

# str() - konwertuje na string
# float() - konwertuje na liczbę zmiennoprzecinkową - float

two_digit_number = input("Type a two digit number: ")

try:
    suma = int(two_digit_number[0]) + int(two_digit_number[1])
except TypeError:
    print("Coś nie tak wpisales")
    exit("Wyjście z błędem TypeError")
except ValueError:
    print("Coś nie tak wpisales")
    exit("Wyjście z błędem ValueError")

print(suma)


age = input("What is your current age? ")
how_long = input("How long you will live (90?) ? ")
years = int(how_long) - int(age)
months = years*12
weeks = years*52
days = years*365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

