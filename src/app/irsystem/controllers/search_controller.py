from . import *
from boto3.dynamodb.conditions import Key
from scipy.optimize import curve_fit
import numpy as np
import boto3
import linear_regression
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
    # Tweets Table
    twitter_table = db.Table('Tweets')

    tweets_list = []
    tweets = twitter_table.query(
        KeyConditionExpression=Key('movie').eq(path)
    )
    tweets_list += tweets['Items']
    while 'LastEvaluatedKey' in tweets:
        tweets = twitter_table.query(
            KeyConditionExpression=Key('movie').eq(path),
            ExclusiveStartKey=tweets['LastEvaluatedKey']
        )
        tweets_list += tweets['Items']

    date_dict = dict()
    date_dict['total_positive'] = 0
    date_dict['total_negative'] = 0
    date_dict['total_positive_reach'] = 0
    date_dict['total_negative_reach'] = 0
    for t in tweets_list:
        date = t['date'][:10]
        positive = (t['polarity'] > 0)
        negative = (t['polarity'] < 0)
        followers = t['followers']
        if date in date_dict:
            date_dict[date]['count'] += 1
            date_dict[date]['count_reach'] += followers
            date_dict[date]['positive'] += positive
            date_dict[date]['negative'] += negative
            date_dict[date]['positive_reach'] += positive * followers
            date_dict[date]['negative_reach'] += negative * followers
        else:
            date_dict[date] = dict()
            date_dict[date]['count'] = 1
            date_dict[date]['count_reach'] = followers
            date_dict[date]['positive'] = positive
            date_dict[date]['negative'] = negative
            date_dict[date]['positive_reach'] = positive * followers
            date_dict[date]['negative_reach'] = negative * followers
        date_dict['total_positive'] += positive
        date_dict['total_negative'] += negative
        date_dict['total_positive_reach'] += positive * followers
        date_dict['total_negative_reach'] += negative * followers
    dates = []
    for date in sorted(date_dict, key=lambda x: x):
        dates.append([date, date_dict[date]])

    total_both_reach = date_dict['total_positive_reach'] + date_dict['total_negative_reach']

    # Movies Table
    movies_table = db.Table('Movies')

    movie = movies_table.get_item (
        Key={
            'now_playing' : 'True',
            'id': int(path)
        }
    )
    movie = movie['Item']
    box_office_dict = movie['box_office']

    opening = int(movie['projected_opening'])
    total = int(movie['projected_total'])
    x = np.array([1, 3, 100])
    y = np.array([1, opening, total])
    xfit = np.linspace(0,100,num=100)
    z = logFunc(xfit, *logFit(x,y))

    new_opening = opening * linear_regression.get_projected_multiplier(float(total_both_reach))
    new_total = total * linear_regression.get_rt_multiplier(float(movie['rt_score']))
    x_new = np.array([1, 3, 100])
    y_new = np.array([1, new_opening, new_total])
    xfit_new = np.linspace(0,100,num=100)
    z_new = logFunc(xfit, *logFit(x_new,y_new))

    box_office = []
    for day in sorted(box_office_dict, key=lambda x: int(x)):
        box_office.append([int(day), int(box_office_dict[day]), z[int(day) + 1], z_new[int(day) + 1]])

    movie['actual_opening'] = addCommas(box_office[2][1])
    movie['actual_total'] = addCommas(box_office[-1][1])
    movie['opening_difference'] = round(100 * (box_office[2][1] - movie['projected_opening']) / movie['projected_opening'], 1)
    if movie['opening_difference'] > 0:
        movie['opening_difference'] = "+" + str(movie['opening_difference']) + "%"
    else:
        movie['opening_difference'] = str(movie['opening_difference']) + "%"
    movie['total_difference'] = round(100 * (box_office[-1][1] - movie['projected_total']) / movie['projected_total'], 1)
    if movie['total_difference'] > 0:
        movie['total_difference'] = "+" + str(movie['total_difference']) + "%"
    else:
        movie['total_difference'] = str(movie['total_difference']) + "%"
    movie['projected_opening'] = addCommas(movie['projected_opening'])
    movie['projected_total'] = addCommas(movie['projected_total'])
    return render_template('now_playing.html',
        movie = movie,
        dates = dates,
        box_office = box_office
    )

@irsystem.route('upcoming/<path:path>', methods=['GET'])
def upcoming_search(path):
    # Tweets Table
    twitter_table = db.Table('Tweets')

    tweets_list = []
    tweets = twitter_table.query(
        KeyConditionExpression=Key('movie').eq(path)
    )
    tweets_list += tweets['Items']
    while 'LastEvaluatedKey' in tweets:
        tweets = twitter_table.query(
            KeyConditionExpression=Key('movie').eq(path),
            ExclusiveStartKey=tweets['LastEvaluatedKey']
        )
        tweets_list += tweets['Items']

    date_dict = dict()
    date_dict['total_positive'] = 0
    date_dict['total_negative'] = 0
    date_dict['total_positive_reach'] = 0
    date_dict['total_negative_reach'] = 0
    for t in tweets_list:
        date = t['date'][:10]
        positive = (t['polarity'] > 0)
        negative = (t['polarity'] < 0)
        followers = t['followers']
        if date in date_dict:
            date_dict[date]['count'] += 1
            date_dict[date]['count_reach'] += followers
            date_dict[date]['positive'] += positive
            date_dict[date]['negative'] += negative
            date_dict[date]['positive_reach'] += positive * followers
            date_dict[date]['negative_reach'] += negative * followers
        else:
            date_dict[date] = dict()
            date_dict[date]['count'] = 1
            date_dict[date]['count_reach'] = followers
            date_dict[date]['positive'] = positive
            date_dict[date]['negative'] = negative
            date_dict[date]['positive_reach'] = positive * followers
            date_dict[date]['negative_reach'] = negative * followers
        date_dict['total_positive'] += positive
        date_dict['total_negative'] += negative
        date_dict['total_positive_reach'] += positive * followers
        date_dict['total_negative_reach'] += negative * followers
    dates = []
    for date in sorted(date_dict, key=lambda x: x):
        dates.append([date, date_dict[date]])

    total_both_reach = date_dict['total_positive_reach'] + date_dict['total_negative_reach']

    # Movies Table
    movies_table = db.Table('Movies')

    movie = movies_table.get_item (
        Key={
            'now_playing' : 'False',
            'id': int(path)
        }
    )
    movie = movie['Item']

    opening = int(movie['projected_opening'])
    total = int(movie['projected_total'])
    x = np.array([1, 3, 100])
    y = np.array([1, opening, total])
    xfit = np.linspace(0,100,num=100)
    z = logFunc(xfit, *logFit(x,y))

    if movie['rt_score']:
        new_opening = opening * linear_regression.get_projected_multiplier(float(total_both_reach))
        new_total = total * linear_regression.get_rt_multiplier(float(movie['rt_score']))
        x_new = np.array([1, 3, 100])
        y_new = np.array([1, new_opening, new_total])
        z_new = logFunc(xfit, *logFit(x_new,y_new))

        box_office = []
        for day in range(99):
            box_office.append([day, z[day + 1], z_new[day + 1]])


    else:
        new_opening = opening * linear_regression.get_projected_multiplier(float(total_both_reach))
        positive_total = total * linear_regression.get_rt_multiplier(80)
        x_positive = np.array([1, 3, 100])
        y_positive = np.array([1, new_opening, positive_total])
        z_positive = logFunc(xfit, *logFit(x_positive,y_positive))

        negative_total = total * linear_regression.get_rt_multiplier(40)
        x_negative = np.array([1, 3, 100])
        y_negative = np.array([1, new_opening, negative_total])
        z_negative = logFunc(xfit, *logFit(x_negative,y_negative))

        box_office = []
        for day in range(99):
            box_office.append([day, z[day + 1], z_positive[day + 1], z_negative[day + 1]])

    movie['projected_opening'] = addCommas(movie['projected_opening'])
    movie['projected_total'] = addCommas(movie['projected_total'])
    return render_template('upcoming.html',
        movie = movie,
        dates = dates,
        box_office = box_office,
    )

@irsystem.route('statistics', methods=['GET'])
def statistics_search():
    # Movies Table
    movies_table = db.Table('Movies')

    now_playing_movies = movies_table.query(
        KeyConditionExpression=Key('now_playing').eq('True')
    )
    now_playing_dict = dict()
    for movie in now_playing_movies['Items']:
        movie_id = str(movie['id'])
        now_playing_dict[movie_id] = movie
        now_playing_dict[movie_id]['count'] = 1
        now_playing_dict[movie_id]['positive'] = 0
        now_playing_dict[movie_id]['negative'] = 0


    upcoming_movies = movies_table.query(
        KeyConditionExpression=Key('now_playing').eq('False')
    )
    upcoming_dict = dict()
    for movie in upcoming_movies['Items']:
        movie_id = str(movie['id'])
        upcoming_dict[movie_id] = movie
        upcoming_dict[movie_id]['count'] = 0
        upcoming_dict[movie_id]['positive'] = 0
        upcoming_dict[movie_id]['negative'] = 0
    
    # Tweets Table
    twitter_table = db.Table('Tweets')

    tweet_list = []
    tweets = twitter_table.scan(
    )
    tweet_list += tweets['Items']
    while 'LastEvaluatedKey' in tweets:
        tweets = twitter_table.scan(
            ExclusiveStartKey=tweets['LastEvaluatedKey']
        )
        tweet_list += tweets['Items']

    for t in tweet_list:
        movie = str(t['movie'])
        positive = (t['polarity'] > 0)
        negative = (t['polarity'] < 0)
        if movie in now_playing_dict:
            now_playing_dict[movie]['count'] += 1
            now_playing_dict[movie]['positive'] += positive
            now_playing_dict[movie]['negative'] += negative
        elif movie in upcoming_dict:
            upcoming_dict[movie]['count'] += 1
            upcoming_dict[movie]['positive'] += positive
            upcoming_dict[movie]['negative'] += negative
    
    now_playing = []
    for movie in now_playing_dict:
        box_office_dict = now_playing_dict[movie]['box_office']
        last_day = sorted(box_office_dict, key=lambda x: int(x),reverse=True)[0]
        now_playing_dict[movie]['actual_total'] = addCommas(box_office_dict[last_day])
        now_playing.append(now_playing_dict[movie])
    now_playing = sorted(now_playing, key=lambda k: int(k['count']), reverse=True)

    upcoming = []
    for movie in upcoming_dict:
        upcoming_dict[movie]['projected_total'] = addCommas(upcoming_dict[movie]['projected_total'])
        upcoming.append(upcoming_dict[movie])
    upcoming = sorted(upcoming, key=lambda k: int(k['count']), reverse=True)

    return render_template('statistics.html',
        now_playing = now_playing,
        upcoming = upcoming
    )

def logFunc(x, a, b):
    return a + b*np.log(x)

def logFit(x,y):
    # cache some frequently reused terms
    sumy = np.sum(y)
    sumlogx = np.sum(np.log(x))

    b = (x.size*np.sum(y*np.log(x)) - sumy*sumlogx)/(x.size*np.sum(np.log(x)**2) - sumlogx**2)
    a = (sumy - b*sumlogx)/x.size

    return a,b

def addCommas(x):
    return "{:,}".format(x)