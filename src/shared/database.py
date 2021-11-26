def muestra_error_segun_codigo(code_error=0):
    try:

        errores = [
            {"codigo": 1062, "respuesta": "Ya se encuentra registro almacenado."},
            {
                "codigo": 1048,
                "respuesta": "Favor enviar todos los campos obligatorios.",
            },
            {
                "codigo": 1452,
                "respuesta": "No se encuentra la relación que intenta agregar.",
            },
            {
                "codigo": 1406,
                "respuesta": "Cantidad de caracteres maximos superados para el campo ingresado.",
            },
        ]

        list_error = filter(lambda error: (error["codigo"] == code_error), errores)

        list_error = list(list_error)

        if list_error == []:
            raise ValueError("Ha ocurrido un error no identificado.")

        salida = {"estado": 200, "respuesta": list(list_error)[0]["respuesta"]}

    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
