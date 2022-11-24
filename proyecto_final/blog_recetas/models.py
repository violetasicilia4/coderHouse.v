from django.db import models


class Receta(models.Model):
    nombre_receta = models.CharField(max_length=50)

    ingrediente_1 = models.CharField(max_length=50)
    cantidad_ingr_1 = models.IntegerField()

    ingrediente_2 = models.CharField(max_length=50)
    cantidad_ingr_2 = models.IntegerField()

    ingrediente_3 = models.CharField(max_length=50)
    cantidad_ingr_3 = models.IntegerField()

    paso_a_paso = models.CharField(max_length=500, default="Descripcion de la receta")

    def __str__(self):
        return f"Nombre de la receta: {self.nombre_receta}"



class Persona(models.Model):

    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 50)
    provincia = models.CharField(max_length = 50)
    pais = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 300)
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}"



# Create your models here.

