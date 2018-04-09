from BeautifulSoup import BeautifulSoup
import requests


tomato_base_url = 'https://www.rottentomatoes.com/m/'
tomato_url = tomato_base_url + 'black_panther_2018'

soup = BeautifulSoup(requests.get(tomato_url).text)  # rotten tomatoes: website parse tree

tomatometer = int(min(soup.find('span', {'class': 'meter-value superPageFontColor'}).contents[0]))
user_score = int(filter(str.isdigit, str(soup.find('span', {'class': 'superPageFontColor'}).contents[0])))

print tomatometer
print user_score