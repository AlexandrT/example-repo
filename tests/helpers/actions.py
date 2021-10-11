import allure

from helpers.auth.signin_page import *
from lib.config import settings


@allure.step("Authorization")
def authorize(driver, base_url):
    driver.get(f"{base_url}/login")

    signin_page = SignInPage(driver)

    signin_page.login = settings.VALID_CREDENTIALS['login']
    signin_page.password = settings.VALID_CREDENTIALS['password']
    signin_page.click_signin_btn()
