from selenium.webdriver.common.by import By

from homework6.pages.BasePage import BasePage


class AdminPage(BasePage):
    LOGO = (By.ID, "header-logo")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    FORGOTTEN_PASSWORD_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    CATALOG_MENU = (By.XPATH, '//a[@href="#collapse1"]')
    PRODUCTS_MENU = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW_PRODUCT_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    PRODUCT_NAME_INPUT = (By.ID, "input-name1")
    SAVE_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    PERMISSION_ALERT = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    FIRST_ELEMENT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='42']")
    DELETE_BUTTON = (By.CLASS_NAME, "btn.btn-danger")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(browser.url + "/admin")
