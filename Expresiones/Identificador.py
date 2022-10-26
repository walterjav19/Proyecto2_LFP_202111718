# from TablaSimbolos.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
# from TablaSimbolos.Tipo import TIPO

class Identificador(Instruccion):
    def __init__(self, ide, fila, columna, tipo = None):
        self.ide = ide
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.ide)
        if simbolo == None:
            # return Excepcion("Semantico", "Variable no encontrada", self.fila, self.colum)
            return 'Error'
        self.tipo = simbolo.getTipo()
        return simbolo.getValor()

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide