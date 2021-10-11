from .locators import *
from helpers.elements import *
from helpers.page import BasePage


class ContractNumber(BaseElement):
    locator = ContractAddPageLocators.CONTRACT_NUMBER

class SignDate(BaseElement):
    locator = ContractAddPageLocators.SIGN_DATE

class StartDate(BaseElement):
    locator = ContractAddPageLocators.START_DATE

class EndDate(BaseElement):
    locator = ContractAddPageLocators.END_DATE

class ContractAddPage(BasePage):
    number = ContractNumber()
    sign_date = SignDate()
    start_date = StartDate()
    end_date = EndDate()

    def click_add_btn(self):
        element = self.find_element_delay(*ContractAddPageLocators.ADD_BUTTON)
        element.click()

    def open_contract_type(self):
        element = self.find_element_delay(*ContractAddPageLocators.CONTRACT_TYPE)
        element.click()

    def select_type(self, con_type):
        self.open_contract_type()
        element = self.find_element_delay(ContractAddPageLocators.CONTRACT_TYPE_ITEM(con_type))
        element.click()

    def fill_name(self, label, name):
        element = self.find_element_delay(ContractAddPageLocators.NAME_INPUT(label))
        element.click()
        element.send_keys(name)

    def click_add_members_btn(self):
        element = self.find_element_delay(*ContractAddPageLocators.ADD_MEMBERS_BUTTON)
        element.click()

    def get_member_card_by_index(self, index):
        elements = self.find_elements_delay(*ContractAddPageLocators.MEMBER_CARD)
        return elements[index]

class ContractorName(ValueElement):
    locator = ContractAddPageLocators.CONTRACTOR_INPUT

class ContractorRole(TextElement):
    locator = ContractAddPageLocators.CONTRACTOR_ROLE

class Member(BasePage):
    contractor_name = ContractorName()
    contractor_role = ContractorRole()

    def __init__(self, driver, parent_el):
        self.parent = parent_el
        super().__init__(driver)

    def click_input_role(self):
        element = self.find_element_delay(*ContractAddPageLocators.ROLE_SELECT)
        element.click()

    def select_role(self, role):
        self.click_input_role()
        element = self.driver.find_element_by_xpath(ContractAddPageLocators.ROLE_ITEM(role))
        element.click()

    def click_save_btn(self):
        element = self.find_element_delay(*ContractAddPageLocators.SAVE_BUTTON)
        element.click()

    def get_contractors(self):
        elements = self.find_elements_delay(*ContractAddPageLocators.CONTRACTORS_LIST)
        return elements

    def select_contractor_by_index(self, index):
        elements = self.get_contractors()
        elements[index].click()
