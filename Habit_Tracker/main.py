# #100days of code - day 37 - Habit Tracker
# Important data are stored in config.py
import requests
from config import *
from datetime import datetime

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{HABIT_USERNAME}/graphs"
GRAPH_ID = "graph1"
USER_PARAMS = {
    "token": HABIT_TOKEN,
    "username": HABIT_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

GRAPH_PARAMS = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

PIXEL_ENDPOINT = f"{USER_ENDPOINT}/{HABIT_USERNAME}/graphs/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": HABIT_TOKEN
}

# ---------------------------- MAIN SECTION ------------------------------- #
# Create user - https://docs.pixe.la/entry/post-user
# response = requests.post(url=USER_ENDPOINT, json=USER_PARAMS)
# print(response.text)
# https://pixe.la/@ib

# Create graph - https://docs.pixe.la/entry/post-graph
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
# print(graph_response.text)
# https://pixe.la/v1/users/ib/graphs/graph1.html

today = datetime.now().strftime("%Y%m%d")
# today = datetime(year=2021, month=12, day=28).strftime("%Y%m%d")
# print(today)

quantity = input("How many km did you walk today?: ")

pixel_params = {
    "date": today,
    "quantity": quantity,
}

# Create new pixel - https://docs.pixe.la/entry/post-pixel
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=HEADERS)
print(pixel_response.text)

# update_endpoint = f"{USER_ENDPOINT}/{HABIT_USERNAME}/graphs/{GRAPH_ID}/20211227"
# update_params = {
#     "quantity": "4.15",
# }

# Update existint pixe or create nwe one - https://docs.pixe.la/entry/put-pixel
# update_response = requests.put(url=update_endpoint, json=update_params, headers=HEADERS)
# print(update_response.text)

# Delete pixel - https://docs.pixe.la/entry/delete-pixel
# delete_endpoint = f"{USER_ENDPOINT}/{HABIT_USERNAME}/graphs/{GRAPH_ID}/20211227"

# delete_response = requests.delete(url=delete_endpoint, headers=HEADERS)
# print(delete_response.text)
