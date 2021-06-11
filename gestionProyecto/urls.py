from django.urls import path
from gestionProyecto import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', v.home),
    path('base/',v.base),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
