from django.db import models



class Alumno(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    dni = models.CharField(max_length=20, unique=True)
    padretutor_fk = models.ForeignKey('inscripciones.PadreTutor',null=True,blank=True,on_delete=models.SET_NULL) #Chequear 
    genero = models.ForeignKey('administracion.Genero',on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    nacionalidad = models.ForeignKey('administracion.Nacionalidad',on_delete=models.CASCADE)
    email = models.EmailField()
    telefono = models.CharField(max_length=20,null=False,blank=False)
    direccion = models.CharField(max_length=50,null=False,blank=False)
    curso = models.ForeignKey('inscripciones.Curso',on_delete=models.CASCADE)
    turno = models.ForeignKey('administracion.Turno',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.apellido},{self.nombre}"