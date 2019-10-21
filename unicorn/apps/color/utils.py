# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def bracket(v, low=0, high=255):
    """Simply brackets a value between 0 and 255."""
    return max(low, min(high, v))


def hex_to_rgb(value):
    """
    Convert hex formatted color to tuple of 3 integers from 0 - 255.
    """
    from .import RGB_ERROR_COLOR

    value = value.lstrip('#')
    length = len(value)

    try:
        assert length == 3 or length == 6
        triplet = tuple(
            bracket(int(value[i:i + length // 3], 16))
            for i in range(0, length, length // 3)
        )
        return triplet
    except AssertionError:
        logger.exception(
            'Unexpected number of digits in hex value: "{}"'.format(value))
        return RGB_ERROR_COLOR
    except ValueError:
        logger.exception(
            'Unable to convert hex "{}" to decimal'.format(value))
        return RGB_ERROR_COLOR
