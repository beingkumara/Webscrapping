# Webscrapping
Web scrapped the Fmovies website

Library Used:
BeautifulSoup - Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

We need the 'requests' framework to connect with the server.

1. movie.py: It contains the code that extracts the movie data from the home page
  a. It writes the output to two different files.
  b. end.txt -> It has the movies which are classified as "Trending"
  c. end1.txt -> It has the movies which are classified as "Latest"

2. show.py: It contains the code that extracts the TV Show data from two different web pages
  a. It writes the output to a single file.
  b. The code 2 webpages stored in a list. Each time the loop runs, the webpage is changed.
  c. tv_show_second.txt -> It stores the entire TV Show information in it.
