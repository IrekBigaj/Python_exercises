# #100days of code - day 33 - Exercises
import requests
from datetime import datetime

MY_LAT = 50.112107
MY_LONG = 20.102972

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")  # ISS Data
response_iss.raise_for_status()  # error msg if occur
iss_location_data = response_iss.json()["iss_position"]
iss_longitude = iss_location_data["longitude"]
iss_latitude = iss_location_data["latitude"]
iss_position = (iss_longitude, iss_latitude)
print(f"Long: {iss_longitude} Lat: {iss_latitude}")
print(iss_position)

parameters = {"lat": MY_LAT, "long": MY_LONG, "formatted": 0, }
response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)  # add parameters
response_sun.raise_for_status()
sun_data = response_sun.json()
sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour, sunset_hour)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)


