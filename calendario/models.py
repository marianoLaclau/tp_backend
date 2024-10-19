from django.db import models


class Evento(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
            return self.nombre


class Calendario(models.Model):
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    fecha = models.DateField()
    titulo = models.CharField(max_length=50,null=False,blank=False)
    descripcion = models.CharField(max_length=50,null=False,blank=False)
    turno = models.ForeignKey('administracion.Turno',on_delete=models.CASCADE)
    autor = models.ForeignKey('administracion.PersonalAdmin',on_delete=models.CASCADE)

    def __str__(self):
            return self.evento.nombre