import pytest

from unicorn.apps.color.utils import bracket, hex_to_rgb


@pytest.mark.parametrize('value,low,high,result', (
        (128, 0, 255, 128),
        (128, 0, 100, 100),
        (-99, 0, 255, 0),
        (1.2, 0, 255, 1.2),
        (-5, -10, 100, -5),
))
def test_bracket(value, low, high, result):
    assert bracket(value, low=low, high=high) == result


@pytest.mark.parametrize("hex_code,rgb_tuple", [
    ('000000', (0, 0, 0)),
    ('FFFFFF', (255, 255, 255)),
    ('00a2Ff', (0, 162, 255)),
    ('ff9429', (255, 148, 41)),
    ('fF2977', (255, 41, 119)),
])
def test_hex_to_rgb(hex_code, rgb_tuple):
    assert hex_to_rgb(hex_code) == rgb_tuple
