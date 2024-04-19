from django.shortcuts import render, redirect
from apps.estabelecimentos.models import Estabelecimento
from django.contrib import messages



def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    estabelecimentos = Estabelecimento.objects.order_by("data_publicada").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            estabelecimentos = estabelecimentos.filter(nome__icontains=nome_a_buscar)

            # user__email=nome_a_buscar)| profiles_friends.filter(user__first_name=nome_a_buscar) | profiles_friends.filter(user__full_name=nome_a_buscar)

    return render(request, 'estabelecimentos/index.html', {"estabelecimentos": estabelecimentos, "palavra": nome_a_buscar})
