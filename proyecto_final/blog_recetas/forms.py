from django import forms

class Form_Receta(forms.Form):

    nombre_receta = forms.CharField()

    ingrediente_1 = forms.CharField()
    cantidad_ingrediente_1 = forms.IntegerField()

    ingrediente_2 = forms.CharField()
    cantidad_ingrediente_2 = forms.IntegerField()

    ingrediente_3 = forms.CharField()
    cantidad_ingrediente_3 = forms.IntegerField()

    paso_a_paso = forms.CharField()


class Form_Persona(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    ciudad = forms.CharField()
    provincia = forms.CharField()
    pais = forms.CharField()
    descripcion = forms.CharField()


    
    