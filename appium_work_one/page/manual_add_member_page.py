from appium.webdriver.common.mobileby import MobileBy

from appium_work_one.page.base_page import BasePage


class ManualAddMemberPage(BasePage):
    def click_save(self):
        from appium_work_one.page.add_member_page import AddMemberPage
        self.find_and_click((MobileBy.XPATH, '//*[contains(@text,"保存")]'))
        return AddMemberPage(self.driver)

    def edit_name(self, member_name):
        member_name_locator = (MobileBy.XPATH,
                               '//*[contains(@text,"姓名")]/following-sibling::*[contains(@text,"必填")]')
        self.find_and_click(member_name_locator)
        self.find_and_input(member_name_locator, member_name)
        return self

    def edit_emil(self, emil):
        emil_locator = (MobileBy.XPATH,
                        '//*[contains(@text,"邮箱")]/following-sibling::*[contains(@text,"选填")]')
        self.find_and_input(emil_locator, emil)
        return self
