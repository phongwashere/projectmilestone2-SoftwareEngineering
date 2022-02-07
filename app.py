import os
from flask import Flask
from tmdb import getMovie

app = Flask(__name__)

titles = []
overviews = []
photos = []
favMovies = ["creed", "creed II", "white chicks", "howl's moving castle"]

def index():
    for name in favMovies:
        data = getMovie(name)
        titles.append(data['titles'])
        overviews.append(data['overviews'])
        photos.append(data['photos'])

print(titles)

#app.run(
#    host=os.getenv('IP', '0.0.0.0'),
#    port=int(os.getenv('PORT', 8080)),
#    debug=True
#)
