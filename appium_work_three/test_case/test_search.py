from appium_work_three.app import App


class TestSearch:
    def test_mark_search(self):
        App().start_app().goto_main().click_market().click_search().search()
