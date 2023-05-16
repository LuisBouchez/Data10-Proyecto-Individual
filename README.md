
# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER

Rol a desarollar : 
- Data engineer

- Descripcion de la problematica:
La problemática es que como Data Scientist en una start-up de servicios de agregación de plataformas de streaming, te encuentras con la tarea de crear un modelo de ML para un sistema de recomendación que aún no ha sido implementado. Sin embargo, al revisar los datos, te das cuenta de que la calidad y madurez de los mismos es nula, lo que hace que tu trabajo sea imposible. Necesitas empezar desde cero, trabajando como Data Engineer para construir un MVP en una semana.


## Proceso de "ETL" (Extract, transform, load)
- ETL significa "Extracción, Transformación y Carga" y es un proceso utilizado en tecnología de la información para integrar datos de diferentes fuentes y prepararlos para su uso en aplicaciones de negocio.

1.- Importación de la librería pandas para el manejo de dataframes.


2.- Ingesta de datos (Archivo .csv provistos por el cliente)

3.- Análisis exploratorio de los distintos datasets para conocer sus características principale.

- Transformaciones 
1.- Desanidar los campos belongs_to_collection, production_companies entre otros para poder hacer las consultas con la API.

2.- Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

3.- Los valores nulos del campo release date deben eliminarse.

4.- De haber fechas, deberán tener el formato AAAA-mm-dd

5.- Crear una columna llamada "return" con los campos revenue y budget, dividiendo estas dos últimas y cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

6.- Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.


## Desarrollo de las funciones

- Se desarollaron las siguientes funciones las cuales fueron probadas localmente mediaten el framework FastAPI.

-FastAPI es un framework de programación web para construir APIs (interfaces de programación de aplicaciones) de manera rápida y eficiente en Python.

1.- La función "peliculas_mes" se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes.

2.- La función "peliculas_dia" se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia.

3.- La función "franquicia" se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio. 

4.- La función "Peliculas_pais" ingresas el pais, retornando la cantidad de peliculas producidas en el mismo.

5.- La función "productoras" ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron.

6.- La función "retorno" ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo.



## Análisis exploratorio de los datos

- EDA significa "Exploratory Data Analysis", que en español se traduce como "Análisis Exploratorio de Datos". Es una técnica utilizada en ciencia de datos para analizar y resumir las características principales de un conjunto de datos, con el fin de obtener una comprensión profunda de los mismos antes de aplicar modelos de aprendizaje automático u otras técnicas estadísticas.
## Sistema de recomendación

- Para el sistema de recomendación se escogio el modelo de "KNN" por su simplicidad y es es relativamente sencillo de entender y de implementar.
El enfoque de "KNN" se basa en encontrar elementos similares en función de la distancia entre ellos. En el caso de la recomendación de películas, esto significa que buscará películas similares a la que le gustó a un usuario en función de características compartidas como la popularidad.

Otra delas razones por la que se escogio este modelo es por los pocos recursos computacionales con los que se contaban.
## Deployment

* Para el Deployment se creo la API con FastAPI y uviconr y este fue desplegado mediante Render.
El URRL de la API desplegada es el siguiente: https://proyecto-individual-data10.onrender.com/docs

Video: https://youtu.be/AHsw5v7woQc


## Instalacion
Para el siguiente proyecto se usaron las siguietes tecnologias y librerias:

-Python

-Pandas

-Numpy

-Searborn

-Matplotlib

-Sklearn

-FastAPI

-Uvicorn

-Visual studio code

    
