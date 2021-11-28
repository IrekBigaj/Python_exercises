# #100days of code - day 7 - Hangman Game
import random
import hangman_art

from cleaner import clean
# pozwala na wyczyszczenie ekranu

# could be used as below
# import hangman_words
# word_list = hangman_words.word_list
# better is user bellow - simpler

from hangman_words import word_list  # po przecinku mogą być kolejne wymieniane

word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)
lives = 6
end_of_game = False

print(hangman_art.logo)

print(f'Pssst, the solution is {word_to_guess}.')

display = []

for n in range(0, word_length):  # alternatively for letter in word_to_guess
    display.append("_")  # alternatively display += "_"

# print(display)

while not end_of_game:  # alternatively while "_" in display
    guess_letter = input("Guess a letter: ").lower()
    clean()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}.")

    for i in range(0, word_length):
        # print(f"Current position: {i}\n Current letter: {word_to_guess[i]}\n Guessed letter: {guess_letter}")
        if guess_letter == word_to_guess[i]:
            display[i] = guess_letter

    print(f"{' '.join(display)}")

    if guess_letter not in word_to_guess:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose! GAME OVER")
            end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
