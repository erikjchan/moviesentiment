from __future__ import print_function # Python 2/3 compatibility
import boto3
import decimal
import json
import settings

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

table = db.Table('Movies')

with open("scrapers/movies.json") as json_file:
    movie_dict = json.load(json_file, parse_float = decimal.Decimal)
    for movie_key in movie_dict:
        movie = movie_dict[movie_key]
        if 'box_office' in movie.keys():
            box_office = movie['box_office']
        else:
            box_office = None
        budget = movie['budget']
        cast = movie['cast']
        duration = movie['duration']
        genres = movie['genres']
        homepage = movie['homepage']
        movie_id = int(movie['id'])
        now_playing = str(movie['now_playing'])
        overview = movie['overview']
        poster = movie['poster']
        projected_opening = movie['projected_opening']
        projected_total = movie['projected_total']
        release_date = movie['release_date']
        rt_score = movie['rt_score']
        title = movie['title']

        print("Adding movie:", movie_id, title, now_playing)

        table.put_item(
           Item={
                'box_office': box_office,
                'budget' : budget,
                'cast' : cast,
                'duration' : duration,
                'genres' : genres,
                'homepage' : homepage,
                'id' : movie_id,
                'now_playing' : now_playing,
                'overview' : overview,
                'poster' : poster,
                'projected_opening' : projected_opening,
                'projected_total' : projected_total,
                'release_date' : release_date,
                'rt_score' : rt_score,
                'title' : title
            }
        )