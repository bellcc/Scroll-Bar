import json
import requests

def get_message():
    return json.loads(requests.get("http://54.86.215.7:80/messages").text).get("phrase");

def post_message(phrase):
    payload = {
        "phrase": phrase
    }

    headers = {
        "content-type": "application/json"
    }

    requests.post("http://54.86.215.7:80/messages", headers=headers, data=json.dumps(payload))
