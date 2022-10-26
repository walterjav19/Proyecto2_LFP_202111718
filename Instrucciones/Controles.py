from tkinter.messagebox import NO
from typing import Dict
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class Control(Instruccion):
    def __init__(self, ide,tipo, fila, columna):
        self.id = ide
        self.tipo = tipo
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        simbolo = Simbolo(str(self.id), self.tipo, self.fila, self.colum)
        result = table.setTabla(simbolo)
        if isinstance(result, Excepcion): return result
        return None

    def setAncho(self, ancho):
        self.ancho = ancho
    
    def setAlto(self, alto):
        self.alto = alto
    
    def getPropiedades(self):
        try:
            return {self.ancho, self.alto}
        except:
            return None
