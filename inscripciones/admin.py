from django.contrib import admin
from .models import Curso,Materia , Vinculo , PadreTutor

admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Vinculo)
admin.site.register(PadreTutor)
