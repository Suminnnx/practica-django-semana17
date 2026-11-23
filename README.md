# Práctica Semana 17 - Django 

Sistema de biblioteca con tres modelos relacionados (Autor, Libro y Préstamo), con CRUD usando formularios de Django y CSS básico.

## Modelos

- **Autor**: nombre, apellido y nacionalidad.
- **Libro**: título, género, año de publicación y autor.
- **Préstamo**: libro, nombre del lector y fecha de préstamo.

## Cómo correrlo

```
git clone https://github.com/Suminnnx/practica-django-semana17.git
cd practica-django-semana17
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py runserver
```

Luego abrir http://127.0.0.1:8000/autores/
