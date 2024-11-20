# forms.py
from django import forms
from .models import Asistencias , Reserva , Calificaciones
from django.db.models import F

class AsistenciasForm(forms.ModelForm):
    class Meta:
        model = Asistencias
        fields = ['alumno', 'curso','año_lectivo','turno','materia','inasistencias']

    # Antes de guardar el form comprobamos si ya existe registro para sumar +=1  sobreescribiendo el metodo save()
    def save(self, commit=True):
        # Obtener los datos limpios del formulario
        alumno = self.cleaned_data['alumno']
        curso = self.cleaned_data['curso']
        año_lectivo = self.cleaned_data['año_lectivo']
        turno = self.cleaned_data['turno']
        materia = self.cleaned_data['materia']

        # Intentar obtener un registro existente , con la variable created comprobamos si se creo o no
        asistencia, created = Asistencias.objects.get_or_create(
            alumno=alumno,
            curso=curso,
            año_lectivo=año_lectivo,
            turno=turno,
            materia=materia,
            defaults={'inasistencias': 1}  # Si es nuevo, inicia con 1
        )

        if not created:
            # Si el registro ya existía, incrementar inasistencias
            Asistencias.objects.filter(id=asistencia.id).update(inasistencias=F('inasistencias') + 1) # La F es para que la sentencia se ejecute directamente en la BBDD sin cargar un objeto en la memoria
            asistencia.refresh_from_db()  # Actualizar el objeto con el nuevo valor

        return asistencia



class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

        widgets = {
                'fecha': forms.DateInput(attrs={'type': 'date'}),
            }

    def save(self, commit=True):
        instance = super().save(commit=False)  # Se usa commit=False para trabajar con la instancia sin guardarla de inmediato
        
        # Restar 1 de la cantidad del recurso asociado
        if instance.recurso.cantidad > 0:
            instance.recurso.cantidad -= 1
        else:
            instance.recurso.cantidad = 0  # Asegurarse de que no sea negativa

        # Actualizar disponibilidad del recurso
        instance.recurso.disponibilidad = instance.recurso.cantidad > 0
        
        # Guardar los cambios si commit es True
        if commit:
            instance.recurso.save(update_fields=['cantidad', 'disponibilidad'])
            instance.save()
        
        return instance


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = '__all__'





    
