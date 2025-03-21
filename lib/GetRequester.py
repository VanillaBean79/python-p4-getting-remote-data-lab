import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            # b'[\n  {\n   ...nd"\n  }\n]\n'
            # breakpoint()
            return response.content
        else:
            return None
        

    def load_json(self):
        response_body = self.get_response_body()

        if response_body:
            return json.loads(response_body)
        else:
            return None
