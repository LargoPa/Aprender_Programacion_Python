
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from typing import List
from abc import ABC, abstractmethod
from domain.models.estudiante_model import EstudianteModel


class EstudianteRepository(ABC):
    @abstractmethod
    def create_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        pass
    
    @abstractmethod
    def get_estudiante_by_id(self, estudiante_id: int) -> EstudianteModel:
        pass

    @abstractmethod
    def update_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        pass
    
    @abstractmethod
    def get_estudiantes(self) -> List[EstudianteModel]:
        pass
    
    @abstractmethod
    def delet_estudiante(self, id_estudiante) -> None:
        pass











