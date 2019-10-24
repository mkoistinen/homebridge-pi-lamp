from django.urls import include, path, register_converter

from .views import (
    GetBrightnessView,
    GetColorView,
    GetStatusView,
    SetColorView,
    SetStatusView,
)


class HexColorConverter:
    regex = '[0-9,a-f,A-F]{6}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value.lower()


class OnOffConverter:
    regex = 'on|off'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value.lower()


register_converter(HexColorConverter, 'hexcolor')
register_converter(OnOffConverter, 'onoff')

app_name = 'api'

urlpatterns = [
    path('v1.0/', include([
        path('status', GetStatusView.as_view(), name='get-status'),
        path('status/<onoff:status>/', SetStatusView.as_view(), name='set-status'),
        path('on', SetStatusView.as_view(), {'status': 'on'}, name='set-status-on'),
        path('off', SetStatusView.as_view(), {'status': 'off'}, name='set-status-off'),
        path('color', GetColorView.as_view(), name='get-color'),
        path('color/<hexcolor:color>', SetColorView.as_view(), name='set-color'),
        path('brightness', GetBrightnessView.as_view(), name='get-brightness'),
    ])),
]

