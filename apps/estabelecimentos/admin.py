from django.contrib import admin
from apps.estabelecimentos.models import Estabelecimento

class ListandoEstabelecimentos(admin.ModelAdmin):
    list_display = ("id", "nome", "local", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 20

admin.site.register(Estabelecimento, ListandoEstabelecimentos)
