from src.shared.jwt import crear_token, valida_token
from src.shared.hash import crear_hash
from src.usuarios.usuarios_database import (
    almacenar_usuarios,
    borrar_usuario,
    cambio_password,
    editar_usuario,
    listar_usuarios,
    login,
    obtener_usuario,
)


def listado_usuarios():
    try:
        listado_usuarios = listar_usuarios()
        if listado_usuarios["estado"] != 200:
            raise ValueError(listado_usuarios["respuesta"])

        salida = {"estado": 200, "respuesta": listado_usuarios["respuesta"]}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def crear_usuarios(usuario):
    try:
        usuario["password"] = crear_hash(usuario["password"])
        user = almacenar_usuarios(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])
        salida = {"estado": 200}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def actualizar_usuario(usuario):
    try:
        user = editar_usuario(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])
        salida = {"estado": 200}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    print("Controller: ", salida)
    return salida


def desactivar_usuario(usuario):
    try:
        user = borrar_usuario(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])
        salida = {"estado": 200}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def trae_usuario(usuario):
    try:
        user = obtener_usuario(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])
        salida = {"estado": 200, "respuesta": user["respuesta"]}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def cambiar_clave(usuario):
    try:
        usuario["password"] = crear_hash(usuario["password"])
        user = cambio_password(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])
        salida = {"estado": 200}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def inicio_sesion(usuario):
    try:
        usuario["password"] = crear_hash(usuario["password"])

        user = login(usuario)
        if user["estado"] != 200:
            raise ValueError(user["respuesta"])

        token = crear_token(user["respuesta"])
        if token["estado"] != 200:
            raise ValueError(token["respuesta"])

        salida = {"estado": 200, "respuesta": token["respuesta"]}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
