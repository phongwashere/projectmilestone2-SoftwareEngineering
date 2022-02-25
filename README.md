If you want to clone my repository, there are a couple steps you will have to do.
## NOTE : All installations are required to run the code on your local machine
## link:
https://project1-softwareengineering.herokuapp.com/

## In your terminal:
1. Install pip in your terminal
2. Install flask
3. Install python3-dotenv
4. Install requests
4. Go to the developer website for imdb and request an 'API_KEY'
## The API_KEY is how imdb will authorize each session
5. Create a .env file in the same respository as the .gitignore
6. Inside the .env file you will want to type out this line:

export API_KEY = $your api key$

## More required installation
7. Install PostgreSQL using these steps (you may run into some errors depending on your system):

brew install postgresql
brew services start postgresql
psql -h localhost  
# this is just to test out that postgresql is installed okay - type "\q" to quit
# if the above command gives you an error like "database <user> does not exist," try the workaround in this link: https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy==2.1


## we now need to setup a heroku database to store all of your information
8. to edit or create apps from heroku we need to login to your account using:

heroku login

9. create a new app with:

heroku create

10. creating a new database

heroku addons:create heroku-postgresql:hobby-dev 
# If that doesn't work, add a -a {your-app-name} to the end of the command, with no braces

11. use this command to show your DATABASE_URL and copy it

heroku config

12. in your .env file, you will need to add:

export DATABASE_URL='$your DATABASE_URL'
# make sure to use " or ' to enclose your DATABASE_URL

13. also make sure that your DATABASE_URL starts with postgresql: instead of postgres:

## Be sure to replace the $$$$ as well
14. Change the directory of your terminal to the repository of the app if you have not already
15. Run python app.py or python3 app.py


## project differed from expectations:
    ~ The project definitely differed from the planning when it came to the actual implementation. A lot of incorporating things like flask-login came with a lot of hurdles. I also struggled with learning how to query tables from flask-SQLAlchemy. Learning from those two components was the only real hurdle I experienced. While planning, everything sounded easy to do, quickly, and simply, but the actual implementation was the hard part.


## Some techinical issues that I came across:
    ~ an issue I have with my milestone was implementing flask-login with code that already had a login system.
        ~ I had to learn how to replace the code that needed to be replaced and how to properly implement this new library to be used efficiently
    ~ another issue I came across was actually taking in reviews and ratings and adding them to tables in the database along with the current_user.
        ~ of course solving that was much easier than it had seemed. I had to manually set the variables inside the reviews table and then add and commit the table.


## we are using flask as our web app framework. libraries such as dotenv are used to grab our .env file. os and random are also other important libraries that we used in our web application. We are now also implementing Flask-SQLAlchemy for our database and flask-login for our authentification.
