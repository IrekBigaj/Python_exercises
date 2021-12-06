# #100days of code - day 14 - Higher or Lower Game
import random
from art import logo, vs
from game_data import data

NO_OF_DATA = len(data)
user_score = 0
game_over = False
# print(NO_OF_DATA)
print(logo)

while not game_over:
    if user_score == 0:
        compare_a_no = random.randint(0, NO_OF_DATA-1)
    # print(compare_a_no)
    compare_a = data[compare_a_no]['name'] + ", a " + data[compare_a_no]['description'] + ", from " + data[compare_a_no]['country'] + "."
    no_of_followers_a = data[compare_a_no]['follower_count']

    # print(no_of_followers_a)
    compare_b_no = random.randint(0, NO_OF_DATA-1)
    while compare_b_no == compare_a_no:
        compare_b_no = random.randint(0, NO_OF_DATA - 1)
    compare_b = data[compare_b_no]['name'] + ", a " + data[compare_b_no]['description'] + ", from " + data[compare_b_no]['country'] + "."
    no_of_followers_b = data[compare_b_no]['follower_count']
    # print(no_of_followers_b)

    print(logo)
    print(f"Compare A: {compare_a}")
    print(vs)
    print(f"Against B: {compare_b}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == "A" and no_of_followers_a > no_of_followers_b:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
    elif user_choice == "B" and no_of_followers_b > no_of_followers_a:
        user_score += 1
        compare_a_no = compare_b_no
        print(f"You're right! Current score: {user_score}")
    else:
        game_over = True
        print(f"You are wrong! Final score: {user_score}. GAME OVER")
