__author__ = 'mengmeng'
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = ROOT_PATH
TEST_DISCOVER_ROOT = ROOT_PATH
TEST_DISCOVER_PATTERN = 'test_*'