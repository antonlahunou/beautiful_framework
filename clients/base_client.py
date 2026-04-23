import requests

from config.settings import ACCESS_TOKEN
from configurations import SERVER_URL

class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        })

    def _url(self, path: str) -> str:
        return f"{SERVER_URL}{path}"

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.session.get(self._url(path), **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.session.post(self._url(path), **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.session.put(self._url(path), **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.session.delete(self._url(path), **kwargs)