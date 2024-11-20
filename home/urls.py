from django.urls import path
from .views import home_docente , home_admin , ayuda


urlpatterns = [
    path('home_docente/',home_docente,name='home_docente'),
    path('home_admin/',home_admin,name='home_admin'),
    path('ayuda/',ayuda,name='ayuda'),
]
