import calendar
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render,redirect
from .models import Calendario
from django.contrib.auth.decorators import login_required 
from collections import defaultdict



@login_required
def calendario_view(request):
    if request.user.groups.filter(name='docentes').exists():  # Restringimos la vista solo a los docentes
        # Obtener mes y año de la URL, o usar el mes/año actual
        mes_actual = int(request.GET.get('month', datetime.now().month))
        año_actual = int(request.GET.get('year', datetime.now().year))

        # Ajustar mes y año si el mes esta fuera de rango
        if mes_actual < 1:
            mes_actual = 12
            año_actual -= 1
        elif mes_actual > 12:
            mes_actual = 1
            año_actual += 1

        # Crear el calendario del mes
        cal = calendar.Calendar(firstweekday=0)
        dias_mes = cal.monthdayscalendar(año_actual, mes_actual)

        # Obtener los eventos del mes actual
        eventos = Calendario.objects.filter(fecha__year=año_actual, fecha__month=mes_actual)

        # Agrupar eventos por día
        eventos_por_dia = defaultdict(list)
        for evento in eventos:
            eventos_por_dia[evento.fecha.day].append(evento)

        # Pasar los datos al template
        contexto = {
            'dias_mes': dias_mes,
            'mes': calendar.month_name[mes_actual],
            'mes_actual': mes_actual,
            'año': año_actual,
            'eventos_por_dia': dict(eventos_por_dia),  # Convertir a dict estándar para pasar a la plantilla
        }

        return render(request, 'calendario/calendario.html', contexto)

    else:
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')




    

    

