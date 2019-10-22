from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import WifiConfigForm


class ConfigureHomeView(TemplateView):
    template_name = 'config/home.html'


class WifiConfigView(FormView):
    http_method_names = ['get', 'post', ]
    form_class = WifiConfigForm
    template_name = 'config/wifi_config.html'
    success_url = reverse_lazy('wifi_config_accepted')


class WifiConfigUpdatingView(TemplateView):
    template_name = 'config/wifi_updating.html'

    def get(self, request, *args, **kwargs):
        # TODO: Set the parameters
        return super().form_valid(request, *args, **kwargs)
