from selenium.webdriver.common.by import By


class RepresentAddPageLocators(object):
    LAST_NAME_INPUT = (By.XPATH, '//input[@formcontrolname="lastName"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@formcontrolname="firstName"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@formcontrolname="middleName"]')
    SSN_INPUT = (By.XPATH, '//input[@formcontrolname="ssn"]')

    COUNTRY = (By.XPATH, '//input[@name="countryCode"]')

    COUNTRY_ITEM = lambda country: (By.XPATH, f'//span[@class="mat-option-text" and contains(., "{country}")]')

    ADD_BUTTON = (By.XPATH, '//button[contains(@class, "mat-flat-button")]')
