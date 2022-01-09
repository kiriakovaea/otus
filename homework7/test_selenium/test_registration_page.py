import allure
from homework6.pages.RegisterPage import RegistrationPage


class TestRegistrationPage:
    @allure.feature('Registration Page')
    @allure.story('Registration new person with exist keys')
    def test_registration_page(self, browser):
        registration_page = RegistrationPage(browser)
        registration_page.send_keys_into_element(RegistrationPage.FIRST_NAME, keys='test_new_name')
        registration_page.send_keys_into_element(RegistrationPage.LAST_NAME, keys='test_new_last_name')
        registration_page.send_keys_into_element(RegistrationPage.EMAIL, keys='test_new_email@mail.ru')
        registration_page.send_keys_into_element(RegistrationPage.TELEPHONE, keys='+79001001022')
        registration_page.send_keys_into_element(RegistrationPage.PASSWORD, keys='Qwerty123')
        registration_page.send_keys_into_element(RegistrationPage.CONFIRM_PASSWORD, keys='Qwerty123')
        registration_page.click_element(RegistrationPage.PRIVATE_POLICE_CHECKBOX)
        registration_page.click_element(RegistrationPage.CONTINUE_BUTTON)
        registration_page.check_success_registration(registration_page.find_element_by_locator(RegistrationPage.REGISTRATION_SUCCESS))
