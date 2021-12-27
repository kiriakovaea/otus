import allure
from selenium.webdriver.common.by import By

from homework6.pages.BasePage import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    TELEPHONE = (By.NAME, "telephone")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm")
    PRIVATE_POLICE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    WARNING_INFO = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    REGISTRATION_SUCCESS = (By.ID, "content")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(browser.url + "index.php?route=account/register")

    def check_success_registration(self, element):
        try:
            assert 'Your Account Has Been Created!' in element.text
        except AssertionError:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            self.logger.error("Registration was failed with error: {}".format(element.text))
            raise AssertionError("Registration was failed with error: {}".format(element.text))
