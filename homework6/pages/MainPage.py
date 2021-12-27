from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework6.pages.BasePage import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.CLASS_NAME, "input-group-btn")
    MAIN_IMAGE = (By.CLASS_NAME, "img-responsive")
    LOGO = (By.ID, 'logo')
    CART = (By.ID, 'cart')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'p.text-center')
    CURRENCY_CHECKBOX = (By.CLASS_NAME, 'btn.btn-link.dropdown-toggle')
    EUR_CURRENCY = (By.CSS_SELECTOR, "button[type='button'][name='EUR']")
    USD_CURRENCY = (By.CSS_SELECTOR, "button[type='button'][name='USD']")
    FIRST_ELEMENT_PRICE = (By.CLASS_NAME, "price-tax")

    def find_search_input(self):
        return self.browser.find_element(*MainPage.SEARCH_INPUT)

    def find_search_button(self):
        return self.browser.find_element(*MainPage.SEARCH_BUTTON)

    def find_main_image(self):
        return self.browser.find_element(*MainPage.MAIN_IMAGE)

    def get_empty_shopping_cart_text(self):
        self.browser.find_element(*MainPage.CART).click()
        empty_cart_text = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(MainPage.EMPTY_CART_TEXT))
        return empty_cart_text
