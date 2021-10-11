from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class OldName(BaseElement):
    locator = ClientShowPageLocators.OLD_NAME

class NewName(BaseElement):
    locator = ClientShowPageLocators.NEW_NAME

class Name(TextElement):
    locator = ClientShowPageLocators.NAME

class ClientShowPage(BasePage):
    name = Name()
    old_name = OldName()
    new_name = NewName()

    def get_contractor_name(self, c_name):
        element = self.find_element_delay(ClientShowPageLocators.CONTRACTOR_NAME(c_name))
        return element.get_attribute('value')

    def click_rename_btn(self):
        element = self.find_element_delay(*ClientShowPageLocators.RENAME_BUTTON)
        element.click()

    def click_save_btn(self):
        element = self.find_element_delay(*ClientShowPageLocators.SAVE_BUTTON)
        element.click()

    def click_no_save_btn(self):
        element = self.find_element_delay(*ClientShowPageLocators.NO_SAVE_BUTTON)
        element.click()

    def click_add_represent_btn(self):
        element = self.find_element_delay(*ClientShowPageLocators.ADD_REPRESENT_BUTTON)
        element.click()

    def get_represent_items(self):
        elements = self.find_elements_delay(*ClientShowPageLocators.REPRESENT_ITEM)
        return elements

    def get_represent_item_by_index(self, index):
        elements = self.get_represent_items()
        return elements[index]

class RepresentNames(TextElement):
    locator = ClientShowPageLocators.REPRESENT_NAMES

class RepresentStatus(TextElement):
    locator = ClientShowPageLocators.REPRESENT_STATUS

class RepresentCard(BasePage):
    represent_names = RepresentNames()
    represent_status = RepresentStatus()

    def __init__(self, driver, parent_el):
        self.parent = parent_el
        super().__init__(driver)

    def click_more_button(self):
        element = self.find_element_delay(*ClientShowPageLocators.REPRESENT_MORE_BUTTON)
        element.click()

    def click_remove_button(self):
        element = self.find_element_delay(*ClientShowPageLocators.REPRESENT_REMOVE_BUTTON)
        element.click()
