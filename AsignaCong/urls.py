
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#voluntarios, plataforma, microfonos, zoom, dashboard, presidentes,lectores,acomodadores, asignados ,exp_pdf_plataf


urlpatterns = [
    path('admin/',admin.site.urls),
    path('acomodadores/',views.acomodadores),
    path('',views.dashboard),
    path('dashboard/',views.dashboard),
    path('lectores/',views.lectores),
    path('microfonos/',views.microfonos),
    path('plataforma/',views.plataforma),  
    path('presidentes/',views.presidentes),   
    path('voluntarios/',views.voluntarios),
    path('asignados/',views.asignados),
    path('zoom/',views.zoom),   
    path('crear_pdf/',views.exp_pdf_plataf),
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

