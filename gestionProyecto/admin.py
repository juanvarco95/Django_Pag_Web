from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

admin.site.register(Clientes, ClientesAdmin)
