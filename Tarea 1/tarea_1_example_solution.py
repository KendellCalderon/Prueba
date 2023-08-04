import re


def separa_letras(Cadena):
    codigo = ""
    cadenaMayus = ""
    cadenaMinus = ""
    if isinstance(Cadena, str):
        if Cadena != "":
            if re.match("[a-zA-Z]", Cadena):
                for caracter in Cadena:
                    if caracter.isupper():
                        cadenaMayus += caracter
                    else:
                        cadenaMinus += caracter
                codigo = 0  # exito
            else:
                codigo = -200  # Caracteres que no pertenecen al abecedario
                cadenaMayus = None
                cadenaMinus = None
        else:
            codigo = -300  # Es string vacio
            cadenaMayus = None
            cadenaMinus = None
    else:
        codigo = -100  # No es string
        cadenaMayus = None
        cadenaMinus = None

    return [codigo, cadenaMayus, cadenaMinus]


def potencia_manual(base, potencia):  # solo numeros enteros positivos
    if isinstance(base, str) or isinstance(potencia, str):
        codigo = -400  # Entradas string
        resultado = None

    else:
        if isinstance(base, int) and isinstance(potencia, int):
            if base >= 0 and potencia >= 0:
                if base == 0:
                    if potencia == 0:
                        resultado = None  # 0 a la 0 es indef
                    else:
                        resultado = 0  # 0 a la x es 0
                else:
                    if potencia == 0:
                        resultado = 1  # x a la 0 es 1
                    else:
                        resultado = base
                        for a in range(potencia-1):
                            baseNueva = resultado

                            for b in range(base-1):
                                resultado += baseNueva

                codigo = 0  # Exito
            else:
                codigo = -500  # Son num negativos
                resultado = None
        else:
            codigo = -600  # Entradas no son enteros
            resultado = None

    return [codigo, resultado]
