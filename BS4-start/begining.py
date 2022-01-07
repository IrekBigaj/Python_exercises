# #100days of code - day 45 - Web Scrapping Exercises
# Important data are stored in config.py
from bs4 import BeautifulSoup
# import lxml

with open("website.html", "r") as file:
    contents = file.read()

# print(contents)

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
print(soup.title.string)
# print(soup.a.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText() + " -> link:  " + tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")  # a tag sitting in p tag
print(company_url)

name = soup.select_one(selector="#name")  # hash sign for using id from HTML file - here id="name"
print(name)

headings = soup.select(".heading")
print(headings)
