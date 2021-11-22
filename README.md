# Microservio de tasks, para la asignatura de saas

## Pre-requisitos 📋
* Tener instalado Python (3.7+), pip (21.0.0+)
* Tener instalado un entorno de desarrollo (IDE).Se  Utilizó **Visual Studio Code**.
* Crear un entorno virtual  

Para crear el entorno virtual se debe abrir una consola o terminal y escribir lo siguiente:

**En Windows**
```
virtualenv <name_env> or
py -m venv <nombre de entorno, se recomiento **env** >

```  
**En Linux**
```
virtualenv env -p python3.7
```

## Instalación e inicialización 🔧
* Clonar el repositorio del proyecto en tu dispositivo local a través de la consola (te recomendamos que lo hagas dentro de la misma carpeta donde se creó el entorno virtual):
* Abrir el proyecto en el IDE y regresamos a la ventana de comandos o terminal.

Activar el entorno virtual desde la consola:

**En Windows**
```
.\<nombre_entorno_virtual>\Scripts\activate 

or

cd <nombre_entorno_virtual>
.\scripts\activate
```
**En Linux**
```
cd env/bin
source activate
```
* Nos dirigimos a la carpeta del proyecto desde la consola con el entorno virtual activo:
Instalamos los requerimientos en la raíz de la carpeta:

**En Windows**
```
pip install -r requeriments.txt
```
**En Linux**
```
pip3 install -r requeriments.txt
```

## Inicializamos el Back-end :

**En Windows**
# Comandos a ejecutar desde el CMD

```
set FLASK_ENV = development
set FLASK_APP = main.py 
flask db init
flask db migrate 
flask db upgrate
flask run
```

## Explicación: 
* set FLASK_ENV, es una variable de entorno que le indica a flask que esta en modo desarrollo
* set FLASK_APP, variable de entorno que le indica a flask el archivo principal para iniciar la ejecuión 
* flask db init, comando usado para inicializar la conexion con la base de datos, solo se utiliza la primera vez que clonamos el proyecto
* flask db migrate, detecta los modelos de datos a implementar, se utiliza cada que vez que modifiquemos el modelo de datos
* flask db upgrade, crea el modelo de datos detectado, dentro de la base de datos relacional usada, solo se usa cuando se hayan hecho modificaciones con el comando anterior

## Los dos primeros comandos son usados siempre que vamos a ejecutar el proyecto

## **flask run** pone en ejecución el proyecto 

## Para crear o actualizar una task, solo es necesario enviar el siguiente json
```
{
    "title": <value>,
    "description": <value>
}
```
