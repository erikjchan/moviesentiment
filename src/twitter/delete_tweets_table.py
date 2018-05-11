from __future__ import print_function # Python 2/3 compatibility
import boto3
import settings

db = boto3.resource('dynamodb', region_name='us-west-2', 
    endpoint_url="http://localhost:8000", aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

table = db.Table('Tweets')

table.delete()