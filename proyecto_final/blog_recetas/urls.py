from django.urls import path
from .views import home, ejemplo_blog, ejercicio, Ejercicio_LV, persona, Persona_LV, Ejercicio_DV, loginView, registerView, modals_prueba, about, editarPerfil, nosotros, contacto, Ejercicio_Create,Ejercicio_Actualizar,Ejercicio_Eliminar,buscar,Persona_Create,Persona_Eliminar,Persona_DV
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home/', home, name='Home'),
    path('blog/', ejemplo_blog),
    path('persona/', persona, name='Perfil'),
    path('editar-perfil/', editarPerfil, name='Editar_perfil'),
    path('login/', loginView, name="Login"),
    path('register/', registerView, name='Register'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name='Logout'),
    path('prueba/', modals_prueba, name="Prueba"),
    path('about/', about, name = 'About'),
    path('nosotros/', nosotros, name = 'Nosotros'),
    path('contacto/', contacto, name = 'Contacto'),
    path('ejercicio/', Ejercicio_Create.as_view(),name='Ejercicio'),
    path('ver-ejercicio/', Ejercicio_LV.as_view(), name='Ver_ejercicio'),
    path('ver-ejercicio-detalle/<pk>', Ejercicio_DV.as_view(), name='Ver_ejercicio_detalle'),
    path('actualizar-ejercicio/<pk>', Ejercicio_Actualizar.as_view(), name='Actualizar_ejercicio'),
    path('eliminar-ejercicio/<pk>', Ejercicio_Eliminar.as_view(), name='Eliminar_ejercicio'),
    path('buscar/', buscar, name = 'Buscar'),
    path('ver-perfil/', Persona_LV.as_view(), name='Ver_perfil'),
    path('consulta/', Persona_Create.as_view() , name='Consulta'),
    path('eliminar-persona/<pk>', Persona_Eliminar.as_view(), name='Eliminar_consulta'),
    path('ver-persona-detalle/<pk>', Persona_DV.as_view(), name='Ver_persona_detalle'),
    
]