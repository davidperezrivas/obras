import jwt
import datetime

key = "secret"


def crear_token(usuario):
    # token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mjk2MTU2NDQsImlkIjoyfQ.X3jWFgxH2Nstu_oZ5mUhqa9fXLycxJt7uKxPlKJG0iE
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
            "id": usuario["id"],
        }
        jwt_payload = jwt.encode(payload, key, algorithm="HS256")

        salida = {"estado": 200, "respuesta": jwt_payload}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida


def valida_token(token):
    try:
        payload = jwt.decode(token, key, algorithms="HS256")
        salida = {"estado": 200, "respuesta": payload}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
