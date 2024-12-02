from django.contrib.auth.models import User, Group
from django.contrib import messages
from apps.administracion.models import Docente, PersonalAdmin
from django import forms
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistroFormulario
from django.contrib.auth.forms import AuthenticationForm

# Crear Registro
class RegistroView(CreateView):
    form_class = RegistroFormulario
    template_name = 'autenticacion/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        dni = form.cleaned_data["dni"]

        # Guardamos el usuario primero, pero sin relaciones many-to-many, esto lo anoto porque no lo sabia
        #y es algo de error que nos paso al intentar guardar el usuario antes de que tenga un grupo asignado
        user = form.save(commit=False)  # Esto no guarda el usuario en la base de datos todavía

        try:
            docente = Docente.objects.get(dni=dni)
            group = Group.objects.get(name="docentes")

            user.save()

            user.groups.add(group)

            user.save()

            messages.success(self.request, "Tu registro fue exitoso! Ya puedes iniciar sesión.")
            return super().form_valid(form)

        except Docente.DoesNotExist:
            try:
                personal_admin = PersonalAdmin.objects.get(dni=dni)
                group = Group.objects.get(name="personal_admin")

                user.save()  

                user.groups.add(group) 

                user.save()

                messages.success(self.request, "Tu registro fue exitoso! Ya puedes iniciar sesión.")
                return super().form_valid(form)

            except PersonalAdmin.DoesNotExist:
                messages.error(self.request, "El DNI no está registrado como docente ni como personal administrativo.")
                return self.form_invalid(form)



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=254)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')


        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError("Contraseña incorrecta")
            except User.DoesNotExist:
                raise forms.ValidationError("Usuario no encontrado")
        return cleaned_data
    
    

class CustomLoginView(LoginView):
    template_name = 'autenticacion/login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        """Redirecciona según el grupo del usuario después de iniciar sesión"""
        user = self.request.user
        try:
            if user.groups.filter(name='docentes').exists():
                return reverse_lazy('home_docente')
            elif user.groups.filter(name='personal_admin').exists():
                return reverse_lazy('home_admin')
            else:
                messages.error(self.request, "No se pudo encontrar un grupo correspondiente.")
                return reverse_lazy('login')
                
        except Exception as e:
            messages.error(self.request, f"Ha ocurrido un error: {str(e)}")
            return reverse_lazy('login')