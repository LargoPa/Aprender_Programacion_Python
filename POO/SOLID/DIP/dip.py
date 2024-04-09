
# class Diccionario():
#     def verificar_palabra(self,palabra):
#         #logica para verificar palabras
#         pass

# class CorrectorOrtografico():
#     def __init__(self) -> None:
#         self.diccionario = Diccionario()
#     def corregir_texto(self,texto):
#         #usamos el diccionario para corregir el texto
#         pass
    
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnLine(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras desde el servicio web
        pass
    
class CorrectorOrtografico():
    def __init__(self,verificador) -> None:
        self.verificador = verificador
    def corregir_texto(self,texto):
        #usamor el verificador para corregir texto
        pass


corrector = CorrectorOrtografico(Diccionario())

