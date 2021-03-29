# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

host = 'http://14.116.252.165:8084/wd/hub'
host2 = 'http://14.116.252.165:8082/wd/hub'

host3 = 'http://127.0.0.1:4444/wd/hub'


class BasePage:
    def __init__(self):
        self.driver = webdriver.Remote(command_executor=host,
                                       desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.get('https://ft1mall.amwaynet.com.cn/login')
        self.driver.set_window_size(1080, 800)
        self.driver.implicitly_wait(8)


class Page(BasePage):
    def Page(self):
        self.driver.find_element('css selector',
                                 '.login-panel>div.loginCenter-main-page>div.account-login-main.login-main-panel>.login-name>input') \
            .send_keys('59375959')
        return self.driver


class TestDemo:
    def test_demo_1(self):
        Page().Page().quit()
