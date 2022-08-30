
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from funciones.views import voluntarios, plataforma, microfonos, zoom, dashboard, presidentes,lectores,acomodadores, asignados ,exp_pdf_plataf


urlpatterns = [
    path('admin/',admin.site.urls),
    path('acomodadores/',acomodadores),
    path('',dashboard),
    path('dashboard/',dashboard),
    path('lectores/',lectores),
    path('microfonos/',microfonos),
    path('plataforma/',plataforma),  
    path('presidentes/',presidentes),   
    path('voluntarios/',voluntarios),
    path('asignados/',asignados),
    path('zoom/',zoom),   
    path('crear_pdf/',exp_pdf_plataf),
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

