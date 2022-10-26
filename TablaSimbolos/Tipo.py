from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    FLOAT = 2
    STRING = 3
    NULO = 4
    IDENTIFICADOR = 5

class CONTROL(Enum):
    ETIQUETA = 1
    BOTON = 2
    CHECK = 3
    RADIOBOTON = 4
    TEXTO = 5
    AREATEXTO = 6
    CLAVE = 7
    CONTENEDOR = 8