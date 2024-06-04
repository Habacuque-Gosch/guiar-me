from django.urls import path
from .views import *




urlpatterns = [
    path('novo-perfil/', novo_perfil, name = 'novo_perfil'),
    path('splash-inicial/<int:foto_user_id>/', splash_home, name='splash_home'),
    path('configuracoes-user/', config_user, name = 'configuracoes_user'),
    path('editar-perfil/<int:resumo_id>QKJBN?', editar_perfil, name="editar_perfil"),
    path('favoritos/', favoritos, name="favoritos"),
    path('favoritar-estabelecimento/<int:estabelecimento_id>/', favoritar_estabelecimento, name="favoritar_estabelecimento"),
    path('desfavoritar-estabelecimento/<int:estabelecimento_id>/', desfavoritar_estabelecimento, name="desfavoritar_estabelecimento"),

]


