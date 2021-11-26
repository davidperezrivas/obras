def valida_campos(array_campos=[], campos_recibidos={}):
    """Funcion que valida que todos los campos esten en el Json"""
    try:
        salida = {"estado": 200, "respuesta": "Todo OK."}

        if array_campos == []:
            raise ValueError("Listado de campos no puede estar vacio")

        if campos_recibidos == {}:
            raise ValueError("No ha llegado ningun registro")

        for llave in array_campos:
            if llave not in campos_recibidos:
                raise ValueError(f"El campo {llave} es necesario")

            if campos_recibidos[llave] == "" or campos_recibidos[llave] is None:
                raise ValueError(f"El campo {llave} no puede estar vacio o nulo")

    except Exception as e:
        salida = {"estado": 500, "respuesta": str(e)}

    return salida
