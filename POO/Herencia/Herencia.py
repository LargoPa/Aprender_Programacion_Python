
class Persona():
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad  
    def hablar(self):
        return("Estoy hablando un poco")

class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")

class Empleado(Persona):    
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    def hablar(self):
        return("No")

class Estudiante(Persona):    
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
    def hablar(self):
        return("Si")

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona().__init__(self,nombre, edad, nacionalidad)
        Artista().__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

roberto = Empleado("Roberto",43,"Argentino","Programador",10000)
roberto.hablar()


