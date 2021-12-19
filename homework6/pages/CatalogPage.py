from selenium.webdriver.common.by import By

from homework6.pages.BasePage import BasePage


class CatalogPage(BasePage):
    LOGO = (By.CLASS_NAME, "img-thumbnail")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    SORTED_BY_BUTTON = (By.ID, 'input-sort')
    SHOW_LIMIT_BUTTON = (By.ID, 'input-limit')
    FIRST_IMAGE = (By.LINK_TEXT, 'Apple Cinema 30"')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.get(browser.url + "index.php?route=product/category&path=20")

    def check_first_element(self, element):
        assert element.text == 'Apple Cinema 30"'
