from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.CLASS_NAME, "input-group-btn")
    MAIN_IMAGE = (By.CLASS_NAME, "img-responsive")
    LOGO = (By.ID, 'logo')
    CART = (By.ID, 'cart')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'p.text-center')
