import sys
import requests

def handle(event, context):

    r = requests.get(event.body)

    return {
        "statusCode": r.status_code,
        "body": r.text
    }
