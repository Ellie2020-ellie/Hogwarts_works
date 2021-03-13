import yaml

from enterprise_wechat_work_two.api.request_adgs import Request_Adgs


class Test():
    def setup_class(self):
        self.api = Request_Adgs()
        with open("../api/request_adgs.yaml") as f:
            datas = yaml.safe_load(f)
        self.datas = datas

    def test_get_number(self):
        # ellie
        self.api.get_member('zhangsan2')

    def test_create_member(self):
        with open("../api/request_adgs.yaml") as f:
            datas = yaml.safe_load(f)
        name = self.datas['create_member']['name']
        userid = self.datas['create_member']['userid']
        department = datas['create_member']['department']
        mobile = datas['create_member']['mobile']
        self.api.create_member(name=name, userid=userid, department=department, mobile=mobile)

    def test_update_member(self):
        name = self.datas['update_member']['name']
        userid = self.datas['update_member']['userid']
        self.api.update_member(name=name, userid=userid)

    def test_delete_member(self):
        userid = self.datas['delete_member']['userid']
        self.api.delete_member(userid)
