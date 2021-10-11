import i18n
import os
import pytest

from helpers.utils import *


pytest_plugins = ['common_fixtures']

i18n.load_path.append(os.path.join(os.path.dirname(__file__), 'helpers/support/translations'))
i18n.set('locale', 'ru')
