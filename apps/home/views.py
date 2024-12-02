from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_docente(request):
    return render(request,'docentes/home_docente.html',{})


@login_required
def home_admin(request):
    return render(request,'administracion/home_admin.html',{})


@login_required
def ayuda(request):
    grupos_usuario = list(request.user.groups.values_list('name', flat=True))

    return render(request,'ayuda.html',{'grupos_usuario':grupos_usuario})