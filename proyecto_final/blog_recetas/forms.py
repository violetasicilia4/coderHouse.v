from django import forms

class Form_Receta(forms.Form):

    nombre_receta = forms.CharField()

    ingrediente_1 = forms.CharField()
    cantidad_ingrediente_1 = forms.IntegerField()

    ingrediente_2 = forms.CharField()
    cantidad_ingrediente_2 = forms.IntegerField()

    ingrediente_3 = forms.CharField()
    cantidad_ingrediente_3 = forms.IntegerField()


    
    