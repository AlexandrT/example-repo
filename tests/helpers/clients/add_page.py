from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class Contractor(BaseElement):
    locator = ClientAddPageLocators.CONTRACTOR_INPUT

class ClientName(BaseElement):
    locator = ClientAddPageLocators.NAME_INPUT

class Title(TextElement):
    locator = ClientAddPageLocators.TITLE

class ClientAddPage(BasePage):
    contractor = Contractor()
    name = ClientName()
    title = Title()

    def click_add_btn(self):
        element = self.find_element_delay(*ClientAddPageLocators.ADD_BUTTON)
        element.click()

    def get_contractors(self):
        elements = self.find_elements_delay(*ClientAddPageLocators.CONTRACTORS_LIST)
        return elements

    def select_contractor_by_name(self, name):
        elements = self.get_contractors()

        for el in elements:
            if el.text == name:
                el.click()
                break

    def select_not_found(self, text):
        element = self.find_element_delay(ClientAddPageLocators.NOT_FOUND_ITEM(text))
        element.click()
