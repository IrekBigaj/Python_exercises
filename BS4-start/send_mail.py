import smtplib
from config import *


class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, text, email_names=[(MY_EMAIL, "Irek")]):
        self.text = text
        self.email_names = email_names

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            # for email in emails:
            for item in email_names:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=item[0], msg=f"Subject:{item[1]} - top article to read!\n\n"
                                                                              f"Hi {item[1]},\n"
                                                                              f"{self.text}".encode('utf-8')

                                    )
