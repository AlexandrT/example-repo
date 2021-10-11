from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class FullName(BaseElement):
    locator = ContractorLegalAddPageLocators.FULLNAME_INPUT

class Name(BaseElement):
    locator = ContractorLegalAddPageLocators.NAME_INPUT

class Inn(BaseElement):
    locator = ContractorLegalAddPageLocators.INN_INPUT

class DateFrom(BaseElement):
    locator = ContractorLegalAddPageLocators.DATE_FROM

class ContractorLegalAddPage(BasePage):
    full_name = FullName()
    name = Name()
    inn = Inn()
    date_from = DateFrom()

    def click_add_btn(self):
        element = self.find_element_delay(*ContractorLegalAddPageLocators.ADD_BUTTON)
        element.click()

    def select_country(self, country):
        self.click_country_input()
        element = self.find_element_delay(ContractorLegalAddPageLocators.COUNTRY_ITEM(country))
        element.click()

    def click_country_input(self):
        element = self.find_element_delay(*ContractorLegalAddPageLocators.COUNTRY)
        element.click()
