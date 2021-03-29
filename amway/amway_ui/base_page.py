from asyncio import threads
from threading import Thread

import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

_url = 'https://ft1mall.amwaynet.com.cn/login'


def handle_black(fun):
    def run(*args, **kwargs):
        with open('../data/black_list.yaml', 'r') as f:
            black_lists = yaml.safe_load(f)
            try:
                return fun(*args, **kwargs)
            except Exception as msg:
                for black in black_lists:
                    black_count = args[0].driver.find_elements(*black)
                    if len(black_count) > 0:
                        black_count[0].click()
                        return fun(*args, **kwargs)
                raise msg

    return run


browsers = [
    DesiredCapabilities.FIREFOX,
    DesiredCapabilities.CHROME
]


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME)
            self.driver.get(_url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
        else:
            self.driver = driver

    def find(self, locator, path):
        return self.driver.find_element(locator, path)

    def find_and_input(self, locator, path, content):
        self.find(locator, path).clear()
        self.find(locator, path).send_keys(content)

    def find_and_click(self, locator, path):
        self.find(locator, path).click()
