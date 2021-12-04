# #100days of code - day 12 - Guess Number Game
import random

logo = """   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
"""

print(logo)
print("Welcome to the Guess Number Game")
print("I'm thinking of a number between 1 and 100.")
player_win = False
no_of_attempts = 0
number_to_guess = random.randint(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
if level == "hard":
    no_of_attempts = 5
elif level == "easy":
    no_of_attempts = 10

while no_of_attempts > 0:

    print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))

    if player_guess == number_to_guess:
        print(f"=> You got it!!! <= The answer was {number_to_guess}")
        no_of_attempts = 0
        player_win = True
    elif player_guess > number_to_guess:
        print("To high!\n")
    else:
        print("To low!\n")
    no_of_attempts = no_of_attempts - 1

if not player_win:
    print(f"You've run out of guesses, you lose! The correct answer was {number_to_guess}")
