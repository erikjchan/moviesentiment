from . import *
from boto3.dynamodb.conditions import Key
from scipy.optimize import curve_fit
import boto3
import settings

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

@irsystem.route('/', methods=['GET'])
def search():
    movies_table = db.Table('Movies')

    now_playing_movies = movies_table.query(
        KeyConditionExpression=Key('now_playing').eq('True')
    )
    now_playing_list = sorted(now_playing_movies['Items'], key=lambda k: k['title']) 


    upcoming_movies = movies_table.query(
        KeyConditionExpression=Key('now_playing').eq('False')
    )
    upcoming_list = sorted(upcoming_movies['Items'], key=lambda k: k['title'])

    return render_template('index.html',
        now_playing_movies = now_playing_list,
        upcoming_movies = upcoming_list
    )

@irsystem.route('now_playing/<path:path>', methods=['GET'])
def now_playing_search(path):
    movies_table = db.Table('Movies')

    movie = movies_table.get_item (
        Key={
            'now_playing' : 'True',
            'id': int(path)
        }
    )
    movie = movie['Item']
    box_office_dict = movie['box_office']

    import numpy as np
    opening = int(movie['projected_opening'])
    total = int(movie['projected_total'])
    print(opening)
    print(total)
    x = np.array([1, 3, 100])
    y = np.array([1, opening, total])

    def logFunc(x, a, b):
        return a + b*np.log(x)

    def logFit(x,y):
        # cache some frequently reused terms
        sumy = np.sum(y)
        sumlogx = np.sum(np.log(x))

        b = (x.size*np.sum(y*np.log(x)) - sumy*sumlogx)/(x.size*np.sum(np.log(x)**2) - sumlogx**2)
        a = (sumy - b*sumlogx)/x.size

        return a,b

    xfit = np.linspace(0,100,num=100)
    z = logFunc(xfit, *logFit(x,y))

    box_office = []
    for day in sorted(box_office_dict, key=lambda x: int(x)):
        box_office.append([int(day), int(box_office_dict[day]), z[int(day) + 1]])

    # Twitter

    twitter_table = db.Table('Tweets')

    tweets = twitter_table.query(
        KeyConditionExpression=Key('movie').eq(path)
    )
    tweets = tweets['Items']
    date_dict = dict()
    date_dict['total_positive'] = 0
    date_dict['total_negative'] = 0
    for t in tweets:
        date = t['date'][:10]
        positive = (t['polarity'] > 0)
        negative = (t['polarity'] < 0)
        if date in date_dict:
            date_dict[date]['count'] += 1
            date_dict[date]['positive'] += positive
            date_dict[date]['negative'] += negative
        else:
            date_dict[date] = dict()
            date_dict[date]['count'] = 1
            date_dict[date]['positive'] = positive
            date_dict[date]['negative'] = negative
        date_dict['total_positive'] += positive
        date_dict['total_negative'] += negative
    dates = []
    for date in sorted(date_dict, key=lambda x: x):
        dates.append([date, date_dict[date]])

    return render_template('now_playing.html',
        movie = movie,
        box_office = box_office,
        dates = dates
    )

@irsystem.route('upcoming/<path:path>', methods=['GET'])
def upcoming_search(path):
    movies_table = db.Table('Movies')

    movie = movies_table.get_item (
        Key={
            'now_playing' : 'False',
            'id': int(path)
        }
    )
    movie = movie['Item']

    return render_template('upcoming.html',
        movie = movie
    )
