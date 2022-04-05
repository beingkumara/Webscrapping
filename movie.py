from bs4 import BeautifulSoup
import requests


web_read = requests.get("https://fmovies.hn/home").text
bsoup = BeautifulSoup(web_read, 'lxml')

trend_movies = bsoup.find('div', class_="tab-pane active")


movie_fin = trend_movies.find('div', class_="film_list-wrap")
movie_fins = movie_fin.find_all('h3', class_="film-name")
file = open("D:\WEBSCRAPE\end.txt", 'w')
for movie in movie_fins:
    file.write(movie.text)
    file.write("\n")
    s = "fmovies.hn" + movie.a['href']
    file.write(s)
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")


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
