from selenium.webdriver.common.by import By


class RegistrationPage:
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    PASSWORD_CONFIRM_INPUT = (By.ID, "input-confirm")
    CONFIRM_AGREE_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    WARNING_INFO = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")

