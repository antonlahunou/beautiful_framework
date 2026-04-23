import pytest

@pytest.fixture(autouse=True, scope='function')
def say_hello():
    print("hello")