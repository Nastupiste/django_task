# django_task

- Descripción
Django es un framework web de alto nivel construido en Python que facilita el desarrollo rápido y limpio de aplicaciones web. Proporciona una estructura organizativa y muchas herramientas útiles para simplificar la creación de aplicaciones web complejas.

- Pre-requisitos
Tener instalado python, pip y disponer de un entorno virtual para realizar pruebas.

- Requisitos
clonar el repositorio e Instalar el fichero requirements.txt con el comando: pip install -r requirements.txt

- Para visualizar resultados
En local
Puede acceder a los resultados en local a través del repositorio con el comando python manage.py runserver en la dirección http://127.0.0.1:8000/

En web
Puede acceder al despliegue de la aplicación a través de https://nastupiste.pythonanywhere.com/

- Funcionamiento
Django sigue el patrón Modelo-Vista-Controlador (MVC), aunque en lugar de Controlador, Django utiliza el concepto de "Template". Aquí hay una descripción básica de cómo funciona:

Modelo: Representa la estructura de la base de datos y define cómo interactuar con ella. Los modelos son definidos en Python y se traducen en tablas de la base de datos.

Vista: Define cómo se presenta la información al usuario. Utiliza plantillas HTML y lógica de presentación para mostrar datos al usuario.

Controlador (Templates en Django): Maneja las solicitudes del usuario y las rutas a las vistas apropiadas. Django utiliza URLs y funciones de vista para procesar las solicitudes del usuario.

La lógica de la aplicación se implementa en las vistas y modelos, y las plantillas se utilizan para representar la interfaz de usuario. Django ofrece un sistema de administración incorporado para facilitar la gestión de datos y una amplia gama de bibliotecas y complementos para ampliar su funcionalidad.

- Contribución
Si deseas contribuir o informar sobre problemas, no dudes en crear una solicitud de extracción o un problema en este repositorio.

- Autor
Manuel Jesús de la Rosa Cosano
