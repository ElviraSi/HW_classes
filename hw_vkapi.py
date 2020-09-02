import requests
from pprint import pprint

TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'

class User:

    def __init__(self, token) -> None:
        self.token = token

    def get_common_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'v': 5.122
            }
        )
        return response.json()

Elvira = User(token=TOKEN)
pprint(Elvira.get_common_friends())