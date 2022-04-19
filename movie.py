# importing the required modules
from bs4 import BeautifulSoup
import webbrowser
import requests
import re

# accessing the website
web_read = requests.get("https://fmovies.hn/home").text
bsoup = BeautifulSoup(web_read, 'lxml')

# reading the webpage.
trend_movies = bsoup.find('div', class_="tab-pane active")

# asking the user for the required movie.
movie_name = input("Enter the movie name: ")


movie_fin = trend_movies.find('div', class_="film_list-wrap")
movie_fins = movie_fin.find_all('h3', class_="film-name")

# initialising a dictionary to access the weblink of the required movie in the further process.
movie_dict = {}

# opening a file to write the extracted details into it.
file = open("D:\WEBSCRAPE\end.txt", 'w')
for movie in movie_fins:
    x = movie.text.replace('\n', '')
    file.write(x)

    file.write("\n")

    s = "fmovies.hn" + movie.a['href']
    x = x.lower()
    movie_dict[x] = s
    file.write("\n")
    file.write(s)
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")

# Function that checks if the movie is in the extracted data or not


def get_movie(name, movie_dict):
    for i in movie_dict:
        if(re.search(name, i) != None):
            return movie_dict[i]
    return 0


# If the movie is present then the hyperlink to the movie is being stored
link = get_movie(movie_name, movie_dict)
print(link)
# Opening the hyperlink.
webbrowser.open(link)

latest_movies = bsoup.find(
    'section', class_='block_area block_area_home section-id-02')


movie_fin = latest_movies.find('div', class_="film_list-wrap")
movie_fins = movie_fin.find_all('h3', class_="film-name")
file1 = open("D:\WEBSCRAPE\end1.txt", 'w')
for movie in movie_fins:
    file1.write(movie.text)
    file1.write("\n")
    s = "fmovies.hn" + movie.a['href']
    file1.write(s)
    file1.write("\n")
    file1.write("-----------------------------------")
    file1.write("\n")
