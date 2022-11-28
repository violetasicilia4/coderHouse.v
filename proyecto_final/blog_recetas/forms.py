from django import forms
from .models import Persona
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class Form_Ejercicio(forms.Form):

    nombre_ejercicio = forms.CharField()
    grupo_muscular = forms.CharField()
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

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    
    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2