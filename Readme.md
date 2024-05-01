# TFG Grado en Ingeniería Informática
Este es el repositorio principal del proyecto final de ingeniería informática

Autor: Jhostin D. Ortiz Moreno

## Creación del proyecto en GCP (Google Cloud Platform)

1. Es necesario crearse una cuenta en google (es gratuito).
2. Acceder al siguiente enlace e iniciar sesión: https://console.cloud.google.com/.
3. Crear un nuevo proyecto de Google Cloud.
4. Una vez creado el proyecto nos dirigimos a crear una cuenta de servicio en IAM con permisos de lectura en BigQuery.

## Settings.ini
1. Crear en la raíz del proyecto el fichero "settings.ini", el cual contendrá las variables de entorno del programa.
2. Guardar las variables necesarias (en nuestro caso: DB_PASS, DB_USER, DB_NAME, DB_HOST, DB_PORT).
3. **IMPORTANTE:** por temas de seguridad, NO subir este fichero al repositorio.

El formato del fichero settings.ini es:
[settings]
DB_PASS=mypassword123
DB_USER=postgres
DB_NAME=postgres
DB_HOST=127.0.0.1
DB_PORT=5432

## Clave de cuenta de servicio de GCP (variable de entorno)
Antes de ejecutar el entorno vía máquina local, es necesario añadir al entorno virtual de python desde el que trabajamos la variable GOOGLE_APPLICATION_CREDENTIALS="/full/path/to/your/client_secret.json", siendo el valor un string que contiene el path a la clave de la cuenta de servicio del proyecto de GCP que hemos descargado anteriormente. Es importante **NO** subir al repositorio esta clave .json por seguridad si el repositorio será público.

## Crear el entorno virtual (venv) de python en VS Code:
1. En el menú de opciones, accedemos a "View/Command Palette".
2. En el buscador, seleccionamos la opción "Python: Create Enviroment" y elegimos nuestro intérprete de python (es necesario tener una versión de python instalada).
3. Permitimos la ejecución de scripts para "Activate.ps1" mediante el siguiente comando en la terminal de PS: <br>
 **Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser**
4. ejecutamos "Activate.ps1" mediante el comando: <br>
**& "RESTO_DEL_PATH_COMPLETO_DEL_PROYECTO/TBD_ETL/.venv/Scripts/Activate.ps1"**

## Gestión de dependencias instaladas (Requirements.txt):
- Para ver dependencias usamos el comando: <br>
**py -m pip freeze**
- Para instalar una nueva dependencia usamos: <br>
**py -m pip install paquete==version**, donde paquete es el nombre de la librería y version es la que deseamos (1.0.7, por ejemplo). Indicar la versión es opcional.
- Para actualizar el archivo requirements.txt es necesario usar el siguiente comando: <br>
**py -m pip freeze > requirements.txt**
- Para instalar todas las dependencias de requirements.txt usamos el siguiente comando: <br>
**py -m pip install -r requirements.txt**

## PostgreSQL
Se necesita tener configurada la base de datos postgreSQL 16 con pgAdmin 4, instalarlo e inicializar desde pgAdmin 4.
Para este ejemplo se ha creado una base de datos llamada "tbd_etl", con username "postgres".

Se ha creado una tabla dentro del schema "public" las tablas "zip_ts_processed" y "zip_ts_raw", con 3 y 6 columnas, respectivamente:
1. index: id autonumérico (generado automáticamente) que actúa como PK.
2. hpi_value_prediction_GRU: predicción de red neuronal de hpi_value usando GRU.
3. hpi_real_prediction_GRU: predicción de red neuronal de hpi_real usando GRU.

1. index: id autonumérico (generado automáticamente) que actúa como PK.
2. zip: código postal.
3. msa: código de área metropolitana estadística.
4. hpi_value: índice de precio nominal de inmueble.
5. hpi_real:  índice de precio real de inmueble ajustando inflación.
