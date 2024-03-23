# Nombre del Proyecto

Devops_examen.

### Descripción

    Este código Python utiliza Flask, un framework de desarrollo web, para crear una API básica que realiza las siguientes acciones:

    Al acceder a la ruta principal ("/"), se devuelve un archivo HTML llamado "index.html".

    Al acceder a la ruta "/datos" mediante el método HTTP GET, se lee un archivo JSON llamado "datos.json" y se devuelve su contenido en formato JSON.

    Al acceder a la ruta "/datos" mediante el método HTTP POST, se espera que se envíen nuevos datos en formato JSON en el cuerpo de la solicitud. Estos nuevos datos se guardan en el archivo "datos.json". Si la operación es exitosa, se devuelve un mensaje indicando que los datos se han cargado correctamente. En caso de error, se devuelve un mensaje de error junto con el código de estado HTTP 500.

    Además, se utiliza Flasgger para generar documentación Swagger para la API, utilizando un archivo de plantilla llamado "swagger.yaml". Y finalmente, el servidor se ejecuta en modo de depuración si el archivo es ejecutado directamente.

## Instalación


A continuación, se detalla cómo instalar y configurar el proyecto:

1. Paso 1: Se descarga la imagen docker "python:3.9-slim".
2. Paso 2: se instala Flask Flasgger.
- pip install flasgger
- pip install Flask

## Despliegue

1. En este caso se utilizo la deteccion del cambio de codigo para hacer el despliegue.

## Pasos del despliegue.

1. Crear un "Dockerfile" el cual descarga la imagen del hub de docker y luego agrega el repositorio  a la imagen e instala las dependencias y ejecuta un cmd que expone el servidor en el puerto 5000 a todos los hosts.
2. Crear in docker-compose para desployar la imagen creada y exponerla. En este caso se utlizo el 5000 que expone el servidor.
3. Crear el Jenkinsfile para automatizar el proceso CI-CD
 -  1. Entra al directorio deployment y si tiene algun archivo o dir lo elimina.
 -  2. Hace un pull del repositorio de la rama master en este caso.
 -  3. Hacer una imagen con el repositorio actualizado ejecutando "docker build ../ -f Dockerfile --target python_base -t dev:1.0"
       el cual lleva nombre, tag y etiqueta (Se podria en casos posteriores hacer un push de repositorios de imagen)
 -  4. Luego se hace un "docker-composer up -p" para que inicie el contenedor con la imagen actualizada. 
 - 

Si tienes preguntas, problemas o sugerencias, puedes contactar a [lpiorelle@gmail.com](mailto:lpiorelle@gmail.com)
