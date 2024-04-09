
from logica.Usuario import Usuario
from db import get_connection

db = get_connection()

class ControladoraPersistencia():
   
    def execute(sql, val):
        try:
            cur = db.cursor()
            cur.execute(sql, val)
            db.commit()
        except Exception as e:
            print(f"Error al ejecutar SQL: {e}")
    
    
    def guardarUsuario(usu):
        sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        val = (usu.nombre, usu.email)
        execute(sql, val)
        




