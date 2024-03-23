# Nombre del Proyecto

Devops_examen.

### Descripción

    Este código Python utiliza Flask, un framework de desarrollo web, para crear una API básica que realiza las siguientes acciones:

    Al acceder a la ruta principal ("/"), se devuelve un archivo HTML llamado "index.html".

    Al acceder a la ruta "/datos" mediante el método HTTP GET, se lee un archivo JSON llamado "datos.json" y se devuelve su contenido en formato JSON.

    Al acceder a la ruta "/datos" mediante el método HTTP POST, se espera que se envíen nuevos datos en formato JSON en el cuerpo de la solicitud. Estos nuevos datos se guardan en el archivo "datos.json". Si la operación es exitosa, se devuelve un mensaje indicando que los datos se han cargado correctamente. En caso de error, se devuelve un mensaje de error junto con el código de estado HTTP 500.

    Además, se utiliza Flasgger para generar documentación Swagger para la API, utilizando un archivo de plantilla llamado "swagger.yaml". Y finalmente, el servidor se ejecuta en modo de depuración si el archivo es ejecutado directamente.

## Instalación y despliegue local


A continuación, se detalla cómo instalar y configurar el proyecto:

1. Crea el ambiente de trabajo en Docker.
    1.  Se descarga la imagen docker "python:3.9-slim".
    2. Actualizar e instalar app.
    - apt-get update 
    - apt-get install -y git
    - pip install flasgger
    - pip install Flask

2. Descargar el repositorio de codigo
    - https://github.com/LksDP/devops_examen.git

3. Levantar app y exponer puerto 
    flask run --host 0.0.0.0 --port 5000

## Despliegue en servidor

1. En este caso se utilizo el despliegue automatico mediante jenkins. Detecta cambio en el codigo y ejecuta "CD".
 En el jenkisfile se muestran los pasos para el despliegue del mismo.
 

Si tienes preguntas, problemas o sugerencias, puedes contactar a [lpiorelle@gmail.com](mailto:lpiorelle@gmail.com)
