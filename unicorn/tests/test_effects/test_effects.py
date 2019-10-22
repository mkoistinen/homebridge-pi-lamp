from unicorn.apps.effects import OceanBoatBlue, CandleLight, Rainbow


def test_candle_light_init(unicorn_hat):
    candle_light = CandleLight(unicorn_hat)
    assert candle_light.width == 4
    assert candle_light.height == 8
    assert candle_light.min_steps == 10
    assert candle_light.max_steps == 50


def test_ocean_boat_blue_init(unicorn_hat):
    ocean_boat_blue = OceanBoatBlue(unicorn_hat)
    assert ocean_boat_blue.width == 4
    assert ocean_boat_blue.height == 8


def test_rainbow_init(unicorn_hat):
    rainbow = Rainbow(unicorn_hat)
    assert rainbow.width == 4
    assert rainbow.height == 8
