from docentes.models import Reserva
from recursos.models import Recursos
from .models import PersonalAdmin
from calendario.models import Calendario
from django.views.generic import ListView , CreateView , FormView , UpdateView
from django.urls import reverse_lazy
from .forms import PersonalForm , CalendarioForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.db.models.functions import ExtractYear
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class ReservasView(LoginRequiredMixin,ListView):
    model = Reserva
    template_name = 'administracion/reservas_admin.html'
    success_url = reverse_lazy('lista_reservas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar la lista de reservas al contexto
        context['reservas'] = Reserva.objects.all().order_by('-fecha')
        # Agregar la lista de recursos al contexto
        context['recursos'] = Recursos.objects.all()
        return context


class CreatePersonalAdmin(LoginRequiredMixin,CreateView):
    model = PersonalAdmin
    template_name = 'administracion/crear_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('lista_personal')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Agregado correctamente")
        return response
    

class EditPersonalAdmin(LoginRequiredMixin,UpdateView):
    model = PersonalAdmin
    template_name = 'administracion/editar_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('lista_personal')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Agregado correctamente")
        return response


class ListaPersonalAdmin(LoginRequiredMixin,ListView):
    model = PersonalAdmin
    template_name = 'administracion/lista_personal.html'
    context_object_name = 'personales'

    #Filtros para dni y apellido . Realizamos la consulta capturando los datos con el "name" del input
    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('buscar', '')
        apellido = self.request.GET.get('apellido', '')

        # Si el parametro pasado por url existe , almacena la respuesta
        if query:
            queryset = queryset.filter(dni__icontains=query)
        
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)

        return queryset

    #Definimos el contexto que vamos a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        # Renderizamos los valores seleccionados para mantener el filtro una vez realizada la busqueda
        context['buscar'] = self.request.GET.get('buscar', '')
        context['apellido'] = self.request.GET.get('apellido', '')

        return context    




class CalendarioAdminView(LoginRequiredMixin, FormView, ListView):
    model = Calendario
    template_name = 'administracion/crear_evento.html'
    context_object_name = 'eventos'
    form_class = CalendarioForm
    success_url = reverse_lazy('crear_evento')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Se creó el evento en el calendario.')
        return super().form_valid(form)

    def get_queryset(self):
        # Anotar el año del campo fecha , usamos ExtracYear por el campo DateTimeField (guarda la fecha entera)
        queryset = super().get_queryset().annotate(año_lectivo=ExtractYear('fecha'))

        # Filtrar por año lectivo si esta presente
        año_lectivo = self.request.GET.get('año_lectivo')
        if año_lectivo:
            queryset = queryset.filter(año_lectivo=año_lectivo)

        # Ordenar por fecha si se solicita
        orden = self.request.GET.get('orden', 'asc') # 2do parametro = default
        if orden == 'desc':
            queryset = queryset.order_by('-fecha')
        else:
            queryset = queryset.order_by('fecha')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        '''Obtener todos los años lectivos disponibles . 
        Equivalente en SQL :O  = SELECT DISTINCT EXTRACT(YEAR FROM fecha) AS año_lectivo FROM calendario ORDER BY año_lectivo ASC;'''
        context['años_lectivos'] = (
            self.get_queryset()
            .values_list('año_lectivo', flat=True)
            .distinct()
            .order_by('año_lectivo')
        )
        # Pasar el año lectivo seleccionado y el orden actual al contexto
        context['año_lectivo_seleccionado'] = self.request.GET.get('año_lectivo', '')
        context['orden'] = self.request.GET.get('orden', 'asc')
        return context



@login_required
@require_POST
def marcar_devuelto(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    recurso = reserva.recurso
    recurso.cantidad += 1
    
    if recurso.cantidad > 0:
        recurso.disponibilidad = True
    else:
        recurso.disponibilidad = False
    recurso.save()
    messages.success(request, f'El recurso {recurso.nombre} ha sido marcado como devuelto.')
    # Redirigir a la lista de reservas
    return redirect('lista_reservas')



def eliminar_registro(request, pk):
    if request.method == "POST" or request.method == "GET":  # Permite POST o GET
        registro = get_object_or_404(Calendario, id=pk)  # Busca el registro
        registro.delete()  # Elimina el registro
        messages.success(request,'Se elimino el registro correctamente.')
        return redirect('crear_evento')  # Redirige tras eliminar
