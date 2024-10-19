from django.db import models
from administracion.models import Genero,Nacionalidad,Turno


class Curso(models.Model):
    año = models.CharField(max_length=20,null=False,blank=False)
    division = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.año

class Materia(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    
class PadreTutor(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    telefono = models.CharField(max_length=20,null=False,blank=False)
    telefono_secundario = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    direccion = models.CharField(max_length=50,null=False,blank=False)
    vinculo = models.CharField(max_length=50,null=False,blank=False)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    dni = models.CharField(max_length=20, unique=True)
    padretutor = models.ForeignKey(PadreTutor,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    email = models.EmailField()
    telefono = models.CharField(max_length=20,null=False,blank=False)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + self.apellido