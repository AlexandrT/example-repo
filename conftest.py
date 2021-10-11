import sys
import os
import allure
import json
from allure_commons.types import AttachmentType
from allure_commons.reporter import AllureReporter


sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

# monkey patching. fix issue https://github.com/allure-framework/allure-python/issues/216
def start_after_fixture(self, parent_uuid, uuid, fixture):
    try:
        self._items.get(parent_uuid).afters.append(fixture)
        self._items[uuid] = fixture
    except:
        self._items[uuid] = fixture

AllureReporter.start_after_fixture = start_after_fixture

def pytest_exception_interact(node, call, report):
    try:
        driver = node._driver

        allure.attach(driver.get_screenshot_as_png(), name=report.location[2], attachment_type=AttachmentType.PNG)

        logs = ""
        for log in driver.get_log('browser'):
            json_string = json.dumps(log)
            logs += f"\n{json_string}"

        allure.attach(logs.encode(), name="log", attachment_type=AttachmentType.JSON)
    except AttributeError:
        pass
