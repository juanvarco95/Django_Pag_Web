from django.urls import path
from . import views as v

app_name = "carro"

urlpatterns = [ 
    path('agregar/<int:producto_id>/', v.agregar_producto, name = "agregar"),
    path('eliminar/<int:producto_id>/', v.eliminar_producto, name = "eliminar"),
    path('restar/<int:producto_id>/', v.restar_producto, name = "restar"),
    path('limpiar/', v.limpiar_carro, name = "limpiar"),
]