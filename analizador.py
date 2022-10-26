import re
from errores_lexicos import Errores
import ply.lex as lex



# Aqui se declaran los nombres de los tokens
reserved = {
    'Controles'        : 'RCONTROLES',
    'Propiedades'      : 'RPROPIEDADES',
    # 'Colocacion'       : 'RCOLOCACION',
    'Etiqueta'         : 'RETIQUETA',
    'Boton'            : 'RBOTON',
    'Check'            : 'RCHECK',
    'RadioButton'      : 'RRADIOBUTTON',
    'Texto'            : 'RTEXTO',
    'AreaTexto'        : 'RAREATEXTO',
    'Clave'             : 'RCLAVE',
    'Contenedor'        : 'RCONTENEDOR',
}

tokens = [
    'EXCLAMACION',
    'LLAA',
    'LLAC',
    #'IGUAL',
    'GUION',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'ID',
    'PTCOMA',
    'PUNTO',
    'PARA',
    'PARC',
    'COMA',
] + list(reserved.values())

# Aqui se dan los valores de cada token
# En este caso decimos el valor que va a contener cada token osea, el lexema

t_EXCLAMACION = r'!'
t_LLAA        = r'<'
t_LLAC        = r'>'
t_GUION       = r'-'
t_PTCOMA      = r';'
t_PUNTO       = r'\.'
t_PARA        = r'\('
t_PARC        = r'\)'
t_COMA        = r','


# GRAMATICAS PARA NÚMEROS
# Pueden repasar la parte de gramáticas en la clase 4

# Gramática para números con punto decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

# Gramática para números enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Esta esa para poder aceptar cadenas de texto, lo vamos a usar más adelante
def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

#Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')# Check for reserved words
    return t

#Comentario de Una Linea
def t_Com_Simple(t):
    r'\/\/.*\n'
    t.lexer.lineno += 1

#Comentario Multilinea
def t_Com_Multiple(t):
    r'\/\*(.|\n)*?\*\/'
    t.lexer.lineno += t.value.count('\n')


# Esta función cuando lee un salto de línea lo agrega al analizador para 
# Saber en qué linea se encuentra
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Caracteres ignorados en este caso los espacios y las tabulaciones
t_ignore = " \t"




# Este es un error léxico, pueden irlos almacenando en un array para obtenerlos después
def t_error(t):
    print("Error Lexico, no se reconoce: '%s'" % t.value[0])
    error = Errores(t.value[0],'Error Lexico', find_column(input,t), t.lineno)
    errores_.append(error)
    t.lexer.skip(1)




def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

lexer = lex.lex(reflags = re.IGNORECASE)

global errores_
errores_ = []
import ply.yacc as yacc
import ply.lex as lex
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
    error = Errores(t.value[0],'Error Sintactico', find_column(input,t), t.lineno)
    errores_.append(error)



import ply.yacc as yacc
parser = yacc.yacc()
def parse(input):
    lexer.lineno = 1
    return parser.parse(input)


#f = open('texto.txt', 'r')
global input

def actualizar_entrada(entrada):
    global input
    input=entrada


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


#for error in errores_:
    #print(error.toString())

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