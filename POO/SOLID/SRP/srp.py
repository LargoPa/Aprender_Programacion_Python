
class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            return "Has movido el auto exitosamente"
        else:
            return "No hay suficiente combustible"
            
    def obtener_posicion(self):
        return self.posicion


tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(10))
print(autito.obtener_posicion())
print(autito.mover(20))
print(autito.obtener_posicion())
print(autito.mover(60))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())



