import json

import requests
from enterprise_wechat_work_two.api.base import Base


class Request_Adgs(Base):
    def create_member(self, userid, name, department, mobile):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        data_info = json.dumps(data)
        r = self.send('post', url, data=data_info)
        print(r)
        return self

    def get_member(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}'
        r = self.send('post', url)
        print(r)
        return self

    def update_member(self, name, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": userid,
            "name": name}
        r = self.send('post', url, data=json.dumps(data))
        print(r)
        return self

    def delete_member(self, userid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?{userid}'
        r = self.send('get', url)
        print(r)
        return self
