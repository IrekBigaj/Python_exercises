# #100days of code - day 32 - Exercises - Motivational Quote Mailer
import smtplib
import datetime as dt
import random

# ---------------------------- CONSTANTS ------------------------------- #
MY_EMAIL = "alienttestowy@gmail.com"
PASSWORD = ""
RECIPIENT_EMAIL = "alientestowy@op.pl"

# ---------------------------- MAIN CODE ------------------------------- #

now = dt.datetime.now()
year = now.year
day_of_week = now.isoweekday()  # monday is 1
if day_of_week == 4:
    print(f"Today is {day_of_week}th day of week!")
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        # print(quotes)

        for x in range(0, len(quotes)):
            quotes[x] = quotes[x].strip()
        # print(quotes)

    quote_of_day = random.choice(quotes)
    print(quote_of_day)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure connection
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL, msg="Subject:Motivational quote for today!"
                                                                              "\n\n"
                                                                              f"{quote_of_day}\n"
                                                                              "Best wishes\n AlienSoft")

# ---------------------------- OTHER EXERCISES ------------------------------- #

# import smtplib
# MY_EMAIL = "alienttestowy@gmail.com"
# PASSWORD = "L2fzMrC6y51cqu2eyjW5"
# RECIPIENT_EMAIL = "alientestowy@op.pl"
# # connection = smtplib.SMTP("smtp.gmail.com")  # location of STMP server
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # secure connection
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL, msg="Subject:Hello from Python again\n\n"
#                                                                           "Hello from Python code.\n"
#                                                                           "Best wishes\n"
#                                                                           "IB")
# connection.close()  # alternative method with ... as ....

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1974, month=1, day=1, hour=10, minute=13)
# print(date_of_birth)
