from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Resumo(models.Model):
    sexo = [
        ('LESBICA','Lésbica'),
        ('GAY','Gay'),
        ('BISSEXUAL','Bissexual'),
        ('TRANSGENERO','Transgênero'),
        ('NAO_BINARIO','Não-Binário'),
        ('HETEROSSEXUAL','Heterossexual'),
        ('OUTRO','Outro'),
    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    idade = models.CharField(max_length=2, null=False, blank=False)
    genero = models.CharField(max_length=100, choices=sexo, default='')
    # pronomes = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')
    # bio = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
    
    def __str__(self):
        return self.nome