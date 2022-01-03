import smtplib
from config import *


class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, price, origin_city, origin_airport, destination_city, destination_airport, date_out, date_ret,
                   airline, link, emails, emails_names, add_msg=""):
        self.price = price
        self.departure = f"{origin_city}-{origin_airport}"
        #self.departure = origin_airport
        self.destination = f"{destination_city}-{destination_airport}"
        self.date_out = date_out
        self.date_ret = date_ret
        self.airline = airline
        self.link = link
        self.add_msg = add_msg
        self.emails = emails
        self.emails_names = emails_names
        # print("Low price alert!")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            # for email in emails:
            for item in emails_names:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=item[0], msg=f"Subject:Low price alert!!\n\n"
                                                                              f"Hey {item[1]}!\n"
                                                                              f"I've found flight with good price!\n"
                                                                              f"Only: {self.price} PLN to fly from: "
                                                                              f"{self.departure}, "
                                                                              f"to: {self.destination}, "
                                                                              f"from {self.date_out} to "
                                                                              f"{self.date_ret}.\n"
                                                                              f"Flight by {self.airline} airlines.\n"
                                                                              f"{self.add_msg}\n"
                                                                              f"Link to booking: {self.link}"
                                                                              f"\n\n"
                                                                              f"Have a nice flight,\n\n"
                                                                              f"Alien Soft".encode('utf-8')
                                    )
