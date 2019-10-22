import pytest
from django.urls import reverse, NoReverseMatch

OK = b'OK'


def test_get_status_view(client):
    response = client.get(reverse('get-status'))
    assert response.content == b'1'


@pytest.mark.parametrize('status, expected', [
    ('on', True),
    ('off', True),
    ('ON', True),
    ('OFF', True),
    ('dim', False)
])
def test_set_status_view(client, status, expected):
    try:
        url = reverse('set-status', kwargs={'status': status})
        response = client.get(url)
        assert response.content == OK
        assert expected is True
    except NoReverseMatch:
        assert expected is False


def test_set_status_on_view(client):
    url = reverse('set-status-on')
    response = client.get(url)
    assert response.content == OK


def test_set_status_off_view(client):
    url = reverse('set-status-off')
    response = client.get(url)
    assert response.content == OK


def test_get_color_view(client):
    url = reverse('get-color')
    response = client.get(url)
    assert response.content == b'007F7F'


@pytest.mark.parametrize('color, expected', [
    ('abcdef', True),
    ('ABCDEF', True),
    ('CCC', False),
    ('red', False),
])
def test_set_color_view(client, color, expected):
    try:
        url = reverse('set-color', kwargs={'color': color})
        response = client.get(url)
        assert response.content == OK
        assert expected is True
    except NoReverseMatch:
        assert expected is False


def test_get_brightness_view(client):
    url = reverse('get-brightness')
    response = client.get(url)
    assert response.content == b'93'
