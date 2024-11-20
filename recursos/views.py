from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect 
from docentes.models import  Reserva 
from docentes.forms import  ReservaForm 
from django.views.generic import CreateView , ListView
from django.urls import reverse_lazy
from django.contrib import messages


class RegistrarResreva(LoginRequiredMixin,CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'recursos/crear_reserva.html'
    success_url = reverse_lazy('reservas')

    def form_valid(self, form):
        recurso = form.cleaned_data['recurso']  # obtener el recurso seleccionado

        # verificar si el recurso esta disponible
        if not recurso.disponibilidad:
            messages.error(self.request, f"El recurso {recurso.nombre} no está disponible en este momento.")
            return redirect('nueva_reserva')  # redirige al formulario

        messages.success(self.request, f"El recurso {recurso.nombre} se ha reservado correctamente.")
        return super().form_valid(form)
    


class ReservasView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'recursos/reservas.html'
    context_object_name = 'reservas'

    def get_queryset(self):
        # ordenar las reservas por fecha en orden descendente (+ reciente primero)
        return Reserva.objects.all().order_by('-fecha')


    
 

