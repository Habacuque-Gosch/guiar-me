from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('', home, name = 'home'),  
    path('plataforma/', home_plataforma, name = 'home_plataforma'),  
    path('login-plataforma/', login_plataforma, name = 'login_plataforma'),
    path('cadastro-plataforma/', cadastro_plataforma, name = 'cadastro_plataforma'),
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
    path('change-pass/', trocar_senha, name = 'trocar_senha'),
    path('novo-perfil/', novo_perfil, name = 'novo_perfil'),
    path('novo-filtro/', novo_filtro, name = 'novo_filtro'),
    path('splash-inicial/<int:foto_user_id>/', splash_home, name='splash_home'),
    path('configuracoes-user/', config_user, name = 'configuracoes_user'),
    path('editar-perfil/<int:resumo_id>QKJBN?', editar_perfil, name="editar_perfil"),
    path('favoritos/', favoritos, name="favoritos"),
    path('favoritar-estabelecimento/<int:estabelecimento_id>/', favoritar_estabelecimento, name="favoritar_estabelecimento"),
    path('desfavoritar-estabelecimento/<int:estabelecimento_id>/', desfavoritar_estabelecimento, name="desfavoritar_estabelecimento"),

]

