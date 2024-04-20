from django.shortcuts import render, redirect, get_list_or_404
from apps.resumo.forms import ResumoForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def novo_perfil(request):
    current_user = request.user

    form = ResumoForms

    if request.method == 'POST':

        form = ResumoForms(request.POST, request.FILES)

        if form.is_valid:
            resumo = form.save(commit=False)
            resumo.usuario = current_user
            resumo.save()
            # messages.success(request, "salvo com sucesso")
            return redirect('index')

    return render(request, 'usuarios/cadastro/idade_e_nome.html', {'form': form})