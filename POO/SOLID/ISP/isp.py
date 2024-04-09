
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comer(ABC):
    @abstractmethod
    def comer(self):
        pass

class Dormir(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador,Comer,Dormir):
    def comer(self):
        print("El humano esta comiendo")
    def trabajar(self):
        print("El humano esta trabajando")
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")

robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.comer()
humano.dormir()


