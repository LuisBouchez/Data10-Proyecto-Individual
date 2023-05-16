from fastapi import FastAPI
import pandas as pd
import locale
from datetime import datetime
import numpy as np
import joblib





app = FastAPI()

df = pd.read_csv('C:/Users/PC/Desktop/API/Data/movies.csv')
knn_model = joblib.load('modelo_pelicula.pkl')

# 1.-Peliculas estrenadas ese mes
@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    locale.setlocale(locale.LC_ALL, 'es.utf8')
    df['mes'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d').dt.strftime('%B').str.lower()
    respuesta = len(df[df['mes'] == mes.lower()])
    df.drop('mes', axis=1, inplace=True)
    return {'Mes': mes, 'Cantidad': respuesta}

#2.- Peliculas estrenadas ese dia 
@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    dias = {'lunes': 'Monday', 'martes': 'Tuesday', 'miercoles': 'Wednesday', 'jueves': 'Thursday', 'viernes': 'Friday', 'sabado': 'Saturday', 'domingo': 'Sunday'}
    # Convertir la columna 'release_date' en formato fecha
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Filtrar por el día de la semana deseado
    peliculas = df[df['release_date'].dt.day_name().str.lower() == dias[dia].lower()]

    # Obtener la cantidad de películas estrenadas ese día
    cantidad = peliculas.shape[0]

    # Retornar el resultado en un diccionario
    respuesta = {'dia': dia, 'cantidad': cantidad}
    return respuesta





#3.-Franquicia que retorna la ganancia total y promedio 
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    filtered_df = df[df['belongs_to_collection'] == franquicia]
    cantidad = len(filtered_df)
    ganancia_total = filtered_df['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad if cantidad > 0 else 0
    resultados = {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}
    return resultados

#4.-Paies y retorna la cantidad de peliculas producidas en el
@app.get('/peliculas_pais/{pais}') 
def peliculas_pais(pais:str):
    df['production_countries'] = df['production_countries'].fillna('')
    cantidad_peliculas = len(df[df['production_countries'].str.contains(pais)])
    return {'pais': pais, 'cantidad': cantidad_peliculas}

#5.-Productora y retornoa la ganancia total y cantidad de peliculas
@app.get('/productoras/{productora}') 
def productoras(productora:str):
    df['production_companies'] = df['production_companies'].fillna('')
    df_productora = df[df['production_companies'].str.contains(productora)]
    cantidad = len(df_productora)
    ganancia_total = df_productora['revenue'].sum()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

#6.-Pelicula y retorna la inversion, la ganancia, el retorno y año de lanzamiento 
@app.get('/retorno/{pelicula}') 
def retorno(pelicula:str):
    # Filtrar el DataFrame por la película deseada
    pelicula_df = df[df['title'] == pelicula]
    
    # Obtener los valores de inversión, ganancias, retorno y año de lanzamiento
    inversion = pelicula_df['budget'].iloc[0].tolist() if not pelicula_df['budget'].isnull().values.any() else 'No disponible'
    ganancia = pelicula_df['revenue'].iloc[0].tolist() if not pelicula_df['revenue'].isnull().values.any() else 'No disponible'
    retorno = pelicula_df['return'].iloc[0].tolist() if not pelicula_df['return'].isnull().values.any() else 'No disponible'
    anio = pelicula_df['release_year'].iloc[0].tolist() if not pelicula_df['release_year'].isnull().values.any() else 'No disponible'
    
    # Retornar un diccionario con los valores obtenidos
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}



#Funcion de recomendacion 
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    pelicula = df[df["title"] == titulo].index.values[0]
    distancias, indices = knn_model.kneighbors(df.loc[pelicula][["popularity", "revenue", "runtime", "vote_average", "release_year"]].values.reshape(1, -1))
    peliculas_recomendadas = df.iloc[indices[0]][["title"]].values.tolist()[1:]
    return {"lista recomendada": peliculas_recomendadas}

