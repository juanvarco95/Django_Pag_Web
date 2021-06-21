from django.contrib import admin
from .models import Servicio

class ServiciosAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'created')
    list_filter = ("created",)
    readonly_fields = ("created", "updated")
    


admin.site.register(Servicio, ServiciosAdmin) 