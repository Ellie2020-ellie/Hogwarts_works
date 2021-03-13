import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from gride.page.main_page import MainPage
from gride.base_page import BasePage


class App(BasePage):

    def start_app(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0.1'
            desired_caps['deviceName'] = '83PBB19724200838'
            desired_caps['udid'] = 'emulator-5554'
            # desired_caps['udid']=os.getenv('udid',None)
            # desired_caps['deviceName'] = '127.0.0.1:7555'
            # desired_caps['systemPort'] = os.getenv('systemPort',None)
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            # 不清空本地缓存
            desired_caps["noReset"] = "true"
            desired_caps["resetKeyboard"] = "true"
            # http://localhost:4723/wd/hub
            # http://192.168.15.1:4444/wd/hub
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def goto_main(self):
        # 模拟黑名单页面
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/post_status").click()
        return MainPage(self.driver)
