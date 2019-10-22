from django.urls import include, path, register_converter

from .views import ConfigureHomeView, WifiConfigView, WifiConfigUpdatingView


urlpatterns = [
    path('configure/', include([
        path('', ConfigureHomeView.as_view(), name='configure-home'),
        path('wifi/', include([
            path('', WifiConfigView.as_view(), name='configure-wifi'),
            path('updating/', WifiConfigUpdatingView.as_view(), name='updating-wifi'),
        ])),
    ])),
]
