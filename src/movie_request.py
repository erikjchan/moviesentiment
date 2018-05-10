import requests
import json
import urllib3

request_url = 'https://api.themoviedb.org/3/'
now_playing_url = 'movie/now_playing?language=en-US&page=1&api_key='
upcoming_url = 'movie/upcoming?language=en-US&page=1&api_key='
genres_url = 'genre/movie/list?api_key='
movie_id = 1
credits_url = 'movie/{movie_id}/credits?api_key='
details_url = 'movie/{movie_id}?api_key='
api_key = '06709af3621440ead23fb1f3e554ee3d'

# Collect information from top 20 playing movies
now_playing_dict = dict()
now_playing_req = requests.get(url= request_url + now_playing_url + api_key);
playing_json = now_playing_req.json()

for res in playing_json['results']:
    movie = dict()
    movie_id = str(res['id'])
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = movie_id
    movie['title'] = movie_details['title']
    movie['releaseDate'] = movie_details['release_date']
    movie['duration'] = movie_details['runtime']
    movie['genres'] = movie_details['genres']
    movie['overview'] = movie_details['overview']
    movie['homepage'] = movie_details['homepage']
    movie['poster'] = "https://image.tmdb.org/t/p/w1280" + movie_details['poster_path']
    movie['budget'] = movie_details['budget']
    credits_req = requests.get(url= request_url + 'movie/' + movie_id + '/credits?api_key=' + api_key);
    credits_json = credits_req.json()
    import time
    time.sleep(1)
    cast = []
    for i in range(min(10, len(credits_json['cast']))):
      cast = cast + [credits_json['cast'][i]['name']]
    movie['cast'] = cast
    now_playing_dict[movie_id] = movie

with open('now_playing.json', 'w') as outfile:
    json.dump(now_playing_dict, outfile, sort_keys=True, indent=4)



# Collect information from top 20 upcoming movies
upcoming_dict = dict()
upcoming_req = requests.get(url= request_url + upcoming_url + api_key);
upcoming_json = upcoming_req.json()

for res in upcoming_json['results']:
    movie = dict()
    movie_id = str(res['id'])
    movie_details_req = requests.get(url= request_url + 'movie/' + movie_id + '?api_key=' + api_key)
    movie_details = movie_details_req.json()
    movie['id'] = movie_id
    movie['title'] = movie_details['title']
    movie['releaseDate'] = movie_details['release_date']
    movie['duration'] = movie_details['runtime']
    movie['genres'] = movie_details['genres']
    movie['overview'] = movie_details['overview']
    movie['homepage'] = movie_details['homepage']
    movie['poster'] = "https://image.tmdb.org/t/p/w1280" + movie_details['poster_path']
    movie['budget'] = movie_details['budget']
    credits_req = requests.get(url= request_url + 'movie/' + movie_id + '/credits?api_key=' + api_key);
    credits_json = credits_req.json()
    import time
    time.sleep(1)
    cast = []
    for i in range(min(10, len(credits_json['cast']))):
      cast = cast + [credits_json['cast'][i]['name']]
    movie['cast'] = cast
    upcoming_dict[movie_id] = movie

with open('upcoming.json', 'w') as outfile:
    json.dump(upcoming_dict, outfile, sort_keys=True, indent=4)

