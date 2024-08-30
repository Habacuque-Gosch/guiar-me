from django.shortcuts import render
from apps.eventos.models import Evento
# from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def buscar_eventos(request):
    ''' Função responsável por buscar eventos na tabela dos Eventos '''
    
    eventos = Evento.objects.order_by("data_publicada").filter(publicada=True)

    if "buscar_eventos" in request.GET:
        nome_a_buscar = request.GET['buscar_eventos']
        if nome_a_buscar:
            eventos = eventos.filter(nome__icontains=nome_a_buscar)

            # user__email=nome_a_buscar)| profiles_friends.filter(user__first_name=nome_a_buscar) | profiles_friends.filter(user__full_name=nome_a_buscar)

    return render(request, 'eventos/index.html', {"eventos": eventos, "palavra": nome_a_buscar})
