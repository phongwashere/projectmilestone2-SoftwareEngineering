import os
import random
from flask import Flask, render_template
from tmdb import getMovie
from Wikiapi import wikiSearch

app = Flask(__name__)

amount = [0, 1, 2, 3]
favMovies = ["creed", "creed II", "white chicks", "howl's moving castle"]

@app.route("/")
def index():
    titles = []
    overviews = []
    photos = []
    i = random.choice(amount)
    data = getMovie(favMovies[i])
    titles.append(data['titles'])
    overviews.append(data['overviews'])
    photos.append((data['photos']))
    return render_template("index.html", favImages = photos, titles = titles, overviews = overviews)
#print(titles, '\n')
#print(overviews, '\n')
#print(photos, '\n')


app.run(
#    host=os.getenv('IP', '0.0.0.0'),
#    port=int(os.getenv('PORT', 8080)),
    debug=True
)
