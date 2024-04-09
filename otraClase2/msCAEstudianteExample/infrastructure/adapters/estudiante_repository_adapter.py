
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.estudiante_model import EstudianteModel
from domain.repositories.estudiante_repository import EstudianteRepository
from infrastructure.adapters.data_sources.db_config import db
from infrastructure.adapters.data_sources.entities.estudiante_entity import (EstudianteEntity)


class EstudianteRepositoryAdapter(EstudianteRepository):
    def create_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        try:
            db_es = EstudianteEntity(
                id_estudiante = estudiante.id_estudiante,
                nombre_estudiante = estudiante.nombre_estudiante,
                documento_estudiante = estudiante.documento_estudiante,
                fecha_de_registro_estudiante = estudiante.fecha_de_registro_estudiante,
            )
            db.add(db_es)
            db.commit()
            
            return EstudianteModel(
                id_estudiante=db_es.id_estudiante,
                nombre_estudiante=db_es.nombre_estudiante,
                documento_estudiante=db_es.documento_estudiante,
                fecha_de_registro_estudiante=db_es.fecha_de_registro_estudiante,
            ).to_dict()
        except Exception as exeption:
            raise NameError(
                f"Ha ocurrido un error creando el usuario, revisa {exeption}"
            )
    
    def get_estudiante_by_id(self, estudiante_id: int) -> EstudianteModel:
        try:
            db_es = (
                db.query(EstudianteEntity)
                .filter(EstudianteEntity.id_estudiante == estudiante_id)
                .first()
            )
            if db_es is not None:
                return EstudianteModel(
                    id_estudiante=db_es.id_estudiante,
                    nombre_estudiante=db_es.nombre_estudiante,
                    documento_estudiante=db_es.documento_estudiante,
                    fecha_de_registro_estudiante=db_es.fecha_de_registro_estudiante,
                ).to_dict()
            return None
        except Exception as exeption:
            raise NameError(
                f"Ha ocurrido un error obteniendo el usuario, revisa {exeption}"
            )

    def update_estudiante(self, estudiante: EstudianteModel) -> EstudianteModel:
        try:
            db_es = (
                db.query(EstudianteEntity)
                .filter(EstudianteEntity.id_estudiante == estudiante.id_estudiante)
                .first()
            )
            db_es.nombre_estudiante = estudiante.nombre_estudiante
            db_es.documento_estudiante = estudiante.documento_estudiante
            db.commit()
            return EstudianteModel(
                id_estudiante=db_es.id_estudiante,
                nombre_estudiante=db_es.nombre_estudiante,
                documento_estudiante=db_es.documento_estudiante,
                fecha_de_registro_estudiante=db_es.fecha_de_registro_estudiante,
            ).to_dict()
        except Exception as exeption:
            raise NameError(
                f"Ha ocurrido un error modificando el usuario, revisa {exeption}"
            )

    def get_estudiantes(self) -> List[EstudianteModel]:
        try:
            db_es = db.query(EstudianteEntity).all()
            return[
                EstudianteModel(
                    id_estudiante=es.id_estudiante,
                    nombre_estudiante=es.nombre_estudiante,
                    documento_estudiante=es.documento_estudiante,
                    fecha_de_registro_estudiante=es.fecha_de_registro_estudiante,
                ).to_dict()
                for es in db_es
            ] 
        except Exception as exeption:
            raise NameError(
                f"Ha ocurrido un error obteniendo los usuarios, revisa {exeption}"
            )

    def delet_estudiante(self, id_estudiante) -> None:
        try:
            db_es = (
                db.query(EstudianteEntity)
                .filter(EstudianteEntity.id_estudiante == id_estudiante)
                .first()
            )
            db.delete(db_es)
            db.commit()
        except Exception as exeption:
            raise NameError(
                f"Ha ocurrido un error eliminando el usuario, revisa {exeption}"
            )






