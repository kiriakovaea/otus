import datetime
import logging
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("/Users/kirakovaekaterina/Desktop/OTUS/otus/homework7"))
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="172.20.10.2")
    parser.addoption("--bversion", action="store", default="95.0")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bversion")

    logger = logging.getLogger('driver')
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    if executor == "local":
        if browser == "chrome":
            service = Service(executable_path=drivers + "/chromedriver")
            driver = webdriver.Chrome(service=service)
        elif browser == "firefox":
            service = Service(executable_path=drivers + "/geckodriver")
            driver = webdriver.Firefox(service=service)
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=drivers + "/operadriver")
        else:
            raise Exception("Driver not supported")

    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Ekaterina",
            'goog:chromeOptions': {}
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )

    driver.maximize_window()

    driver.test_name = test_name
    driver.log_level = log_level

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    driver.get(url)
    driver.url = url
    return driver
