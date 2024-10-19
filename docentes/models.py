from django.db import models
from incripciones.models import Alumno ,Curso ,Materia
from administracion.models import Estado
from docentes.models import Docente
from recursos.models import Recursos

class Asistencias(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    inasistencias = models.IntegerField()

    def __str__(self):
        return self.inasistencias
    
    

class Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    parcial_1 = models.FloatField()
    parcial_2 = models.FloatField()
    nota_final = models.FloatField()
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.alumno.nota
    
    
class Reserva(models.Model):
    docente = models.ForeignKey(Docente,on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recursos,on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):    
        return self.docente.nombre