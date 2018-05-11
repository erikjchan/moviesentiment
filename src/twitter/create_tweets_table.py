from __future__ import print_function # Python 2/3 compatibility
import boto3
import settings
import json

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

table = db.create_table(
    TableName='Tweets',
    KeySchema=[
        {
            'AttributeName': 'movie',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'created',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'movie',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'created',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
