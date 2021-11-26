from src.shared.funciones import valida_campos
from src.roles.roles_model import Rol
from src.usuarios.usuarios_controller import (
    actualizar_usuario,
    cambiar_clave,
    crear_usuarios,
    desactivar_usuario,
    inicio_sesion,
    listado_usuarios,
    trae_usuario,
)
from flask import request
from flask_restplus import Resource, Namespace
from dotenv import load_dotenv
import os


if os.getenv("MODO") == "PROD":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev", verbose=True)

usuarios = Namespace(
    "Funciones para los usuarios",
    description="Mantenedor para la creacion de usuarios, login, JWT y mas",
)


@usuarios.route("/listar_usuarios", methods=["GET"])
class listar_usuarios(Resource):
    def get(self):
        """
        Funcion Get para listar los usuarios
        Parameters: N/A
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            lista = listado_usuarios()
            if lista["estado"] != 200:
                raise ValueError(lista["respuesta"])

            salida = {"estado": 200, "respuesta": lista["respuesta"]}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida


@usuarios.route("/crear_usuario", methods=["POST"])
class crear_usuario(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["nombre", "apellido", "correo", "password", "rol_id"]
            campos_validos = valida_campos(array_campos, usuario)
            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario_creado = crear_usuarios(usuario)
            if usuario_creado["estado"] == 500:
                raise ValueError(usuario_creado["respuesta"])

            salida = {"estado": 200, "respuesta": "Usuario creado correctamente"}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida


@usuarios.route("/actualizar_usuario", methods=["POST"])
class actualiza_usuario(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["nombre", "apellido", "correo", "rol_id", "id"]
            campos_validos = valida_campos(array_campos, usuario)
            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario_creado = actualizar_usuario(usuario)
            if usuario_creado["estado"] == 500:
                raise ValueError(usuario_creado["respuesta"])

            salida = {"estado": 200, "respuesta": "Usuario actualizado correctamente"}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida


@usuarios.route("/eliminar_usuario", methods=["POST"])
class eliminar_usuario(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["id"]
            campos_validos = valida_campos(array_campos, usuario)
            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario_eliminado = desactivar_usuario(usuario)

            if usuario_eliminado["estado"] == 500:
                raise ValueError(usuario_eliminado["respuesta"])

            salida = {"estado": 200, "respuesta": "Usuario eliminado del sistema"}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida


@usuarios.route("/obtener_usuario", methods=["POST"])
class obtener_usuario(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["id"]
            campos_validos = valida_campos(array_campos, usuario)

            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario = trae_usuario(usuario)

            if usuario["estado"] == 500:
                raise ValueError(usuario["respuesta"])

            salida = {"estado": 200, "respuesta": usuario["respuesta"]}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        print("Routes: %s" % salida)
        return salida


@usuarios.route("/cambio_pass", methods=["POST"])
class cambio_pass(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["id", "password"]
            campos_validos = valida_campos(array_campos, usuario)

            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario = cambiar_clave(usuario)

            if usuario["estado"] == 500:
                raise ValueError(usuario["respuesta"])

            salida = {"estado": 200, "respuesta": "Password actualizada"}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida


@usuarios.route("/login", methods=["POST"])
class login(Resource):
    def post(self):
        """
        Funcion para almacenar usuario enviado
        Parameters: JSON con los parametros nombre, apellido, correo, password, rol_id
        Returns:
        JSON: con un estado en 200 / 500 y mensaje
        """
        try:
            usuario = request.get_json()
            array_campos = ["correo", "password"]
            campos_validos = valida_campos(array_campos, usuario)

            if campos_validos["estado"] == 500:
                raise ValueError(campos_validos["respuesta"])

            usuario = inicio_sesion(usuario)

            if usuario["estado"] == 500:
                raise ValueError(usuario["respuesta"])

            salida = {"estado": 200, "respuesta": usuario["respuesta"]}

        except Exception as e:
            salida = {"estado": 500, "respuesta": str(e)}

        return salida
