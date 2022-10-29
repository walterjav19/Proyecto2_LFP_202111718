class HTML_Archivo:
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>HTML Salida</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>\n'''

    cuerpo=''''''

    pie='''</body>
</html>'''




    def set_cuerpo(self,etiqueta):
        self.cuerpo+=etiqueta+"\n"

    def crear_archivo(self):
        string=self.cabecera+self.cuerpo+self.pie
        archivo=open("salida.html","w")
        archivo.write(string)
        archivo.close()

class Archivo_CSS:
    contenido=""
    def set_contenido(self,css):
        self.contenido+=css+"\n"


    def crear_archivo(self):
        archivo=open("estilo.css","w")
        archivo.write(self.contenido)
        archivo.close()

class Etiqueta:
    Ancho=None
    Alto=None
    top=None
    left=None
    bg_r=None
    bg_g=None
    bg_b=None
    Co_r=None
    Co_g=None
    Co_b=None
    Texto=None
    
    propiedades=["setTexto","setAncho","setAlto","setColorFondo","setColorLetra"]
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<label id="{self.id}"></label>'    

    def set_Ancho(self,ancho):
        self.Ancho=str(ancho)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    color: rgb('''+str(self.Co_r)+''','''+str(self.Co_g)+''','''+str(self.Co_b)+''');
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Alto(self,alto):
        self.Alto=str(alto)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    color: rgb('''+str(self.Co_r)+''','''+str(self.Co_g)+''','''+str(self.Co_b)+''');
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''
    def set_Color_Letra(self,r,g,b):
        self.Co_r=str(r)
        self.Co_g=str(g)
        self.Co_b=str(b)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+''' px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    color: rgb('''+str(self.Co_r)+''','''+str(self.Co_g)+''','''+str(self.Co_b)+''');
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Color(self,r,g,b):
        self.bg_r=str(r)
        self.bg_g=str(g)
        self.bg_b=str(b)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    color: rgb('''+str(self.Co_r)+''','''+str(self.Co_g)+''','''+str(self.Co_b)+''');
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    color: rgb('''+str(self.Co_r)+''','''+str(self.Co_g)+''','''+str(self.Co_b)+''');
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<label id="{self.id}">{self.Texto}</label>' 
    def borrar_etiqueta(self):
        self.etiqueta=""


class Boton:
    Ancho="100"
    Alto="25"
    top=None
    left=None
    clase=""
    Texto=""
    Text_Align="left"
    propiedades=["setTexto","setAlineacion"]
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type="submit" id="{self.id}"/>'


    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<input type="submit" id="{self.id}" value="{self.Texto}"/>'

    def set_Text_Align(self,Align):
        if Align=="Centro":
            self.Text_Align="center"
        elif Align=="Izquierdo":
            self.Text_Align="left"
        elif Align=="Derecho":
            self.Text_Align="rigth"
        else:
            self.Text_Align=Align            
        self.Text_Align=Align
        self.etiqueta=f'<input type="submit" id="{self.id}" value="{self.Texto}" style="text-align:{self.Text_Align};" />' 

    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def borrar_etiqueta(self):
        self.etiqueta=""

class Check:
    Texto=""
    Mark=False
    Grupo=""
    Ancho="100"
    Alto="25"
    top=None
    left=None
    propiedades=["setTexto","setMarcada","setGrupo"]
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type="checkbox" id="{self.id}"/>'     

    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<input type="checkbox" id="{self.id}"/>{self.Texto}'

    def set_Group(self,group):
        self.Grupo=group
        self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'    

    def set_Marcada(self,bool):
        if bool=="true":
            self.Mark=True
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}" checked/>{self.Texto}'
        elif bool=="false":
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'
            self.Mark=False
        else:
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'    
    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def borrar_etiqueta(self):
        self.etiqueta=""    

class RadioBoton:
    clase=""
    Texto=""
    Mark=False
    Grupo=""
    Ancho="100"
    Alto="25"
    top=None
    left=None
    propiedades=["setTexto","setMarcada","setGrupo"]
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type="radio" id="{self.id}"/>'

    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<input type="radio" id="{self.id}"/>{self.Texto}'

    def set_Group(self,group):
        self.Grupo=group
        self.etiqueta=f'<input type="radio"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'

    def set_Marcada(self,bool):
        if bool=="true":
            self.Mark=True
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}" checked/>{self.Texto}'
        elif bool=="false":
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'
            self.Mark=False
        else:
            self.etiqueta=f'<input type="checkbox"  name="{self.Grupo}" id="{self.id}"/>{self.Texto}'    
    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    }'''

    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def borrar_etiqueta(self):
        self.etiqueta=""

class Texto:
    clase=""
    Texto=""
    Text_Align=""
    Ancho="100"
    Alto="25"
    top=None
    left=None
    propiedades=["setTexto","setAlineacion"]
    def __init__(self,id):
        self.id=id        
    def crear_etiqueta(self):
        self.etiqueta=f'<input type = "text" id="{self.id}"/>'

    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<input type = "text" id="{self.id}" value="{self.Texto}"/>'

    def set_Text_Align(self,align):
        self.Text_Align=align
        self.etiqueta=f'<input type = "text" id="{self.id}" value="{self.Texto}"  style="text-align:{self.Text_Align};"/>'

    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''    
    def borrar_etiqueta(self):
        self.etiqueta=""


class AreaTexto:
    clase=""
    Ancho="150"
    Alto="150"
    top=None
    left=None
    Texto=""
    propiedades=["setTexto"]
    def __init__(self,id):
        self.id=id     
    def crear_etiqueta(self):
        self.etiqueta=f'<TEXTAREA id="{self.id}"></TEXTAREA> '

    def set_Texto(self,texto):
        self.Texto=texto
        self.etiqueta=f'<TEXTAREA id="{self.id}">{self.Texto}</TEXTAREA> '   

    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''     
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def borrar_etiqueta(self):
        self.etiqueta=""


class Clave:
    clase=""
    Texto=""
    Ancho="100"
    Alto="25"
    top=None
    left=None
    Text_Align=""
    propiedades=["setTexto","setAlineacion"]
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type = "password" id="{self.id}"/>'    

    def set_Texto(self,Texto):
        self.Texto=Texto
        self.etiqueta=f'<input type = "password" id="{self.id}" value="{self.Texto}"/>'

    def set_Text_Align(self,align):
        self.Text_Align=align
        self.etiqueta=f'<input type="password" id="{self.id}" value="{self.Texto}" style="text-align:{self.Text_Align}"/>'

    def iniciar_clase(self):
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    font-size: 12px;
    } 
    '''
    def borrar_etiqueta(self):
        self.etiqueta=""

class Contendor:
    clase=""
    Ancho=None
    Alto=None
    top=None
    left=None
    bg_r=None
    bg_g=None
    bg_b=None
    Color_fondo=None
    propiedades=["setAncho","setAlto","setColorFondo"]
    def __init__(self,id):
        self.id=id
    def crear_etiqueta(self):
        self.etiqueta=f'<div id="{self.id}"></div>'

    def borrar_etiqueta(self):
        self.etiqueta=""
        
    etiquetas_interiores=""
        
    def insertar_etiqueta(self,eti):
        self.etiquetas_interiores+=eti+"\n"
        self.etiqueta=f'<div id="{self.id}">\n{self.etiquetas_interiores}\n</div>'

    def set_Ancho(self,ancho):
        self.Ancho=str(ancho)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Alto(self,alto):
        self.Alto=str(alto)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Color(self,r,g,b):
        self.bg_r=str(r)
        self.bg_g=str(g)
        self.bg_b=str(b)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''

    def set_Posicion(self,left,top):
        self.left=str(left)
        self.top=str(top)
        self.clase='''#'''+self.id+'''{
    position:absolute;
    top :'''+str(self.top)+'''px; 
    left:'''+str(self.left)+'''px; 
    width:'''+str(self.Ancho)+'''px;
    height:'''+str(self.Alto)+'''px;
    background-color: rgb('''+str(self.bg_r)+''','''+str(self.bg_g)+''','''+str(self.bg_b)+''');
    font-size: 12px;
    } 
    '''    