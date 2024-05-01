from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index, name = 'index'),
    path('buscar/', buscar, name="buscar"),
    path('estabelecimento/<int:estabelecimento_id>/', estabelecimento, name="estabelecimento"),

]
