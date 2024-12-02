from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistroFormulario(forms.ModelForm):
    dni = forms.CharField(max_length=10, label='DNI', required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'dni', 'contraseña']

    def __init__(self, *args, **kwargs):
        super(RegistroFormulario, self).__init__(*args, **kwargs)
        
        # Asignar clases CSS personalizadas a los campos
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['dni'].widget.attrs.update({'class': 'form-control'})
        self.fields['contraseña'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["contraseña"])
        if commit:
            user.save()
        return user
    

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