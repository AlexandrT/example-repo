from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class FirstName(BaseElement):
    locator = RepresentAddPageLocators.FIRST_NAME_INPUT

class LastName(BaseElement):
    locator = RepresentAddPageLocators.LAST_NAME_INPUT

class MiddleName(BaseElement):
    locator = RepresentAddPageLocators.MIDDLE_NAME_INPUT

class Ssn(BaseElement):
    locator = RepresentAddPageLocators.SSN_INPUT

class RepresentAddPage(BasePage):
    first_name = FirstName()
    last_name = LastName()
    middle_name = MiddleName()
    ssn = Ssn()

    def click_add_btn(self):
        element = self.find_element_delay(*RepresentAddPageLocators.ADD_BUTTON)
        element.click()

    def select_country(self, country):
        self.click_country_input()
        element = self.find_element_delay(RepresentAddPageLocators.COUNTRY_ITEM(country))
        element.click()

    def click_country_input(self):
        element = self.find_element_delay(*RepresentAddPageLocators.COUNTRY)
        element.click()
