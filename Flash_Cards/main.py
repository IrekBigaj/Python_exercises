# #100days of code - day 31 - Flash Cards App

from tkinter import *
import pandas
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIME = 3 * 1000  # 3 * 1000 millisecond
current_card = {}
to_learn_words = {}

# ---------------------------- DATA OPERATE ------------------------------- #
# to_learn_data = pandas.read_csv("data/french_words.csv")
try:
    to_learn_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    to_learn_data = pandas.read_csv("data/french_words.csv")

to_learn_words = to_learn_data.to_dict(orient="records")
print(len(to_learn_words))


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_words)
    canvas.itemconfig(card_name, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_image, image=card_front_img)
    flip_timer = window.after(TIME, reverse_card)


def reverse_card():
    canvas.itemconfig(background_image, image=card_back_img)
    canvas.itemconfig(card_name, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known():
    to_learn_words.remove(current_card)
    print(len(to_learn_words))
    data_to_save = pandas.DataFrame(to_learn_words)
    data_to_save.to_csv("data/words_to_learn.csv", index=False)
    canvas.itemconfig(words_to_learn, text=f"Words to learn: {len(to_learn_words)-1}")
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FlashCards by Alien 👽")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIME, reverse_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Text
words_to_learn = canvas.create_text(400, 50, text=f"Words to learn: {len(to_learn_words)-1}", font=(FONT_NAME, 15))
card_name = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

# Buttons
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
