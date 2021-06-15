from django.shortcuts import render, redirect
from .carro import Carro
from Tienda.models import T_Producto

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = T_Producto.objects.get(id = producto_id)
    carro.agregar(producto)

    return redirect("Tienda/tienda.html")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = T_Producto.objects.get(id = producto_id)
    carro.eliminar(producto)

    return redirect("Tienda/tienda.html")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = T_Producto.objects.get(id = producto_id)
    carro.restar_producto(producto)

    return redirect("Tienda/tienda.html")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("Tienda/tienda.html")