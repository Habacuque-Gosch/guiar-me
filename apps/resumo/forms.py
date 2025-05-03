from django import forms
from apps.resumo.models import Resumo




class ResumoForms(forms.ModelForm):
    class Meta:
        model = Resumo
        exclude = ['usuario', 'estabelecimentos_fav']

        labels = {
            'foto' : ' ',
            'orientacao_sexual' : ' ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo','placeholder':'Digite seu nome'}),
            'idade': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo-age', 'placeholder':'Digite sua idade'}),
            'orientacao_sexual': forms.Select(attrs={'class': 'select-user', 'id': 'sexo', 'placeholder':'Selecione seu sexo'}),
            'foto': forms.FileInput(attrs={'class': 'upload-img', 'id': 'upload-img'}),
            'tags_filtro': forms.SelectMultiple(attrs={'class': 'tags_filtro', 'id': 'tags_filtro'}),
        }