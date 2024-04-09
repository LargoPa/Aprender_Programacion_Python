
#importar un modulo y asignandole un nombre 
#import modulo_saludar as m_saludar

#importar por funcion
#from modulo_saludar import saludar,saludar_raro

#importar todas las funciones
from modulo_saludar import *

#importar funciones dentro de otra carpeta
from funciones_buenas.modulo_saludar2 import *


print(saludar("Rodrigo"))

print(saludar_raro("Pedro"))

