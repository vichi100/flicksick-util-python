import tmdbsimple as tmdb
import pprint
import requests
import json

tmdb.API_KEY = '8c643e62fa2e9201b30ef1f251603347'

tmdb.REQUESTS_SESSION = requests.Session()

pp = pprint.PrettyPrinter(indent=4)

movie = tmdb.Movies()
for x in range(1, 501):
    response = movie.popular(language="hi", page=x, region="IN")
    # pp.pprint (response)
# pp.pprint(response.get("results"))
    with open("/Users/vichi/Documents/tmdb/movie/popular_IN/tmdb_popular"+str(x)+".txt", 'w+') as outfile:
        json.dump(response.get("results"), outfile)
else:
    print("complete")

# // write data to file


# // read data to file
# with open('/Users/vichi/Documents/tmdb_popular.txt') as json_file:
#     data = json.load(json_file)
#     pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data)

# my_data_file = open('data.txt', 'w')


# >>> import pprint
# >>> pp = pprint.PrettyPrinter(indent=4)
# >>> pp.pprint(response)


# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

# python -m pip install pymongo --user 


# pip3 install nanoid

# https://www.themoviedb.org/documentation/api/wrappers-libraries
