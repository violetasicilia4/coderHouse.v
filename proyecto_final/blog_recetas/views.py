from django.shortcuts import render


def home(request):

    return render(request, "inicio.html")

# Create your views here.
