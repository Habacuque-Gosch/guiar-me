from django.urls import path
from .views import *

from django.views.generic import TemplateView



urlpatterns = [
    path('index/', index, name = 'index'),
    path('buscar/', buscar, name = "buscar"),
    path('estabelecimento/<int:estabelecimento_id>/', estabelecimento, name= "estabelecimento"),
    path('map/<int:estabelecimento_id>/', maps, name="map"),
]
