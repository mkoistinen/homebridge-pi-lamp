# -*- coding: utf-8 -*-

from colorsys import rgb_to_hsv, hsv_to_rgb
import logging

from unicorn.apps.color.utils import hex_to_rgb


logger = logging.getLogger('unicorn.utils')


def get_rgb_brightness(color):
    """
    Given an RGB _color (hex format), return it's brightness.
    """
    r, g, b = hex_to_rgb(color)
    hsv = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    return hsv[2] * 100


def set_rgb_brightness(color, brightness):
    """
    Given an RGB _color (hex format) and brightness, return a new RGB _color.
    :param color: hex format RGB _color string
    :param brightness: Integer from 0 to 100
    """
    r, g, b = hex_to_rgb(color)
    hsv = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    rgb = hsv_to_rgb(hsv[0], hsv[1], brightness/100.0)
    return (
        int(rgb[0] * 255.0 + 0.5),
        int(rgb[1] * 255.0 + 0.5),
        int(rgb[2] * 255.0 + 0.5),
    )
