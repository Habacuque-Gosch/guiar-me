from django.urls import path
from .views import *


urlpatterns = [
    path('index_eventos/', index_eventos, name = 'index_eventos'),
    path('buscar_eventos/', buscar_eventos, name="buscar"),    
]
