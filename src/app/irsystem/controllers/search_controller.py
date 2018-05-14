from . import *
from boto3.dynamodb.conditions import Key
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

    return render_template('now_playing.html',
        movie = movie
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
