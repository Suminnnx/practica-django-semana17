from django import forms
from .models import Autor, Libro, Prestamo


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'anio_publicacion', 'autor']
        labels = {
            'titulo': 'Título',
            'genero': 'Género',
            'anio_publicacion': 'Año de publicación',
        }


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'nombre_lector', 'fecha_prestamo']
        labels = {
            'nombre_lector': 'Nombre del lector',
            'fecha_prestamo': 'Fecha de préstamo',
        }
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
        }