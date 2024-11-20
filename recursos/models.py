from django.db import models

class NombreRecurso(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self) :
        return self.nombre
    

class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self) :
        return self.nombre
    

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self) :
        return self.nombre
    

class Recursos(models.Model):
    nombre = models.ForeignKey(NombreRecurso,on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoRecurso,on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    cantidad = models.IntegerField() 
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre.nombre


   
    