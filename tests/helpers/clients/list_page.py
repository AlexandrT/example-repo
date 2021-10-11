from .locators import *
from helpers.page import BasePage


class ClientsListPage(BasePage):
    def click_add_btn(self):
        element = self.find_element_delay(*ClientsListPageLocators.ADD_BUTTON)
        element.click()
