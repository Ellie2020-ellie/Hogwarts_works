import time
from threading import Thread

import yaml
from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.remote import webdriver

from selenium.webdriver.remote.webdriver import WebDriver

ds = {'platform': 'ANY',
      'browserName': "chrome",
      # 'version': '89',
      'javascriptEnabled': True
      }


def test_():
    driver = webdriver.Chrome()
    # DesiredCapabilities.CHROME
    # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
    #                           desired_capabilities=DesiredCapabilities.FIREFOX)
    # driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("kw").screenshot("D:/拉钩/笔记/selenium_grid/code.png")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()


browsers = [
    DesiredCapabilities.FIREFOX,
    DesiredCapabilities.CHROME,
    DesiredCapabilities.CHROME
]
host = 'http://14.116.252.165:8084/wd/hub'
host2 = 'http://14.116.252.165:8082/wd/hub'

host3 = 'http://127.0.0.1:4444/wd/hub'


class BasePage:

    def __init__(self):
        threads = []
        for bs in browsers:
            driver = webdriver.Remote(command_executor=host3,
                                      desired_capabilities=bs)
            t = Thread(target=self.Page, args=(driver,))
            self.driver.get('https://www.baidu.com')
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
            threads.append(t)
        # 启动所有线程
        for thr in threads:
            thr.start()
        for the in threads:
            the.join()

    def Page(self):
        self.driver.find_element_by_id('kw').send_keys('bs')
        self.driver.find_element_by_id('su').click()
        self.driver.quit()
