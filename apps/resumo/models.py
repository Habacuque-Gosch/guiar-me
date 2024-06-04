from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from apps.estabelecimentos.models import Estabelecimento





# class EstabelecimentosFavoritos(models.Model):
#     estabelecimentos_favoritos = models.ManyToManyField(Estabelecimento, null=True, related_name='estabelecimentos_favoritos')


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
    # pronomes = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')
    # bio = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    estabelecimentos_fav = models.ManyToManyField(Estabelecimento, related_name='estabelecimentos_favoritos')
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
    
    def __str__(self):
        return self.nome
    
    # def estabe_favoritos(user_id):
    #     return Estabelecimento.objects.all()