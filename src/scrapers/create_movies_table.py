from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import settings

db = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_ACCESS_SECRET)

table = db.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'now_playing',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'now_playing',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
