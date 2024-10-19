from django.db import models
from incripciones.models import Materia 


class Estado(models.Model):
    nombre = models.CharField(max_length=25,null=False,blank=False)

    def __str__(self):
        return self.nombre
    
    
class Genero(models.Model):
    tipo = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.tipo
    
class Turno(models.Model):
    turno = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.turno

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.pais
    
class Docente(models.Model):
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField()
    direccion = models.CharField(max_length=50,null=False,blank=False)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + self.apellido
    
    
class PersonalAdmin(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    telefono = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField()
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + self.apellido