# #100days of code - day 5 - Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised - in sequence
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""

for letter in range(0, nr_letters):  # tyle razy ile ma byc liter
    easy_password += letters[random.randint(0, len(letters)-1)]   # wylosuj literkę z listy i dodaj do hasła

for symbol in range(0, nr_symbols):  # tyle razy ile ma byc symboli
    easy_password += symbols[random.randint(0, len(symbols)-1)]   # wylosuj symbol z listy i dodaj do hasła

for number in range(0, nr_numbers):  # tyle razy ile ma byc liczba
    easy_password += numbers[random.randint(0, len(numbers)-1)]   # wylosuj liczbe z listy i dodaj do hasła

print('Easy password: ' + easy_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_password = ""

for character in range(0, len(easy_password)):
    random_password += random.choice(easy_password)

print('Randomised password: ' + random_password)

password_list = []

for letter in range(0, nr_letters):  # tyle razy ile ma byc liter
    password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):  # tyle razy ile ma byc symboli
    password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):  # tyle razy ile ma byc liczba
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
haslo = ""

for znak in password_list:
    haslo += znak

print('Randomised second way password: ' + haslo)
