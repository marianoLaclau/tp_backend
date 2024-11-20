from django.urls import path
from .views import CreateAlumno, ListaTutores , CreatePadreTutor, ViewDocente, CreateDocente,EditarDocente, EditarTutor



urlpatterns = [
   path('agregar/',CreateAlumno.as_view(),name='agregar'),
   path('tutor/',ListaTutores.as_view(),name='tutor'),
   path('agregar_tutor/',CreatePadreTutor.as_view(),name='agregar_tutor'),
   path('agregar_docente/',CreateDocente.as_view(),name='agregar_docente'),
   path('lista_docente/',ViewDocente.as_view(),name='lista_docente'),
   path('editar_docente/<int:pk>',EditarDocente.as_view(),name='editar_docente'),
   path('editar_tutor/<int:pk>',EditarTutor.as_view(),name='editar_tutor'),
]


