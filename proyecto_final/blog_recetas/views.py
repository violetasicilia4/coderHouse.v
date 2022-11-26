from django.shortcuts import render
from .forms import Form_Receta, Form_Persona
from .models import Receta, Persona
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def home(request):

    return render(request, "inicio.html")

def ejemplo_blog(request):

    return render(request, "nav_bar.html")

# Create your views here.


 
def receta(request):
 
    if request.method == "POST":

        miFormulario = Form_Receta(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            receta = Receta(nombre_receta=informacion["nombre_receta"], ingrediente_1=informacion["ingrediente_1"], cantidad_ingr_1 = informacion["cantidad_ingrediente_1"], ingrediente_2=informacion["ingrediente_2"], cantidad_ingr_2 = informacion["cantidad_ingrediente_2"], ingrediente_3=informacion["ingrediente_3"], cantidad_ingr_3 = informacion["cantidad_ingrediente_3"], paso_a_paso = informacion["paso_a_paso"])
            receta.save()
            return render(request, "inicio.html")
    else:
        miFormulario = Form_Receta()
        
    return render(request, "form_ingredientes.html", {"miFormulario": miFormulario})

def persona(request):
 
    if request.method == "POST":

        form_persona = Form_Persona(request.POST) # Aqui me llega la informacion del html
        print(form_persona)

        if form_persona.is_valid:
            informacion = form_persona.cleaned_data
            persona = Persona(nombre=informacion["nombre"], apellido=informacion["apellido"], ciudad = informacion["ciudad"], provincia=informacion["provincia"], pais = informacion["pais"], descripcion=informacion["descripcion"])
            persona.save()
            return render(request, "inicio.html")
    else:
        form_persona = Form_Persona()
        
    return render(request, "form_persona.html", {"form_persona": form_persona})

"""CLASES PARA RECETAS"""

class Receta_LV(ListView):
    model= Receta
    template_name= "ver_receta.html"

class Receta_DV(DetailView):
    model= Receta
    template_name= "ver_receta_detalle.html"

"""CLASES PARA PERSONAS"""
class Persona_LV(ListView):
    model= Persona
    template_name= "ver_perfil.html"


"""Login"""

def loginView(request):

    if request.method == 'POST':
        form_login = AuthenticationForm(request, data = request.POST)

        if form_login.is_valid():  # Si pasó la validación de Django
            
            data = form_login.cleaned_data
            usuario = data["username"]
            contrasenia = data["password"]

            user = authenticate(username= usuario, password=contrasenia)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
        
        return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})
           
    else:

        form_login = AuthenticationForm()

        return render(request, "login.html", {"form_login": form_login})

def registerView(request):

    if request.method == 'POST':
        form_register = UserCreationForm(request.POST)

        if form_register.is_valid():  # Si pasó la validación de Django
            
            username = form_register.cleaned_data["username"]
            
            form_register.save()
           
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        
        else:
            
            return render(request, "inicio.html", {"mensaje":f"Error al crear el usuario"})
        
    else:

        form_register = UserCreationForm()

        return render(request, "register.html", {"form_register": form_register})  


def modals_prueba(request):

    return render(request, "modal.html")