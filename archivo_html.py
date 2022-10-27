class HTML_Archivo:
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Erores lexicos</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>'''

cuerpo=''''''

pie='''</body>
</html>'''


class Etiqueta:
    color_letra=None
    color_fondo=None
    Texto=None
    
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<label id="{self.id}"></label>'    



class Boton:
    Texto=None
    Text_Align=None
    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type="submit" id="{self.id}"/>'   



class Check:
    Texto=None
    Mark=False
    Grupo=None

    def __init__(self,id):
        self.id=id

    def crear_etiqueta(self):
        self.etiqueta=f'<input type="checkbox" id="{self.id}"/>'     

class RadioBoton:
    Texto=None
    Mark=False
    Grupo=None
    def __init__(self,id):
        self.id=id
    def crear_etiqueta(self):
        self.etiqueta=f'<input type="radio" id="{self.id}"/>'     



class Texto:
    Texto=None
    Text_Align=None
    def __init__(self,id):
        self.id=id        
    def crear_etiqueta(self):
        self.etiqueta=f'<input type = "text" id="{self.id}"/>'



class AreaTexto:
    Texto=None
    def __init__(self,id):
        self.id=id     
    def crear_etiqueta(self):
        self.etiqueta=f'<TEXTAREA id="{self.id}"></TEXTAREA> '

class Clave:
    Texto=None
    Text_Align=None
    def __init__(self,id):
        self.id=id
    def crear_etiqueta(self):
        self.etiqueta=f'<input type = "password" id="{self.id}"/>'    

class Contendor:
    Ancho=None
    Alto=None
    Color_fondo=None
    def __init__(self,id):
        self.id=id
    def crear_etiqueta(self):
        self.etiqueta=f'<div id="{self.id}"></div>'             