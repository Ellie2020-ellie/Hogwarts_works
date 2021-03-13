import pytest


@pytest.mark.parametrize("name", ["燕春01", "发哥02"])
def test_hook(name):
    print('hello')
    print(name)


def test_cmdline(cmdoption):
    print(cmdoption,'>>>')
