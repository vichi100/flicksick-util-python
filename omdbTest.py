from omdb import OMDBClient
import json
import pprint
from pymongo import MongoClient

pp = pprint.PrettyPrinter(indent=4)
clientOMDB = OMDBClient(apikey='5ba2f7bc')
count = 0;
try:

    client = MongoClient('mongodb+srv://vichi:vichi123@cluster0.emt5x.mongodb.net/flicksick_india?retryWrites=true&w=majority')
    print("Connected successfully!!!")
    movie = client.flicksick_india.movies
    for x in movie.find({}):
        pp.pprint(x['imdb_id'])
        imdb_id = x['imdb_id']
        omdbData = clientOMDB.imdbid(imdb_id, fullplot=True, tomatoes=True);
        if omdbData:
            movie.update_many({'imdb_id':imdb_id}, {"$set": {"ratings": omdbData["ratings"]}}, upsert=False)
        else:
            movie.update_many({'imdb_id':imdb_id}, {"$set": {"ratings": []}}, upsert=False)
        # pp.pprint(omdbData["ratings"])
        pp.pprint(count)
        count = count+1;
        
except x:
    print(x)

# {"imdb_id": "tt14476720"}