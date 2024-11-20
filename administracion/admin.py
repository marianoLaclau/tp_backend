from django.contrib import admin
from .models import Turno,Genero,Nacionalidad ,Estado , PersonalAdmin , Docente


admin.site.register(Turno)
admin.site.register(Genero)
admin.site.register(Nacionalidad)
admin.site.register(Estado)
admin.site.register(PersonalAdmin)
admin.site.register(Docente)