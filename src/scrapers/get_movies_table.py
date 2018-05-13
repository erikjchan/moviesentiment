# Retrieves all movies released in the year 1985.
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import settings
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

table = db.Table('Movies')

print("Movies from 1985")

response = table.query(
    KeyConditionExpression=Key('now_playing').eq('True')
)

for i in response['Items']:
    print(i)
    # print(i['title'])
    # print(i['year'], ":", i['title'])