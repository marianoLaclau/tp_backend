from django.urls import path
from .views import RegistrarInasistenciaView , CalificacionesView , EditarCalificacionView , RegistrarCalificacion , InasistenciasView , sumarInasistencia


urlpatterns = [
    path('inasistencias/', InasistenciasView.as_view(), name='inasistencia'),
    path("crear_inasistencia/",RegistrarInasistenciaView.as_view(), name="nueva_inasistencia"),
    path('sumar_inasistencia/<int:pk>',sumarInasistencia,name='sumar_inasistencia'),
    path('calificaiones/',CalificacionesView.as_view(),name='calificaciones'),
    path('editar_nota/<int:pk>',EditarCalificacionView.as_view(),name='registrar_nota'),
    path('crear_calificacion',RegistrarCalificacion.as_view(),name='nueva_calificacion'),
]






