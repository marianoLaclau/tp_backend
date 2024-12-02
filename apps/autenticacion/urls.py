from django.urls import path
from .views import RegistroView,CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registro/",RegistroView.as_view(),name="registro"),
    path("",CustomLoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]

