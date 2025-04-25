from django.urls import path
from .views import *


urlpatterns = [
    path('index-eventos/', index_eventos, name = 'index_eventos'),
    path('buscar-eventos/', buscar_eventos, name="buscar_eventos"),    
    path('evento/<int:evento_id>/', evento, name="evento"),
]
