from django.db import models

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=50)

    ingrediente_1 = models.CharField(max_length=50)
    cantidad_ingr_1 = models.IntegerField()

    ingrediente_2 = models.CharField(max_length=50)
    cantidad_ingr_2 = models.IntegerField()

    ingrediente_3 = models.CharField(max_length=50)
    cantidad_ingr_3 = models.IntegerField()

# Create your models here.

