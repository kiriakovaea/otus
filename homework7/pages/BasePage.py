import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _verify_element_presence(self, locator: tuple):
        self.logger.info("Verify element present: {}".format(locator))
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            self.logger.error("Cant find element by locator: {}".format(locator))
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step('Принимаем браузерное сообщение')
    def accept_alert(self):
        try:
            self.logger.info("Accept browser allert")
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            self.logger.error("Cant accept alert")
            raise Exception('Cant accept alert')

    def _element(self, locator: tuple):
        self.logger.info("Return element presense: {}".format(locator))
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        self.logger.info("Click element after waiting: {}".format(element))
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        self.logger.info("Click element: {}".format(element))
        element.click()

    @allure.step('Дожидаемся отображения элемента {locator}')
    def waiting_element_visible(self, locator):
        self.logger.info("Waiting element visible: {}".format(locator))
        return self._verify_element_presence(locator)

    @allure.step('Поиск элемента по локатору {locator}')
    def find_element_by_locator(self, locator):
        self.logger.info("Find element by locator: {}".format(locator))
        return self.browser.find_element(*locator)

    @allure.step('Записываем значение {keys} в элемент {locator}')
    def send_keys_into_element(self, locator, keys):
        self.logger.info("Send keys {} in input {}".format(keys, locator))
        element = self.find_element_by_locator(locator)
        element.clear()
        element.send_keys(keys)
        return element

    @allure.step('Ожидаем элемент {locator} и делаем клик')
    def wait_and_click_element(self, locator):
        self.logger.info("Wait and click element: {}".format(locator))
        element = self._verify_element_presence(locator)
        self._simple_click_element(element)

    @allure.step('Делаем клик элемента {locator}')
    def click_element(self, locator):
        element = self.find_element_by_locator(locator)
        self._simple_click_element(element)
