from selenium.webdriver.common.by import By


class ClientsListPageLocators(object):
    ADD_BUTTON = (By.XPATH, '//a[contains(@class, "mat-flat-button")]')

class ClientAddPageLocators(object):
    CONTRACTOR_INPUT = (By.XPATH, '//input[@name="contractorInput"]')
    CONTRACTORS_LIST = (By.XPATH, '//span[@class="mat-option-text"]/div[@class="mat-body"]')
    NAME_INPUT = (By.XPATH, '//input[@formcontrolname="name"]')

    NOT_FOUND_ITEM = lambda item_text: (By.XPATH, f'//span[@class="mat-option-text" and contains(., "{item_text}")]')

    ADD_BUTTON = (By.TAG_NAME, 'button')

    TITLE = (By.XPATH, '//client-client-new/h1')

class ClientShowPageLocators(object):
    NAME = (By.XPATH, '//h1')
    CONTRACTOR_NAME = lambda c_name: (By.XPATH, f'//input[@placeholder="{c_name}"]')

    RENAME_BUTTON = (By.XPATH, '//button[contains(@class, "mat-stroked-button")]')

    SAVE_BUTTON = (By.XPATH, '//mat-dialog-container/*//button[contains(@class, "mat-flat-button")]')
    NO_SAVE_BUTTON = (By.XPATH, '//mat-dialog-container/*//button[contains(@class, "mat-stroked-button")]')

    OLD_NAME = (By.XPATH, '//mat-dialog-container/*//input[@disabled]')
    NEW_NAME = (By.XPATH, '//mat-dialog-container/*//input[not(@disabled)]')

    ADD_REPRESENT_BUTTON = (By.XPATH, '//repr-represents/*//button[contains(@class, "mat-primary")]')

    REPRESENT_ITEM = (By.XPATH, '//mat-list-item[contains(@class, "mat-list-item-avatar")]')
    REPRESENT_NAMES = (By.XPATH, './/h4')
    REPRESENT_STATUS = (By.XPATH, './/div[contains(@class, "status-chip")]')
    REPRESENT_MORE_BUTTON = (By.XPATH, './/button[contains(@class, "mat-icon-button")]')
    REPRESENT_REMOVE_BUTTON = (By.XPATH, '//button[contains(@class, "mat-menu-item")]')

