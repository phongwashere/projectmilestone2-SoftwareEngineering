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

## Be sure to replay the $$$$ as well
7. Change the directory of your terminal to the repository of the app if you have not already
8. Run python app.py or python3 app.py


## Additional features I would like to add are:
    ~ To have a user input a title of a film of their choice to have its information displayed
    ~ To be able to play trailers


## Some techinical issues that I came across:
    ~ Having to find a way to grab the url from mediawiki after obtaining the pageid
        I solved that by using a generic search url for wikipedia and attaching the pageid to it
    ~ Figuring out a good way to randomize the movie being displayed
        I solved this by creating a list of numbers that contained the same amount of numbers
        as there were films. I then used the random library to randomly select a number within
        that list and display that movie.
    ~ The most recent issue I've come across is a keyError after deploying my web app to heroku
        I solved this by making sure my API_KEYs for my third party APIs are all included in the heroku variable config file.


## we are using flask as our web app framework. libraries such as dotenv are used to grab our .env file. os and random are also other important libraries that we used in our web application.
