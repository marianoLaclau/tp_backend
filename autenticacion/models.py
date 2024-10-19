from django.db import models


class Usuario(models.Model):
    usuario = models.CharField(max_length=50,null=False,blank=False)
    contraseña = models.CharField(max_length=50,null=False,blank=False)
    personal_asignado = models.ForeignKey('administracion.PersonalAdmin', on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario