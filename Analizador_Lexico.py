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

global input
def actualizar_entrada(entrada):
    global input
    input=entrada
    


def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

lexer = lex.lex(reflags = re.IGNORECASE)

global errores_
errores_ = []