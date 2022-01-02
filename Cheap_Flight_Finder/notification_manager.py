import smtplib
from config import *
from email.mime.text import MIMEText


class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, price, origin_city, origin_airport, destination_city, destination_airport, date_out, date_ret,
                   airline, link):
        self.price = price
        # self.departure = f"{origin_city}-{origin_airport}"
        self.departure = origin_airport
        # self.departure = MIMEText(f"{origin_city}-{origin_airport}", "plain", "utf-8").as_string()
        self.destination = f"{destination_city}-{destination_airport}"
        # self.destination = MIMEText(f"{destination_city}-{destination_airport}", "plain", "utf-8").as_string()
        # self.destination = destination_airport
        self.date_out = date_out
        self.date_ret = date_ret
        self.airline = airline
        self.link = link
        # print("Low price alert!")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Low price alert!!\n\nHey!\n"
                                                                           f"I've found flight with good price!\n"
                                                                           f"Only: {self.price} PLN to fly from: "
                                                                           f"{self.departure}, "
                                                                           f"to: {self.destination}, "
                                                                           f"from {self.date_out} to {self.date_ret}.\n"
                                                                           f"Flight by {self.airline}.\n"
                                                                           f"Link to booking: {self.link}"
                                                                           f"\n\n"
                                                                           f"Regards,\n\nAlien Soft"
                                )
