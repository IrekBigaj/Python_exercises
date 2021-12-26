# #100days of code - day 35 - Rain Alert App
# Important data are stored in config.py
import requests
import smtplib
from config import *

# ---------------------------- CONSTANTS ------------------------------- #
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"  # https://openweathermap.org/api/one-call-api
API_PARAMETERS = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
    }

weather_data = ""
weather_cond_forecast = []
will_rain = False


# ---------------------------- FUNCTIONS ------------------------------- #
def send_email():
    # print("☂️Take your umbrella! It will be raining today :(")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Take your umbrella!\n\n"
                                                                       "Hey!\n"
                                                                       "Take your umbrella!\n"
                                                                       "It will be raining today in next 12 hours!\n\n"
                                                                       "Regards,\n\n"
                                                                       "Alien Soft"
                            )


def check_forecast():
    """Check 24h forecast for configured location"""
    response = requests.get(OWM_API_ENDPOINT, params=API_PARAMETERS)
    response.raise_for_status()
    # print(response.status_code)
    global weather_data
    weather_data = response.json()


def is_it_raining():
    check_forecast()
    for i in range(0, 11):  # for next 12 hours
        global weather_cond_forecast
        global will_rain
        condition_code = weather_data["hourly"][i]["weather"][0]["id"]
        weather_cond_forecast.append(condition_code)
        if int(condition_code) < 700:
            will_rain = True

    if will_rain:
        send_email()

    # print(weather_cond_forecast)


# ---------------------------- MAIN SECTION ------------------------------- #
is_it_raining()
