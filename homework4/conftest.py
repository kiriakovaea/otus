import pytest as pytest

from api_client import Client, FunctionClient


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://ya.ru', help="api url")
    parser.addoption("--status_code", action="store", default=200, help="status code")


@pytest.fixture(scope="session")
def client(pytestconfig):
    url = pytestconfig.getoption("url")
    return Client(url)


@pytest.fixture(scope="session")
def module_client(pytestconfig):
    url = pytestconfig.getoption("url")
    status_code = pytestconfig.getoption("status_code")
    return FunctionClient(url, status_code)
