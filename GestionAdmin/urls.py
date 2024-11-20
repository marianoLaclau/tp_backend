
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('autenticacion.urls')),
    path('', include('home.urls')),
    path('',include('inscripciones.urls')),
    path('',include('calendario.urls')),
    path('',include('docentes.urls')),
    path('',include('administracion.urls')),
    path('',include('alumno.urls')),
    path('',include('recursos.urls')),
]
