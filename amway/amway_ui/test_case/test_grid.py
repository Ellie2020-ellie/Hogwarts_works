# coding = utf-8
import threading
import time
from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

from selenium.webdriver.remote.webdriver import WebDriver

host = 'http://14.116.252.165:8084/wd/hub'
host2 = 'http://14.116.252.165:8082/wd/hub'

host3 = 'http://127.0.0.1:4444/wd/hub'


class BasePage:
    def __init__(self):
        self.driver = webdriver.Remote(command_executor=host3,
                                       desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get('https://www.baidu.com')


class Page(BasePage):
    def Page(self):
        self.driver.find_element_by_id('kw').send_keys('bs')
        self.driver.find_element_by_id('su').click()
        return self.driver


class TestDemo:
    def test_demo_1(self):
        Page().Page().quit()

    def test_baidu_search_2(driver):
        Page().Page().quit()

    def test_demo_2(self):
        Page().Page().quit()

    def test_baidu_search_2(driver):
        Page().Page().quit()

    def test_demo(self):
        Page().Page().quit()

    def test_baidu_search(driver):
        Page().Page().quit()
