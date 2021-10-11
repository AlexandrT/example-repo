import time
import pytest

from helpers.contractors_legal.add_page import *
from helpers.clients.add_page import *
from helpers.utils import *
from helpers.actions import *
from helpers.models import *
from faker import Faker


@allure.feature("Contractors legal")
class TestContractorsLegal(BaseTest):
    def setup_method(self):
        fake = Faker('ru_RU')

        name = fake.company()
        self.contractor = Contractor(
            full_name = name,
            name = name,
            inn = fake.businesses_inn(),
            date_from = fake.date_between(start_date='-50d', end_date='-30d').strftime("%d.%m.%Y"),
            country = fake.country(),
        )

    @allure.title("create")
    @pytest.mark.nondestructive
    @pytest.mark.run(order=1)
    @pytest.mark.repeat(3)
    def test_create_contractor_legal(self, selenium, base_url):
        authorize(selenium, base_url)

        selenium.get(f"{base_url}#/contractors-legal/new")

        contractor_add_page = ContractorLegalAddPage(selenium)
        contractor_add_page.full_name = self.contractor.full_name
        contractor_add_page.name = self.contractor.name
        contractor_add_page.inn = self.contractor.inn
        contractor_add_page.date_from = self.contractor.date_from
        contractor_add_page.select_country(self.contractor.country)

        contractor_add_page.click_add_btn()

        client_add_page = ClientAddPage(selenium)
        assert client_add_page.title == self.translator.get_translator('co.client.new.title')

