
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from typing import List
from domain.models.estudiante_model import EstudianteModel
from domain.repositories.estudiante_repository import EstudianteRepository


class EstudianteUseCase:
    def __init__(self, estudiante_repository: EstudianteRepository):
        self.estudiante_repository = estudiante_repository
    
    def crear_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        return self.estudiante_repository.create_estudiante(estudiante)
    
    def obtener_estudiante(self, id_estudiante: int) -> EstudianteModel:
        return self.estudiante_repository.get_estudiante_by_id(id_estudiante)

    def actualizar_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        return self.estudiante_repository.update_estudiante(estudiante)

    def obtener_estudiantes(self) -> List[EstudianteModel]:
        return self.estudiante_repository.get_estudiantes()

    def eliminar_estudiante(self, id_estudiante) -> None:
        return self.estudiante_repository.delet_estudiante(id_estudiante)


