
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.adapters.data_sources.db_config import Base, engine

class EstudianteEntity(Base):
    __tablename__ = "estudiantes"
    
    id_estudiante = Column(Integer, primary_key=True, index=True)
    nombre_estudiante = Column(String(255))  # Se especifica la longitud máxima (255 en este caso)
    documento_estudiante = Column(String(20))  # Aquí también se especifica una longitud máxima
    fecha_de_registro_estudiante = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)



