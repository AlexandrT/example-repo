from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import *
from helpers.page import BasePage
from helpers.elements import *


class ContractNumber(ValueElement):
    locator = ContractShowPageLocators.CONTRACT_NUMBER

class ContractName(ValueElement):
    locator = ContractShowPageLocators.CONTRACT_NAME

class SignDate(ValueElement):
    locator = ContractShowPageLocators.SIGN_DATE

class StartDate(ValueElement):
    locator = ContractShowPageLocators.START_DATE

class EndDate(ValueElement):
    locator = ContractShowPageLocators.END_DATE

class ContractShowPage(BasePage):
    number = ContractNumber()
    name = ContractName()
    sign_date = SignDate()
    start_date = StartDate()
    end_date = EndDate()

    def check_contract_card(self):
        element_present = EC.presence_of_element_located(ContractShowPageLocators.CONTRACT_CARD)
        WebDriverWait(self.driver, 5).until(element_present)
