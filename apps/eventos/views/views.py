from django.shortcuts import render, redirect, get_list_or_404
from apps.eventos.models import Evento
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .views import *
from apps.resumo.models import Resumo




# @login_required(login_url='login')
def index_eventos(request):
    '''  '''

    user = request.user

    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login')

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    eventos = Evento.objects.filter(publicada=True)

    return render(request, 'eventos/index.html', {'eventos': eventos})