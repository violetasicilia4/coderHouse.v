# Generated by Django 4.1.2 on 2022-11-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='paso_a_paso',
            field=models.CharField(default='Descripcion de la receta', max_length=500),
        ),
    ]
