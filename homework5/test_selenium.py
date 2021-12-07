from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from homework5.selectors.AdminPage import AdminPage
from homework5.selectors.CatalogPage import CatalogPage
from homework5.selectors.MainPage import MainPage
from homework5.selectors.ProductCartPage import ProductCartPage
from homework5.selectors.RegistrationPage import RegistrationPage


def test_main_page(browser):
    browser.find_element(*MainPage.SEARCH_INPUT)
    browser.find_element(*MainPage.SEARCH_BUTTON)
    browser.find_element(*MainPage.MAIN_IMAGE)
    browser.find_element(*MainPage.LOGO)
    cart_button = browser.find_element(*MainPage.CART)
    cart_button.click()
    empty_cart_text = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(MainPage.EMPTY_CART_TEXT))
    assert empty_cart_text.text == 'Your shopping cart is empty!'


def test_admin_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*AdminPage.LOGO)
    browser.find_element(*AdminPage.USERNAME_INPUT)
    browser.find_element(*AdminPage.PASSWORD_INPUT)
    browser.find_element(*AdminPage.SUBMIT_BUTTON)
    forgotten_password = browser.find_element(*AdminPage.FORGOTTEN_PASSWORD_LINK)
    forgotten_password.click()
    forgotten_password_text = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(AdminPage.FORGOTTEN_PASSWORD_TEXT))
    assert forgotten_password_text.text == 'Forgot Your Password?'


def test_catalog_page(browser):
    browser.get(browser.url + "index.php?route=product/category&path=20")
    browser.find_element(*CatalogPage.LOGO)
    browser.find_element(*CatalogPage.SHOW_LIMIT_BUTTON)
    browser.find_element(*CatalogPage.SORTED_BY_BUTTON)
    list_view = browser.find_element(*CatalogPage.LIST_VIEW_BUTTON)
    list_view.click()
    first_list_image = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(CatalogPage.FIRST_IMAGE))
    assert first_list_image.text == 'Apple Cinema 30"'
    table_view = browser.find_element(*CatalogPage.GRID_VIEW_BUTTON)
    table_view.click()
    first_table_image = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(CatalogPage.FIRST_IMAGE))
    assert first_table_image.text == 'Apple Cinema 30"'
    browser.find_element(*CatalogPage.SORTED_BY_BUTTON)


def test_product_page(browser):
    browser.get(browser.url + "index.php?route=product/product&path=20&product_id=42")
    browser.find_element(*ProductCartPage.MAIN_PHOTO)
    browser.find_element(*ProductCartPage.LIKE_BUTTON)
    browser.find_element(*ProductCartPage.DESCRIPTION)
    browser.find_element(*ProductCartPage.SPECIFICATION).click()
    processor_info = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(ProductCartPage.PROCESSOR_INFO))
    assert processor_info.text == 'Clockspeed 100mhz'
    browser.find_element(*ProductCartPage.ADD_TO_CART_BUTTON)
    browser.find_element(*ProductCartPage.REVIEWERS).click()
    browser.find_element(*ProductCartPage.CONTINUE_BUTTON).click()
    warning_info = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(ProductCartPage.WARNING_INFO))
    assert warning_info.text == 'Warning: Please select a review rating!'


def test_registration_page(browser):
    browser.get(browser.url + "index.php?route=account/register")
    browser.find_element(*RegistrationPage.FIRST_NAME_INPUT)
    browser.find_element(*RegistrationPage.LAST_NAME_INPUT)
    browser.find_element(*RegistrationPage.EMAIL_INPUT)
    browser.find_element(*RegistrationPage.TELEPHONE_INPUT)
    browser.find_element(*RegistrationPage.PASSWORD_INPUT)
    browser.find_element(*RegistrationPage.PASSWORD_CONFIRM_INPUT)
    browser.find_element(*RegistrationPage.CONFIRM_AGREE_CHECKBOX)
    browser.find_element(*RegistrationPage.CONTINUE_BUTTON).click()
    warning_info = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located(RegistrationPage.WARNING_INFO))
    assert warning_info.text == 'Warning: You must agree to the Privacy Policy!'
