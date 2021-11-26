from hash import crear_hash
from database import muestra_error_segun_codigo
from funciones import valida_campos


def test_hash_correcto():
    string_hash = crear_hash("testo")
    assert string_hash["estado"] == 200


def test_hash_caracteres_especiales():
    string_hash = crear_hash('"#$!%&/ñ|@·~½¬{[]}\\')
    assert string_hash["estado"] == 200


def test_hash_parametro_vacio():
    string_hash = crear_hash("")
    assert string_hash["estado"] == 500
    assert string_hash["respuesta"] == "Valor no puede estar vacio."


def test_database_error_no_encontrado():
    error = muestra_error_segun_codigo(100)

    assert error["estado"] == 500
    assert error["respuesta"] == "Ha ocurrido un error no identificado."


def test_database_con_error_definido():
    error = muestra_error_segun_codigo(1062)

    assert error["estado"] == 200
    assert error["respuesta"] == "Ya se encuentra registro almacenado."


def test_database_sin_parametro():
    error = muestra_error_segun_codigo()
    assert error["estado"] == 500
    assert error["respuesta"] == "Ha ocurrido un error no identificado."


def test_funciones_valida_campos_correcto():
    campos_necesarios = ["nombre", "rut", "edad"]
    campos_ingresados = {"nombre": "nombre", "rut": "rut", "edad": "edad"}

    error = valida_campos(campos_necesarios, campos_ingresados)
    assert error["estado"] == 200
    assert error["respuesta"] == "Todo OK."


def test_funciones_valida_campos_falta_campo():
    campos_necesarios = ["nombre", "rut", "edad"]
    campos_ingresados = {"nombre": "nombre", "rut": "rut"}

    error = valida_campos(campos_necesarios, campos_ingresados)
    assert error["estado"] == 500
    assert error["respuesta"] == "El campo edad es necesario"


def test_funciones_valida_campos_campo_vacio():
    campos_necesarios = ["nombre", "rut", "edad"]
    campos_ingresados = {"nombre": "nombre", "rut": "", "edad": "edad"}

    error = valida_campos(campos_necesarios, campos_ingresados)
    assert error["estado"] == 500
    assert error["respuesta"] == "El campo rut no puede estar vacio o nulo"


def test_funciones_valida_campos_sin_campos_necesarios():
    campos_necesarios = []
    campos_ingresados = {"nombre": "nombre", "rut": "", "edad": "edad"}

    error = valida_campos(campos_necesarios, campos_ingresados)
    assert error["estado"] == 500
    assert error["respuesta"] == "Listado de campos no puede estar vacio"


def test_funciones_valida_campos_sin_campos_ingresados():
    campos_necesarios = ["nombre", "rut", "edad"]
    campos_ingresados = {}

    error = valida_campos(campos_necesarios, campos_ingresados)
    assert error["estado"] == 500
    assert error["respuesta"] == "No ha llegado ningun registro"
