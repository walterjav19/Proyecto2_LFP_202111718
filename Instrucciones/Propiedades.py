from tkinter.messagebox import NO
from typing import Dict
from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos

class Propiedades(Instruccion):

    def __init__(self, id, fila, columna,  propiedades):
        self.fila = fila
        self.columna = columna
        self.propiedades = propiedades
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.id)
        if simbolo == None: return Excepcion("Semantico", "Variable no encontrada", self.fila, self.columna)
        simbolo.setPropiedades(self.propiedades)
        return None