
class Persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad= edad
    def imprimirNombreEdad(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante (Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado=grado
    def imprimirGrado(self):
        print(f"Estoy en el {self.grado} grado")

estudiante = Estudiante("Juan",12,"cuarto")

estudiante.imprimirNombreEdad()
estudiante.imprimirGrado()





