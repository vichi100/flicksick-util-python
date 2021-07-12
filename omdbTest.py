from omdb import OMDBClient
import json
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

pp = pprint.PrettyPrinter(indent=4)
clientOMDB = OMDBClient(apikey='5ba2f7bc')
count = 0;
try:

    # client = MongoClient('mongodb+srv://vichi:vichi123@cluster0.emt5x.mongodb.net/flicksick_india?retryWrites=true&w=majority')
    client = MongoClient('mongodb://flicksick:flicksick123@209.145.57.26:27017/?authSource=flicksick_india&compressors=disabled&gssapiServiceName=mongodb')
    
    print("Connected successfully!!!")
    movie = client.flicksick_india.movies
    # movieData = movie.find().sort([("_id", 1)])
    movieData = movie.find({"_id": {"$lt": ObjectId('60eb35f489c12b98a06ac750')}}).sort([("_id", 1)])
    
    for x in movieData:
        try: 
            pp.pprint(x['imdb_id'])
            pp.pprint(x['_id'])
            imdb_id = x['imdb_id']
            omdbData = clientOMDB.imdbid(imdb_id, fullplot=True, tomatoes=True);
            if omdbData:
                movie.update_many({'imdb_id':imdb_id}, {"$set": {"ratings": omdbData["ratings"]}}, upsert=False)
            # else:
            #     movie.update_many({'imdb_id':imdb_id}, {"$set": {"ratings": []}}, upsert=False)
            # pp.pprint(omdbData["ratings"])
            pp.pprint(count)
            count = count+1;
        except Exception as  err:
            print(err)
        
except Exception as e:
    print(e)

# {"imdb_id": "tt14476720"}