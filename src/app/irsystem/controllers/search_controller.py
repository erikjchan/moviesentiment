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

    upcoming_movies = movies_table.query(
        KeyConditionExpression=Key('now_playing').eq('False')
    )

    return render_template('index.html',
        now_playing_movies = now_playing_movies['Items'],
        upcoming_movies = upcoming_movies['Items']
    )
