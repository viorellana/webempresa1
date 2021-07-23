from django.contrib import admin
from .models import Link


# Creacion del sector administrativo de Redes Sociales en Django. Register your models here.
class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
