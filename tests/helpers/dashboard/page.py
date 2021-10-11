from .locators import *
from helpers.page import BasePage


class DashboardPage(BasePage):
    def click_item_clients(self):
        element = self.find_element_delay(*DashboardPageLocators.CLIENTS_ITEM)
        element.click()

    def click_item_contracts(self):
        element = self.find_element_delay(*DashboardPageLocators.CONTRACTS_ITEM)
        element.click()
