
from Usuario import Usuario
from database.ControladoraPersistencia import ControladoraPersistencia

class Controladora():
    
    controlPersis = ControladoraPersistencia()
    
    def crearUsuarios(self, nombre, email):
        usu = Usuario(nombre, email)
        
        controlPersis.guardarUsuario(usu)












