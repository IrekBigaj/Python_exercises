# #100days of code - day 36 - Stock Price News Project
# Important data are stored in config.py
import requests
import smtplib
from config import *

# ---------------------------- CONSTANTS AND GLOBALS ------------------------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"  # https://www.alphavantage.co/documentation/
STOCK_API_PARAMETERS = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": ALPHA_API_KEY,
    }

NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_PARAMETERS = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

stock_data = ""


# ---------------------------- FUNCTIONS ------------------------------- #
def send_email(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:{STOCK} price info\n\n"
                                                                       "Hey!\n"
                                                                       f"{msg}\n"
                                                                       "Regards,\n"
                                                                       "Alien Soft"
                            )


def check_and_store_data():
    """Check stock data for give stock"""
    stock_response = requests.get(STOCK_API_ENDPOINT, params=STOCK_API_PARAMETERS)
    # stock_response = requests.get("https://www.alphavantage.co/query", params={"function": "TIME_SERIES_DAILY",
    # "symbol": "IBM", "apikey": "demo"})
    stock_response.raise_for_status()
    # print(response.status_code)
    global stock_data
    stock_data = stock_response.json()
    # print(stock_data)
    # data_list = [value for (key, value) in data.items()]  # alternative way to convert to list


def analyze_data():
    check_and_store_data()
    price_data = {}
    daily_data = stock_data["Time Series (Daily)"]
    for day in daily_data:
        # print(day)
        # print(daily_data[day]["4. close"])
        price_data[day] = float(daily_data[day]["4. close"])
    # print(price_data)
    # print(list(price_data.values()))
    last_closed_price = list(price_data.values())[0]
    last_closed_day = list(price_data.keys())[0]
    previous_closed_price = list(price_data.values())[1]
    previous_closed_day = list(price_data.keys())[1]
    diff_price = last_closed_price - previous_closed_price
    diff_percent = diff_price/previous_closed_price * 100
    # print(diff_percent)
    if diff_percent > 0:
        return f"UP {round(abs(diff_percent))}% from: {previous_closed_price} ({previous_closed_day}) to: " \
               f"{last_closed_price} ({last_closed_day})"
    else:
        return f"DOWN {round(abs(diff_percent))}% from: {previous_closed_price} ({previous_closed_day}) to: " \
               f"{last_closed_price} ({last_closed_day})"


def find_news():
    """Check news about company and return string with 3 hot news"""
    news_package = ""
    news_response = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMETERS)
    news_response.raise_for_status()
    # print(response.status_code)
    news_data = news_response.json()
    for i in range(0, 3):
        # print("Headline: " + news_data["articles"][i]["title"] + "\nBrief: " +
        # news_data["articles"][i]["description"])
        news_package += ("Headline: " + news_data["articles"][i]["title"] + "\nLink: " +
                         news_data["articles"][i]["url"] + "\n\n")
        # news_package += ("Headline: " + news_data["articles"][i]["title"] + "\n\n")

    # print(news_package)
    return news_package


# ---------------------------- MAIN SECTION ------------------------------- #
msg_to_send = f"{STOCK} {analyze_data()}\n{find_news()}"
print(msg_to_send)
send_email(msg_to_send)
