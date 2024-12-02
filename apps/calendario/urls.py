from django.urls import path
from .views import calendario_view

urlpatterns = [
    path('calendario/', calendario_view, name='calendario'),
    
]
