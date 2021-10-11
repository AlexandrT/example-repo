from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class ContractType(BaseElement):
    locator = ContractsListPageLocators.TYPE_SELECT

class Search(BaseElement):
    locator = ContractsListPageLocators.SEARCH_INPUT

class ContractsListPage(BasePage):
    contract_type = ContractType()
    search = Search()

    def click_add_btn(self):
        element = self.find_element_delay(*ContractsListPageLocators.ADD_BUTTON)
        element.click()

    def click_select_type(self):
        element = self.find_element_delay(*ContractsListPageLocators.TYPE_SELECT)
        element.click()

    def select_type(self, contract_type):
        self.click_select_type()
        element = self.find_element_delay(ContractsListPageLocators.TYPE_ITEM(contract_type))
        element.click()

    def get_contract_items(self):
        elements = self.find_elements_delay(*ContractsListPageLocators.CONTRACT_ITEM)
        return elements

    def get_contract_item_by_index(self, index):
        elements = self.get_contract_items()
        return elements[index]

class ContractNumber(TextElement):
    locator = ContractsListPageLocators.CONTRACT_NAME

class MembersCount(TextElement):
    locator = ContractsListPageLocators.MEMBERS_COUNT

class SignDate(TextElement):
    locator = ContractsListPageLocators.SIGN_DATE

class Period(TextElement):
    locator = ContractsListPageLocators.PERIOD

class Status(TextElement):
    locator = ContractsListPageLocators.STATUS

class ContractCard(BasePage):
    contract_number = ContractNumber()
    members_count = MembersCount()
    sign_date = SignDate()
    period = Period()
    status = Status()

    def __init__(self, driver, parent_el):
        self.parent = parent_el
        super().__init__(driver)
