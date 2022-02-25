""" System Module. """
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def getmovie(namemovie):
    """ grabbing movie data using tmdb api. """
    base_url = "https://api.themoviedb.org/3/search/movie"
    api_key = os.getenv("API_KEY")

    params = {
    "api_key": api_key,
    "query": namemovie,
    "page": 1
    }

    response = requests.get(base_url, params = params)
    movies = response.json()
    datas = movies['results']

    for data in datas[0:1]:
        return{
            'titles': data['title'],
            'overviews': data['overview'],
            'photos': data['poster_path'],
            'movieid': data['id']
        }

def getgenre(movieid):
    """ grabbing movie genre using tmdb api. """
    base_url = ("https://api.themoviedb.org/3/movie/"+str(movieid))
    api_key = os.getenv("API_KEY")

    params = {
    "api_key": api_key,
    }

    feedback = requests.get(base_url, params = params)
    genres = feedback.json()['genres']
    titles = feedback.json()['original_title']
    overviews = feedback.json()['overview']
    moviegenre = []
    for genre in genres:
        moviegenre.append(genre['name'])

    return {
        'moviegenre': moviegenre,
        'titles': titles,
        'overviews': overviews
    }
    
