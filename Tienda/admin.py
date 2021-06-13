from django.contrib import admin
from .models import  T_Producto, prueba_Categoria



class T_Producto_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

class prueba_Admin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(prueba_Categoria, prueba_Admin)    
admin.site.register(T_Producto, T_Producto_Admin)


