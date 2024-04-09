

archivo_sin_leer = open("archivos\\txt\\texto.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer archivo linea por linea
lineas = archivo_sin_leer.readlines()

#leer una sola linea
#linea = archivo_sin_leer.readline()

#cerrar el archivo
archivo_sin_leer.close()

print(lineas)