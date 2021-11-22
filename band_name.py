# Band name generator #100days of code - day 1
import introOutro

# Special line for intro
introOutro.intro_program("The Band Name Generator")

# 1. Create a greeting for your program.
print('Welcome to the Band Name Generator')
# 2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew in?\n")

# 3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

# 4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
print("Your band name could be " + band_name)

# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

# try do it in 1 line
print("---- Shorter ----")
print("Your band name could be " + input("What's name of the city you grew in?\n") + " " + input("What's your pet's name?\n"))
