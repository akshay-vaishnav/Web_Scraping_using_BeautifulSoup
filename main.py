#here we are writing a program in which from a site we will scratch 100 movies name, we should watch.

import requests #use pip install requests
from bs4 import BeautifulSoup #use pip install beautifulsoup4

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]

# for n in range(len(movie_titles) - 1, -1, -1):#this will reverse the list but we will use another method.
#   print(movie_titles[n])

movies = movie_titles[::-1] #this will reverse the list

with open("movies.txt", mode="w", encoding="utf-8") as file:
  for movie in movies:
    file.write(f"{movie}\n") #here we are saving movie list in movies.txt file.
