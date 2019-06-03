import sys
import requests

def handle(event, context):

    requests.get("https://www.google.com/")

    sys.stderr.write("My special debug message.\n")

    return {
        "statusCode": 200,
        "body": "Hello from OpenFaaS!"
    }
