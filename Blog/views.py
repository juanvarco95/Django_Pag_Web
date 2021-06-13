from django.shortcuts import get_object_or_404, render
from .models import Categoria, Post

def blogs(request):
    p = Post.objects.all()
    ctx = {"post" : p}
    
    return render(request, 'Blogs/blog.html', ctx)

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    p = Post.objects.filter(categorias = categoria)
    ctx =  {'categoria': categoria , "post" : p}

    return render(request, "Blogs/categoria.html", ctx)