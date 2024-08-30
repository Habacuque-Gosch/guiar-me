from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from apps.estabelecimentos.models import Estabelecimento


class TagsFilterUser(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    # nivel = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.nome

class Resumo(models.Model):
    orientacao_sexual = [
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
    orientacao_sexual = models.CharField(max_length=100, choices=orientacao_sexual, default='')
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    estabelecimentos_fav = models.ManyToManyField(Estabelecimento, related_name='estabelecimentos_favoritos', blank=True, null=True)
    tags_filtro = models.ManyToManyField(TagsFilterUser, related_name='tags_user', blank=True, null=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
    
    def __str__(self):
        return self.nome
    