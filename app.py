""" System Module. """
import os
import random
import flask
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from tmdb import getmovie, getgenre
from wikimovie import wikisearch
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.secret_key = os.getenv('secretKey')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('db_url')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index2"

@login_manager.user_loader
def load_user(user_id):
    """ grabbing user_id to track """
    return userRating.query.get(int(user_id))

class userRating(db.Model, UserMixin):
    """ creating database """
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable=False, unique=True)

class reviews(db.Model):
    """ review database """
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    movieID = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(100), nullable=True)

db.create_all()

class RegisterForm(FlaskForm):
    """ creating a register form to sign up """
    username = StringField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Username"})
    submit = SubmitField("Register")
    def validate_username(self, username):
        """ raising validation errors """
        existing_user_username = userRating.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('User already exists. Please choose a different username.')

class LoginForm(FlaskForm):
    """ creating a login form to authentificate user """
    username = StringField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"placeholder": "Username"})
    submit = SubmitField("Login")

moviecount = []
favMovies = ["Thor Ragnarok", "creed II", "white chicks", "Iron Man 3", "Aladdin"]
for i in range(len(favMovies)):
    moviecount.append(i)

@app.route("/", methods=["GET", "POST"])
def index():
    """ route to show signup page """
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = userRating(username=form.username.data)
        db.session.add(new_user)
        db.session.commit()
        return flask.redirect(flask.url_for('index2'))
    if userRating.query.filter_by(username=form.username.data).first():
        flask.flash("User already exists. Please choose a different username.")
    return flask.render_template("signup.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def index2():
    """ route to show login page """
    form = LoginForm()
    if form.validate_on_submit():
        user = userRating.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return flask.redirect(flask.url_for('forum'))
        else:
            flask.flash("User does not exist")
    return flask.render_template("login.html", form=form)

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    """ logging the user out """
    logout_user()
    return flask.redirect(flask.url_for('index2'))

@app.route("/forum", methods=["GET", "POST"])
@login_required
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
    genre = genres['moviegenre']
    titles.append(data['titles'])
    overviews.append(data['overviews'])
    photos.append((data['photos']))
    return flask.render_template(
        "index.html", websites = websites, genres = genre,
        favImages = photos, titles = titles, overviews = overviews
    )

@app.route("/request", methods=["GET", "POST"])
@login_required
def rating():
    """ route to show movie search and ratings by user """
    try:
        data = flask.request.form
        movie = data['movieID']
        moviedata = getgenre(movie)
        movieinfo = getmovie(moviedata['titles'])
        titles = moviedata['titles']
        wiki = wikisearch(titles)
        overviews = moviedata['overviews']
        photos = movieinfo['photos']
        genres = moviedata['moviegenre']
        new_rating = reviews(username=current_user.username ,movieID=data['movieID'], rating=data['rating'], review=data['review'])
        db.session.add(new_rating)
        db.session.commit()
        rows = reviews.query.filter_by(movieID=movie).all()
        return flask.render_template('reviews.html',rows=rows, movie=movie,
        wiki = wiki, genres = genres, favImages = photos, titles = titles, overviews = overviews, websites = wiki
        )
    except:
        flask.flash("movieID does not exist. Please try again.")
        return flask.redirect(flask.url_for("forum"))

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
