from django.views.generic import View

from ..unicorn import unicorn

OK = 'OK'


class BaseApiView(View):
   http_method_names = ['get', ]


class GetStatusView(BaseApiView):
    def get(self, request, *args, **kwargs):
        return unicorn.status


class SetStatusView(BaseApiView):
    def get(self, request, *args, **kwargs):
        status = self.kwargs.get('status')
        unicorn.set_status(status == 'on')
        return OK


class GetColorView(BaseApiView):
    def get(self, request, *args, **kwargs):
        return unicorn.color.as_hex()


class SetColorView(BaseApiView):
    def get(self, request, *args, **kwargs):
        color = self.kwargs.get('color')
        unicorn.set_color(Color(hex=color))
        return OK


class GetBrightnessView(BaseApiView):
    def get(self, request, *args, **kwargs):
        return str(unicorn.color.brightness)

