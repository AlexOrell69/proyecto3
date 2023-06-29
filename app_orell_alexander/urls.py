from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   
    path('',views.index, name='index'),
    path('logout/', views.exit, name="exit"),
    path('contenido/', views.contenido, name="contenido"),
    path('servicios/', views.servicios, name="servicios"),
    path('productos/', views.productos, name="productos"),
    path('contacto/', views.contacto, name="contacto"),
    path('agregar/', views.agregar, name='agregar' ),
    path('agregarrec/', views.agregarrec, name='agregarrec' ),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar' ),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar' ),
    path('actualizar/actualizarrec/<int:id>/', views.actualizarrec, name='actualizarrec' ),
    path('register/', views.register, name='register'),
]
