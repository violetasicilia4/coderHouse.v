from django.urls import path
from .views import home, ejemplo_blog, ejercicio, Ejercicio_LV, persona, Persona_LV, Ejercicio_DV, loginView, registerView, modals_prueba, about, editarPerfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home/', home, name='Home'),
    path('blog/', ejemplo_blog),
    path('ejercicio/', ejercicio,name='Ejercicio'),
    path('ver-ejercicio/', Ejercicio_LV.as_view(), name='Ver_ejercicio'),
    path('ver-ejercicio-detalle/', Ejercicio_DV.as_view(), name='Ver_ejercicio_detalle'),
    path('persona/', persona, name='Perfil'),
    path('ver-perfil/', Persona_LV.as_view(), name='Ver_perfil'),
    path('editar-perfil/', editarPerfil, name='Editar_perfil'),
    path('login/', loginView, name="Login"),
    path('register/', registerView, name='Register'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name='Logout'),
    path('prueba/', modals_prueba, name="Prueba"),
    path('about/', about, name = 'About')
]