import yaml
from amway.amway_ui.base_page import BasePage
from amway.amway_ui.page.home_page import HomePage


class LoginPage(BasePage):
    def login_success(self, ):
        with open('../data/login_page.yaml') as f:
            datas = yaml.safe_load(f)
        login_user = datas['login_success']['login_user']['locator']
        login_password = datas['login_success']['login_password']['locator']
        btn = datas['login_success']['login_btn']['locator']
        self.find_and_input(*login_user)
        self.find_and_input(*login_password)
        self.find_and_click(*btn)
        return HomePage(self.driver)

    def goto_home_page(self, ):
        with open('../data/login_page.yaml') as f:
            datas = yaml.safe_load(f)
        login_user = datas['login_success']['login_user']['locator']
        login_password = datas['login_success']['login_password']['locator']
        btn = datas['login_success']['login_btn']['locator']
        self.find_and_input(*login_user)
        self.find_and_input(*login_password)
        self.find_and_click(*btn)
        return HomePage(self.driver)
