
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('Servicios.urls')),
    path('contacto/', include ('Contacto.urls')),
    path('blog/', include('Blog.urls')),
    path('tienda/', include('Tienda.urls')),
    path('', include('gestionProyecto.urls')),

]
