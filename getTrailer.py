import os
import tmdbsimple as tmdb
import pprint
import requests
import json
import tmdbsimple as tmdb
import pprint
import requests
import json
from bson.json_util import dumps
from bson.json_util import loads
from pymongo import MongoClient
pp = pprint.PrettyPrinter(indent=4)
tmdb.API_KEY = '8c643e62fa2e9201b30ef1f251603347'

tmdb.REQUESTS_SESSION = requests.Session()

try:
    client = MongoClient("mongodb+srv://vichi:vichi123@cluster0.3gcit.mongodb.net/flixsee?retryWrites=true&w=majority")
    print("Connected successfully!!!")
    movie_trailer_collection = client.flixsee.tv_trailer_us



    with open('/Users/vichi/Documents/tmdb/tv/tv_id_US.txt') as json_file:
        dataList = json.load(json_file)
        # pp.pprint(dataList)
        for x in dataList:
            # print(x)
            # movie = tmdb.Movies(x);
            # response = movie.videos();
            # movie_trailer_collection.insert_one(response);
            print(x)
            tv = tmdb.TV(x);
            response = tv.videos();
            movie_trailer_collection.insert_one(response);


            

    # results = [460465, 544401, 791373]
    # for result in results:
    #     pp.pprint(result)
    #     movie = tmdb.Movies(result);
    #     response = movie.videos();
    #     movie_trailer_collection.insert(response);
        
    # for name in client.list_database_names():  
    #     print(name)  

except x:  
    print(x)
    

# cd /Applications/Python\ 3.9/
# ./Install\ Certificates.command
    # collection = client.tmdbmovies
    # # collection = db.tmdbmovies
    # results = collection.find()
    # for result in results:
    #     pp.pprint(result)
    # dbs = client.list_database_names();
    # for db in dbs:
    #     print(db)

    # db = cluster["Cluster0"]
    # collection = db["flixsee"]
    # results = collection.tmdbmovies.find()
    # for result in results:
    #     pp.pprint(result)
    

# # db = client.flicksee
# # results = db.tmdbmovies.find()
# # for result in results:
# #     pp.pprint(result)

# # pp.pprint(loads(dumps(fivestar))):


# tmdb.API_KEY = '8c643e62fa2e9201b30ef1f251603347'

# tmdb.REQUESTS_SESSION = requests.Session()



# # movie = tmdb.Movies(460465);
# # response = movie.videos()
# # pp.pprint(response)

# with open('/Users/vichi/Documents/tmdb/movie/movie_id.txt') as json_file:
#     dataList = json.load(json_file)
#     # pp.pprint(dataList)
#     # for x in dataList:
#     #     print(x)

        


        #     booksData = [  
  
#       {  
#          "id":"01",  
#          "language": "Java",  
#          "edition": "third",  
#          "author": "Herbert Schildt"  
#       },  
  
#       {  
#          "id":"07",  
#          "language": "C++",  
#          "edition": "second",  
#          "author": "E.Balagurusamy"  
#       }  
#    ]  
    # collection.insert_many(booksData)
    # print(collection.find({}))
    # results = collection.find({})
    # print(results[0]["id"])