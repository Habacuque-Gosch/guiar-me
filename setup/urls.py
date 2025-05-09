from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.estabelecimentos.urls')),
    path('', include('apps.eventos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     print(settings.DEBUG)
#     import debug_toolbar
#     urlpatterns = [
#         path("__debug__/", include("debug_toolbar.urls")),
#     ] + urlpatterns

from django.views.static import serve
from django.urls import re_path
if settings.DEBUG:
    pass
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]