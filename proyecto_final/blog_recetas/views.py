from django.shortcuts import render
from .forms import Form_Ejercicio, Form_Persona
from .models import Ejercicio, Persona
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

def modals_prueba(request):

    return render(request, "footers.html")

def buscar(request):
 
    if request.GET["nombre_ejercicio"]:

        nombre_ejercicio = request.GET["nombre_ejercicio"]

        ejercicios = Ejercicio.objects.filter(nombre_ejercicio__icontains=nombre_ejercicio)
        
        print(nombre_ejercicio,ejercicios)

        return render(request, "buscar.html", {"ejercicios": ejercicios, "nombre_ejercicio": nombre_ejercicio})

    """if request.GET["grupo_muscular"]:

        grupo_muscular = request.GET["grupo_muscular"]

        nombre_ejercicios = Ejercicio.objects.filter(grupo_muscular__icontains=grupo_muscular)
        

        return render(request, "buscar.html", {"nombre_ejercicios": nombre_ejercicios, "grupo_muscular": grupo_muscular})"""



def home(request):

    return render(request, "home.html")

def about(request):

    return render(request, "about.html")

def nosotros(request):

    return render(request, "nosotros.html")

def contacto(request):

    return render(request, "contacto.html")

def ejemplo_blog(request):

    return render(request, "nav_bar.html")
 
def ejercicio(request):
    
    print('method:', request.method)
    print('post: ', request.POST)
 
    if request.method == "POST":

        miFormulario = Form_Ejercicio(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            ejercicio = Ejercicio(nombre_ejercicio=informacion["nombre_ejercicio"],grupo_muscular=informacion["grupo_muscular"], paso_a_paso = informacion["paso_a_paso"])
            ejercicio.save()
            return render(request, "form_rutina.html",{"miFormulario": miFormulario,"mensaje":"Ejercicio guardado con ??xito"})
    else:
        miFormulario = Form_Ejercicio()
        
    return render(request, "form_rutina.html", {"miFormulario": miFormulario})

def persona(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == "POST":

        form_persona = Form_Persona(request.POST) # Aqui me llega la informacion del html
        print(form_persona)

        if form_persona.is_valid():
            informacion = form_persona.cleaned_data
            persona = Persona(nombre=informacion["nombre"], apellido=informacion["apellido"], ciudad = informacion["ciudad"], provincia=informacion["provincia"], pais = informacion["pais"], descripcion=informacion["descripcion"])
            persona.save()
            return render(request, "inicio.html")
    else:
        form_persona = Form_Persona()
        
    return render(request, "form_persona.html", {"form_persona": form_persona})

"""CLASES PARA EJERCICIO"""

class Ejercicio_LV(ListView):
    model= Ejercicio
    template_name= "ver_rutina.html"

class Ejercicio_DV(DetailView):
    model= Ejercicio
    template_name= "ver_rutina_detalle.html"

class Ejercicio_Create(CreateView):

    model = Ejercicio
    template_name = 'crear_rutina.html'
    fields = ['nombre_ejercicio','grupo_muscular','paso_a_paso']
    success_url = '/modificar-nombre/ver-ejercicio/'
    

class Ejercicio_Actualizar(UpdateView):

    model = Ejercicio
    template_name = 'actualizar_rutina.html'
    fields = ('__all__')
    success_url = '/modificar-nombre/ver-ejercicio/'

class Ejercicio_Eliminar(DeleteView):

    model = Ejercicio
    template_name = 'eliminar_rutina.html'
    success_url = '/modificar-nombre/ver-ejercicio/'

"""CLASES PARA PERSONAS"""
class Persona_LV(ListView):
    model= Persona
    template_name= "ver_perfil.html"

class Persona_DV(DetailView):
    model= Persona
    template_name= "ver_perfil_detalle.html"

class Persona_Create(CreateView):

    model = Persona
    template_name = 'consulta.html'
    fields = ['nombre','apellido','edad','sexo','dni','telefono','descripcion']
    success_url = '/modificar-nombre/home'

class Persona_Eliminar(DeleteView):

    model = Persona
    template_name = 'eliminar_consulta.html'
    success_url = '/modificar-nombre/ver-perfil/'

"""Login"""

def loginView(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        form_login = AuthenticationForm(request, data = request.POST)

        if form_login.is_valid():  # Si pas?? la validaci??n de Django
            
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

        if form_register.is_valid():  # Si pas?? la validaci??n de Django
            
            username = form_register.cleaned_data["username"]
            
            form_register.save()
           
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        
        else:
            
            return render(request, "inicio.html", {"mensaje":f"Error al crear el usuario"})
        
    else:

        form_register = UserCreationForm()

        return render(request, "register.html", {"form_register": form_register})  





# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        user_editForm = UserEditForm(request.POST)

        if user_editForm.is_valid():

            informacion = user_editForm.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.set_password(informacion['password1'])
    

            usuario.save()

            return render(request, "editar_perfil.html", {"user_editForm": user_editForm, "usuario": usuario,"mensaje1" : f"Datos actualizados correctamente"})

        else:
            
            return render(request, "editar_perfil.html", {"user_editForm": user_editForm, "usuario": usuario})
    else:

        user_editForm = UserEditForm(instance=request.user)

        return render(request, "editar_perfil.html", {"user_editForm": user_editForm, "usuario": usuario})
