import yaml

from amway.amway_ui.base_page import BasePage


class ResultSearchPage(BasePage):
    def add_product_to_car(self):
        with open('../data/result_search_page.yaml.yaml', 'r') as f:
            datas = yaml.safe_load(f)
        print(datas, '>>>>>>>>>>>>>>>>>>')
        data = datas['add_product_to_car']['click_add_car']['locator']
        print('jjjjjjjjjjjjjjjjjjjjjjj')
        self.find_and_click(*data)

        # from amway.amway_ui.page.home_page import HomePage
        # return HomePage(self.driver)
