
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flask import Flask, jsonify, request
from domain.uses_cases.estudiante_use_case import EstudianteUseCase

from domain.models.estudiante_model import EstudianteModel
from infrastructure.adapters.estudiante_repository_adapter import (EstudianteRepositoryAdapter)
from datetime import datetime

app = Flask(__name__)

estudiante_repository = EstudianteRepositoryAdapter()
estudiante_use_case = EstudianteUseCase(estudiante_repository)


class ApiRest:
    @app.route("/api/agregar-estudiante", methods=["POST"])
    def agregar_estudiante_api():
        data: dict = request.get_json()
        
        estudiante_data = EstudianteModel(
            nombre_estudiante=data.get("nombre_estudiante"),
            documento_estudiante=data.get("documento_estudiante"),
        )
        respuesta = estudiante_use_case.crear_estudiante(estudiante_data)
        return{
            "respuesta": respuesta,
        }

    @app.route("/api/obtener-estudiante/<int:estudiante_id>", methods=["GET"])
    def obtener_estudiante_api(estudiante_id: int):
        estudiante = estudiante_use_case.obtener_estudiante(estudiante_id)
        return {"estudiante": estudiante}

    @app.route("/api/actualizar-estudiante", methods=["PUT"])
    def actualizar_estudiante_api():
        data: dict = request.get_json()
        
        estudiante_data = EstudianteModel(
            id_estudiante=data.get("id_estudiante"),
            nombre_estudiante=data.get("nombre_estudiante"),
            documento_estudiante=data.get("documento_estudiante"),
        )
        respuesta = estudiante_use_case.actualizar_estudiante(estudiante_data)
        return{
            "respuesta": respuesta,
        }

    @app.route("/api/obtener-estudiantes", methods=["GET"])
    def obtener_estudiantes_api():
        estudiantes = estudiante_use_case.obtener_estudiantes()
        return {"estudiantes": estudiantes}

    @app.route("/api/eliminar-estudiante/<int:estudiante_id>", methods=["DELETE"])
    def eliminar_estudiante_api(estudiante_id: int):
        return estudiante_use_case.obtener_estudiante(estudiante_id)


