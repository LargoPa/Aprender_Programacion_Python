
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self._nombre=nombre
        self._edad=edad
        self._sexo=sexo
        self._actividad=actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self._nombre} y tengo {self._edad} años.")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self._actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando de: {self._actividad}")

rodrigo = Estudiante("Rodrigo",21,"Masculino","Programacion")
pedro = Trabajador("Pedro",30,"Masculino","Carpintero")
rodrigo.hacer_actividad()
pedro.hacer_actividad()




