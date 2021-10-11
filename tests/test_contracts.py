import pytest

from helpers.dashboard.page import *
from helpers.contracts.add_page import *
from helpers.contracts.show_page import *
from helpers.contracts.list_page import *
from helpers.utils import *
from helpers.actions import *
from helpers.models import *
from random import randrange
from faker import Faker


@allure.feature("Contracts")
class TestContract(BaseTest):
    def setup_method(self):

        fake = Faker('ru_RU')
        number = randrange(10000)
        self.contract = Contract(
            number = number,
            name = f"Договор №{number}",
            sign_date = fake.date_between(start_date='-29d', end_date='-10d').strftime("%d.%m.%Y"),
            start_date = fake.date_between(start_date='-9d', end_date='today').strftime("%d.%m.%Y"),
            end_date = fake.date_between(start_date='+29d', end_date='+300d').strftime("%d.%m.%Y"),
        )

    @allure.title("create contract")
    @pytest.mark.nondestructive
    def test_create_contract(self, selenium, base_url):
        authorize(selenium, base_url)
        selenium.get(base_url)

        with allure.step("navigate on dashboard"):
            dashboard_page = DashboardPage(selenium)
            dashboard_page.click_item_contracts()

        with allure.step("create contract"):
            contracts_list_page = ContractsListPage(selenium)
            contracts_list_page.click_add_btn()

            contract_add_page = ContractAddPage(selenium)
            contract_add_page.number = self.contract.number
            contract_add_page.sign_date = self.contract.sign_date
            contract_add_page.start_date = self.contract.start_date
            contract_add_page.end_date = self.contract.end_date

            contract_add_page.select_type(self.translator.get_translator('co.contracts.list.types.contract.name'))

            contract_add_page.fill_name(self.translator.get_translator('co.contracts.new.name_placeholder'), self.contract.name)

            roles = self.translator.get_translator('co.contracts.list.types.contract.roles')

            for index, role in enumerate(roles):
                with allure.step(f"Add {role} in contract"):
                    contract_add_page.click_add_members_btn()

                    member_card = contract_add_page.get_member_card_by_index(index)

                    member = Member(selenium, member_card)
                    member.contractor_name = "   "
                    member.select_contractor_by_index(index)
                    member.select_role(role)

                    contractor_name = member.contractor_name

                    member.click_save_btn()

                    contract_add_page = ContractAddPage(selenium)

                    assert member.contractor_role == role
                    assert member.contractor_name == contractor_name

            contract_add_page.click_add_btn()

            contract_show_page = ContractShowPage(selenium)

            contract_show_page.check_contract_card()

            assert contract_show_page.number == str(self.contract.number)
            assert contract_show_page.name == self.contract.name
            #TODO bug from TODO-List
            #  assert contract_show_page.sign_date == self.contract.sign_date
            #  assert contract_show_page.start_date == self.contract.start_date
            #  assert contract_show_page.end_date == self.contract.end_date

        with allure.step("navigate on dashboard"):
            dashboard_page = DashboardPage(selenium)
            dashboard_page.click_item_contracts()

        with allure.step("Contracts list"):
            contracts_list_page = ContractsListPage(selenium)
            contracts_list_page.select_type(self.translator.get_translator('co.contracts.list.types.contract.name'))
            contracts_list_page.search = str(self.contract.number)
            time.sleep(1)

            contract_item = contracts_list_page.get_contract_item_by_index(0)

            contract_card = ContractCard(selenium, contract_item)

            assert get_first_line(contract_card.contract_number) == str(self.contract.number)
            assert get_first_line(contract_card.sign_date) == self.contract.sign_date
            assert get_first_line(contract_card.period) == f"{self.contract.start_date} — {self.contract.end_date}"
            assert get_first_line(contract_card.status) == self.translator.get_translator("co.contracts.list.status.current")
            assert get_int(contract_card.members_count) == len(roles)

    @allure.title("create GDFO")
    @pytest.mark.nondestructive
    def test_create_gdfo(self, selenium, base_url):
        authorize(selenium, base_url)

        with allure.step("navigate on dashboard"):
            dashboard_page = DashboardPage(selenium)
            dashboard_page.click_item_contracts()

        with allure.step("create GDFO"):
            contracts_list_page = ContractsListPage(selenium)
            contracts_list_page.click_add_btn()

            contract_add_page = ContractAddPage(selenium)
            contract_add_page.number = self.contract.number
            contract_add_page.sign_date = self.contract.sign_date
            contract_add_page.start_date = self.contract.start_date
            contract_add_page.end_date = self.contract.end_date

            contract_add_page.select_type(self.translator.get_translator('co.contracts.list.types.gdfo.name'))

            roles = self.translator.get_translator('co.contracts.list.types.gdfo.roles')

            for index, role in enumerate(roles):
                with allure.step(f"Add {role} in contract"):
                    contract_add_page.click_add_members_btn()

                    member_card = contract_add_page.get_member_card_by_index(index)

                    member = Member(selenium, member_card)
                    member.contractor_name = "   "
                    member.select_contractor_by_index(index)
                    member.select_role(role)

                    contractor_name = member.contractor_name

                    member.click_save_btn()

                    contract_add_page = ContractAddPage(selenium)

                    assert member.contractor_role == role
                    assert member.contractor_name == contractor_name

            contract_add_page.click_add_btn()

            contract_show_page= ContractShowPage(selenium)

            contract_show_page.check_contract_card()

            assert contract_show_page.number == str(self.contract.number)
            #TODO bug from TODO-List
            #  assert contract_show_page.sign_date == self.contract.sign_date
            #  assert contract_show_page.start_date == self.contract.start_date
            #  assert contract_show_page.end_date == self.contract.end_date

        with allure.step("navigate on dashboard"):
            dashboard_page = DashboardPage(selenium)
            dashboard_page.click_item_contracts()

        with allure.step("Contracts list"):
            contracts_list_page = ContractsListPage(selenium)
            contracts_list_page.search = str(self.contract.number)
            time.sleep(1)

            contract_item = contracts_list_page.get_contract_item_by_index(0)

            contract_card = ContractCard(selenium, contract_item)

            assert get_first_line(contract_card.contract_number) == str(self.contract.number)
            assert get_first_line(contract_card.sign_date) == self.contract.sign_date
            assert get_first_line(contract_card.period) == f"{self.contract.start_date} — {self.contract.end_date}"
            assert get_first_line(contract_card.status) == self.translator.get_translator("co.contracts.list.status.current")
            assert get_int(contract_card.members_count) == len(roles)

