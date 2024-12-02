from django.db import models


class Vinculo(models.Model):
    vinculo = models.CharField(max_length=50,blank=False,null=True)
    
    def __str__(self):
        return self.vinculo
    

class Curso(models.Model):
    año = models.CharField(max_length=20,null=False,blank=False)
    division = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return f"{self.año},{self.division}"

class Materia(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre
    
    
class PadreTutor(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    dni = models.CharField(max_length=50,blank=False,null=False)
    telefono = models.CharField(max_length=20,null=False,blank=False)
    telefono_secundario = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    direccion = models.CharField(max_length=50,null=False,blank=False)
    vinculo = models.ForeignKey(Vinculo,on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey('administracion.Nacionalidad', on_delete=models.CASCADE)
    alumno_fk = models.ForeignKey('alumno.Alumno',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.apellido},{self.nombre}"


