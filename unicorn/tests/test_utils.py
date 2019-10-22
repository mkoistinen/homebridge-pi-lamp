# -*- coding: utf-8 -*-

import pytest

from unicorn.utils import (
    get_rgb_brightness,
    set_rgb_brightness,
)


@pytest.mark.parametrize("hex_code,brightness", [
    ('000000', 0),
    ('FFFFFF', 100),
    ('2F9429', 58),
    ('00527F', 49),
    ('293F77', 46),
])
def test_rgb_brightness(hex_code, brightness):
    assert int(get_rgb_brightness(hex_code)) == brightness


@pytest.mark.parametrize("hex_code,brightness,new_rgb", [
    ('000000', 10, (26, 26, 26)),
    ('FFFFFF', 90, (230, 230, 230)),
    ('2F9429', 20, (16, 51, 14)),
    ('00527F', 80, (0, 132, 204)),
    ('293F77', 50, (44, 67, 128)),
])
def test_set_rgb_brightness(hex_code, brightness, new_rgb):
    assert set_rgb_brightness(hex_code, brightness) == new_rgb
