""" System Module. """
import os
import random
import flask
from flask_sqlalchemy import SQLAlchemy
from tmdb import getmovie, getgenre
from wikimovie import wikisearch
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.secret_key = os.getenv('secretKey')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class userRating(db.Model):
    """ creating database """
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))

db.create_all()

moviecount = []
favMovies = ["Thor Ragnarok", "creed II", "white chicks", "Iron Man 3", "Aladdin"]
for i in range(len(favMovies)):
    moviecount.append(i)

@app.route("/", methods=["GET", "POST"])
def index():
    """ route to show signup page """
    return flask.render_template("signup.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """ signing up function """
    if flask.request.method == "POST":
        data = flask.request.form
        new_user = userRating(username=data["Username"])
        if userRating.query.filter_by(username=data["Username"]).first() is None:
            db.session.add(new_user)
            db.session.commit()
            return flask.redirect("/login")
        else:
            flask.flash("Username is taken")
        return flask.redirect("/")

@app.route("/login", methods=["GET", "POST"])
def index2():
    """ route to show login page """
    return flask.render_template("login.html")

@app.route("/login2", methods=["GET", "POST"])
def login():
    """ signing up function """
    if flask.request.method == "POST":
        data = flask.request.form
        if userRating.query.filter_by(username=data["Username"]).first() is not None:
            return flask.redirect("/forum")
        else:
            flask.flash("User does not exists")
        return flask.redirect("/login")

@app.route("/forum", methods=["GET", "POST"])
def forum():
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
    return flask.render_template(
        "index.html", websites = websites, genres = genres,
        favImages = photos, titles = titles, overviews = overviews
    )

@app.route("/request", methods=["GET", "POST"])
def rating():
    """ route to show movie search and ratings by user """
    return

app.run(
    #host=os.getenv('IP', '0.0.0.0'),
    #port=int(os.getenv('PORT', 8080)),
    debug=True
)
