# #100days of code - day 29 - Password Manager
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_data.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = str(website_data.get())
    email = str(email_data.get())
    password = str(password_data.get())
    data = website + " | " + email + " | " + password + "\n"
    # print(data)

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Correct it!", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(data)
            file.close()
            website_data.delete(0, END)
            password_data.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by Alien 👽")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Data fields
website_data = Entry(width=52)
website_data.grid(column=1, row=1, columnspan=2)
website_data.focus()

email_data = Entry(width=52)
email_data.grid(column=1, row=2, columnspan=2)
email_data.insert(0, "mojmail@gmail.com")

password_data = Entry(width=33)
password_data.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
