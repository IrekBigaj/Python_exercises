# #100days of code - day 45 - Web Scrapping - Movie List

from bs4 import BeautifulSoup
import requests

WEBPAGE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(WEBPAGE_URL)  # get data from specified URL
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_titles = []
for movie in all_movies:
    movie_title = movie.getText()
    # print(movie_title)
    movies_titles.append(movie_title)

top_100_movies = [movie for movie in movies_titles[::-1]]
# print(top_100_movies)

with open("movies_list.txt", "w") as file:
    for item in top_100_movies:
        file.write(f"{item}\n")

print("Finished -> open file and check data :)")
