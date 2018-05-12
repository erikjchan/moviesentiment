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

# Collect information from top 15 playing movies
now_playing_dict = dict()
now_playing_ids = [268896, 284054, 299536, 333339, 370567, 419478, 427641, 432301, 437557, 447332, 454619, 460019, 460668]

for now_playing_id in now_playing_ids:
    movie = dict()
    movie_id = str(now_playing_id)
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = now_playing_id
    movie['title'] = movie_details['title']
    movie['releaseDate'] = movie_details['release_date']
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
    now_playing_dict[now_playing_id] = movie

with open('scrapers/now_playing.json', 'w') as outfile:
    json.dump(now_playing_dict, outfile, sort_keys=True, indent=4)

################################################################################

# Collect information from top 15 upcoming movies
upcoming_dict = dict()
upcoming_ids = [260513, 348350, 351286, 383498, 399796, 400535, 402900, 425148, 429300, 454283, 455980, 474335, 497814, 502682]

for upcoming_id in upcoming_ids:
    movie = dict()
    movie_id = str(upcoming_id)
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = upcoming_id
    movie['title'] = movie_details['title']
    movie['releaseDate'] = movie_details['release_date']
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
    upcoming_dict[upcoming_id] = movie

with open('scrapers/upcoming.json', 'w') as outfile:
    json.dump(upcoming_dict, outfile, sort_keys=True, indent=4)

