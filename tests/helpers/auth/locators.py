from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    LOGIN_INPUT = (By.NAME, 'login')
    PASSWORD_INPUT = (By.NAME, 'password')

    SIGNIN_BUTTON = (By.XPATH, '//button[contains(@class, "mat-flat-button")]')

    ERROR_MESSAGE = (By.XPATH, '//h3[contains(@class, "error")]')
