import tkinter
from tkinter import Entry, ttk,filedialog
from tkinter import messagebox
from tkinter.font import Font
import webbrowser as wb
import math
from archivo_html import HTML_Archivo,Archivo_CSS
from Analizador_Sintactico import parse,errores_,lista_objetos_tokens,componentes
from Analizador_Lexico import actualizar_entrada
#from analizador import parse,errores_,actualizar_entrada


principal=tkinter.Tk()
def inicio():
    principal.title("Menu Principal")
    principal.geometry("500x500")


    curso=tkinter.Label(principal,text="Nombre del curso: Lab Lenguajes Formales y de Programacion")
    curso.place(x=10,y=10)


    nombre=tkinter.Label(principal,text="Nombre del estudiante: Walter Javier Santizo Mazariegos")
    nombre.place(x=10,y=50)

    carne=tkinter.Label(principal,text="Carne del estudiante: 202111718")
    carne.place(x=10,y=90)

    Cargar=tkinter.Button(principal,text="Archivo",command=Archivo)
    Cargar.place(x=200,y=130)

    gestionar=tkinter.Button(principal,text="Help",command=help)
    gestionar.place(x=200,y=170)

    salir=tkinter.Button(principal,text="Salir",command=funcion_salir)
    salir.place(x=200,y=220)

    principal.mainloop()
        

def Archivo():
    global gestionar,entry
    principal.withdraw()
    gestionar=tkinter.Tk()
    gestionar.title("Archivo")
    gestionar.geometry("900x500")
    entry=tkinter.Text(gestionar)
    entry.place(x=0,y=0,width=900,height=300)
    Linea=tkinter.Label(gestionar,text="Linea: {}".format(entry.index("insert").split('.')[0]))
    Linea.place(x=600,y=300)
    Columna=tkinter.Label(gestionar,text="Columna: {}".format(entry.index("insert").split('.')[1]))
    Columna.place(x=650,y=300)
    btnListar=tkinter.Button(gestionar,text="abrir",command=abrir)
    btnListar.place(x=200,y=450)
    btnAgregar=tkinter.Button(gestionar,text="guardar",command=guardar)
    btnAgregar.place(x=250,y=450)
    btnEditar=tkinter.Button(gestionar,text="guardar como",command=guardar_como)
    btnEditar.place(x=350,y=450)
    def actualizar_pos(event):
        Linea.configure(text="Linea: {}".format(entry.index("insert").split('.')[0]))
        Columna.configure(text="Columna: {}".format(entry.index("current").split('.')[1]))    
    entry.bind("<Button-1>", actualizar_pos)
    def nuevo():
        texto_o=entry.get(1.0,"end")
        texto_s=texto_o.replace("\n","")
        respuesta=messagebox.askquestion("Desea Abrir un Nuevo Archivo","El progreso actual de este archivo se guardara")
        if respuesta=="yes":
            f = filedialog.asksaveasfile(mode='w', defaultextension=".lfp")
            if (f): 
                f.write(entry.get(1.0,"end"))
                f.close()
                messagebox.showinfo("Aviso","Archivo guardado correctamente")
                entry.delete(1.0,"end")
        else:
            messagebox.showinfo("Aviso","Continue editando su archivo")       
         
    btnEliminar=tkinter.Button(gestionar,text="Nuevo",command=nuevo)
    btnEliminar.place(x=450,y=450)
    def analizar():
        errores_.clear()
        lista_objetos_tokens.clear()
        componentes.clear()
        actualizar_entrada(entry.get(1.0,"end"))
        variable =parse(entry.get(1.0,"end"))


        
        archivo=HTML_Archivo()
        for comp in componentes:
            archivo.set_cuerpo(comp.etiqueta)

        archivo.crear_archivo()    


        archivo_css=Archivo_CSS()
        for comp in componentes:
            archivo_css.set_contenido(comp.clase)

        archivo_css.crear_archivo() 

        #for error in errores_:
            #print(error.toString())

        #for token in lista_objetos_tokens:
            #print(token.toString())
        #messagebox.showinfo("Aviso","Revise su carpeta archivos creados")        
    btnEliminar=tkinter.Button(gestionar,text="Analizar",command=analizar)
    btnEliminar.place(x=720,y=450)
    btnEliminar=tkinter.Button(gestionar,text="errores",command=generar_repo)
    btnEliminar.place(x=550,y=450)
    btnEliminar=tkinter.Button(gestionar,text="Tabla de Tokens",command=generar_tabla_tokens)
    btnEliminar.place(x=800,y=450)

    def funcion_regresar_gestionar_principal():
        principal.deiconify()
        gestionar.withdraw()
    Regresar=tkinter.Button(gestionar,text="Regresar",command=funcion_regresar_gestionar_principal)
    Regresar.place(x=650,y=450)    

def generar_tabla_tokens():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".html")
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Tabla de Tokens</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>
<table class="default" border="1">
  <tr>
    <th>No.</th>
    <th>Token</th>
    <th>Lexema</th>
  </tr>  
'''
    cuerpo=''''''
    for i in range(len(lista_objetos_tokens)):
        cuerpo+='''  <tr>
    <th>'''+str(i+1)+'''</th>
    <th>'''+lista_objetos_tokens[i].token+'''</th>
    <th>'''+lista_objetos_tokens[i].lexema+'''</th>
  </tr>'''

    pie='''
    </table>
</body>
</html>'''
    if (f):
        f.write(cabecera+cuerpo+pie)
        f.close ()
        messagebox.showinfo("Aviso","Archivo Generado por favor revise su carpeta")


def generar_repo():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".html")
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Erores Del Archivo</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>
<table class="default" border="1">
  <tr>
    <th>No.</th>
    <th>Lexema</th>
    <th>Tipo</th>
    <th>Columna</th>
    <th>Linea</th>
  </tr>  
'''
    cuerpo=''''''
    for i in range(len(errores_)):
        cuerpo+='''  <tr>
    <th>'''+str(i+1)+'''</th>
    <th>'''+errores_[i].lexema+'''</th>
    <th>'''+errores_[i].tipo+'''</th>
    <th>'''+str(errores_[i].columna)+'''</th>
    <th>'''+str(errores_[i].fila)+'''</th>
  </tr>'''

    pie='''
    </table>
</body>
</html>'''
    if (f):
        f.write(cabecera+cuerpo+pie)
        f.close ()
        messagebox.showinfo("Aviso","Archivo Generado por favor revise su carpeta")





def abrir():
    global entry,path
    entry.delete(1.0,"end")
    path=filedialog.askopenfilename()
    if(path):
        file=open(path,"r")
        text=file.read()
        file.close()
        entry.insert(1.0,text)


 

def guardar():
    global path,entry
    file=open(path,"w")
    file.write(entry.get(1.0,"end"))
    file.close()
    messagebox.showinfo("Aviso","Su archivo se guardo correctamente")


def guardar_como():
    global entry
    f = filedialog.asksaveasfile(mode='w', defaultextension=".lfp")
    if (f): 
        f.write(entry.get(1.0,"end"))
        f.close()
        messagebox.showinfo("Aviso","Archivo guardado correctamente")

def help():
    global gestionar
    principal.withdraw()
    gestionar=tkinter.Tk()
    gestionar.title("Gestionar")
    gestionar.geometry("500x500")
    btnListar=tkinter.Button(gestionar,text="Manual de Usuario",command=abrir_usuario)
    btnListar.place(x=200,y=100)
    btnAgregar=tkinter.Button(gestionar,text="Manual Tecnico",command=abrir_tecnico)
    btnAgregar.place(x=200,y=150)
    btnEditar=tkinter.Button(gestionar,text="Temas de ayuda",command=ayuda)
    btnEditar.place(x=200,y=200)
    def funcion_regresar_gestionar_principal():
        principal.deiconify()
        gestionar.withdraw()
    Regresar=tkinter.Button(gestionar,text="Regresar",command=funcion_regresar_gestionar_principal)
    Regresar.place(x=200,y=300)        

def abrir_usuario():
    wb.open_new("Manual_usuario.pdf")

def abrir_tecnico():
    wb.open_new("Manual_tecnico.pdf")
    
def ayuda():
    messagebox.showinfo("INFORMACION DEL DESARROLADOR","Nombre: WALTER JAVIER SANTIZO MAZARIEGOS\nCarnet: 202111718\nCUI: 2070097670101")    




def ventana_conteo():
    fuente=Font(family="Roboto Cn",size=14)
    principal.withdraw()
    conteo=tkinter.Tk()
    conteo.title("Conteo")
    conteo.geometry("500x500")
    titulo=tkinter.Label(conteo,text="Creditos aprobados, Cursando y pendientes Totales",font=fuente)
    titulo.place(x=30,y=20)
    obligatorios=tkinter.Label(conteo,text="Creditos Aprobados hasta semestre N: ")
    obligatorios.place(x=30,y=140)
    txtCobligatorios=tkinter.Entry(conteo)
    txtCobligatorios.place(x=235,y=140,width=70,height=20)
    Semestre=tkinter.Label(conteo,text="Semestre")
    Semestre.place(x=60,y=180)
    spin1=ttk.Spinbox(conteo,width=10,from_=1,to=10,increment=1)
    spin1.place(x=135,y=180)
    def funcion_regresar_conteo_principal():
        principal.deiconify()
        conteo.withdraw()
    Regresar=tkinter.Button(conteo,text="Regresar",command=funcion_regresar_conteo_principal)
    Regresar.place(x=400,y=400)   

def funcion_salir():
    principal.destroy()
    exit()
    



inicio()