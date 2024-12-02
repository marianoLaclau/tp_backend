
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.autenticacion.urls')),
    path('', include('apps.home.urls')),
    path('',include('apps.inscripciones.urls')),
    path('',include('apps.calendario.urls')),
    path('',include('apps.docentes.urls')),
    path('',include('apps.administracion.urls')),
    path('',include('apps.alumno.urls')),
    path('',include('apps.recursos.urls')),
]
