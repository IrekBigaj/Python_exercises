import requests
from config import *
from flight_data import FlightData
# from pprint import pprint

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# CURR = "GBP"
CURR = "PLN"


# ---------------------------- CLASSES ------------------------------- #
class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURR
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:  # if there are any direct flights
            data = response.json()["data"][0]
        except IndexError:
            print(f"No direct flights found from {origin_city_code} to: {destination_city_code}.")
            new_query = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 14,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 2,
                "curr": CURR
            }

            new_response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=new_query,
            )

            print(new_response.status_code)
            print(new_response.json())
            try:
                new_data = new_response.json()["data"][0]
            except IndexError:
                print("No flights with 1 stopover found.")
            except:
                print("No flights found. Sorry.")
            else:
                print(new_data)
                new_flight_data = FlightData(
                    price=new_data["price"],
                    origin_city=new_data["route"][0]["cityFrom"],
                    origin_airport=new_data["route"][0]["flyFrom"],
                    destination_city=new_data["route"][1]["cityTo"],
                    destination_airport=new_data["route"][1]["flyTo"],
                    out_date=new_data["route"][0]["local_departure"].split("T")[0],
                    return_date=new_data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=new_data["route"][0]["cityTo"],
                    airline=new_data["airlines"][0],
                    link=new_data["deep_link"]
                    )
                return new_flight_data
        else:
            # print(response.json())
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                airline=data["airlines"][0],
                link=data["deep_link"]
            )

            return flight_data
