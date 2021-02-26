import pytest


@pytest.fixture(scope="session")
def hello():
    print('hello>>>>>>>>')
