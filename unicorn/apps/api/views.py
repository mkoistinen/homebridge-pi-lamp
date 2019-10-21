from django.http import HttpResponse
from django.views.generic import View

from unicorn.apps.color import Color
from unicorn.apps.unicorn_phat.unicorn import unicorn_phat

OK = 'OK'


class BaseApiView(View):
   http_method_names = ['get', ]


class GetStatusView(BaseApiView):
    """
    Returns the on/off status of the lamp.
    """
    def get(self, request, *args, **kwargs):
        print('Hello there!')
        return HttpResponse("1" if unicorn_phat.status else "0")


class SetStatusView(BaseApiView):
    """
    Sets the on/off status of the lamp.
    """
    def get(self, request, *args, **kwargs):
        status = self.kwargs.get('status')
        unicorn_phat.set_status(status == 'on')
        return HttpResponse(OK)


class GetColorView(BaseApiView):
    """
    Returns the current color of the lamp.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(unicorn_phat.color.as_hex())


class SetColorView(BaseApiView):
    """
    Sets the color of the lamp.
    """
    def get(self, request, *args, **kwargs):
        color = self.kwargs.get('color')
        unicorn_phat.set_color(Color(hex=color))
        return HttpResponse(OK)


class GetBrightnessView(BaseApiView):
    """
    Returns the brightness of the lamp (based on its current color values).
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(unicorn_phat.color.brightness)
