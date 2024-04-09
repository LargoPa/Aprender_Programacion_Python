
class Persona():
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    def __str__(self) -> str:
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}",{self.edad})'
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)


pedro = Persona("Pedro",21)
rodrigo = Persona("Rodrigo",30)

nueva_persona = pedro+rodrigo

print(nueva_persona.nombre)



