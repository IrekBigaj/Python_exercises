# #100days of code - day 45 - Web Scrapping Exercises
# Important data are stored in config.py

from bs4 import BeautifulSoup
import requests
from send_mail import NotificationManager

notification_manager = NotificationManager()

WEBPAGE_URL = "https://news.ycombinator.com/news"
response = requests.get(WEBPAGE_URL)  # get data from specified URL
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")  # all links from the page
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    if "http" not in article_link:
        article_link = article_link.replace("item?", "https://news.ycombinator.com/item?")  # add prefix to internal pages
    article_links.append(article_link)
    # print(article_text + " https://news.ycombinator.com/"+article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
# print(largest_index)
mail_text = "Data from webpage: " + soup.title.string + " " + WEBPAGE_URL + "\n\n"
mail_text += f"Today most popular article is:\n{article_texts[largest_index]}\nlink: {article_links[largest_index]}\nwith {largest_number} votes."
mail_text += "\n\nBest regards,\nAlien Soft"

print(mail_text)
notification_manager.send_email(mail_text)

