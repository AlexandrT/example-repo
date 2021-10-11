import allure
import pytest

from helpers.dashboard.page import *
from helpers.clients.list_page import *
from helpers.clients.add_page import *
from helpers.clients.show_page import *
from helpers.contractors_legal.add_page import *
from helpers.represents.add_page import *
from helpers.utils import *
from helpers.actions import *
from helpers.models import *
from faker import Faker


@allure.feature("Clients")
class TestClient(BaseTest):
    def setup_method(self):
        fake = self.fake

        name = fake.company()
        self.contractor = Contractor(
            full_name = name,
            name = name,
            inn = fake.businesses_inn(),
            date_from = fake.date_between(start_date='-50d', end_date='-30d').strftime("%d.%m.%Y"),
            country = "Россия",
        )

        self.represent_count = 2
        self.represents = []
        for _ in range(self.represent_count):
            represent = Representer(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                middle_name = fake.middle_name(),
                ssn = fake.ssn(),
                country = fake.country(),
            )

            self.represents.append(represent)

        self.client = Client(
            name = fake.company()
        )

        self.not_existed_contractor = fake.text()

        self.new_client = Client(
            name = fake.company()
        )

    @allure.title("create with existed contractor")
    def test_create_client(self, selenium, base_url):
        authorize(selenium, base_url)

        #  with allure.step("navigate on dashboard"):
            #  dashboard_page = DashboardPage(selenium)
            #  dashboard_page.click_item_clients()

        with allure.step("create contractor via new client page"):
            clients_list_page = ClientsListPage(selenium)
            clients_list_page.click_add_btn()

            client_add_page = ClientAddPage(selenium)
            client_add_page.contractor = self.not_existed_contractor
            client_add_page.select_not_found(self.translator.get_translator('co.client.search_contractor.not_found'))

            contractor_add_page = ContractorLegalAddPage(selenium)
            contractor_add_page.full_name = self.contractor.full_name
            contractor_add_page.name = self.contractor.name
            contractor_add_page.inn = self.contractor.inn
            contractor_add_page.date_from = self.contractor.date_from
            contractor_add_page.select_country(self.contractor.country)

            contractor_add_page.click_add_btn()

        with allure.step("create client"):
            client_add_page = ClientAddPage(selenium)
            client_add_page.contractor = self.contractor.full_name
            client_add_page.select_contractor_by_name(self.contractor.full_name)
            client_add_page.name = self.client.name

            client_add_page.click_add_btn()

        with allure.step("assert info on show page"):
            client_show_page = ClientShowPage(selenium)
            #  assert self.client.name == client_show_page.name
            #  assert self.contractor.name == \
              #  client_show_page.get_contractor_name(self.translator.get_translator( \
                #  'co.client.show.contractor_name'))
        with allure.step("add represents"):
            for i, represent in enumerate(self.represents):
                client_show_page.click_add_represent_btn()
                represent_add_page = RepresentAddPage(selenium)
                represent_add_page.first_name = represent.first_name
                represent_add_page.last_name = represent.last_name
                represent_add_page.middle_name = represent.middle_name
                represent_add_page.ssn = represent.ssn
                represent_add_page.select_country(represent.country)

                represent_add_page.click_add_btn()

                represent_item = client_show_page.get_represent_item_by_index(i)

                represent_card = RepresentCard(selenium, represent_item)

                names = represent_card.represent_names

                assert represent.last_name in names
                assert represent.first_name in names
                assert represent.middle_name in names

                assert represent_card.represent_status == self.translator.get_translator('co.client.show.represent.status.no_access')

                client_show_page = ClientShowPage(selenium)

        with allure.step("remove represent"):
            client_show_page = ClientShowPage(selenium)

            represent_item = client_show_page.get_represent_item_by_index(1)
            represent_card = RepresentCard(selenium, represent_item)

            represent_card.click_more_button()
            represent_card.click_remove_button()

            assert len(client_show_page.get_represent_items()) == 1

        with allure.step("rename client"):
            client_show_page.click_rename_btn()

            assert client_show_page.old_name.get_attribute("value") == self.client.name

            client_show_page.new_name = self.new_client.name
            client_show_page.click_no_save_btn()

            assert self.client.name == client_show_page.name

            client_show_page.click_rename_btn()
            client_show_page.new_name = self.new_client.name
            client_show_page.click_save_btn()

            assert self.new_client.name == client_show_page.name
