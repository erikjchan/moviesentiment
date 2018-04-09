import requests
import json
import urllib3

api_key = "06709af3621440ead23fb1f3e554ee3d"

r = requests.get(url='https://api.themoviedb.org/3/genre/movie/list?api_key='+ api_key);
print(r.json())
# req = requests.get('https://github.com/timeline.json')
# req.json()