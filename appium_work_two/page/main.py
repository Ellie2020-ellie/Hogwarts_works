# -- coding: utf-8 -
from appium.webdriver.common.mobileby import MobileBy

from appium_work_one.page.add_member_page import AddMemberPage
from appium_work_one.page.base_page import BasePage


class Main(BasePage):
    def click_Contact(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return AddMemberPage(self.driver)
