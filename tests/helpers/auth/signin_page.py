from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class Login(BaseElement):
    locator = SignInPageLocators.LOGIN_INPUT

class Password(BaseElement):
    locator = SignInPageLocators.PASSWORD_INPUT

class ErrorMessage(TextElement):
    locator = SignInPageLocators.ERROR_MESSAGE

class SignInPage(BasePage):
    login = Login()
    password = Password()
    error_message = ErrorMessage()

    def click_signin_btn(self):
        element = self.find_element_delay(*SignInPageLocators.SIGNIN_BUTTON)
        element.click()
