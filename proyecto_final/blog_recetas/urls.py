from django.urls import path
from .views import home, ejemplo_blog, receta, Receta_LV

urlpatterns = [
    path('home', home, name='Home'),
    path('blog', ejemplo_blog),
    path('receta', receta,name='Receta'),
    path('ver-receta', Receta_LV.as_view() ,name='Ver_receta'),
]