from django.urls import path
from .views import *



urlpatterns = [
    path('novo-perfil/', novo_perfil, name = 'novo_perfil'),
    path('splash-inicial/<int:foto_user_id>/', splash_home, name='splash_home'),
]


