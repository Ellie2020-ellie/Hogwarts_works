import pytest
import yaml

from appium_work_one.page.app import App


def get_data():
    with open("../data/member.yaml") as f:
        data = yaml.safe_load(f)
        return data


class TestAddMember:
    @pytest.mark.parametrize("name,emil", get_data()["add_member"])
    def test_add_contact(self, name, emil):
        toast = App().start_app().goto_main().click_Contact().click_manual_add_member().edit_name(name).edit_emil(
            emil).click_save().get_toast()
        assert toast == "添加成功"
