from amway.amway_ui.page.login_page import LoginPage


class TestSearchProduct:
    def test_search(self):
        LoginPage().login_success().goto_result_search_page()
            # .add_product_to_car()
            # .goto_car_page()
