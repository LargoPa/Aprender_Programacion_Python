
import re

texto = '''Hola pai, 1251 como estas perro 1. to bien pai.
Esta es la segunda linea(2)_ de texto fuaaaa.
Esta es la tercera(3)_ y ultima perro'''

#haciendo una busqueda simple
#resultado = re.findall("Esta",texto)

#con flags=re.IGNORECASE se ignoran las May y min
#resultado = re.findall("Esta",texto,flags=re.IGNORECASE)

#\d ==> busca digitos numericos del 0 al 9
#resultado = re.findall(r"\d",texto)

#\D ==> busca TODO MENOS digitos numericos del 0 al 9
#resultado = re.findall(r"\D",texto)

#\w ==> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto)

#\W ==> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W",texto)

#\s ==> busca espacios en blanco => espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto)

#\S ==> busca TODO MENOS espacios en blanco
#resultado = re.findall(r"\S",texto)

#. ==> busca TODO MENOS saltos de linea
#resultado = re.findall(r".",texto)

#\n ==> busca saltos de linea
#resultado = re.findall(r"\n",texto)

#\. ==> cancelar caracteres especiales
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(f"\d\.\s",texto)

#^ ==> busca el comienzo de una linea (buscando Hola)
#resultado = re.findall(f'^Hola',texto)
#flags=re.MULTILINE activa la multilinea
#resultado = re.findall(f'^Esta',texto,flags=re.MULTILINE)

#$ ==> buscar el final de una linea
#resultado = re.findall(r"perro$",texto)

#{n} ==> busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r"\d{4}\s",texto)

#{n,m} ==> al menos n y como maximo m
#resultado = re.findall(r"\d{2,4}",texto)

#| ==> busca una cosa o la otra
#resultado = re.findall(r"\d{2,4}|Hola",texto)

#print(resultado)

