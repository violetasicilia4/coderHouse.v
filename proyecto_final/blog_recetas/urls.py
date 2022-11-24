from django.urls import path
from .views import home, ejemplo_blog, receta

urlpatterns = [
    path('home', home, name='Home'),
    path('blog', ejemplo_blog),
    path('receta', receta,name='Receta'),
]