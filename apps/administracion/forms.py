from django.forms import ModelForm 
from .models import PersonalAdmin
from apps.calendario.models import Calendario
from django import forms


class PersonalForm(ModelForm):
    class Meta:
        model = PersonalAdmin
        fields = '__all__'



class CalendarioForm(ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'

        widgets = {
                'fecha': forms.DateInput(attrs={'type': 'date'}),
            }

