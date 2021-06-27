import os
import tmdbsimple as tmdb
import pprint
import requests
import json
import tmdbsimple as tmdb
import pprint
import requests
import json

tmdb.API_KEY = '8c643e62fa2e9201b30ef1f251603347'

tmdb.REQUESTS_SESSION = requests.Session()

pp = pprint.PrettyPrinter(indent=4)



fileList = os.listdir('/Users/vichi/Documents/tmdb/tv/popular_IN')
for file in fileList:
    
    if  not file.endswith('.txt'):
        continue
    with open('/Users/vichi/Documents/tmdb/tv/popular_IN/'+file) as json_file:
        print("file name: ", file)
        dataList = json.load(json_file)
        
        for data in dataList:
            tv = tmdb.TV(data.get("id"))
            response = tv.info()
            # pp.pprint(response)
            with open("/Users/vichi/Documents/tmdb/tv/tv_info_IN/"+file, 'a+') as outfile:
                json.dump(response, outfile)
            # pp.pprint(data.get("id"))
    os.remove('/Users/vichi/Documents/tmdb/tv/popular_IN/'+file);

        

# // read data to file
# with open('/Users/vichi/Documents/tmdb/movie/popular_IN/tmdb_popular1.txt') as json_file:
#     data = json.load(json_file)
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(data[0].get("id"))
