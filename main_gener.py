import tmdbsimple as tmdb
import pprint
import requests
import json

tmdb.API_KEY = '8c643e62fa2e9201b30ef1f251603347'

tmdb.REQUESTS_SESSION = requests.Session()



genres = tmdb.Genres()
# movie_genres =  genres.movie_list()
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint (movie_genres)

tv_genres =  genres.tv_list()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint (tv_genres)
















# movie = tmdb.Movies()
# for x in range(1, 501):
#     response = movie.popular(language="hi", page=x, region="IN")
#     # pp.pprint (response)
# # pp.pprint(response.get("results"))
#     with open("/Users/vichi/Documents/tmdb/movie/popular_IN/tmdb_popular"+str(x)+".txt", 'w+') as outfile:
#         json.dump(response.get("results"), outfile)
# else:
#     print("complete")

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


# 54597
# 525946
# 74777
# 38570
# 28005
# 12819
# 1252
# 264568
# 21925
# 19042
# 23706
# 14585
# 14208
# 20483
# 13220
# 20697
# 1389
# 1251
# 541569
# 37088
# 520016
# 653729
# 51052
# 16725
# 20604
# 17483
# 20764
# 478860
