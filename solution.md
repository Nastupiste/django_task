# Guía práctica para la creación de una Aplicación Web con Django:

## 1. Disponer de Python y entorno virtual

```SYS
mkvirtualenv django_task
```

## 2. Usar el fichero requirements.txt con el comando pip install -r requirements.txt

## 3. En la terminal usar el comando django-admin startproject "nombre_sitio" . 
    - Ésto crea la estructura de carpetas y ficheros necesaria para nuestra aplicación.

## 4. Editar la configuración básica en settings.py:
    - Hora de nuestra web
    - Lenguaje
    - Allocated host
    - Directorio static

## 5. Enlazar la base de datos en settings.py.
    - python manage.py makemigrations
    - python manage.py migrate

## 6. Arrancar el servidor para acceder a la web a nivel local con el comando: 
    - python manage.py runserver

## 7. Crear la aplicación "nombre de la aplicación" usamos el comando:
    - python manage.py startapp "nombre de la aplicación"
    - Agrega la estructura de directorios y ficheros necesarios para gestionar nuestra aplicación

## 8. Añadir nuestra nueva aplicación, en nuestro caso blog, a la lista de app instaladas:
    - En settings.py

## 9. Crear un modelo en models.py para nuestra base de datos:
    - En lugar de tablas, utilizaremos clases con "atributos" que serán nuestros campos y métodos que definirán su comportamiento. 

## 10. Ahora actualizamos la base de datos:
    - python manage.py makemigration blog (prepara la actualización)
    - python manage.py migrate blog (la ejecuta)
    - Es importante poner blog, de manera que sólo actualicemos la bbdd de nuestra aplicación, no de todo.

## 11. Modificar site admin en admin.py importando los modelos creados, además:
    - Incluimos también los modelos que serán visibles desde el administrador. 
    - Creamos un superusuario con python manage.py createsuperuser

## 12. Añadir a urls.py lo siguiente
    - urls.py (global) hacemos un include de la aplicación "blog"
    - urls.py (de blog) En urlpatterns agregamos los patrones que definamos para cada una de las direcciones y las vistas a las que corresponderían, además podemos asignarles un nombre. 

## 13. A través de views.py podemos acceder a los datos del modelo, ¿Cómo?
    - Definiendo los los distintos métodos que usará nuestra aplicación blog.
    - Los métodos llamarán a un template u a otro dependiendo de la funcionalidad que utilicemos.
    - Por ejemplo; el método post_list filtrará las publicaciones y las ordenará por fecha de publicación. 
    Además, renderizará el template en la ruta 'blog/post_list.html'.

## 14. En el directorio templates\blog\ tendremos los diferentes ficheros html que enviaremos a la vista
    - Cada fichero es un html propio de una página o funcionalidad pero todos comparten elementos comunes.
    - Los elementos comunes se extienden desde el fichero base.html a los demás con {% extends 'blog/base.html' %}
    - Los contenidos propios de cada template se encierran entre {% block content %} y {% endblock %}
    - Para utilizar código python dentro de los html utilizamos la siguiente acotación:  
        - {% for post in posts %}
        - Etiquetas html (aquí también puede existir más código)
        - {% endfor %}

## 15. El estilo CSS se añadirá en la dirección static\css\blog.css:
    - Definimos los estilos, en el caso de la práctica utilizando boostrap y CSS
    - Aplicamos los estilos a los diferentes templates a través del base con {% load static %}
    - Cómo al template base se le aplican los estilos, los demás también los tendrán por la extensión {% extends 'blog/base.html' %}

## 16. Para añadir la funcionalidad formularios seguimos los siguientes pasos: 
    - Añadimos el path de la url a urls.py (del blog)
    - En views.py definimos la nueva funcionalidad (puede que necesitemos varios métodos) y hacemos la llamada al template correspondiente
    - En templates\blog\post_edit.html definimos lo que se verá el usuario
