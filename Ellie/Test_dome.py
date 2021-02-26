import pytest


class TestDemo:
    @pytest.mark.f
    def test_est(self, hello):
        print(hello)
        print('test')
