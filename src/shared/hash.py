import hashlib


def crear_hash(hash):
    try:

        if hash == "":
            raise ValueError("Valor no puede estar vacio.")

        h = hashlib.sha3_512(str(hash).encode("utf-8"))
        salida = {"estado": 200, "respuesta": h.hexdigest()}
    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
