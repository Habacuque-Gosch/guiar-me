from django import forms
from apps.resumo.models import Resumo




class ResumoForms(forms.ModelForm):
    class Meta:
        model = Resumo
        exclude = ['usuario']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user'}),
            'idade': forms.TextInput(attrs={'class': 'campo-user'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'upload-img'}),
            # 'usuario': forms.Select(attrs={'class': 'form-control'})
        }