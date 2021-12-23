# #100days of code - day 32 - Automated Birthday Wisher
import smtplib
import datetime as dt
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
MY_EMAIL = "alienttestowy@gmail.com"
PASSWORD = ""
LETTERS_LIST = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# ---------------------------- MAIN CODE ------------------------------- #
now = dt.datetime.now()
month = now.month
day = now.day

birthdays_data = pandas.read_csv("birthdays.csv")
# print(birthdays_data)
birthdays_dict = {row.first_name: row.email for (index, row) in birthdays_data.iterrows() if (row.month == month
                                                                                              and row.day == day)}
# print(birthdays_dict)

for name in birthdays_dict:
    name_to_send = name
    address_to_send = birthdays_dict[name]
    # print(f"{name_to_send} today is your birthday! I'll send you email to: {address_to_send}")

    file_name = random.choice(LETTERS_LIST)

    with open("letter_templates/"+file_name) as file:
        letter_content = file.read()
        letter_content = letter_content.replace("[NAME]", name_to_send)
    print(letter_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=address_to_send, msg=f"Subject:Happy Birthday!\n\n"
                                                                              f"{letter_content}")
