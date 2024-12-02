from django.forms import ModelForm 
from apps.administracion.models import Docente
from apps.alumno.models import Alumno 
from .models import PadreTutor
from django import forms

class FormAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

        widgets = {
                'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            }
    
    #Normalizar los datos antes de almacenarlos
    def clean(self):
        cleaned_data = super().clean()
        # Convertir los campos 'nombre', 'apellido' 
        for field_name in ['nombre', 'apellido']:
            if field_name in cleaned_data and isinstance(cleaned_data[field_name], str):
                cleaned_data[field_name] = cleaned_data[field_name].title()#Todos comienzan con mayusculas
        return cleaned_data
    


class TutorForm(ModelForm):
    class Meta:
        model = PadreTutor
        fields = '__all__'
    
    #Normalizar los datos antes de almacenarlos
    def clean(self):
        cleaned_data = super().clean()
        # Convertir los campos 'nombre', 'apellido' y 'direccion' 
        for field_name in ['nombre', 'apellido']:
            if field_name in cleaned_data and isinstance(cleaned_data[field_name], str):
                cleaned_data[field_name] = cleaned_data[field_name].title()#Todos comienzan con mayusculas
        return cleaned_data
    
    
class FormDocente(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

        widgets = {
                'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            }
    
    #Normalizar los datos antes de almacenarlos
    def clean(self):
        cleaned_data = super().clean()
        # Convertir los campos 'nombre', 'apellido' 
        for field_name in ['nombre', 'apellido']:
            if field_name in cleaned_data and isinstance(cleaned_data[field_name], str):
                cleaned_data[field_name] = cleaned_data[field_name].title()#Todos comienzan con mayusculas
        return cleaned_data
    
    