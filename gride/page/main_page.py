# -- coding: utf-8 -
from gride.base_page import BasePage
from gride.page.market_page import MarketPage


class MainPage(BasePage):
    def click_market(self):
        # self.find_and_click((MobileBy.XPATH, '//*[@text="行情"]'))
        self.run_step("main_page.yaml", "click_market")
        return MarketPage(self.driver)
