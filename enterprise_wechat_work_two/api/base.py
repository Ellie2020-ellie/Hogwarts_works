# import requests
import requests


class Base:
    def __init__(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3600a59a9c93005c&corpsecret=IT5ATZ_O5dO438LpVKBXb3jmO75Kb9RUleOgLNIAZ8w'
        r = requests.get(url).json()
        self.token = r['access_token']
        self.session = requests.session()
        self.session.params = {
            'access_token': self.token
        }

    def send(self, *args, **kwargs):
        r = self.session.request(*args, **kwargs)
        return r.json()
