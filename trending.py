
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
};

try:
    # TMDB get trending -START
    trendingArray = [
'movie/497698', 'movie/588228',
  'movie/520763', 'tv/84958',
  'movie/508943', 'movie/591273',
  'movie/591274', 'movie/459151',
  'tv/110642',    'movie/385128',
  'movie/423108', 'movie/649409',
  'movie/337404', 'movie/522478',
  'movie/522931', 'movie/399566',
  'movie/646207', 'movie/460465',
  'movie/529106', 'tv/60625',
  'movie/615457', 'movie/672741',
  'tv/126280',    'movie/602734',
  'movie/641501', 'tv/90461',
  'movie/846214', 'movie/346687',
  'movie/637693', 'movie/637649',
  'movie/447332', 'movie/791568',
  'movie/774714', 'movie/791373',
  'movie/607259', 'movie/527774',
  'movie/739542', 'movie/299534',
  'movie/736073', 'movie/800497',
  'movie/581726', 'movie/760873',
  'movie/604360', 'tv/76669',
  'tv/95249',     'movie/467909',
  'movie/458576', 'movie/602063',
  'movie/588921', 'tv/105971',
  'tv/37854',     'tv/96677',
  'tv/1399',      'tv/71578',
  'movie/412656', 'movie/550205',
  'movie/632357', 'movie/691179',
  'tv/60735',     'movie/379686'
]

    # TMDB get trending -END
    # client = MongoClient('mongodb+srv://vichi:vichi123@cluster0.emt5x.mongodb.net/flicksick_india?retryWrites=true&w=majority')
    client = MongoClient('mongodb://flicksick:flicksick123@209.145.57.26:27017/?authSource=flicksick_india&compressors=disabled&gssapiServiceName=mongodb')
    
    print("Connected successfully!!!")
    movie = client.flicksick_india.tmdb_trendings

    url = "https://streaming-availability.p.rapidapi.com/get/basic"

    headers = {
    'x-rapidapi-key': "03fe41fbaamsh36e3caed36bbea5p18c791jsndbf3b6fe4482",
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
    }

    for x in trendingArray:
        time.sleep(1)
        querystring = {"country":"in","tmdb_id":x}
        response = requests.request("GET", url, headers=headers, params=querystring)
        pp.pprint(response.text)
        if "no records are found" in response.text: 
            continue
        item = json.loads(response.text)
        # pp.pprint(x)
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
        
        mediaType = "movie"
        for trendingId in trendingArray:
            if(item["tmdbID"] in trendingId):
                if("tv" in trendingId):
                    mediaType = "series"
                elif ("movie" in trendingId):
                    mediaType = "movie"
            

        runtime = None
        if "runtime" in item:
            runtime = item["runtime"]
        else:
            runtime = None

        movie_dict ={
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
            "runtime": runtime,
            "spoken_languages": [ item["originalLanguage"] ],
            "status": None,
            "tagline": item["tagline"],
            "title": item["title"],
            "trailer": item["video"],
            "cast": item["cast"],
            "category": None, 
            "media_type": mediaType, 
            "fs_rating": {
                "loved_it": 0,
                "dumb_but_entertaining": 0,
                "just_time_pass": 0,
                "worthless": 0,
                "total_votes": 0
            },
            "ratings":[]
        }
		 
        movie.insert_one(movie_dict);
        
        # dataList = x["results"]
        # pp.pprint(len(dataList))
        
        
        # for item in dataList:
        #     # pp.pprint(item)
        #     genresArray = item["genres"]
        #     # pp.pprint(genresArray)
        #     genresObjArray = []
        #     for gen in genresArray:
        #         value = genresX[str(gen)]
        #         genresObj={
        #             "id": gen,
        #             "name": value
        #         }
        #         genresObjArray.append(genresObj)
			
        #     movie_dict = {
		# 			"fs_id": generate(),
		# 			"tmdb_id": item["tmdbID"],
		# 			"tmdb_rating": item["tmdbRating"],
		# 			"tmdb_vote_count": None,
		# 			"age": item["age"],
		# 			"adult": False,
		# 			"backdrop_path": item["backdropPath"],
		# 			"backdrop_urls": item["backdropURLs"],
		# 			"belongs_to_collection": None,
		# 			"budget": None,
		# 			"genres": genresObjArray,
		# 			"homepage": None,
		# 			"imdb_id": item["imdbID"],
		# 			"imdb_rating": item["imdbRating"],
		# 			"imdb_vote_count": item["imdbVoteCount"],
		# 			"rotten_tomatoes_rating": None,
		# 			"streaming_info": item["streamingInfo"],
		# 			"original_language": item["originalLanguage"],
		# 			"original_title": item["originalTitle"],
		# 			"overview": item["overview"],
		# 			"poster_urls": item["posterURLs"],
		# 			"poster_path": item["posterPath"],
		# 			"release_date": item["year"],
		# 			"revenue": None,
		# 			"runtime": None,
		# 			"spoken_languages": [ item["originalLanguage"] ],
		# 			"status": None,
		# 			"tagline": item["tagline"],
		# 			"title": item["title"],
		# 			"trailer": item["video"],
		# 			"cast": item["cast"],
		# 			"category": None, 
		# 			"media_type": 'series', 
        #             "fs_rating": {
		# 				"loved_it": 0,
		# 				"dumb_but_entertaining": 0,
		# 				"just_time_pass": 0,
		# 				"worthless": 0,
		# 				"total_votes": 0
		# 			}
		# 		};
        #     movie.insert_one(movie_dict);
            
        
        # pp.pprint(len(x["results"]))
        # print(x)
        
except x:  
    print(x)








