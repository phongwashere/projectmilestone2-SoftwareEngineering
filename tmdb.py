import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def getMovie(nameMovie):
    BASE_URL = "https://api.themoviedb.org/3/search/movie"
    API_KEY = os.getenv("API_KEY")

    params = {
    "api_key": API_KEY,
    "query": nameMovie,
    "page": 1
    }

    response = requests.get(BASE_URL, params = params)
    movies = response.json()
    data = movies['results']

    def get_title(info):
        return info['title']

    def get_overview(info):
        return info['overview']

    def get_photo(info):
        return info['poster_path']

    titles = map(get_title, data)
    overviews = map(get_overview, data)
    photos = map(get_photo, data)

    return{
        'titles': list(titles)[0:1],
        'overviews': list(overviews)[0:1],
        'photos': list(photos)[0:1]
    }
    #print("Title:", list(titles)[0:1], "\n")
    #print("Overview:", list(overviews)[0:1], "\n")
    #print("Photo:", list(photos)[0:1], "\n")

