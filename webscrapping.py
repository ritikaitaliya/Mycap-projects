import requests
from bs4 import BeautifulSoup

import time
start = time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get("https://www.insider.com/best-movies-to-watch-2017-4")

req.status_code
#print (req.status_code)

webpage = BeautifulSoup(req.content, 'html.parser')

data = webpage.find_all("h2", {"class":"slide-title-text"})
top_movies = data[0:50]

top_movies_data = []
for movies in top_movies:
  top_movies_data.append(movies.text)

def parse_movies(movies):
  return_dict = {}
  movies_data = movies.split(".")
  position = movies_data[0]
  movie = movies_data[1]
  return_dict["position"] = position
  return_dict["movie"] = movie
  return return_dict

top_movies = (list(map(parse_movies, top_movies_data)))
print (top_movies)

end = time.time()
print (f"time taken by the script to run {end-start}")
