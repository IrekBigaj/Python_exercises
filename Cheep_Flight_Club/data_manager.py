import requests
from config import *
# from pprint import pprint

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
HEADERS_SHHETY = {
    "Authorization": SHHETY_AUTH
}


# ---------------------------- CLASSES ------------------------------- #
class DataManager:
    def __init__(self):
        self.destination_data = {}

    # for each city (iataCode) find cheapest flight from tomorrow to sixth month
    # if price is lower than stored in sheety for that city - notify me by email
    def get_destination_data(self):
        sheety_response = requests.get(url=SHEETY_API_GET, headers=HEADERS_SHHETY)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        # pprint(sheety_response.text)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_GET}/{city['id']}",
                json=new_data,
                headers=HEADERS_SHHETY
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_API_POST
        response = requests.get(url=customers_endpoint, headers=HEADERS_SHHETY)
        data = response.json()
        # print(data)
        self.customer_data = data["users"]
        return self.customer_data
