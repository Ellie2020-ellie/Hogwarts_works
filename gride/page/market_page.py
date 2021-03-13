from appium.webdriver.common.mobileby import MobileBy

from gride.base_page import BasePage
from gride.page.market_search_page import MarketSearchPage


class MarketPage(BasePage):
    def click_search(self):
        # self.find_and_click(
        #     (MobileBy.ID, 'com.xueqiu.android:id/action_search'))
        self.run_step("market_page.yaml", "click_search")
        return MarketSearchPage(self.driver)
