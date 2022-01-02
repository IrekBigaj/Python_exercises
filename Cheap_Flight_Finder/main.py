# #100days of code - day 39-40 - Flight Finder

from data_manager import DataManager
# from pprint import pprint
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
# ORIGIN_CITY_IATA = "LON"
ORIGIN_CITY_IATA = "KRK"

price = 0
origin_city = "Departure"
origin_airport = "Airport"
destination_city = "Destination"
destination_airport = "Airport"
date_out = "YYYY-MM-DD"
date_ret = "YYYY-MM-DD"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# ---------------------------- MAIN SECTION ------------------------------- #
data_manager = DataManager()
sheety_data = data_manager.get_destination_data()
# pprint(sheety_data)

flight_search = FlightSearch()
notification_manager = NotificationManager()


# checking iata code and if empty - insert proper value
if sheety_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheety_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheety_data}")

    data_manager.destination_data = sheety_data
    data_manager.update_destination_codes()


# checking flights for each destination
for destination in sheety_data:
    flight = flight_search.check_flights(
        # ORIGIN_CITY_IATA,
        destination["iataFrom"],
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None:

        if flight.price < destination["lowestPrice"]:
            print(f"{flight.origin_airport} to {flight.destination_city}: {flight.price}PLN - Out: {flight.out_date} "
                  f"Return: {flight.return_date}")
            notification_manager.send_email(
                price=flight.price,
                origin_city=flight.origin_city,
                origin_airport=flight.origin_airport,
                destination_city=flight.destination_city,
                destination_airport=flight.destination_airport,
                date_out=flight.out_date,
                date_ret=flight.return_date,
                airline=flight.airline,
                link=flight.link
            )
