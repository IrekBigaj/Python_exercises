# Rock, papper, scissors - #100days of code - day 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

possible_choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print('You typed wrong number, you lose!')
else:
    print(f'{possible_choices[user_choice]}')

    computer_choice = random.randint(0, 2)
    print(f'Computer chose:\n {possible_choices[computer_choice]}')

    # Rock wins against scissors. 0 > 2
    # Scissors win against paper. 2 >1
    # Paper wins against rock. 1> 0

    if user_choice == 0 and computer_choice == 2:
        print("You WIN!")
    elif computer_choice > user_choice:
        print("You lose :(")
    elif computer_choice == user_choice:
        print("It's a draw")
    elif user_choice > computer_choice:
        print("You WIN!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose :(")
