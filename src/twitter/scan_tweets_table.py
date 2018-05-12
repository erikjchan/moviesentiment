from __future__ import print_function # Python 2/3 compatibility
import boto3
import decimal
import json
import settings

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

table = db.Table('Tweets')
response = table.scan(
    )
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

print("Table status:", table.table_status)