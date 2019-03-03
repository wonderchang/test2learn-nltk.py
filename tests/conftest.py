import os

import pytest


@pytest.fixture(scope='session')
def corenlp_host_url():
    return 'http://' + os.environ.get('CORENLP_HOST')


# vi:et:ts=4:sw=4:cc=80
