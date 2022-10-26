
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMA DECIMAL ENTERO EXCLAMACION GUION ID LLAA LLAC PARA PARC PTCOMA PUNTO RAREATEXTO RBOTON RCHECK RCLAVE RCONTENEDOR RCONTROLES RETIQUETA RPROPIEDADES RRADIOBUTTON RTEXTOinit : instruccionesinstrucciones    : instrucciones instruccioninstrucciones : instruccioninstruccion : LLAA EXCLAMACION GUION GUION RCONTROLES controles RCONTROLES GUION GUION LLAC\n                    | LLAA EXCLAMACION GUION GUION RPROPIEDADES propiedades RPROPIEDADES GUION GUION LLAC\n                    controles    : controles controlcontroles : controlcontrol : RETIQUETA ID PTCOMA\n                | RBOTON ID PTCOMA\n                | RCHECK ID PTCOMA\n                | RRADIOBUTTON ID PTCOMA\n                | RTEXTO ID PTCOMA\n                | RAREATEXTO ID PTCOMA\n                | RCLAVE ID PTCOMA\n                | RCONTENEDOR ID PTCOMA\n                propiedades    : propiedades propiedadpropiedades : propiedadpropiedad : ID PUNTO ID PARA parametros PARC PTCOMA\n                parametros : parametros COMA parametroparametros : parametroparametro : expresionexpresion : ENTERO\n    expresion : DECIMAL\n    expresion : CADENA\n    expresion : ID\n    '
    
_lr_action_items = {'LLAA':([0,2,3,5,51,52,],[4,4,-3,-2,-4,-5,]),'$end':([1,2,3,5,51,52,],[0,-1,-3,-2,-4,-5,]),'EXCLAMACION':([4,],[6,]),'GUION':([6,7,24,34,37,46,],[7,8,37,46,48,49,]),'RCONTROLES':([8,11,12,25,38,39,40,41,42,43,44,45,],[9,24,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RPROPIEDADES':([8,21,22,35,62,],[10,34,-17,-16,-18,]),'RETIQUETA':([9,11,12,25,38,39,40,41,42,43,44,45,],[13,13,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RBOTON':([9,11,12,25,38,39,40,41,42,43,44,45,],[14,14,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RCHECK':([9,11,12,25,38,39,40,41,42,43,44,45,],[15,15,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RRADIOBUTTON':([9,11,12,25,38,39,40,41,42,43,44,45,],[16,16,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RTEXTO':([9,11,12,25,38,39,40,41,42,43,44,45,],[17,17,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RAREATEXTO':([9,11,12,25,38,39,40,41,42,43,44,45,],[18,18,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RCLAVE':([9,11,12,25,38,39,40,41,42,43,44,45,],[19,19,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'RCONTENEDOR':([9,11,12,25,38,39,40,41,42,43,44,45,],[20,20,-7,-6,-8,-9,-10,-11,-12,-13,-14,-15,]),'ID':([10,13,14,15,16,17,18,19,20,21,22,35,36,50,61,62,],[23,26,27,28,29,30,31,32,33,23,-17,-16,47,53,53,-18,]),'PUNTO':([23,],[36,]),'PTCOMA':([26,27,28,29,30,31,32,33,60,],[38,39,40,41,42,43,44,45,62,]),'PARA':([47,],[50,]),'LLAC':([48,49,],[51,52,]),'ENTERO':([50,61,],[57,57,]),'DECIMAL':([50,61,],[58,58,]),'CADENA':([50,61,],[59,59,]),'PARC':([53,54,55,56,57,58,59,63,],[-25,60,-20,-21,-22,-23,-24,-19,]),'COMA':([53,54,55,56,57,58,59,63,],[-25,61,-20,-21,-22,-23,-24,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,5,]),'controles':([9,],[11,]),'control':([9,11,],[12,25,]),'propiedades':([10,],[21,]),'propiedad':([10,21,],[22,35,]),'parametros':([50,],[54,]),'parametro':([50,61,],[55,63,]),'expresion':([50,61,],[56,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','Analizador_Sintactico.py',19),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Analizador_Sintactico.py',23),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_2','Analizador_Sintactico.py',29),
  ('instruccion -> LLAA EXCLAMACION GUION GUION RCONTROLES controles RCONTROLES GUION GUION LLAC','instruccion',10,'p_instrucciones_evaluar','Analizador_Sintactico.py',36),
  ('instruccion -> LLAA EXCLAMACION GUION GUION RPROPIEDADES propiedades RPROPIEDADES GUION GUION LLAC','instruccion',10,'p_instrucciones_evaluar','Analizador_Sintactico.py',37),
  ('controles -> controles control','controles',2,'p_controles_lista','Analizador_Sintactico.py',42),
  ('controles -> control','controles',1,'p_controles_2','Analizador_Sintactico.py',48),
  ('control -> RETIQUETA ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',58),
  ('control -> RBOTON ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',59),
  ('control -> RCHECK ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',60),
  ('control -> RRADIOBUTTON ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',61),
  ('control -> RTEXTO ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',62),
  ('control -> RAREATEXTO ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',63),
  ('control -> RCLAVE ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',64),
  ('control -> RCONTENEDOR ID PTCOMA','control',3,'p_instrucciones_controles','Analizador_Sintactico.py',65),
  ('propiedades -> propiedades propiedad','propiedades',2,'p_propiedades_lista','Analizador_Sintactico.py',96),
  ('propiedades -> propiedad','propiedades',1,'p_propiedades_2','Analizador_Sintactico.py',102),
  ('propiedad -> ID PUNTO ID PARA parametros PARC PTCOMA','propiedad',7,'p_instrucciones_propiedades','Analizador_Sintactico.py',109),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros_lista','Analizador_Sintactico.py',117),
  ('parametros -> parametro','parametros',1,'p_parametros_2','Analizador_Sintactico.py',122),
  ('parametro -> expresion','parametro',1,'p_parametro','Analizador_Sintactico.py',126),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Analizador_Sintactico.py',130),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Analizador_Sintactico.py',135),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','Analizador_Sintactico.py',140),
  ('expresion -> ID','expresion',1,'p_expresion_ID','Analizador_Sintactico.py',145),
]