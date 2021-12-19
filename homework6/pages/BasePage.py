from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def accept_alert(self):
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            raise Exception('Cant accept alert')

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @staticmethod
    def _simple_click_element(element):
        element.click()

    def waiting_element_visible(self, locator):
        return self._verify_element_presence(locator)

    def find_element_by_locator(self, locator):
        return self.browser.find_element(*locator)

    def send_keys_into_element(self, locator, keys):
        element = self.find_element_by_locator(locator)
        element.clear()
        element.send_keys(keys)
        return element

    def wait_and_click_element(self, locator):
        element = self._verify_element_presence(locator)
        self._simple_click_element(element)

    def click_element(self, locator):
        element = self.find_element_by_locator(locator)
        self._simple_click_element(element)
