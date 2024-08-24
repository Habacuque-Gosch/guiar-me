from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('index/', index, name = 'index'),
    path('buscar/', buscar, name = "buscar"),
    path('estabelecimento/<int:estabelecimento_id>/', estabelecimento, name= "estabelecimento"),
    path('map/<int:estabelecimento_id>/', maps_estabelecimentos, name="map"),

    path('dashboard', dashboard, name = 'dashboard'),
    # path('menu', menu, name = 'menu'),
    # path('my-events', my_events, name = 'my_events'),
    # path('my-reviews', my_reviews, name = 'my_reviews'),
    # path('business-settings', business_settings, name = 'business_settings'),
]
