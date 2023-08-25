from django.contrib import admin
from .models import MediaCatalog, MediaUsuarios, MediaUsuariosCount

admin.site.register(MediaCatalog)
admin.site.register(MediaUsuarios)
admin.site.register(MediaUsuariosCount)