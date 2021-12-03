# #100days of code - day 11 - Black Jack Game
from art import logo
import random


def deal_card():
    """Return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = cards[random.randint(0, len(cards)-1)]
    return random_card


def calculate_score(list_of_cards):
    """Input is a list of cards. Return is a score calculated from list of cards."""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        # print("You lose!")
        return 0

    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("A draw!")
    elif computer_score == 0:
        print("Computer win")
    elif user_score == 0:
        print("You win")
    elif user_score > 21:
        print("Computer win")
    elif computer_score > 21:
        print("You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("Computer win!")


def play():
    player_cards = []
    computer_cards = []
    print(logo)

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    to_continue = True
    end_of_game = False

    if calculate_score(player_cards) == 0:
        # print("You win :)")
        to_continue = False
        end_of_game = True
    if calculate_score(computer_cards) == 0:
        # print("You lose! Computer win")
        to_continue = False
        end_of_game = True

    while to_continue:
        print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        another_card = input("Type 'y' to get another card, type 'n' to pass:\n")

        if another_card == "y":
            player_cards.append(deal_card())
            if calculate_score(player_cards) == 0:
                # print("You win :)")
                to_continue = False
                end_of_game = True
            elif calculate_score(player_cards) > 21:
                # print("You lose!")
                to_continue = False
                end_of_game = True
        else:
            to_continue = False

    if calculate_score(computer_cards) >= 17:
        end_of_game = True

    while not end_of_game:
        computer_cards.append(deal_card())
        if calculate_score(computer_cards) >= 17:
            end_of_game = True

    print(f"    => Your final hand: {player_cards}, your score: {sum(player_cards)}")
    print(f"    => Computer's final hand: {computer_cards}, computer score: {sum(computer_cards)}")
    compare(calculate_score(player_cards), calculate_score(computer_cards))

    if input("Do you want play again? Type 'y' to play again, type 'n' to finish:\n").lower() == 'y':
        play()
    else:
        print("Goodbye!")


play()
