from ast import If
from re import A
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
from tokens import Token
from archivo_html import *
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
                    | LLAA EXCLAMACION GUION GUION RCOLOCACION colocaciones RCOLOCACION GUION GUION LLAC
                    '''
    a=Token('LLAA',t[1])
    lista_objetos_tokens.append(a)
    a=Token('EXCLAMACION',t[2])
    lista_objetos_tokens.append(a)
    a=Token('GUION',t[3])
    lista_objetos_tokens.append(a)
    a=Token('GUION',t[4])
    lista_objetos_tokens.append(a)
    a=Token('Palabra Reservada',t[5])
    lista_objetos_tokens.append(a)
    a=Token('Palabra Reservada',t[7])
    lista_objetos_tokens.append(a)
    a=Token('GUION',t[8])
    lista_objetos_tokens.append(a)
    a=Token('GUION',t[9])
    lista_objetos_tokens.append(a)
    a=Token('LLAC',t[10])
    lista_objetos_tokens.append(a)






    #print(t[1],t[2],t[3],t[4],t[5],t[7],t[8],t[9],t[10])#< ! - - Controles Controles - - >                
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
lista_objetos_tokens=[]
componentes=[]



def p_instrucciones_controles(t):
    '''control : RETIQUETA ID PTCOMA
                | RBOTON ID PTCOMA
                | RCHECK ID PTCOMA
                | RRADIOBOTON ID PTCOMA
                | RTEXTO ID PTCOMA
                | RAREATEXTO ID PTCOMA
                | RCLAVE ID PTCOMA
                | RCONTENEDOR ID PTCOMA
                '''
    print('Control: ', t[1], ' ID: ', t[2])
    objeto_tokn=Token('Control',t[1])
    lista_objetos_tokens.append(objeto_tokn)
    objeto_tokn=Token('Id',t[2])
    lista_objetos_tokens.append(objeto_tokn)
    objeto_tokn=Token('Punto y Coma',t[3])
    lista_objetos_tokens.append(objeto_tokn)   
    if t[1] == 'Etiqueta':
        t[0] = Control(t[2], CONTROL.ETIQUETA, t.lineno(1), find_column(input, t.slice[1]))
        comp=Etiqueta(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Boton':
        t[0] = Control(t[2], CONTROL.BOTON, t.lineno(1), find_column(input, t.slice[1]))
        comp=Boton(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Check':
        t[0] = Control(t[2], CONTROL.CHECK, t.lineno(1), find_column(input, t.slice[1]))
        comp=Check(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'RadioBoton':
        t[0] = Control(t[2], CONTROL.RADIOBOTON, t.lineno(1), find_column(input, t.slice[1]))
        comp=RadioBoton(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Texto':
        t[0] = Control(t[2], CONTROL.TEXTO, t.lineno(1), find_column(input, t.slice[1]))
        comp=Texto(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'AreaTexto':
        t[0] = Control(t[2], CONTROL.AREATEXTO, t.lineno(1), find_column(input, t.slice[1]))
        comp=AreaTexto(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Clave':
        t[0] = Control(t[2], CONTROL.CLAVE, t.lineno(1), find_column(input, t.slice[1]))
        comp=Clave(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
        #lista_objetos_controles.append(t[0])
    elif t[1] == 'Contenedor':
        t[0] = Control(t[2], CONTROL.CONTENEDOR, t.lineno(1), find_column(input, t.slice[1]))
        comp=Contendor(t[2])
        comp.crear_etiqueta()
        componentes.append(comp)
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


def encontrar_componente(id):
    for comp in componentes:
        if comp.id==id:
            return comp


def p_instrucciones_propiedades(t):
    '''propiedad : ID PUNTO ID PARA parametros PARC PTCOMA
                '''
    #print('ID: ', t[1], ' Propiedad: ', t[3], ' Parametros: ', t[5])
    parametros=t[5]
    print(t[1],t[2],t[3],t[4],t[6],t[7])# Nombre . setColorLetra ( ) ;
    if encontrar_componente(t[1])==None:
        objeto_error=Errores(t[1],'Error Sintactico',"N/A",t.lineno(1))
        errores_.append(objeto_error)
    else:    
        comp=encontrar_componente(t[1])
        if type(comp)==Etiqueta:
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setAncho":
                    comp.set_Ancho(t[5][0].valor)
                elif t[3]=="setAlto":
                    comp.set_Alto(t[5][0].valor)
                elif t[3]=="setColorFondo":
                    comp.set_Color(t[5][0].valor,t[5][1].valor,t[5][2].valor)
                    #print(t[5][0].valor,t[5][1].valor,t[5][2].valor)
                elif t[3]=="setColorLetra":
                    comp.set_Color_Letra(t[5][0].valor,t[5][1].valor,t[5][2].valor)
                    #print(t[5][0].valor,t[5][1].valor,t[5][2].valor)
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)      
        elif type(comp)==Boton:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setAlineacion":
                    #print(t[5][0].valor)
                    comp.set_Text_Align(t[5][0].valor)
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)      
        elif type(comp)==Check:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setMarcada":
                    #print(t[5][0].valor)
                    comp.set_Marcada(t[5][0].valor)
                elif t[3]=="setGrupo":
                    #print(t[5][0].valor)
                    comp.set_Group(t[5][0].valor)    
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)  
        elif type(comp)==RadioBoton:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setMarcada":
                    #print(t[5][0].valor)
                    comp.set_Marcada(t[5][0].valor)
                elif t[3]=="setGrupo":
                    #print(t[5][0].valor)
                    comp.set_Group(t[5][0].valor)    
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)
        elif type(comp)==Texto:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setAlineacion":
                    #print(t[5][0].valor)
                    comp.set_Text_Align(t[5][0].valor)
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)   
        elif type(comp)==AreaTexto:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)                    
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)  
        elif type(comp)==Clave:
            comp.iniciar_clase()
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setAlineacion":
                    #print(t[5][0].valor)
                    comp.set_Text_Align(t[5][0].valor)
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)
        elif type(comp)==Contendor:
            if t[3] in comp.propiedades:
                if t[3]=="setTexto":
                    comp.set_Texto(t[5][0].valor)
                elif t[3]=="setAncho":
                    comp.set_Ancho(t[5][0].valor)
                elif t[3]=="setAlto":
                    comp.set_Alto(t[5][0].valor)
                elif t[3]=="setColorFondo":
                    comp.set_Color(t[5][0].valor,t[5][1].valor,t[5][2].valor)
                    #print(t[5][0].valor,t[5][1].valor,t[5][2].valor)
            else:
               objeto_error=Errores(t[3],'Error Sintactico',"N/A",t.lineno(1))
               errores_.append(objeto_error)     
   






    a=Token('Id',t[1])
    lista_objetos_tokens.append(a)
    a=Token('Punto',t[2])
    lista_objetos_tokens.append(a)
    a=Token('Propiedad',t[3])
    lista_objetos_tokens.append(a)
    a=Token('PARA',t[4])
    lista_objetos_tokens.append(a)
    a=Token('PARC',t[6])
    lista_objetos_tokens.append(a)
    a=Token('Punto y Coma',t[7])
    lista_objetos_tokens.append(a)        

    for para in parametros:
        if para.tipo == TIPO.ENTERO:
            tkn=Token('ENTERO',str(para.valor))
            lista_objetos_tokens.append(tkn)
        elif para.tipo==TIPO.STRING:   
            tkn=Token('STRING',para.valor)
            lista_objetos_tokens.append(tkn)


    #parte de setear los valores 





    t[0] = t[1]


def p_colocaciones_lista(t):
    'colocaciones    : colocaciones colocacion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_colocaciones_2(t):
    'colocaciones : colocacion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]


def p_instrucciones_colocaciones(t):
    '''colocacion : ID PUNTO ID PARA parametros PARC PTCOMA ID PUNTO ID PARA parametros PARC PTCOMA
                 '''
    #print('ID: ', t[1], ' Propiedad: ', t[3], ' Parametros: ', t[5])             
    print(t[1],t[2],t[3],t[4],t[6],t[7])
    print(t[8],t[9],t[10],t[11],t[13],t[14])
    parametros1=t[5]
    parametros2=t[12]
    if encontrar_componente(t[1])==None:
        objeto_error=Errores(t[1],'Error Sintactico',"N/A",t.lineno(1))
        errores_.append(objeto_error)
    else:
        comp=encontrar_componente(t[1])
        if t[3] =="setPosicion":
            #print(t[5][0].valor,t[5][1].valor)
            comp.set_Posicion(t[5][0].valor,t[5][1].valor)
        else:
            objeto_error=Errores(t[1],'Error Sintactico',"N/A",t.lineno(1))
            errores_.append(objeto_error)              





def p_parametros_lista(t):
    'parametros : parametros COMA parametro'
    tkn=Token('Coma',t[2])
    lista_objetos_tokens.append(tkn)
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