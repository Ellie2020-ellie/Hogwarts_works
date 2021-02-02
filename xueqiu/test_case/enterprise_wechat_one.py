import json
import time

from selenium import webdriver


class TestEnterpriseWechat:
    def setup_method(self):
        chrom = webdriver.ChromeOptions()
        chrom.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome
        # self.driver = webdriver.Chrome(options=chrom)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def get_cookie(self):
        cookie = self.driver.get_cookies()
        with open('cookie.json', 'w') as f:
            json.dump(cookie, f)

    def test_cookie(self):
        self.driver.get('https://work.weixin.qq.com')
        with open('cookie.json', 'r') as f:
            cookie = json.load(f)
        for i in cookie:
            self.driver.add_cookie(i)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element('id', 'menu_customer').click()
        self.driver.quit()
