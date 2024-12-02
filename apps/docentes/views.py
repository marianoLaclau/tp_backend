from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView , ListView , UpdateView
from .models import Asistencias  , Calificaciones
from apps.inscripciones.models import Materia , Curso 
from apps.administracion.models import Estado , Turno
from .forms import AsistenciasForm  , CalificacionForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.utils.http import url_has_allowed_host_and_scheme



class RegistrarInasistenciaView(LoginRequiredMixin,CreateView):
    model = Asistencias
    form_class = AsistenciasForm
    template_name = 'docentes/crear_asistencia.html'
    success_url = reverse_lazy('inasistencia')

    def form_valid(self, form):
        messages.success(self.request,'La inasistencia se registro correctamente.')
        return super().form_valid(form)


class InasistenciasView(LoginRequiredMixin, ListView):
    model = Asistencias
    template_name = 'docentes/asistencias.html'
    context_object_name = 'inasistencias'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener los datos por URL desde el formulario HTML
        turno_id = self.request.GET.get('turno', '')
        curso_id = self.request.GET.get('curso', '')
        anio_lectivo = self.request.GET.get('anio', '')
        materia_id = self.request.GET.get('materia','')

        # Si no hay filtros aplicados, devolver un queryset vacio
        if not any([turno_id, curso_id, anio_lectivo,materia_id]):
            return queryset.none()

        # Aplicar filtros si los valores existen
        if turno_id:
            queryset = queryset.filter(turno_id=turno_id)
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        if anio_lectivo:
            queryset = queryset.filter(año_lectivo=anio_lectivo)
        if materia_id:
            queryset = queryset.filter(materia_id=materia_id)

        # Relacionar los modelos para optimizar consultas
        queryset = queryset.select_related('turno', 'curso','materia')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cargar todas las opciones para los desplegables
        context['turnos'] = Turno.objects.all()
        context['cursos'] = Curso.objects.all()
        context['materias'] = Materia.objects.all()

        # Obtener años unicos de `año_lectivo` para el desplegable
        context['año_lectivo'] = Asistencias.objects.values_list('año_lectivo', flat=True).distinct()

        # Mantener los valores seleccionados en los filtros
        context['turno_id'] = self.request.GET.get('turno', '')
        context['curso_id'] = self.request.GET.get('curso', '')
        context['anio'] = self.request.GET.get('anio', '')
        context['materia_id'] = self.request.GET.get('materia','')

        return context


def sumarInasistencia(request, pk):
    asistencia = get_object_or_404(Asistencias, pk=pk)
    asistencia.inasistencias += 1
    asistencia.save()
    messages.success(request, 'Se agregó la inasistencia correctamente.')
    
    next_url = request.GET.get('next')
    if not next_url or not url_has_allowed_host_and_scheme(next_url, allowed_hosts=request.get_host()):
        next_url = reverse('inasistencia')
    return redirect(next_url)


class RegistrarCalificacion(LoginRequiredMixin,CreateView):
    model = Calificaciones
    form_class = CalificacionForm
    template_name = 'docentes/crear_calificacion.html'
    success_url = reverse_lazy('calificaciones')

    def form_valid(self, form):
        messages.success(self.request,'Se agrego el nuevo registro con exito.')
        return super().form_valid(form)

    
class EditarCalificacionView(LoginRequiredMixin,UpdateView):
    model = Calificaciones
    form_class = CalificacionForm
    template_name = 'docentes/editar_calificacion.html'
    success_url = reverse_lazy('calificaciones')

    def form_valid(self, form):
        messages.success(self.request,'Se agrego la calificacion correctamente.')
        return super().form_valid(form)


class CalificacionesView(LoginRequiredMixin, ListView):
    model = Calificaciones
    template_name = 'docentes/calificaciones.html'
    context_object_name = 'calificaciones'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener los datos por url desde el formulario HTML
        materia_id = self.request.GET.get('materia', '')
        curso_id = self.request.GET.get('curso', '')
        estado_id = self.request.GET.get('estado', '')
        año_lectivo = self.request.GET.get('año_lectivo', '')

        # Si no hay filtros aplicados, devolver un queryset vacio
        if not any([materia_id, curso_id, estado_id, año_lectivo]):
            return queryset.none()

        # Aplicar filtros si los valores existen
        if materia_id:
            queryset = queryset.filter(materia_id=materia_id)
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        if estado_id:
            queryset = queryset.filter(estado_id=estado_id)
        if año_lectivo:
            queryset = queryset.filter(año_lectivo=año_lectivo)

        # Relacionar los modelos para optimizar consultas
        queryset = queryset.select_related('materia', 'curso', 'estado')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cargar todas las opciones para los desplegables
        context['materias'] = Materia.objects.all()
        context['cursos'] = Curso.objects.all()
        context['estados'] = Estado.objects.all()

        # Obtener años únicos de `año_lectivo` para el desplegable
        context['años_lectivos'] = Calificaciones.objects.values_list('año_lectivo', flat=True).distinct()

        # Mantener los valores seleccionados en los filtros
        context['materia_id'] = self.request.GET.get('materia', '')
        context['curso_id'] = self.request.GET.get('curso', '')
        context['estado_id'] = self.request.GET.get('estado', '')
        context['año_lectivo'] = self.request.GET.get('año_lectivo', '')

        return context




        


