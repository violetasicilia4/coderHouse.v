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
        return f"Nombre de la receta: {self.nombre_receta}\nIngredientes:\n{self.ingrediente_1}: {self.cantidad_ingr_1}\n{self.ingrediente_2}: {self.cantidad_ingr_2}\n{self.ingrediente_3}: {self.cantidad_ingr_3}\nDescripcion de la receta:\n{self.paso_a_paso}"
# Create your models here.

