import requests

def wikiSearch(movieName):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    SEARCHPAGE = "Nelson Mandela"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": SEARCHPAGE
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    if DATA['query']['search'][0]['title'] == SEARCHPAGE:
        ("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")