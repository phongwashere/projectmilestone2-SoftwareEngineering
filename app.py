import os
from flask import Flask, render_template
from tmdb import getMovie

app = Flask(__name__)

titles = []
overviews = []
photos = []
favMovies = ["creed", "creed II", "white chicks", "howl's moving castle"]



@app.route("/")
def index():
    for name in favMovies:
        data = getMovie(name)
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
