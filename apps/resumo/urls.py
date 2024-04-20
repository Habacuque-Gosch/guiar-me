from django.urls import path
from .views import *



urlpatterns = [
    path('novo-perfil', novo_perfil, name = 'novo_perfil'),
]


