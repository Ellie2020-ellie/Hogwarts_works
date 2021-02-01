from appium import webdriver

from appium_work_one.page.base_page import BasePage
from appium_work_one.page.main import Main


class App(BasePage):

    def start_app(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0.1'
            desired_caps['deviceName'] = '83PBB19724200838'
            # desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps["noReset"] = "true"
            desired_caps["resetKeyboard"] = "true"
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def goto_main(self):
        return Main(self.driver)


if __name__ == '__main__':
    App().start_app()
