from __future__ import print_function

import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '200' if err else '400',
        'body': err,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    print(event)
    return respond(json.dumps(event))