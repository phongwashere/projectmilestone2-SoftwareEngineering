""" System Module. """
import requests

def wikisearch(moviename):
    """ Searches wiki for movie data. """
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"

    searchpage = moviename

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": searchpage
    }

    rsession = session.get(url=url, params=params)
    data = rsession.json()

    if data['query']['search'][0]['title'] == searchpage:
        print("Your search page '" + searchpage + "' exists on English Wikipedia")
