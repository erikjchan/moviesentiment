from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import dataset
import json
import settings
import tweepy
import boto3
from decimal import *
import datetime

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

# db = dataset.connect(settings.CONNECTION_STRING)
reverse_keywords_dict = json.load(open('scrapers/reverse_keywords.json'))

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        blob = TextBlob(text)
        sent = blob.sentiment

        if status.retweeted or status.user.followers_count < 100 or text[:2] == 'RT' or abs(sent.polarity) < 0.1:
            return

        name = status.user.screen_name
        followers = status.user.followers_count
        created = status.created_at.strftime('%m-%d-%Y %H:%M:%S')

        movie = ''
        found = False
        for keyword in settings.TRACK_TERMS:
            if keyword.lower() in text.lower():
                movie = reverse_keywords_dict[keyword]
                found = True
                break
        if found != True:
            return

        table = db.Table('Tweets')
        response = table.put_item(
           Item={
                'text' : text,
                'username' : name,
                'followers' : followers,
                'created' : created,
                'polarity' : Decimal(str(sent.polarity)),
                'subjectivity' : Decimal(str(sent.subjectivity)),
                'movie' : str(movie)
            }
        )

    def on_error(self, status_code):
        if status_code == 420:
            return False

auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
api = tweepy.API(auth)
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS, languages=['en'])
