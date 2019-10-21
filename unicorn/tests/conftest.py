# -*- coding: utf-8 -*-

import pytest

from unicorn.apps.color import Color
from unicorn.apps.unicorn_phat.fake_unicorn_hat import fake_unicornhat
from unicorn.apps.unicorn_phat import Unicorn


@pytest.fixture(scope="module")
def unicorn_hat():
    return fake_unicornhat


@pytest.fixture(scope="module")
def color():
    return Color(hex='007F7F')


@pytest.fixture
def unicorn(color, unicorn_hat):
    return Unicorn(unicorn_hat, color)
