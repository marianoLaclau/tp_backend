from django.db import models
from datetime import datetime


class Asistencias(models.Model):
    alumno = models.ForeignKey('alumno.Alumno',on_delete=models.CASCADE)
    curso = models.ForeignKey('inscripciones.Curso',on_delete=models.CASCADE)
    inasistencias = models.IntegerField()
    año_lectivo = models.IntegerField(default=datetime.now().year)
    turno = models.ForeignKey('administracion.Turno',on_delete=models.CASCADE)
    materia = models.ForeignKey('inscripciones.Materia',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alumno.apellido} : {self.inasistencias}"
    
    
class Calificaciones(models.Model):
    alumno = models.ForeignKey('alumno.Alumno',on_delete=models.CASCADE)
    curso = models.ForeignKey('inscripciones.Curso',on_delete=models.CASCADE)
    materia = models.ForeignKey('inscripciones.Materia',on_delete=models.CASCADE)
    trimestre_1 = models.FloatField(blank=True,null=True,default=0) 
    trimestre_2 = models.FloatField(blank=True,null=True,default=0)
    trimestre_3 = models.FloatField(blank=True,null=True,default=0)
    nota_final = models.FloatField(blank=True,null=True,default=0)
    estado = models.ForeignKey('administracion.Estado',on_delete=models.CASCADE)
    año_lectivo = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return f"{self.alumno} : T1: {self.trimestre_1} , T2: {self.trimestre_2} , T3: {self.trimestre_3}"
    
    
class Reserva(models.Model):
    docente = models.ForeignKey('administracion.Docente',on_delete=models.CASCADE)
    recurso = models.ForeignKey('recursos.Recursos',on_delete=models.CASCADE) 
    fecha = models.DateField()
    observaciones = models.CharField(max_length=50,default='Sin observaciones.')
    
    def __str__(self):    
        return f"{self.recurso.nombre}"