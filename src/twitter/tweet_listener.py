from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import dataset
import json
import settings
import tweepy

db = dataset.connect(settings.CONNECTION_STRING)
reverse_keywords_dict = json.load(open('scrapers/reverse_keywords.json'))

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        blob = TextBlob(text)
        sent = blob.sentiment

        if status.retweeted or status.user.followers_count < 100 or text[:2] == 'RT' or sent.polarity == 0.0:
            return

        name = status.user.screen_name
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at

        movie = ''
        found = False
        for keyword in settings.TRACK_TERMS:
            if keyword.lower() in text.lower():
                movie = reverse_keywords_dict[keyword]
                found = True
                break
        if found != True:
            return

        print(text)
        print(sent.polarity)
        print(movie)

        table = db[settings.TABLE_NAME]
        try:
            table.insert(dict(
                text=text,
                user_name=name,
                user_followers=followers,
                id_str=id_str,
                created=created,
                polarity=sent.polarity,
                subjectivity=sent.subjectivity,
                movie=movie
            ))
        except ProgrammingError as err:
            print(err)

    def on_error(self, status_code):
        if status_code == 420:
            return False

auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
api = tweepy.API(auth)
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS, languages=['en'])
