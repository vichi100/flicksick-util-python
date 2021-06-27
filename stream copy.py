from pymongo import MongoClient
from nanoid import generate
import json
import pprint
import requests
import time

pp = pprint.PrettyPrinter(indent=4)
genresX = {
	'1': 'Biography',
	'2': 'Film Noir',
	'3': 'Game Show',
	'4': 'Musical',
	'5': 'Sport',
	'6': 'Short',
	'7': 'Adult',
	'12': 'Adventure',
	'14': 'Fantasy',
	'16': 'Animation',
	'18': 'Drama',
	'27': 'Horror',
	'28': 'Action',
	'35': 'Comedy',
	'36': 'History',
	'37': 'Western',
	'53': 'Thriller',
	'80': 'Crime',
	'99': 'Documentary',
	'878': 'Science Fiction',
	'9648': 'Mystery',
	'10402': 'Music',
	'10749': 'Romance',
	'10751': 'Family',
	'10752': 'War',
	'10763': 'News',
	'10764': 'Reality',
	'10767': 'Talk Show'
}

try:
    client = MongoClient('mongodb+srv://vichi:vichi123@cluster0.emt5x.mongodb.net/flicksick_india?retryWrites=true&w=majority')
    print("Connected successfully!!!")
    movie = client.flicksick_india.movies

    url = "https://streaming-availability.p.rapidapi.com/search/ultra"
    headers = {
    'x-rapidapi-key': "03fe41fbaamsh36e3caed36bbea5p18c791jsndbf3b6fe4482",
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
    }

    for x in range(1,87):
        time.sleep(1)
        querystring = {"country":"in","services":"prime,netflix","type":"series","order_by":"year","page":x,"desc":"true"}
        pp.pprint("page: "+str(x))
        response = requests.request("GET", url, headers=headers, params=querystring)
        x = json.loads(response.text)
        dataList = x["results"]
        pp.pprint(len(dataList))
        for item in dataList:
            # pp.pprint(item)
            genresArray = item["genres"]
            # pp.pprint(genresArray)
            genresObjArray = []
            for gen in genresArray:
                value = genresX[str(gen)]
                genresObj={
                    "id": gen,
                    "name": value
                }
                genresObjArray.append(genresObj)
			
            movie_dict = {
					"fs_id": generate(),
					"tmdb_id": item["tmdbID"],
					"tmdb_rating": item["tmdbRating"],
					"tmdb_vote_count": None,
					"age": item["age"],
					"adult": False,
					"backdrop_path": item["backdropPath"],
					"backdrop_urls": item["backdropURLs"],
					"belongs_to_collection": None,
					"budget": None,
					"genres": genresObjArray,
					"homepage": None,
					"imdb_id": item["imdbID"],
					"imdb_rating": item["imdbRating"],
					"imdb_vote_count": item["imdbVoteCount"],
					"rotten_tomatoes_rating": None,
					"streaming_info": item["streamingInfo"],
					"original_language": item["originalLanguage"],
					"original_title": item["originalTitle"],
					"overview": item["overview"],
					"poster_urls": item["posterURLs"],
					"poster_path": item["posterPath"],
					"release_date": item["year"],
					"revenue": None,
					"runtime": None,
					"spoken_languages": [ item["originalLanguage"] ],
					"status": None,
					"tagline": item["tagline"],
					"title": item["title"],
					"trailer": item["video"],
					"cast": item["cast"],
					"category": None, 
					"media_type": 'series', 
                    "fs_rating": {
						"loved_it": 0,
						"dumb_but_entertaining": 0,
						"just_time_pass": 0,
						"worthless": 0,
						"total_votes": 0
					}
				};
            movie.insert_one(movie_dict);
            
        
        # pp.pprint(len(x["results"]))
        # print(x)
        
except x:  
    print(x)









# pp.pprint(response.text)



# insert in mongodb




# print(response.text)