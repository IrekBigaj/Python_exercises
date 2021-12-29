# #100days of code - day 38 - Workout Tracker with Google Sheets
# Important data are stored in config.py
from config import *
import requests
from datetime import datetime
#from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
EXERCISES_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": NUT_APP_ID,
    "x-app-key": NUT_APP_KEY,
    "x-remote-user-id": "0",
}

HEADERS_SHHETY = {
    "Authorization": SHHETY_AUTH
}


# ---------------------------- MAIN SECTION ------------------------------- #

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

exercises = input("Tell me which exercises you did: ")

ex_data = {"query": exercises,
           "gender": GENDER,
           "weight_kg": WEIGHT_KG,
           "height_cm": HEIGHT_CM,
           "age": AGE
           }

print(ex_data)
exercises_response = requests.post(url=EXERCISES_ENDPOINT, json=ex_data, headers=HEADERS)
exercises_response.raise_for_status()
exercises_data = exercises_response.json()
exercises_data2 = exercises_data["exercises"]
print(exercises_data2)

for exercise in exercises_data2:
    to_save_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
      }
    sheety_response = requests.post(url=SHEETY_API_POST, json=to_save_data, headers=HEADERS_SHHETY)
    # sheety_response = requests.post(url=SHEETY_API_POST, json=to_save_data, headers=HEADERS_SHHETY)
    print(sheety_response.text)
