import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response_body = requests.get(self.url)
        return response_body.content

    def load_json(self):
        response = self.get_response_body()
        return json.loads(response)