import allure
from homework6.pages.AdminPage import AdminPage


class TestAdminPage:
    @allure.feature('Admin Page')
    @allure.story('Check elements and forgot password')
    def test_admin_page(self, browser):
        admin_page = AdminPage(browser)
        admin_page.find_element_by_locator(AdminPage.LOGO)
        admin_page.find_element_by_locator(AdminPage.USERNAME_INPUT)
        admin_page.find_element_by_locator(AdminPage.PASSWORD_INPUT)
        admin_page.find_element_by_locator(AdminPage.SUBMIT_BUTTON)
        forgotten_password = admin_page.find_element_by_locator(AdminPage.FORGOTTEN_PASSWORD_LINK)
        admin_page._simple_click_element(forgotten_password)
        forgotten_password_text = admin_page.waiting_element_visible(AdminPage.FORGOTTEN_PASSWORD_TEXT)
        assert forgotten_password_text.text == 'Forgot Your Password?'

    @allure.feature('Admin Page')
    @allure.story('Add new product')
    def test_add_new_product(self, browser):
        admin_page = AdminPage(browser)
        admin_page.send_keys_into_element(AdminPage.USERNAME_INPUT, keys='admin')
        admin_page.send_keys_into_element(AdminPage.PASSWORD_INPUT, keys='admin')
        admin_page.click_element(AdminPage.SUBMIT_BUTTON)
        admin_page.click_element(AdminPage.CATALOG_MENU)
        admin_page.wait_and_click_element(AdminPage.PRODUCTS_MENU)
        admin_page.click_element(AdminPage.ADD_NEW_PRODUCT_BUTTON)
        admin_page.send_keys_into_element(AdminPage.PRODUCT_NAME_INPUT, keys='new_product_name')
        admin_page.click_element(AdminPage.SAVE_BUTTON)
        alert = admin_page.waiting_element_visible(AdminPage.PERMISSION_ALERT).text
        assert alert == 'Warning: You do not have permission to modify products!\n×'

    @allure.feature('Admin Page')
    @allure.story('Delete product')
    def test_delete_product(self, browser):
        admin_page = AdminPage(browser)
        admin_page.send_keys_into_element(AdminPage.USERNAME_INPUT, keys='admin')
        admin_page.send_keys_into_element(AdminPage.PASSWORD_INPUT, keys='admin')
        admin_page.click_element(AdminPage.SUBMIT_BUTTON)
        admin_page.click_element(AdminPage.CATALOG_MENU)
        admin_page.wait_and_click_element(AdminPage.PRODUCTS_MENU)
        admin_page.wait_and_click_element(AdminPage.FIRST_ELEMENT_CHECKBOX)
        admin_page.click_element(AdminPage.DELETE_BUTTON)
        admin_page.accept_alert()
        alert = admin_page.waiting_element_visible(AdminPage.PERMISSION_ALERT).text
        assert alert == 'Warning: You do not have permission to modify products!\n×'
