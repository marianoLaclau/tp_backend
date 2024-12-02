from django.urls import path
from .views import ViewAlumno , EditAlumnoView , VerAlumnoView , VerCalificaciones , VerInasistencias


urlpatterns = [
   path('ver_alumnos/',ViewAlumno.as_view(),name='lista_alumnos'),
   path('editar_alumno/<int:pk>/',EditAlumnoView.as_view(),name='editar_alumno'),
   path('ver_alumno/<int:pk>/', VerAlumnoView.as_view(),name='ver_alumno'),
   path('ver_calificaciones/<int:pk>/', VerCalificaciones.as_view(), name='ver_calificaciones'),
   path('ver_inasistencias/<int:pk>/',VerInasistencias.as_view(),name='ver_inasistencias'),
]


