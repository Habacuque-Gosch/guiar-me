from django.shortcuts import render, redirect
from apps.estabelecimentos.models import Estabelecimento
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def buscar(request):
    ''' função responsavél por entregar os objetos da tabela Estabelecimento correspondende com a palavra digitada'''

    estabelecimentos = Estabelecimento.objects.order_by("data_publicada").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            estabelecimentos = estabelecimentos.filter(nome__icontains=nome_a_buscar)

    return render(request, 'estabelecimentos/index.html', {"estabelecimentos": estabelecimentos, "palavra": nome_a_buscar})


# def filtrar(request):

#     estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

#     # if "tipo" in request.GET:
#     key_a_buscar = request.GET['tipo']
#     if key_a_buscar:
#         estabelecimentos = estabelecimentos.filter(tipo_de_vaga__icontains=key_a_buscar)

#     # if "local" in request.GET:
#     key_a_buscar = request.GET['local']
#     if key_a_buscar:
#         estabelecimentos = estabelecimentos.filter(categoria__icontains=key_a_buscar)

#     return render(request, 'estabelecimentos/index.html', {"estabelecimentos": estabelecimentos})