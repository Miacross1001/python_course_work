import requests
from lib import token
import upload_yandex
import json
from datetime import datetime
from lib import MyProgressBar


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def _get_photos(self, user_id=None):
        url = 'https://api.vk.com/method/photos.get'
        album = ['profile', 'wall']

        for al in album:
            params = {
                'owner_id': user_id,
                'album_id': al,
                'extended': 1,
                'feed_type': 'photo',
            }
            print(al)
            response = requests.get(url, params={**self.params, **params})

        return response.json()

    def _get_name(self, id):
        self.id = id
        dict_photos = self._get_photos(self.id)
        name_photos = {}
        date = {}
        check = set()

        for elem in dict_photos['response']['items']:
            url = elem['sizes'][-1]['url']
            count_likes = elem['likes']['count']
            date[url] = elem['date']

            if count_likes not in check:
                name_photos[url] = count_likes
                check.add(count_likes)
            else:
                name_photos[url] = datetime.utcfromtimestamp(int(date[url])).strftime('%Y-%m-%d')

        return name_photos

    def upload(self, id):
        self.id = id
        dict_name = self._get_name(self.id)

        b3 = MyProgressBar.MyProgressBar(dict_name)
        b3.oper_text('Upload photos in disc')
        for url, name in dict_name.items():
            ya = upload_yandex.Yandex()
            ya.upload(url, name)
            b3.Bar()

        with open('info.json', 'w') as f:
            step_info = []
            for key, value in dict_name.items():
                step_info.append(
                   {
                       'file_name': value,
                       'url': key,
                       'size': 'z'
                   }
                )

            json.dump(step_info, f)
        return 'Загрузка завершена!'

if __name__ == '__main__':
    access_token = token.TOKEN
    user_id = str(input('Enter id: '))
    vk = VK(access_token, user_id)
    print(vk.upload(user_id))
