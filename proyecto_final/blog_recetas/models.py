from django.db import models


class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=200)
    grupo_muscular = models.CharField(max_length=50)
    paso_a_paso = models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre del ejercicio: {self.nombre_ejercicio}"



class Persona(models.Model):

    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length = 50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    descripcion = models.CharField(max_length = 500)
    


    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}"



# Create your models here.

