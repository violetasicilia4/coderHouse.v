from django import forms
from .models import Persona
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class Form_Ejercicio(forms.Form):

    nombre_ejercicio = forms.CharField()

    paso_a_paso = forms.CharField()


class Form_Persona(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    sexo = forms.CharField(max_length = 50)
    ciudad = forms.CharField()
    provincia = forms.CharField()
    pais = forms.CharField()
    descripcion = forms.CharField()

'''class Form_Persona(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('__all__')
'''

class UserEditForm(UserChangeForm):
    
    password = forms.CharField(
        help_text = "",
        widget = forms.HiddenInput(), required=False
    )
    
    class Meta:
        model = User
        fields = (["email", "first_name", "last_name"])