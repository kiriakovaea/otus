from selenium.webdriver.common.by import By

from homework6.pages.BasePage import BasePage


class ProductCartPage(BasePage):
    MAIN_PHOTO = (By.CSS_SELECTOR, "a.thumbnail"[0])
    LIKE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']"[0])
    COMPARE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']"[0])
    DESCRIPTION = (By.XPATH, '//a[@href="#tab-description"]')
    SPECIFICATION = (By.XPATH, '//a[@href="#tab-specification"]')
    ADD_TO_CART_BUTTON = (By.ID, 'button-cart')
    PROCESSOR_INFO = (By.CSS_SELECTOR, 'table.table-bordered tbody')
    REVIEWERS = (By.LINK_TEXT, 'Reviews (0)')
    CONTINUE_BUTTON = (By.ID, 'button-review')
    WARNING_INFO = (By.CSS_SELECTOR, 'div.alert.alert-danger.alert-dismissible')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(browser.url + "index.php?route=product/product&path=20&product_id=42")
