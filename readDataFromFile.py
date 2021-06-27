import tmdbsimple as tmdb
import pprint
import requests
import json

# // read data to file
with open('/Users/vichi/Documents/tmdb/movie/popular_IN/tmdb_popular1.txt') as json_file:
    data = json.load(json_file)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data[0].get("id"))