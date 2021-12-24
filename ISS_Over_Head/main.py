# #100days of code - day 33 - ISS over head detector

import requests
from datetime import datetime
import smtplib
import time

# ---------------------------- CONSTANTS ------------------------------- #
MY_LAT = 50.112107
MY_LONG = 20.102972
MY_EMAIL = "alienttestowy@gmail.com"
PASSWORD = ""
PAUSE = 6  # 60 seconds

# ---------------------------- MAIN FUNCTIONS ------------------------------- #


def iss_is_over_head():
    """Returns True if ISS is over my head"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True
    else:
        return False


def is_dark():
    """Returns True if in my location is dark"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now <= sunrise or hour_now >= sunset:
        return True
    else:
        return False


def send_email_to_me():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up! 👆 ISS over your head!\n\n"
                                                                       "Hey!\n"
                                                                       "ISS is over your head! 👆\n\n"
                                                                       "Regards,\n\n"
                                                                       "Alien Soft"
                            )


# ---------------------------- PROGRAM ------------------------------- #
# FOREVER LOOP to check every 60 sec and send mail
while True:
    if is_dark() and iss_is_over_head():
        print('Watch ISS over your head! 👆')
        send_email_to_me()
    else:
        print("Sorry. Not now. Is dark?: " + str(is_dark()) + ". Is ISS near me?: " + str(iss_is_over_head()))

    time.sleep(PAUSE)  # 60 sec pause
