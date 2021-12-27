from selenium.webdriver.common.by import By


class AdminPage:
    LOGO = (By.ID, "header-logo")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    FORGOTTEN_PASSWORD_TEXT = (By.CSS_SELECTOR, "h1.panel-title")