import yaml
from amway.amway_ui.base_page import BasePage
from amway.amway_ui.page.car_page import CarPage
from amway.amway_ui.page.result_search_page import ResultSearchPage


def handle_black(fun):
    def run(*args, **kwargs):
        with open('../data/black_list.yaml', 'r') as f:
            black_lists = yaml.safe_load(f)
            try:
                for black in black_lists:
                    black_count = args[0].driver.find_elements(*black)
                    if len(black_count) > 0:
                        black_count[0].click()
            except Exception as msg:
                fun(*args, **kwargs)
            finally:
                fun(*args, **kwargs)

    return run


class HomePage(BasePage):

    @handle_black
    def goto_result_search_page(self):
        with open('../data/home_page.yaml') as f:
            datas = yaml.safe_load(f)
        product_locator = datas['search_product']['search_product_input']['locator']
        click_element = datas['search_product']['click_search']['locator']
        self.find_and_input(*product_locator)
        self.find_and_click(*click_element)
        return ResultSearchPage(self.driver)

    def goto_car_page(self):
        with open('../data/home_page.yaml') as f:
            datas = yaml.safe_load(f)
        click_add_car = datas['goto_car']['locator']
        self.find_and_click(*click_add_car)
        return CarPage(self.driver)
