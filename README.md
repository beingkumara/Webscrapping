# Webscrapping

Summary of the Combined Codes:

1. TV Show Web Scraping:
   - The first part of the code scrapes TV show data from the "https://www.fmovies.ink/tv-show" webpage using BeautifulSoup and requests.
   - It extracts TV show titles and corresponding weblinks from the webpage and appends them to the "tv_show_second.txt" file with clear separators.

2. Movie Web Scraping and Searching:
   - The second part of the code scrapes movie data from the "https://fmovies.ink/" webpage.
   - It allows the user to input a movie name and search for the movie in the extracted data using regular expressions.
   - If the movie is found, its corresponding weblink is stored and opened using the web browser module.

3. Latest Movie Data Extraction:
   - The last part of the code extracts the details of the latest movie on the website from the specified section.
   - It saves the movie names, web links, and separators to the "end1.txt" file for further analysis.

Overall, the combined code demonstrates two different web scraping tasks: one for TV shows and the other for movies. The code showcases the ability to extract relevant data from web pages, organize it in files, and perform movie searches using regular expressions.
