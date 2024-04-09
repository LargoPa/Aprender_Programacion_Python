
from click import DateTime
from datetime import datetime

class EstudianteModel:
    def __init__(self, nombre_estudiante:str, documento_estudiante: str, fecha_de_registro_estudiante: DateTime = datetime.now(), id_estudiante: int = None):
        self.id_estudiante = id_estudiante
        self.nombre_estudiante = nombre_estudiante
        self.documento_estudiante = documento_estudiante
        self.fecha_de_registro_estudiante = fecha_de_registro_estudiante

    def to_dict(self):
        return{
            "id_estudiante": self.id_estudiante,
            "nombre_estudiante": self.nombre_estudiante,
            "documento_estudiante": self.documento_estudiante,
            "fecha_de_registro_estudiante": self.fecha_de_registro_estudiante,
        }


