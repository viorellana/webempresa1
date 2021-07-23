from django.contrib import admin
from .models import Service


# Creacion del sector administrativo de Servicios en Django. Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceAdmin)