from django.urls import path

from . import views


class HexColorConverter:
    regex = '[0-9,a-f,A-F]{6}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value.tolower()

class OnOffConverter:
    regex = 'on|off'

    def to_python(self, value)
        return str(value)

    def to_url(self, value):
        return value.tolower()

register_converter(HexColorConverter, 'hexcolor')
register_converter(OnOffConverter, 'onoff')

urlpatterns = [
    path('v1.0', include([
        path('status', GetStatusView.as_view(), name='get-status'),
        path('status/<onoff:status>/', SetStatusView.as_view(), name='set-status'),
        path('on', SetStatusView.as_view(), {'status': 'on'}, name='set-status-on'),
        path('off', SetStatusView.as_view(), {'status': 'off'}, name='set-status-off'),
        path('color', GeteColorView.as_view(), name='get-color'),
        path('color/<hexcolor:color>', SetColorView.as_view(), name='set-color'),
        path('brightness', GetBrightnessView.as_view(), name='get-brightness'),
    ])),
]

