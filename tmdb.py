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
    datas = movies['results']

    for data in datas[0:1]:
        return{
            'titles': data['title'],
            'overviews': data['overview'],
            'photos': data['poster_path']
        }
    #print("Title:", list(titles)[0:1], "\n")
    #print("Overview:", list(overviews)[0:1], "\n")
    #print("Photo:", list(photos)[0:1], "\n")

