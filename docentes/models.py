from django.db import models


class Asistencias(models.Model):
    alumno = models.ForeignKey('inscripciones.Alumno',on_delete=models.CASCADE)
    curso = models.ForeignKey('inscripciones.Curso',on_delete=models.CASCADE)
    inasistencias = models.IntegerField()

    def __str__(self):
        return self.inasistencias
    
    

class Calificaciones(models.Model):
    alumno = models.ForeignKey('inscripciones.Alumno',on_delete=models.CASCADE)
    curso = models.ForeignKey('inscripciones.Curso',on_delete=models.CASCADE)
    materia = models.ForeignKey('inscripciones.Materia',on_delete=models.CASCADE)
    parcial_1 = models.FloatField()
    parcial_2 = models.FloatField()
    nota_final = models.FloatField()
    estado = models.ForeignKey('administracion.Estado',on_delete=models.CASCADE)

    def __str__(self):
        return self.nota_final
    
    
class Reserva(models.Model):
    docente = models.ForeignKey('administracion.Docente',on_delete=models.CASCADE)
    recurso = models.ForeignKey('recursos.Recursos',on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):    
        return self.recurso