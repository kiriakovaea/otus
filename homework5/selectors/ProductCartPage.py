from selenium.webdriver.common.by import By


class ProductCartPage:
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

