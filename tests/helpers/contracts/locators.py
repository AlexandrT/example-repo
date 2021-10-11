from selenium.webdriver.common.by import By


class ContractAddPageLocators:
    CONTRACT_NUMBER = (By.XPATH, '//input[@formcontrolname="number"]')
    SIGN_DATE = (By.XPATH, '//input[@name="signDate"]')
    START_DATE = (By.XPATH, '//input[@name="startDate"]')
    END_DATE = (By.XPATH, '//input[@name="endDate"]')
    NAME_INPUT = lambda label: (By.XPATH, f'//input[@placeholder="{label}"]')

    CONTRACT_TYPE = (By.XPATH, '//input[@role="combobox"]')
    CONTRACT_TYPE_ITEM = lambda con_type: (By.XPATH, f'//span[@class="mat-option-text" and contains(., "{con_type}")]')

    ADD_BUTTON = (By.XPATH, '//button[contains(@class, "button-submit")]')
    ADD_MEMBERS_BUTTON = (By.XPATH, '//button[contains(@class, "button-add")]')

    CONTRACTOR_INPUT = (By.XPATH, './/input[@name="contractorInput"]')
    CONTRACTORS_LIST = (By.XPATH, '//span[@class="mat-option-text"]/div[@class="mat-body"]')
    ROLE_SELECT = (By.XPATH, './/mat-select')
    ROLE_ITEM = lambda role: f'//span[@class="mat-option-text" and contains(., "{role}")]'
    SAVE_BUTTON = (By.XPATH, './/div[contains(@class, "participant__buttons")]/button[contains(@class, "mat-flat-button")]')

    MEMBER_CARD = (By.XPATH, './/mat-card[contains(@class, "participant")]')
    CONTRACTOR_ROLE = (By.XPATH, './/span[contains(@class, "mat-select-value-text")]')

class ContractsListPageLocators:
    ADD_BUTTON = (By.XPATH, '//a[contains(@class, "mat-primary")]')

    TYPE_SELECT = (By.XPATH, '//vtbf-contract-type-picker/*//input')
    TYPE_ITEM = lambda con_type: (By.XPATH, f'//span[@class="mat-option-text" and contains(., "{con_type}")]')

    SEARCH_INPUT = (By.XPATH, '//input[@formcontrolname="query"]')

    CONTRACT_ITEM = (By.TAG_NAME, 'mat-card')
    CONTRACT_NAME = (By.XPATH, './/div[@class="contract__column-number"]')
    MEMBERS_COUNT = (By.XPATH, './/div[@class="contract__column-number"]/div[@class="caption"]')
    SIGN_DATE = (By.XPATH, './/div[@class="contract__column-sign-date"]')
    PERIOD = (By.XPATH, './/div[@class="contract__column-valid-range"]')
    STATUS = (By.XPATH, './/div[@class="contract__column-status"]')

class ContractShowPageLocators:
    CONTRACT_NUMBER = (By.XPATH, '//input[@formcontrolname="number" and @disabled]')
    SIGN_DATE = (By.XPATH, '//input[@name="signDate" and @disabled]')
    START_DATE = (By.XPATH, '//input[@name="startDate" and @disabled]')
    END_DATE = (By.XPATH, '//input[@name="endDate" and @disabled]')
    CONTRACT_NAME = (By.XPATH, '//input[@formcontrolname="name" and @disabled]')

    CONTRACT_CARD = (By.XPATH, '//mat-card[contains(@class, "card_gray")]')
