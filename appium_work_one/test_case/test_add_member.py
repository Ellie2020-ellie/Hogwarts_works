import pytest

from appium_work_one.page.app import App


class TestAddMember:
    def test_add_contact(self):
        toast = App().start_app().goto_main().click_Contact().click_manual_add_member().edit_name('haha').edit_emil(
            'test444@qq.com').click_save().get_toast()
        assert toast == "添加成功"
