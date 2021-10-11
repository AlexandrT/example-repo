import time
import pytest
import allure

from faker import Faker
from helpers.auth.signin_page import *
from helpers.utils import *
from helpers.support.assertions import *
from lib.config import settings


@allure.feature("Authorization")
class TestAuth(BaseTest):
    def setup_method(self):
        fake = self.fake

        self.wrong_password = fake.text()

    @allure.title("with incorrect credentials")
    @pytest.mark.nondestructive
    def test_bad_credentials(self, selenium, base_url):
        selenium.get(base_url)

        signin_page = SignInPage(selenium)

        signin_page.login = settings.VALID_CREDENTIALS['login']
        signin_page.password = self.wrong_password
        signin_page.click_signin_btn()

        assert signin_page.error_message == self.translator.get_translator('co.signin.error')

    @allure.title("with empty credentials")
    @pytest.mark.nondestructive
    def test_empty_credentials(self, selenium, base_url):
        selenium.get(base_url)

        signin_page = SignInPage(selenium)

        signin_page.login = ""
        signin_page.password = ""
        signin_page.click_signin_btn()

        assert_field_error(signin_page.login)
        assert_field_error(signin_page.password)
