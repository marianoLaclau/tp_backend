from .models import Curso , PadreTutor 
from administracion.models import Docente , Turno
from alumno.models import Alumno
from .forms import FormAlumno ,TutorForm ,FormDocente
from django.views.generic import CreateView , ListView , UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CreatePadreTutor(LoginRequiredMixin,CreateView):
    model = PadreTutor
    template_name = 'inscripcion/crear_tutor.html'
    form_class = TutorForm
    success_url = reverse_lazy('tutor')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Agregado correctamente.")
        return response
    

class ListaTutores(LoginRequiredMixin,ListView):
    model = PadreTutor
    template_name = 'inscripcion/lista_tutores.html'
    context_object_name = 'tutores'

    #Filtros para dni y apellido . Realizamos la consulta capturando los datos con el "name" del input
    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('buscar', '')
        apellido_alumno = self.request.GET.get('apellido', '')

        # Si el parametro pasado por url existe , almacena la respuesta
        if query:
            queryset = queryset.filter(dni__icontains=query)
        
        if apellido_alumno:
            queryset = queryset.filter(alumno_fk__apellido=apellido_alumno)

        return queryset

    #Definimos el contexto que vamos a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Renderizamos los valores seleccionados para mantener el filtro una vez realizada la busqueda
        context['buscar'] = self.request.GET.get('buscar', '')
        context['apellido'] = self.request.GET.get('apellido', '')

        return context    



class CreateAlumno(LoginRequiredMixin,CreateView):
    model = Alumno
    template_name = 'inscripcion/crear_alumno.html'
    form_class=FormAlumno
    success_url = reverse_lazy('lista_alumnos')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Agregado correctamente.")
        return response



class ViewDocente(LoginRequiredMixin,ListView):
    model = Docente
    template_name = 'inscripcion/lista_docentes.html'
    context_object_name = 'docentes'

    # Filtros para dni , turno, curso y buscar . Realizamos la consulta capturando los datos con el "name" del input
    def get_queryset(self): 
        queryset = super().get_queryset()
        query = self.request.GET.get('buscar', '')
        turno_id = self.request.GET.get('turno', '')
        curso_id = self.request.GET.get('curso', '')

        # Si el parametro pasado por url existe , almacena la respuesta
        if query:
            queryset = queryset.filter(dni__icontains=query)
        
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
        context['curso_id'] = self.request.GET.get('curso', '')
        context['turno_id'] = self.request.GET.get('turno', '')
        
        return context
    
    
    

class CreateDocente(LoginRequiredMixin,CreateView):
    model = Docente
    template_name = 'inscripcion/crear_docentes.html'
    form_class = FormDocente
    success_url = reverse_lazy('lista_docente')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Agregado correctamente.")
        return response



class EditarDocente(LoginRequiredMixin,UpdateView):
    model = Docente
    template_name = 'inscripcion/editar_docente.html'
    form_class = FormDocente
    success_url = reverse_lazy('lista_docente')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Modificacion realizada correctamente.")
        return response


class EditarTutor(LoginRequiredMixin,UpdateView):
    model = PadreTutor
    template_name = 'inscripcion/editar_tutor.html'
    form_class = TutorForm
    success_url = reverse_lazy('tutor')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Modificacion realizada correctamente.")
        return response