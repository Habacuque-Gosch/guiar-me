from django.contrib import admin
from .models import Profile


admin.sites.AdminSite.site_header = 'GuiarMe'
admin.sites.AdminSite.index_title = 'GuiarMe'
admin.sites.AdminSite.site_title = 'Admin Site'



# @admin.action(description="Desativar")
# def action_desactivate(modeladmin, request, queryset):
#     for a in queryset:
#         a.publicada = False
#         a.save()

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "usuario")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("orientacao_sexual", "usuario")
    # list_editable = ("publicada",)
    list_per_page = 20
    # autocomplete_fields = ['']
    # actions = [action_desactivate]

    # class Media:
    #     js = ('js/')
    #     css = {
    #     'all': ('css/jobs/',)
    #     }