from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_and_click(self, locator):
        self.driver.find_element(*locator).click()

    def find_and_input(self, locator, input_info):
        self.driver.find_element(*locator).send_keys(input_info)

    def find_and_text(self, locator):
        return self.driver.find_element(*locator).text

    def find(self, locator):
        return self.driver.find_element(*locator)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)

    def keycode(self):
        self.driver.press_keycode(29)
