from django.urls import path
from .views import  RegistrarResreva , ReservasView


urlpatterns = [
    path('reservas/',ReservasView.as_view(), name='reservas'),
    path('agregar_reserva/',RegistrarResreva.as_view(),name='nueva_reserva'),
]






