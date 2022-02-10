""" System Module. """
#import os
import random
from flask import Flask, render_template
from tmdb import getmovie, getgenre
from wikimovie import wikisearch

app = Flask(__name__)

moviecount = []
favMovies = ["Thor Ragnarok", "creed II", "white chicks", "Iron Man 3", "Aladdin"]
for i in range(len(favMovies)):
    moviecount.append(i)

@app.route("/")
def index():
    """ dynamically generating the data and returning webpage data. """
    titles = []
    overviews = []
    photos = []
    websites = []
    counter = random.choice(moviecount)
    data = getmovie(favMovies[counter])
    websites.append(wikisearch(favMovies[counter]))
    genres = getgenre(data['movieid'])
    titles.append(data['titles'])
    overviews.append(data['overviews'])
    photos.append((data['photos']))
    return render_template(
        "index.html", websites = websites, genres = genres, 
        favImages = photos, titles = titles, overviews = overviews
    )

app.run(
#    host=os.getenv('IP', '0.0.0.0'),
#    port=int(os.getenv('PORT', 8080)),
    debug=True
)
