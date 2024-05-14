from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from apps.eventos.models import Evento
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .views import *
from apps.resumo.models import Resumo



@cache_page(60 * 5)
@login_required(login_url='login')
def index_eventos(request):
    ''' função responsavél por entregar os objetos do banco de dados: Evento'''

    user = request.user

    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login')

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    eventos = Evento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    return render(request, 'eventos/index.html', {'eventos': eventos})

@login_required(login_url='login')
def evento(request, evento_id):
    ''' função responsavél por entregar os dados de um determinado objeto filtradao por id do banco de dados: Evento'''

    user = request.user

    try:
        eventos = get_object_or_404(Evento, pk=evento_id)

    except:
        return render(request, 'eventos/evento.html')


    return render(request, 'eventos/evento.html', {'eventos': eventos})

