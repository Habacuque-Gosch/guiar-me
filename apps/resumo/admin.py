from django.contrib import admin
from apps.resumo.models import Resumo



class ListandoResumo(admin.ModelAdmin):
    list_display = ("id", "nome", "usuario")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("genero", "usuario")
    # list_editable = ("publicada",)
    list_per_page = 20

admin.site.register(Resumo, ListandoResumo)