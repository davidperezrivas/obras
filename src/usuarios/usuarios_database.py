from src.shared.database import muestra_error_segun_codigo
from src.usuarios.usuarios_model import Usuario
from sqlalchemy import exc
from server import db

no_encontrado = "Usuario no encontrado"


def listar_usuarios():
    try:
        usuarios = Usuario.query.all()

        listado_usuarios = []
        for usuario in usuarios:
            obj = {}
            obj["id"] = usuario.id
            obj["nombre"] = usuario.nombre
            obj["apellido"] = usuario.apellido
            obj["correo"] = usuario.correo
            obj["rol"] = {
                "id": usuario.rol.id,
                "nombre": usuario.rol.nombre,
            }
            obj["estado"] = usuario.estado
            listado_usuarios.append(obj)

        salida = {"estado": 200, "respuesta": listado_usuarios}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def almacenar_usuarios(usuario):
    try:
        user = Usuario()
        user.nombre = usuario["nombre"]
        user.apellido = usuario["apellido"]
        user.correo = usuario["correo"]
        user.password = usuario["password"]
        user.rol_id = usuario["rol_id"]

        db.session.add(user)
        db.session.commit()

        salida = {"estado": 200}
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        db.session.rollback()
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def editar_usuario(usuario):
    try:
        user = Usuario.query.get(usuario["id"])
        if user is None:
            raise ValueError(no_encontrado)

        user.nombre = usuario["nombre"]
        user.apellido = usuario["apellido"]
        user.correo = usuario["correo"]
        user.rol_id = usuario["rol_id"]

        db.session.commit()

        salida = {"estado": 200}
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        db.session.rollback()
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def borrar_usuario(usuario):
    try:
        user = Usuario.query.get(usuario["id"])
        if user is None:
            raise ValueError(no_encontrado)

        estado = False if user.estado else True
        user.estado = estado
        db.session.commit()
        salida = {"estado": 200}

    except exc.SQLAlchemyError as e:
        db.session.rollback()

        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        db.session.rollback()
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def obtener_usuario(usuario):
    try:
        user = Usuario.query.get(usuario["id"])

        if user is None:
            raise ValueError(no_encontrado)

        usuario = {}
        usuario["nombre"] = user.nombre
        usuario["apellido"] = user.apellido
        usuario["correo"] = user.correo
        usuario["password"] = user.password
        usuario["rol"] = {"id": user.rol.id, "nombre": user.rol.nombre}
        usuario["estado"] = user.estado

        salida = {"estado": 200, "respuesta": usuario}

    except exc.SQLAlchemyError as e:
        db.session.rollback()
        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}
        db.session.rollback()

    print("DB: ", usuario)
    return salida


def cambio_password(usuario):
    try:
        user = Usuario.query.get(usuario["id"])
        if user is None:
            raise ValueError(no_encontrado)

        user.password = usuario["password"]
        db.session.commit()
        salida = {"estado": 200}
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        db.session.rollback()
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def login(usuario):
    try:
        user = Usuario.query.filter_by(
            correo=usuario["correo"], password=usuario["password"], estado=True
        ).first()
        if user is None:
            raise ValueError(no_encontrado)

        usuario_logeado = {}
        usuario_logeado["id"] = user.id

        salida = {"estado": 200, "respuesta": usuario_logeado}

    except exc.SQLAlchemyError as e:
        db.session.rollback()
        salida = muestra_error_segun_codigo(str(e))
    except Exception as e:
        db.session.rollback()
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
