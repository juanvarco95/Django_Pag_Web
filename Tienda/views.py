from django.shortcuts import render, get_object_or_404
from .models import prueba_Categoria, T_Producto

def tienda(request):
    p = T_Producto.objects.all()
    ctx = {"producto" : p}
  
    return render(request, "Tienda/tienda.html", ctx)

def categoria(request, categoria_id):
    cat = prueba_Categoria.objects.get(id = categoria_id)
    pro = T_Producto.objects.filter(pro_categorias = cat)
    ctx = {'categoria': cat, "producto" : pro}

    return render(request, "Tienda/categoria_pro.html", ctx)