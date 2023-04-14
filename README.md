# Squadmakers

Prueba técnica de Squadmakers

# ¿En que consiste?

La realización de esta prueba se basará en hacer un API Rest según las 
características que se especifiquen.


Para ello se necesitará crear un repositorio online en el servicio que se 
prefiera (Gitlab, Github...) donde se subirá el código resultante de la prueba 
junto con los archivos que sean necesarios.El lenguaje a utilizar como base 
será Python (última versión).


La prueba consiste en crear un API Rest en el framework Django utilizando 
los siguientes repositorios como base de datos:

- https://api.chucknorris.io/
- https://icanhazdadjoke.com/api

# Requisitos

Crear el API REST con los siguientes endpoints y su diseño en yaml para swagger:

ENDPOINT DE CHISTES

- GET: Se devolverá un chiste aleatorio si no se pasa ningún path param. Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”. Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io, si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api,  en caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente.


- POST: guardará en una base de datos el chiste (texto pasado por parámetro)

- UPDATE: actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”

- DELETE: elimina el chiste indicado en el parametro number.


ENDPOINT MATEMÁTICO

- GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La respuesta de este 
endpoint debe ser el mínimo común múltiplo de ellos'.
- GET: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1.

# ¿Qué repositorio utilizarías?

PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Serve

1. Razona tu respuesta

2. Crea la sentencia para crear la BBDD y el modelo de datos que requerirías

3. Lo mismo que el punto anterior (si lo hiciste con una SQL) pero para un repositorio noSQL.

# Razonamiento

Para el desarrollo de esta aplicación se tomaron en cuenta varios factores:

- Escalabilidad
- Requerimientos
- Facilidad de ejecución
- Mantenibilidad
- Robustez

Debido a ello se tomó la decisión de elegir como base de datos el gestor postgreSQL, debido a que a pesar de que actualmente se manejan pocos datos en él, éstos datos podrían ser fácilmente cambiantes y de mayor robustez en el tiempo, se podrán tener los siguientes beneficios tales como: 

- Agregar autenticación JWT para inicio de sesión
- Crear una lista con usuarios el cuál este podría agregar sus chistes preferidos
- Conectarse y almacenar nuevos chistes por medio de API
- Consultas de registros más grandes.
- Menos sujeto a fallas.

Esa es principalmente la razón por la cual se eligió usar un gestor de base de datos relacional, ante uno no relacional NoSQL.

Uno de los requisitos principales de esta prueba, es usar de la interfaz Swagger para realizar una documentación de cada endpoint, debido a eso se usó el componente ```drf-yasg``` para adaptar la interfaz swagger UI en el framework Django.

También se tomó la decisión de usar Django REST Framework para crear la aplicación, ya que éste framework resulta bastante robusto a la hora de crear y trabajar con Apis, apoyado con muchas librerias y una comunidad bastante grande a la cual se puede consultar en cualquier momento en caso de que se requiera hacerlo.

Se crearon dos aplicaciones en el proyecto de Django

- jokes: Aplicación para manipular los endpoints de chistes, modelo y serializador.
- maths: Aplicación para manipular los endpoints de las operaciones matemáticas.

# Tecnología utilizada

- Python 3.11.3 (Última versión actualmente)
- Django 3.0.8
- Django REST Framework 3.11.0
- OpenAPI 3.0 Swagger
- PostgreSQL

# Instalación y uso

1- Para instalar la aplicación se debe contar con Python en la version 3.11.3 y postgreSQL 15 el cual puede bajarse de la página oficial.

Python: https://www.python.org/downloads/
PostgreSQL: https://www.postgresql.org/

2- En Python lo más recomendable es usar un entorno virtual para trabajar con proyectos:

Para crear el entorno virtual:

```python -m venv squadmakers-env```

Para activar el entorno virtual

```squadmakers-env\Scripts\activate.bat```

3- Al activar el entorno virtual ejecuta el siguiente comando para instalar las dependencias del proyecto:

```pip install -r requirements.txt```

4- Previamente y antes de abrir el proyecto se debe crear la base de datos en postgreSQL

Acceder a la consola de postgreSQL:

```psql -U "usuario"```

Crear base de datos:

```CREATE DATABASE squadmakers;```

5- Por seguridad y para no mostrar datos sensibles a la hora de desplegar el código en GitHub, siguiendo parte de la metodología twelve-factor el archivo de configuración se establece con la variable de entorno de Django .env, el cuál está excluido del repositorio. Se debe crear el archivo .env en la raíz del proyecto y establecer los parámetros de acuerdo a tu configuración de conexión base de datos y tu SECRET_KEY, existe un archivo llamado .env.example de modo de ejemplo:

```
SECRET_KEY=tu-clave-secreta
DEBUG=True
DB_NAME=squadmakers
DB_USER=root
DB_PASSWORD=1234
DB_HOST=localhost
ALLOWED_HOSTS=127.0.0.1, localhost
```
    
6- Dentro del entorno virtual ejecutar las migraciones con el comando:

```python manage.py migrate```

7- Finalmente, ejecutar el proyecto con:

```python manage.py runserver```

# Endpoints

El proyecto cuenta en total con cuatro endpoints, dos de ellos son correspondientes al modelo de Chistes (Jokes), y los otros dos correspondientes a los endpoint matemáticos (Maths).

![image](https://user-images.githubusercontent.com/44822982/231859704-a51fb6fc-5f06-4375-8762-bc85a82dee18.png)

ENDPOINT ```/jokes/```:

- GET: Obtiene toda la lista de chistes almacenadas.
- POST: Agrega un nuevo chiste por query param "text".
- PUT: Modificar chiste almacenado, tiene dos query params: "joke", el texto con el nuevo chiste y "number", el cuál corresponde al ID del chiste a modificar.
- DELETE: Elimina chiste almacenado, tiene un query param "number", el cuál corresponde al ID del chiste a eliminar.

ENDPOINT ```/jokes/{type}/```:

- GET: Obtiene un chiste aleatorio por medio de consulta de api, tiene un path param el cuál debe ser "Chuck"o "Dad", en caso de no colocar ninguno lanza error.

ENDPOINT ```/math/lcm/```:

- GET: Obtiene el mínimo común múltiplo del arreglo de enteros introducido por query param.

ENDPOINT ```/math/plus/```:

- GET: Obtiene el cálculo del número introducido por query param + 1

Cada Endpoint lanzará un response con un índice de dato booleano llamado "success", el cuál servirá para saber si la consulta fue satisfactoria o no, para tomar decisiones dependiendo del caso en caso de conectarse con un frontend.

# Unit Test

Cada endpoint tiene su test unitario, para ejecutarlos todos se debe escribir el siguiente comando:

```python manage.py test```

Para ejecutar un test de manera individual se debe especificar la ruta donde se encuentra el test, el cual se encuentra en el archivo tests.py de cada aplicación, tal como este ejemplo:

```python manage.py test jokes.tests.JokesTestCase.test_random_joke```


# Sentencias para crear la base de datos requerida

Sentencia SQL:

```
CREATE DATABASE squadmakers;

  USE squadmakers;
  
  CREATE TABLE IF NOT EXISTS jokes_joke
  (
      id integer NOT NULL,
      joke text NOT NULL,
      CONSTRAINT jokes_joke_pkey PRIMARY KEY (id)
  )
```

Sentencia NoSQL (Cassandra):

```
CREATE KEYSPACE squadmakers WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
 
  USE squadmakers;

  CREATE TABLE jokes_joke (
    id int PRIMARY KEY,
    joke text
  );
```











