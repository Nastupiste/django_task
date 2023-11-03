# Guía práctica para la creación de una Aplicación Web con Django:

## 1. Disponer de Python y entorno virtual

Creación:

```SYS
mkvirtualenv django_task
```

Trabajar en el entorno:

```SYS
workon django_task
```

Actualizar pip:

```SYS
python -m pip install --upgrade pip
```

## 2. Usar el fichero requirements.txt con el comando:

```SYS
pip install -r requirements.txt
```

## 3. Para crear estructura de carpetas, en la terminal usar el comando django-admin startproject "nombre_sitio" .

```SYS
django-admin startproject nastu_site .
```

## 4. Editar la configuración básica en settings.py:

    - Hora de nuestra web: EUROPE/Madrid
    - Lenguaje: es-es
    - Allocated host: '127.0.0.1',
    - Añadir directorio static: STATIC_ROOT = BASE_DIR/ 'static'

## 5. Enlazar la base de datos en settings.py.

Prepara las actualizaciones de la base de datos, si no existe, la crea:

```SYS
python manage.py makemigrations
```

Realiza los cambios:

```SYS
python manage.py migrate
```

## 6. Arrancar el servidor para acceder a la web a nivel local con el comando:

```SYS
python manage.py runserver
```

## 7. Crear la aplicación "nombre de la aplicación" usamos el comando:

Crea la estructura de directorios y ficheros necesarios para gestionar nuestra aplicación

```SYS
python manage.py startapp task
```

## 8. Añadir nuestra nueva aplicación, en nuestro caso task, a la lista de app instaladas:

En settings.py:

```settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task.apps.TaskConfig',
]
```

## 9. Crear un modelo en models.py para nuestra base de datos:

En lugar de tablas, utilizaremos clases con "atributos" que serán nuestros campos y métodos que definirán su comportamiento.

En models.py:

```python
class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## 10. Ahora actualizamos la base de datos:

```SYS
python manage.py makemigrations
```

Realiza los cambios:

```SYS
python manage.py migrate
```

Es importante poner blog, de manera que sólo actualicemos la bbdd de nuestra aplicación, no de todo.

## 11. Modificar nastu_site admin en admin.py importando los modelos creados, además:

Incluimos también los modelos que serán visibles desde el administrador en admin.py:

```python
from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
```

Creamos un superusuario (User: nastupiste / password: root1234):

```SYS
python manage.py createsuperuser
```

## 12. Añadir a urls.py lo siguiente

En urls.py (global) hacemos un include de la aplicación "task":

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task.urls')),
]
```

En urls.py (de task) En urlpatterns agregamos los patrones que definamos para cada una de las direcciones y las vistas a las que corresponderían, además podemos asignarles un nombre.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]
```

## 13. A través de views.py podemos acceder a los datos del modelo, ¿Cómo?

13.1 Importamos de models.py la clase Task
Definiendo los los distintos métodos que usará nuestra aplicación task.

```python
from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    tasks= object.all()
    return render(request, 'task_list.html', {'tasks':tasks})
```

Los métodos llamarán a un template u a otro dependiendo de la funcionalidad que utilicemos.
Por ejemplo; el método task_list mostrará las tareas que existan en el modelo
Además, renderizará el template en la ruta 'tareas/task_list.html'.

## 14. En el directorio templates\ tendremos los diferentes ficheros html que enviaremos a la vista

Creamos el fichero task_list.html y añadimos el siguiente contendio:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tareas App</title>
  </head>
  <body>
    <h1>Lista de tareas</h1>
    <ul>
      {% for task in tasks %}
      <li>
        <pre><b>Nombre:</b>  {{ task.title }}     <b>Descripción:</b> {{ task.description }}      <b>Completada:</b>({{ task.completed|yesno:"Sí,No"}})</pre>
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

Cada fichero es un html propio de una página o funcionalidad pero todos comparten elementos comunes.
Los elementos comunes se extienden desde el fichero base.html a los demás con {% extends 'task/base.html' %}
Los contenidos propios de cada template se encierran entre {% block content %} y {% endblock %}
Para utilizar código python dentro de los html utilizamos la siguiente acotación: - {% for post in posts %} - Etiquetas html (aquí también puede existir más código) - {% endfor %}

## 15. Para añadir la funcionalidad formularios seguimos los siguientes pasos:

    - Añadimos el path de la url a urls.py (del blog)
    - En views.py definimos la nueva funcionalidad (puede que necesitemos varios métodos) y hacemos la llamada al template correspondiente
    - En templates\blog\post_edit.html definimos lo que se verá el usuario
