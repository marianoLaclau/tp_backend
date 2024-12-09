from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView , UpdateView , DetailView
from .models import Alumno 
from apps.inscripciones.models import Curso 
from apps.administracion.models import Turno
from apps.docentes.models import Calificaciones , Asistencias
from apps.inscripciones.forms import FormAlumno
from django.contrib import messages


class ViewAlumno(LoginRequiredMixin,ListView):
    model = Alumno
    template_name = 'alumno/lista_alumnos.html'
    context_object_name = 'alumnos'
    paginate_by = 20

    # Filtros para dni , turno, curso y buscar . Realizamos la consulta capturando los datos con el "name" del input
    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('buscar', '')
        apellido = self.request.GET.get('apellido','')
        turno_id = self.request.GET.get('turno', '')
        curso_id = self.request.GET.get('curso', '')

        # Si el parametro pasado por url existe , almacena la respuesta
        if query:
            queryset = queryset.filter(dni__icontains=query)
        
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        
        if turno_id:
            queryset = queryset.filter(turno_id=turno_id)
        
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)
        
        queryset = queryset.select_related('turno', 'curso', 'genero') # Relacionamos los modelos para obtener filtros combinados

        return queryset

    # Definimos el contexto que vamos a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Para los desplegables usamos las lookup
        context['cursos'] = Curso.objects.all()
        context['turnos'] = Turno.objects.all()
        # Renderizamos los valores seleccionados para mantener el filtro una vez realizada la busqueda
        context['buscar'] = self.request.GET.get('buscar', '')
        context['apellido']=self.request.GET.get('apellido','')
        context['curso_id'] = self.request.GET.get('curso', '')
        context['turno_id'] = self.request.GET.get('turno', '')
        
        return context
    


class EditAlumnoView(LoginRequiredMixin,UpdateView):
    model = Alumno
    form_class = FormAlumno
    template_name = 'alumno/editar_alumno.html'
    success_url = reverse_lazy('lista_alumnos')

    def form_valid(self, form):
        # Agregar mensaje de exito
        messages.success(self.request, "Alumno actualizado exitosamente.")
        # Continuar con el flujo normal de `form_valid`
        return super().form_valid(form)


class VerAlumnoView(LoginRequiredMixin,DetailView):
    model = Alumno
    template_name = 'alumno/ver_alumno.html'

    

class VerCalificaciones(LoginRequiredMixin, ListView):
    model = Calificaciones
    template_name = 'alumno/ver_calificaciones.html'
    context_object_name = 'calificaciones'

    def get_queryset(self):
        # Filtra las calificaciones segun el alumno especificado en la URL
        alumno_id = self.kwargs.get('pk')
        queryset = Calificaciones.objects.filter(alumno_id=alumno_id)

        # Filtrar adicionalmente por año lectivo si se proporciona en la solicitud
        año_lectivo = self.request.GET.get('año_lectivo')
        if año_lectivo:
            queryset = queryset.filter(año_lectivo=año_lectivo)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el objeto Alumno correspondiente al pk de la URL
        alumno_id = self.kwargs.get('pk')
        context['alumno'] = get_object_or_404(Alumno, id=alumno_id)

        # Añadir solo los años lectivos registrados para este alumno
        context['años_lectivos'] = Calificaciones.objects.filter(alumno_id=alumno_id).values_list('año_lectivo', flat=True).distinct()
        
        # Mantener el año lectivo seleccionado en el contexto
        context['año_lectivo_seleccionado'] = self.request.GET.get('año_lectivo', '')

        return context
      

class VerInasistencias(LoginRequiredMixin, ListView):
    model = Asistencias
    template_name = 'alumno/ver_inasistencias.html'
    context_object_name = 'inasistencias'

    def get_queryset(self):
        # Filtra las calificaciones segun el alumno especificado en la URL
        alumno_id = self.kwargs.get('pk')
        queryset = Asistencias.objects.filter(alumno_id=alumno_id)

        # Filtrar adicionalmente por año lectivo si se proporciona en la solicitud
        año_lectivo = self.request.GET.get('año_lectivo')
        if año_lectivo:
            queryset = queryset.filter(año_lectivo=año_lectivo)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el objeto Alumno correspondiente al pk de la URL
        alumno_id = self.kwargs.get('pk')
        context['alumno'] = get_object_or_404(Alumno, id=alumno_id)

        # Añadir solo los años lectivos registrados para este alumno
        context['años_lectivos'] = Calificaciones.objects.filter(alumno_id=alumno_id).values_list('año_lectivo', flat=True).distinct()
        
        # Mantener el año lectivo seleccionado en el contexto
        context['año_lectivo_seleccionado'] = self.request.GET.get('año_lectivo', '')

        return context
