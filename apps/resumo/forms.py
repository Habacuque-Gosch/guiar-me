from django import forms
from apps.resumo.models import Resumo




class ResumoForms(forms.ModelForm):
    class Meta:
        model = Resumo
        # exclude = ['usuario','sexo','foto']
        exclude = ['usuario']

        labels = {
            'foto' : ' ',
            'genero' : ' ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo','placeholder':'Digite seu nome'}),
            'idade': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo-age', 'placeholder':'Digite sua idade'}),
            'genero': forms.Select(attrs={'class': 'select-user', 'id': 'sexo', 'placeholder':'Selecione seu sexo'}),
            'foto': forms.FileInput(attrs={'class': 'upload-img', 'id': 'upload-img'}),
            # 'usuario': forms.Select(attrs={'class': 'form-control'})
        }