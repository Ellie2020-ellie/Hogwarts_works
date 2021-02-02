# -- coding: utf-8 -
from appium.webdriver.common.mobileby import MobileBy
from appium_work_three.base_page import BasePage
from appium_work_three.page.market_page import MarketPage


class Main(BasePage):
    def click_market(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="行情"]'))
        return MarketPage(self.driver)
