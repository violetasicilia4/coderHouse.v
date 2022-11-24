from django.shortcuts import render
from .forms import Form_Receta
from .models import Receta


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
            receta = Receta(nombre_receta=informacion["nombre_receta"], ingrediente_1=informacion["ingrediente_1"], cantidad_ingr_1 = informacion["cantidad_ingrediente_1"], ingrediente_2=informacion["ingrediente_2"], cantidad_ingr_2 = informacion["cantidad_ingrediente_2"], ingrediente_3=informacion["ingrediente_3"], cantidad_ingr_3 = informacion["cantidad_ingrediente_3"])
            receta.save()
            return render(request, "inicio.html")
    else:
        miFormulario = Form_Receta()
        
    return render(request, "form_ingredientes.html", {"miFormulario": miFormulario})