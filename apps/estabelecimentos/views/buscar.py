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

            # user__email=nome_a_buscar)| profiles_friends.filter(user__first_name=nome_a_buscar) | profiles_friends.filter(user__full_name=nome_a_buscar)

    return render(request, 'estabelecimentos/index.html', {"estabelecimentos": estabelecimentos, "palavra": nome_a_buscar})


# def filtrar(request, estabelecimento_nome):

#     estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

#     # categorias = Estabelecimento.categoria

#     # print(categorias)

#     if request.GET:
#         nome_a_buscar = estabelecimento_nome
#         print(nome_a_buscar)
#         if nome_a_buscar:
#             estabelecimentos = estabelecimentos.filter(nome__icontains=nome_a_buscar)

#             # user__email=nome_a_buscar)| profiles_friends.filter(user__first_name=nome_a_buscar) | profiles_friends.filter(user__full_name=nome_a_buscar)

#     return render(request, 'estabelecimentos/index.html', {"estabelecimentos": estabelecimentos})