from django import forms
from apps.resumo.models import Resumo




class ResumoForms(forms.ModelForm):
    class Meta:
        model = Resumo
        # exclude = ['usuario','sexo','foto']
        exclude = ['usuario']

        labels = {
            'foto' : ' ',
            'sexo' : ' ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo','placeholder':'Digite seu nome'}),
            'idade': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo', 'placeholder':'Digite sua idade'}),
            'sexo': forms.Select(attrs={'class': 'select-user', 'id': 'sexo', 'placeholder':'Selecione seu sexo'}),
            'foto': forms.FileInput(attrs={'class': 'upload-img'}),
            # 'usuario': forms.Select(attrs={'class': 'form-control'})
        }