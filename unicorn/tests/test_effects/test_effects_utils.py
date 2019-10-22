import pytest

from unicorn.apps.effects.utils import transition


@pytest.mark.parametrize('step,result', (
    (0, (0, 0, 0)),
    (50, (127, 127, 127)),
    (100, (255, 255, 255)),
))
def test_transition(step, result):
    new_rgb = transition(0, 0, 0, 255, 255, 255, step, 100)
    new_rgb = tuple(int(c + 0.5) for c in new_rgb)
    assert new_rgb == result
