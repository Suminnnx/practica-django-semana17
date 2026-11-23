from django.urls import path
from . import views

urlpatterns = [
    # Autor
    path('autores/',views.autor_list,name='autor_list'),
    path('autores/agregar/',views.autor_create,name='autor_create'),
    path('autores/editar/<int:pk>',views.autor_update,name='autor_update'),
    path('autores/eliminar/<int:pk>',views.autor_delete,name='autor_delete'),

    # Libro
    path('libros/',views.libro_list,name='libro_list'),
    path('libros/agregar/',views.libro_create,name='libro_create'),
    path('libros/editar/<int:pk>',views.libro_update,name='libro_update'),
    path('libros/eliminar/<int:pk>',views.libro_delete,name='libro_delete'),

    # Prestamo
    path('prestamos/',views.prestamo_list,name='prestamo_list'),
    path('prestamos/agregar/',views.prestamo_create,name='prestamo_create'),
    path('prestamos/editar/<int:pk>',views.prestamo_update,name='prestamo_update'),
    path('prestamos/eliminar/<int:pk>',views.prestamo_delete,name='prestamo_delete'),
]