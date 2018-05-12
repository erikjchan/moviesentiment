import datetime
import json
import requests
import time
import urllib3

request_url = 'https://api.themoviedb.org/3/'
genres_url = 'genre/movie/list?api_key='
movie_id = 1
credits_url = 'movie/{movie_id}/credits?api_key='
details_url = 'movie/{movie_id}?api_key='
api_key = '06709af3621440ead23fb1f3e554ee3d'

# Collect information from top playing movies
movie_dict = dict()
movie_ids = [268896, 284054, 299536, 333339, 370567, 419478, 427641, 432301, 437557, 447332, 454619, 460019, 460668]

for movie_id in movie_ids:
    movie = dict()
    movie_id = str(movie_id)
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = movie_id
    movie['now_playing'] = True
    movie['title'] = movie_details['title']
    movie['release_date'] = datetime.datetime.strptime(str(movie_details['release_date']), '%Y-%m-%d').strftime('%m-%d-%Y')
    movie['duration'] = movie_details['runtime']
    movie['genres'] = [genre["name"] for genre in movie_details['genres']]
    movie['overview'] = movie_details['overview']
    movie['homepage'] = movie_details['homepage']
    movie['poster'] = "https://image.tmdb.org/t/p/w1280" + movie_details['poster_path']
    movie['budget'] = movie_details['budget']
    credits_req = requests.get(url= request_url + 'movie/' + movie_id + '/credits?api_key=' + api_key);
    credits_json = credits_req.json()
    time.sleep(0.5)
    cast = []
    for i in range(min(10, len(credits_json['cast']))):
        cast = cast + [credits_json['cast'][i]['name']]
    movie['cast'] = cast
    movie_dict[movie_id] = movie

################################################################################

# Collect information from top upcoming movies
upcoming_ids = [260513, 348350, 351286, 383498, 399796, 400535, 402900, 425148, 429300, 454283, 455980, 474335, 497814, 502682]

for upcoming_id in upcoming_ids:
    movie = dict()
    movie_id = str(upcoming_id)
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = upcoming_id
    movie['now_playing'] = False
    movie['title'] = movie_details['title']
    movie['release_date'] = datetime.datetime.strptime(str(movie_details['release_date']), '%Y-%m-%d').strftime('%m-%d-%Y')
    movie['duration'] = movie_details['runtime']
    movie['genres'] = [genre["name"] for genre in movie_details['genres']]
    movie['overview'] = movie_details['overview']
    movie['homepage'] = movie_details['homepage']
    if movie_details['poster_path']:
        movie['poster'] = "https://image.tmdb.org/t/p/w1280" + movie_details['poster_path']
    movie['budget'] = movie_details['budget']
    credits_req = requests.get(url= request_url + 'movie/' + movie_id + '/credits?api_key=' + api_key);
    credits_json = credits_req.json()
    time.sleep(0.5)
    cast = []
    for i in range(min(10, len(credits_json['cast']))):
        cast = cast + [credits_json['cast'][i]['name']]
    movie['cast'] = cast
    movie_dict[upcoming_id] = movie

with open('scrapers/movies.json', 'w') as outfile:
    json.dump(movie_dict, outfile, sort_keys=True, indent=4)

