import requests
from config import *

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
HEADERS_SHHETY = {
    "Authorization": SHHETY_AUTH
}


# ---------------------------- CLASSES SECTION ------------------------------- #

class Customer:
    def __init__(self):
        pass

    def add_new(self):
        print("Welcome to Alien Flight Club.")
        print("We find the cheapest flight deals and email you.")
        self.first_name = input("What is your first name?\n")
        self.second_name = input("What is your last name?\n")
        self.email = input("What is your email?\n")
        self.verify_email = input("Type your email again:\n")
        if self.email == self.verify_email:
            to_save_data = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.second_name,
                    "email": self.email
                }
            }
            sheety_response = requests.post(url=SHEETY_USERS_API_POST, json=to_save_data, headers=HEADERS_SHHETY)
            # print(sheety_response.status_code)
            # print(sheety_response.text)
            if sheety_response.status_code == 200:
                print("Now you're in the club!")
                return True
            else:
                print(f"Sorry, something goes wrong with code: {sheety_response.status_code}. Try again later.")
                return False
        else:
            print("Sorry, incorrect email address. Correct email address and try again.")
            return False


new_customer = Customer()
# check for errors and if not succeeded ask for data again
if not new_customer.add_new():
    new_customer.add_new()
else:
    pass
