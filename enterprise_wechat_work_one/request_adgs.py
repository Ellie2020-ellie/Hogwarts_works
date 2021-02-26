import json

import requests


def get_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3600a59a9c93005c&corpsecret=IT5ATZ_O5dO438LpVKBXb3jmO75Kb9RUleOgLNIAZ8w'
    r = requests.get(url)
    return_json = r.json()
    token = return_json['access_token']
    return token


def test_create_member():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "department": [1],
        "mobile": "+86 13800900000"
    }
    data_info = json.dumps(data)
    r = requests.post(url=url, data=data_info)
    print(r.status_code, r.json())


def test_get_member():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ellie'
    r = requests.post(url)
    print(r.text)


def test_update_member():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}'
    data = {
        "userid": "zhangsan",
        "name": "李四"}
    r = requests.post(url, data=json.dumps(data))
    print(r.status_code, r.text)


def test_delete_member():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan'
    r = requests.get(url)
    print(r.status_code, r.json())
