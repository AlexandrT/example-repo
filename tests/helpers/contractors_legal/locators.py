from selenium.webdriver.common.by import By


class ContractorLegalAddPageLocators:
    FULLNAME_INPUT = (By.XPATH, '//input[@formcontrolname="fullName"]')
    DATE_FROM = (By.XPATH, '//input[@name="effectiveFrom"]')
    NAME_INPUT = (By.XPATH, '//input[@formcontrolname="shortName"]')
    INN_INPUT = (By.XPATH, '//input[@formcontrolname="taxId"]')
    COUNTRY = (By.XPATH, '//input[@name="countryCode"]')

    COUNTRY_ITEM = lambda country: (By.XPATH, f'//span[@class="mat-option-text" and contains(., "{country}")]')

    ADD_BUTTON = (By.XPATH, '//button[contains(@class, "mat-flat-button")]')
