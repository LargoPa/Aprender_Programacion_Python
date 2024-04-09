
class Persona():
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,new_nombre):
        self.__nombre=new_nombre

rodrigo = Persona("Rodrigo",12)

rodrigo.set_nombre("Pedro")

print(rodrigo.get_nombre())

    









