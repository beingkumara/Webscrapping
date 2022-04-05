from bs4 import BeautifulSoup
import requests
web_pages = ["https://fmovies.hn/tv-show?page=2", "https://fmovies.hn/tv-show"]
for page in web_pages:
    web_request = requests.get(page).text

    bsoup = BeautifulSoup(web_request, 'lxml')

    tv_shows = bsoup.find('div', class_="film_list-wrap")
    tv_show = tv_shows.find_all('div', class_="flw-item")
    file = open("tv_show_second.txt", 'a+')
    file.write("TV SHOWS")
    file.write("\n")
    file.write("\n")
    for show in tv_show:
        title = show.a['title']
        file.write(title)
        file.write("\n")
        link = show.a['href']
        file.write(link)
        file.write("\n")
        file.write("-----------------------------------")
        file.write("\n")
        file.write("\n")
