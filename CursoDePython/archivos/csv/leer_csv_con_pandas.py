
import pandas as pd

#funcion read_csv para leer archivos csv
df = pd.read_csv("archivos\\csv\\datos.csv")
df2 = pd.read_csv("archivos\\csv\\datos.csv")

#obteniendo los valores de la columna nombre
nombres = df["nombre"]

#cadena = "0123456789"
#elijo de donde hasta donde mostrar
#print(cadena[1:7])

#ordenando por edad de forma ascendete
df_ordenado_edad_ascendente = df.sort_values("edad")

#ordenando por edad de forma descendete
df_ordenado_edad_descendete = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes (df)
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 fila con head()
primeras_filas = df.head(2)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape desepaquetandolo
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico del df con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)


