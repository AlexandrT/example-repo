from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    def __set__(self, obj, value):
        if hasattr(obj, "parent"):
            driver = obj.parent
        else:
            driver = obj.driver

        WebDriverWait(driver, 10).until(lambda driver:
                driver.find_element(*self.locator))

        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        if hasattr(obj, "parent"):
            driver = obj.parent
        else:
            driver = obj.driver

        WebDriverWait(driver, 10).until(lambda driver:
                driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element


class ValueElement(BaseElement):
    def __get__(self, obj, owner):
        element = BaseElement.__get__(self, obj, owner)
        return element.get_attribute("value")

class TextElement(BaseElement):
    def __get__(self, obj, owner):
        element = BaseElement.__get__(self, obj, owner)
        return element.text
