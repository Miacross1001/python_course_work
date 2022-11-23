from lib import token
import requests

class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self):
        self.TOKEN = token.token_yandex

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.TOKEN}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        return request_url

    def upload(self, url, name):
        self.url = url
        self.name = name
        request_url = self._get_upload_link(self.name)
        params = {
            'url': self.url,
            'path': self.name,
            "method": "string",
            "templated": True
        }
        response = requests.post(request_url, headers=self.get_headers(), params=params)
