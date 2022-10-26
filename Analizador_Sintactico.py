from ast import If
import ply.yacc as yacc
import ply.lex as lex
from Analizador_Lexico import tokens
from Analizador_Lexico import lexer,errores_
from Analizador_Lexico import find_column
from errores_lexicos import Errores
from Expresiones.Identificador import Identificador
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Tabla_Simbolos import Tabla_Simbolos
from TablaSimbolos.Tipo import TIPO, CONTROL
#from menu import entry
from Instrucciones.Controles import Control

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_evaluar(t):
    '''instruccion : LLAA EXCLAMACION GUION GUION RCONTROLES controles RCONTROLES GUION GUION LLAC
                    | LLAA EXCLAMACION GUION GUION RPROPIEDADES propiedades RPROPIEDADES GUION GUION LLAC
                    '''
    t[0] = t[6]

def p_controles_lista(t):
    'controles    : controles control'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_controles_2(t):
    'controles : control'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]



lista_objetos_controles=[]
def p_instrucciones_controles(t):
    '''control : RETIQUETA ID PTCOMA
                | RBOTON ID PTCOMA
                | RCHECK ID PTCOMA
                | RRADIOBUTTON ID PTCOMA
                | RTEXTO ID PTCOMA
                | RAREATEXTO ID PTCOMA
                | RCLAVE ID PTCOMA
                | RCONTENEDOR ID PTCOMA
                '''
    print('Control: ', t[1], ' ID: ', t[2])
    if t[1] == 'Etiqueta':
        t[0] = Control(t[2], CONTROL.ETIQUETA, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Boton':
        t[0] = Control(t[2], CONTROL.BOTON, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Check':
        t[0] = Control(t[2], CONTROL.CHECK, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'RadioBoton':
        t[0] = Control(t[2], CONTROL.RADIOBOTON, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Texto':
        t[0] = Control(t[2], CONTROL.TEXTO, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'AreaTexto':
        t[0] = Control(t[2], CONTROL.AREATEXTO, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Clave':
        t[0] = Control(t[2], CONTROL.CLAVE, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Contenedor':
        t[0] = Control(t[2], CONTROL.CONTENEDOR, t.lineno(1), find_column(input, t.slice[1]))
        #lista_objetos_controles.append(t[0])
    else: 
        t[0] = ''

def p_propiedades_lista(t):
    'propiedades    : propiedades propiedad'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_propiedades_2(t):
    'propiedades : propiedad'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_propiedades(t):
    '''propiedad : ID PUNTO ID PARA parametros PARC PTCOMA
                '''
    print('ID: ', t[1], ' Propiedad: ', t[3], ' Parametros: ', t[5])
    
    t[0] = t[1]


def p_parametros_lista(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_2(t):
    'parametros : parametro'
    t[0] = [t[1]]

def p_parametro(t):
    'parametro : expresion'
    t[0] = t[1]

def p_expresion_entero(t):
    '''expresion : ENTERO
    '''
    t[0] = Primitivos(TIPO.ENTERO, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    '''expresion : DECIMAL
    '''
    t[0] = Primitivos(TIPO.FLOAT, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    '''expresion : CADENA
    '''
    t[0] = Primitivos(TIPO.STRING, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_ID(t):
    '''expresion : ID
    '''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]), TIPO.IDENTIFICADOR)

def p_error(t):
    print("Error de sintaxis en '%s'" % t.value," Linea:", t.lineno, " Columna:",find_column(input,t))
    Error_sintaxis=Errores(t.value,'Error de Sintaxis',find_column(input,t),t.lineno)
    errores_.append(Error_sintaxis)



import ply.yacc as yacc
parser = yacc.yacc()
def parse(input):
    lexer.lineno = 1
    return parser.parse(input)


#f = open('texto.txt', 'r')
#global input

#input = f.read()
#f.close()

'''def actualizar_input(entrada):
    global input
    input=entrada
    variable=parse(input)
    for error in errores_:
        print(error.toString())'''


#print("ARCHIVO DE SALIDA:")
#variable =parse(input)

#ast = Arbol(variable)




#TsgGlobal = Tabla_Simbolos()
#ast.setTSglobal(TsgGlobal)

# for error in errores:
#     ast.getExcepciones().append(error)
#     ast.updateConsola(error.toString())

#for instruccion in ast.getInst():
    #if isinstance(instruccion, list):
        #for instr in instruccion:
            #if isinstance(instr, Control):
                #value = instr.interpretar(ast, TsgGlobal)
                #if isinstance(value, Excepcion):
                    #ast.getExcepciones().append(value)
                    #ast.updateConsola(value.toString())

# for instruccion in ast.getInst():
#     if isinstance(instruccion, Funcion):
#         ast.setFunciones(instruccion)
#     if isinstance(instruccion, Declaracion):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())

# for instruccion in ast.getInst():
#     if isinstance(instruccion, Imprimir):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     if isinstance(instruccion, Identificador):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     if isinstance(instruccion, Llamada_Funcion):
#         value = instruccion.interpretar(ast,TsgGlobal)
#         if isinstance(value, Excepcion):
#             ast.getExcepciones().append(value)
#             ast.updateConsola(value.toString())
#     #value = instruccion.interpretar(ast,TsgGlobal)
#     # if isinstance(value, Excepcion):
#     #         ast.getExcepciones().append(value)
#     #         ast.updateConsola(value.toString())
# print(ast.getConsola())