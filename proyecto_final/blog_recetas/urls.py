from django.urls import path
from .views import home, ejemplo_blog, receta, Receta_LV, persona, Persona_LV, Receta_DV, loginView, registerView, modals_prueba
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home', home, name='Home'),
    path('blog', ejemplo_blog),
    path('receta', receta,name='Receta'),
    path('ver-receta', Receta_LV.as_view(), name='Ver_receta'),
    path('ver-receta-detalle', Receta_DV.as_view(), name='Ver_receta_detalle'),
    path('persona', persona, name='Perfil'),
    path('ver-perfil', Persona_LV.as_view(), name='Ver_perfil'),
    path('login', loginView, name="Login"),
    path('register', registerView, name='Register'),
    path('logout', LogoutView.as_view(template_name = "logout.html"), name='Logout'),
    path('prueba', modals_prueba, name="Prueba"),
]