
import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\problemaCSV\\datos.csv")

#convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)
#motrar el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#remplazando los datos "De Pol" por "maestro"
df["apellido"].replace("De Pol","maestro",inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()
#eliminando las columnas con datos vacios
#df = df.dropna(axis=1)

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe(df) resultante limpio
df.to_csv("archivos_problemas_resueltos\\problemaCSV\\datos_limpios.csv")



