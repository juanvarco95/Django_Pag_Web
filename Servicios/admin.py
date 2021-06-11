from django.contrib import admin
from Servicios.models import Servicio
from gestionProyecto.models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

class ServiciosAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'created')
    list_filter = ("created",)
    readonly_fields = ("created", "updated")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Servicio, ServiciosAdmin)