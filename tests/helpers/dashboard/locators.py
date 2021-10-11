from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    CLIENTS_ITEM = (By.XPATH,'//a[contains(@href, "clients")]')
    CONTRACTS_ITEM = (By.XPATH,'//a[contains(@href, "contracts")]')
