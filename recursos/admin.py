from django.contrib import admin
from .models import NombreRecurso,TipoRecurso,Ubicacion,Recursos


admin.site.register(NombreRecurso)
admin.site.register(TipoRecurso)
admin.site.register(Ubicacion)
admin.site.register(Recursos)

