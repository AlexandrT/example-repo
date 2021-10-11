from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        if hasattr(self, "parent"):
            self.driver = self.parent
        else:
            self.driver = driver

    def find_element_delay(self, *args):
        if len(args) == 1:
            args = args[0]

        WebDriverWait(self.driver, 10).until(lambda driver:
                self.driver.find_element(*args))
        element = self.driver.find_element(*args)
        return element

    def find_elements_delay(self, *args):
        if len(args) == 1:
            args = args[0]

        WebDriverWait(self.driver, 10). until(lambda driver:
                self.driver.find_elements(*args))
        elements = self.driver.find_elements(*args)
        return elements
