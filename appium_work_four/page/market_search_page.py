from appium.webdriver.common.mobileby import MobileBy

from appium_work_four.base_page import BasePage


class MarketSearchPage(BasePage):
    def search(self):
        # self.find_and_input((MobileBy.ID, "com.xueqiu.android:id/search_input_text"), 'ellie')
        self.run_step("./market_search_page.yaml", "search")
        return True
