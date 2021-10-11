import os
import re
import i18n
import datetime

from dateutil.relativedelta import *


class CustomTranslator:
    def __init__(self):
        self.locale = i18n.config.get('locale')
        i18n.resource_loader.load_directory(os.path.join(os.path.dirname(__file__), 'support/translations'), self.locale)

    def get_translator(self, key):
        result = i18n.translations.container[self.locale][key]

        return result

class BaseTest(object):
    def setup_class(cls):
        cls.translator = CustomTranslator()

    def setup_method(self, method):
        print('\n==================TEST STARTED==================')
        print(os.environ.get('PYTEST_CURRENT_TEST').split(":")[-1].split(" ")[0])

    def teardown_method(self, method):
        print('\n------------------TEST FINISHED------------------')


def get_date(**kwargs):
    cur_date = datetime.datetime.now()
    date = cur_date

    for k in kwargs:
        date = date + duration(k, kwargs[k])

    return date.strftime("%d.%m.%Y")

def duration(k, v):
    switcher = {
        'minutes': datetime.timedelta(minutes=v),
        'hours': datetime.timedelta(hours=v),
        'days': datetime.timedelta(days=v),
        'weeks': datetime.timedelta(weeks=v),
        'months': relativedelta(months=v),
        'years': relativedelta(years=v),
    }

    func = switcher.get(k)
    return func

def current_locale():
    env = os.environ.get('TEST_LANG')
    return DEFAULT_LANG if env == None else env

def get_first_line(text):
    return text.splitlines()[0]

def get_int(text):
    num = int(re.search(r'\d+', text).group())
    return num
