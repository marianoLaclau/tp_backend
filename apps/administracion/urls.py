from django.urls import path
from .views import ReservasView , ListaPersonalAdmin , CalendarioAdminView , CreatePersonalAdmin,marcar_devuelto, EditPersonalAdmin, eliminar_registro

urlpatterns = [
    path('reservas_admin/', ReservasView.as_view(), name='lista_reservas'),
    path('lista_personal/',ListaPersonalAdmin.as_view(),name='lista_personal'),
    path('crear_evento/',CalendarioAdminView.as_view(),name='crear_evento'),
    path('crear_personal/',CreatePersonalAdmin.as_view(),name='crear_personal'),
    path('marcar-devuelto/<int:reserva_id>/',marcar_devuelto, name='marcar_devuelto'),
    path('editar_personal/<int:pk>/',EditPersonalAdmin.as_view(),name='editar_personal'),
    path('eliminar_evento/<int:pk>/', eliminar_registro, name='eliminar_evento'),

]






