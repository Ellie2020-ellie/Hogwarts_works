from appium.webdriver.common.mobileby import MobileBy

from appium_work_four.base_page import BasePage
from appium_work_four.page.market_search_page import MarketSearchPage


class MarketPage(BasePage):
    def click_search(self):
        # self.find_and_click(
        #     (MobileBy.ID, 'com.xueqiu.android:id/action_search'))
        self.run_step("./market_page.yaml", "click_search")
        return MarketSearchPage(self.driver)
