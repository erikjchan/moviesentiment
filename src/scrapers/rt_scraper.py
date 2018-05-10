# import imdb as imdb  # to access imdb API
# import pandas as pd  # for data array handling
from BeautifulSoup import BeautifulSoup  # for website parsing and scraping (rotten tomatoes)
import requests  # for http access
# import re  # for regular expressions
# from ggplot import *  # for plotting
# import urllib2  # for accessing url object (movie covers)
# import matplotlib.pyplot as plt  # for plotting
# from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

# imdb_http = imdb.IMDb()  # create imdb API object
# StarTrek = imdb_http.search_movie('Star Trek')  # general search for Star Trek among movie and series titles
# STF = [i for i in StarTrek if i.data['kind'] == 'movie']
# StarTrekIII = imdb_http.search_movie('Star Trek III the Search for Spock')
# StarTrekIV = imdb_http.search_movie('Star Trek IV the voyage home')
# StarTrekV = imdb_http.search_movie('Star Trek V the Final Frontier')
# StarTrekVI = imdb_http.search_movie('Star Trek VI the Undiscovered Country')
# StarTrekFC = imdb_http.search_movie('Star Trek First Contact')
# STF.extend([StarTrekIII[0], StarTrekIV[0], StarTrekV[0], StarTrekVI[0], StarTrekFC[0]])


# df = pd.DataFrame(columns=['date', 'IMDb_rating', 'Metacritic_rating', 'title', 'image_url'])  # initialise data frame

# for i in range(len(STF)):  # for each Star Trek movie

#     imdb_http.update(STF[i])  # IMDb: augment movie info
#     x = imdb_http.get_movie_critic_reviews(STF[i].movieID)  # Meta critic

#     # rotten tomato: prepare website parsing
#     tomato_base_url = 'https://www.rottentomatoes.com/m/'
#     tomato_url = tomato_base_url + re.sub(':', '', re.sub(' ', '_', str(STF[i]['title'])))
#     if 'Star Trek' not in STF[i]['title']:  # fix first contact problem
#         tomato_url = tomato_base_url + re.sub(':', '', re.sub(' ', '_', 'Star Trek ' + str(STF[i]['title'])))
#     elif 'Khan' in STF[i]['title']:  # fix wrath of khan problem
#         tomato_url = tomato_base_url + re.sub(':', '_II', re.sub(' ', '_', str(STF[i]['title'])))
#     soup = BeautifulSoup(requests.get(tomato_url).text)  # rotten tomatoes: website parse tree
#     # add data to pandas data frame
#     if 'year' in STF[i].data.keys() and bool(x['data']):  # filter out movies in production and those without MC data
#         df = df.append(pd.DataFrame(data={
#             'date': STF[i].data['year'],
#             'IMDb_rating': [((STF[i].data['rating'] - 1) / 9.0) * 5],  # normalised to 5 star system
#             'Metacritic_rating': [int(x['data']['metascore']) / 20.0],  # normalised to 5 star system
#             'Tomatometer': [
#                 int(min(soup.find('span', {'class': 'meter-value superPageFontColor'}).contents[0])) / 20.0],
#         # rotten tomatoe score (normalised to 5 star system)
#             'Tomato_user': [
#                 int(filter(str.isdigit, str(soup.find('span', {'class': 'superPageFontColor'}).contents[0]))) / 20.0],
#         # tomato audience score (normalised to 5 star system)
#             'title': STF[i].data['title'],
#             'image_url': STF[i]['cover url']}))

tomato_base_url = 'https://www.rottentomatoes.com/m/'
tomato_url = tomato_base_url + 'black_panther_2018'

soup = BeautifulSoup(requests.get(tomato_url).text)  # rotten tomatoes: website parse tree

tomatometer = int(min(soup.find('span', {'class': 'meter-value superPageFontColor'}).contents[0]))
user_score = int(filter(str.isdigit, str(soup.find('span', {'class': 'superPageFontColor'}).contents[0])))

print tomatometer
print user_score