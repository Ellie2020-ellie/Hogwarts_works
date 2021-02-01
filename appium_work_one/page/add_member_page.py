import time

from appium.webdriver.common.mobileby import MobileBy

from appium_work_one.page.manual_add_member_page import ManualAddMemberPage
from appium_work_one.page.base_page import BasePage


class AddMemberPage(BasePage):

    def click_manual_add_member(self):
        self.scroll_find_click("添加成员")
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return ManualAddMemberPage(self.driver)

    def get_toast(self):
        ele = self.find_and_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return ele
