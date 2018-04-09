import requests
import json
import urllib3

request_url = 'https://api.themoviedb.org/3/'
now_playing_url = 'movie/now_playing?language=en-US&page=1&api_key='
genres_url = 'genre/movie/list?api_key='
movie_id = 1
credits_url = 'movie/{movie_id}/credits?api_key='
details_url = 'movie/{movie_id}?api_key='
api_key = '06709af3621440ead23fb1f3e554ee3d'

r = requests.get(url= request_url + now_playing_url + api_key);
playing_json = r.json()

# {u'poster_path': u'/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg',
# u'title': u'Coco', 
# u'overview': u"Despite his family\u2019s baffling generations-old ban on music, Miguel dreams of becoming an accomplished musician like his idol, Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events. Along the way, he meets charming trickster Hector, and together, they set off on an extraordinary journey to unlock the real story behind Miguel's family history.", 
# u'release_date': u'2017-10-27', 
# u'popularity': 311.848958, 
# u'original_title': u'Coco', 
# u'backdrop_path': u'/askg3SMvhqEl4OL52YuvdtY40Yb.jpg', 
# u'vote_count': 3686, 
# u'video': False, 
# u'adult': False, 
# u'vote_average': 7.8, 
# u'genre_ids': [12, 35, 10751, 16], 
# u'id': 354912, 
# u'original_language': 
# u'en'}
for res in playing_json['results']:
	print ' '
	movie_id = str(res['id'])
	r = requests.get(url= request_url + 'movie/' + movie_id + '/credits?api_key=' + api_key);
	credits_json = r.json()
	print res['title']
	for i in range(min(10, len(credits_json['cast']))):
		print credits_json['cast'][i]['name']

# {u'poster_path': u'/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg', 
# u'production_countries': [{u'iso_3166_1': u'US', u'name': u'United States of America'}], 
# u'revenue': 700920729, 
# u'overview': u"Despite his family\u2019s baffling generations-old ban on music, Miguel dreams of becoming an accomplished musician like his idol, Ernesto de la Cruz. Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events. Along the way, he meets charming trickster Hector, and together, they set off on an extraordinary journey to unlock the real story behind Miguel's family history.", 
# u'video': False, 
# u'id': 354912, 
# u'genres': [{u'id': 12, u'name': u'Adventure'}, {u'id': 35, u'name': u'Comedy'}, {u'id': 10751, u'name': u'Family'}, {u'id': 16, u'name': u'Animation'}], 
# u'title': u'Coco', 
# u'tagline': u'The celebration of a lifetime', 
# u'vote_count': 3745, 
# u'homepage': u'https://www.pixar.com/feature-films/coco', 
# u'belongs_to_collection': None, 
# u'original_language': u'en', 
# u'status': u'Released', 
# u'spoken_languages': [{u'iso_639_1': u'es', u'name': u'Espa\xf1ol'}],
# u'imdb_id': u'tt2380307', 
# u'adult': False, 
# u'backdrop_path': u'/askg3SMvhqEl4OL52YuvdtY40Yb.jpg', 
# u'production_companies': [{u'origin_country': u'US', u'logo_path': u'/1TjvGVDMYsj6JBxOAkUHpPEwLf7.png', u'id': 3, u'name': u'Pixar'}], 
# u'release_date': u'2017-10-27', 
# u'popularity': 310.848958, 
# u'original_title': u'Coco', 
# u'budget': 175000000, 
# u'vote_average': 7.8, 
# u'runtime': 105}
r = requests.get(url= request_url + 'movie/354912?api_key=' + api_key);
# print r.json()