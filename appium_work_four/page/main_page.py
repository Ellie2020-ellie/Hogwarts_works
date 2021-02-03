# -- coding: utf-8 -
from appium_work_four.base_page import BasePage
from appium_work_four.page.market_page import MarketPage


class MainPage(BasePage):
    def click_market(self):
        # self.find_and_click((MobileBy.XPATH, '//*[@text="行情"]'))
        self.run_step("./main_page.yaml", "click_market")
        return MarketPage(self.driver)
