
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNA COMA CORDER CORIZQ CTEBOOL CTEFLOAT CTEINT CTESTRING DIFERENTE DIV DOSPUNTOS EQUALS ID LLAVEDER LLAVEIZQ MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MULT OR PARDER PARIZQ PUNTO PYC avg bool else end false float for func if int length main max median min mode program read return stdev string true var variance void while write\n    programa : program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC\n    \n    programa : program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC\n    \n    cuadGotoMain :\n    \n    cuadEnd :\n    auxprograma :\n    \n    varsaux : vars varsaux\n            | empty\n    \n    paux2 : function paux2\n          | empty\n    \n    vars : var type vaux PYC\n         | empty\n    \n    vaux : ID agregaVar nextvar\n         | ID CORIZQ CTEINT CORDER agregaVar nextvar\n         | ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar\n    \n    nextvar : COMA vaux\n            | empty\n    \n    agregaVar :\n    \n    guardarTipoVar :\n    \n    guardarTipoFunc :\n    \n    mainfunction : func main agregaFunc PARIZQ PARDER bloque\n    \n    bloque : LLAVEIZQ bloqueaux LLAVEDER\n           | LLAVEIZQ empty LLAVEDER\n    \n    bloqueaux : estatuto bloqueaux\n              | estatuto\n    \n    type : int guardarTipoVar\n         | float guardarTipoVar\n         | string guardarTipoVar\n         | bool guardarTipoVar\n    \n    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux bloque\n             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux bloque\n    \n    agregaFunc :\n    \n    ftype : int guardarTipoFunc\n          | float guardarTipoFunc\n          | string guardarTipoFunc\n          | bool guardarTipoFunc\n          | void guardarTipoFunc\n    \n    funcaux : type ID agregaVar masParam\n            | type ID CORIZQ CTEINT CORDER agregaVar masParam\n            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar masParam\n    \n    masParam : funcaux\n             | empty\n    \n    estatuto : asignacion\n             | escritura\n             | llamada\n             | condicion\n             | whileloop\n             | forloop\n             | lectura\n             | estReturn\n    \n    asignacion : ID checkID asignaux ASIGNA expresion cuadAsignacion PYC\n               | ID checkID asignaux ASIGNA llamada_esp PYC\n               | ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC\n    \n    checkID :\n    \n    cuadAsignacion :\n    \n    asignaux : CORIZQ expresion CORDER\n             | CORIZQ expresion COMA expresion CORDER\n             | empty\n    \n    escritura : write PARIZQ escaux PARDER PYC\n    \n    escaux : expresion cuadEsc nextexp\n           | CTESTRING cuadEsc nextexp\n           | llamada_esp nextexp\n           | llamada nextexp\n    \n    cuadEsc :\n    \n    nextexp : COMA escaux\n            | empty\n    \n    llamada : ID PARIZQ expresion llamaux PARDER\n            | ID PARIZQ llamada_esp llamaux PARDER\n            | ID PARIZQ PARDER\n    \n    llamaux : expresion nextparametro\n            | llamada_esp nextparametro\n    \n    nextparametro : COMA llamaux\n                  | empty\n    \n    condicion : if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf\n    \n    condicionAux : else cuadGoto bloque\n                 | empty\n    \n    whileloop : while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile\n    \n    migaja :\n    \n    cuadFinWhile :\n    \n    forloop : for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor\n    \n    checkExpFor :\n    \n    gotoFor :\n    \n    returnFor :\n    \n    lectura : read PARIZQ ID checkID PARDER PYC\n    \n    estReturn : return PARIZQ retAux PARDER PYC\n    \n    retAux : expresion\n           | CTESTRING\n           | true\n           | false\n           | llamada\n    \n    expresion : andExpresion\n              | andExpresion OR pushOper andExpresion\n    \n    andExpresion : relopExpresion\n                 | relopExpresion AND pushOper relopExpresion\n    \n    relopExpresion : aritExpresion cuadArit\n                   | aritExpresion cuadArit relopAux aritExpresion cuadArit\n    \n    relopAux : MAYORQUE pushOper \n             | MENORQUE pushOper \n             | MAYORIGUAL pushOper\n             | MENORIGUAL pushOper\n             | EQUALS pushOper\n             | DIFERENTE pushOper\n    \n    aritExpresion : term cuadTerm\n                  | term cuadTerm aritAux term cuadTerm\n    \n    aritAux : MAS pushOper\n            | MENOS pushOper\n    \n    term : factor \n         | factor cuadFactor termAux factor cuadFactor\n    \n    termAux : MULT pushOper\n            | DIV pushOper\n    \n    factor : PARIZQ expresion PARDER\n           | CTEINT pushOT\n           | CTEFLOAT pushOT\n           | true pushOT\n           | false pushOT\n           | ID checkID pushOT\n           | llamada_esp pushOT\n           | llamada pushOT\n    \n    llamada_esp : ID PUNTO especiales PARIZQ PARDER\n    \n    especiales : length\n               | max\n               | min\n               | avg\n               | median\n               | mode\n               | variance\n               | stdev\n    \n    pushOper :\n    \n    pushOT :\n    \n    cuadTerm :\n    \n    cuadFactor :\n    \n    cuadArit :\n    \n    cuadGotof : \n    \n    cuadFinIf :\n    \n    cuadGoto :\n    \n    empty : \n    '
    
_lr_action_items = {'program':([0,],[2,]),'$end':([1,61,63,],[0,-2,-1,]),'ID':([2,3,5,25,26,27,28,29,34,42,43,44,45,58,71,75,83,84,85,86,87,88,89,90,91,104,105,108,109,110,112,113,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,147,148,149,161,164,170,171,172,173,174,176,177,178,179,180,185,199,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,238,240,244,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,267,269,270,272,273,274,275,276,278,279,282,284,286,288,289,],[-3,4,7,41,-18,-18,-18,-18,49,-25,-26,-27,-28,41,78,92,92,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,125,145,147,147,151,158,147,-53,147,125,-68,125,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,147,125,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,145,147,-115,-110,125,-66,-67,147,147,147,-127,-127,-127,-127,-127,-127,147,-127,-127,147,-127,-127,-58,147,-84,-51,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-135,-83,-50,-52,-118,-95,-103,-107,-133,-75,-78,-73,-76,-74,-82,-79,]),'PYC':([4,6,7,40,41,46,48,51,53,55,57,59,65,66,72,79,80,103,121,125,128,130,131,132,133,134,135,136,137,138,139,147,148,164,170,173,174,176,177,178,179,180,181,192,195,196,197,209,210,214,216,239,243,245,249,250,251,258,261,272,273,274,275,],[-5,8,9,50,-17,-4,-4,-135,61,63,-12,-16,-15,-17,-135,-13,-17,-135,-14,-53,-68,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,-128,-116,-94,-102,-111,-112,-113,-114,-117,232,240,-54,244,-54,-115,-110,-66,-67,267,269,270,-91,-93,-131,-129,-130,-118,-95,-103,-107,]),'var':([8,11,12,50,76,77,],[13,13,-11,-10,13,13,]),'int':([8,10,11,12,13,16,24,50,64,78,101,104,105,115,116,159,193,242,268,],[-135,19,-135,-7,26,19,-6,-10,26,-17,26,-21,-22,-29,-30,-17,26,-17,26,]),'float':([8,10,11,12,13,16,24,50,64,78,101,104,105,115,116,159,193,242,268,],[-135,20,-135,-7,27,20,-6,-10,27,-17,27,-21,-22,-29,-30,-17,27,-17,27,]),'string':([8,10,11,12,13,16,24,50,64,78,101,104,105,115,116,159,193,242,268,],[-135,21,-135,-7,28,21,-6,-10,28,-17,28,-21,-22,-29,-30,-17,28,-17,28,]),'bool':([8,10,11,12,13,16,24,50,64,78,101,104,105,115,116,159,193,242,268,],[-135,22,-135,-7,29,22,-6,-10,29,-17,29,-21,-22,-29,-30,-17,29,-17,29,]),'void':([8,10,11,12,16,24,50,104,105,115,116,],[-135,23,-135,-7,23,-6,-10,-21,-22,-29,-30,]),'func':([8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,33,35,36,37,38,39,50,104,105,115,116,],[-135,-135,-135,-135,-7,31,31,-135,-9,34,-19,-19,-19,-19,-19,-6,-8,-32,-33,-34,-35,-36,-10,-21,-22,-29,-30,]),'LLAVEIZQ':([11,12,24,50,68,76,77,99,100,188,236,237,265,277,283,285,287,],[-135,-7,-6,-10,75,-135,-135,75,75,-132,75,-132,75,-134,75,-81,75,]),'end':([30,32,74,104,105,],[46,48,-20,-21,-22,]),'main':([31,],[47,]),'CORIZQ':([41,78,92,107,],[52,102,-53,123,]),'COMA':([41,51,60,66,72,80,103,120,125,128,129,130,131,132,133,134,135,136,137,138,139,141,142,143,144,145,147,148,162,164,166,168,170,173,174,176,177,178,179,180,182,183,209,210,214,216,249,250,251,258,261,272,273,274,275,],[-17,58,67,-17,58,-17,58,160,-53,-68,-128,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-63,-63,185,185,-53,-53,-128,199,-128,212,212,-116,-94,-102,-111,-112,-113,-114,-117,185,185,-115,-110,-66,-67,-91,-93,-131,-129,-130,-118,-95,-103,-107,]),'PARIZQ':([47,49,54,56,92,93,94,95,96,97,98,108,109,110,111,112,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,145,147,148,149,158,161,164,170,171,172,173,174,176,177,178,179,180,185,199,200,201,202,203,204,205,206,207,208,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,238,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,272,273,274,275,],[-31,-31,62,64,108,109,110,-77,112,113,114,126,126,126,149,126,126,126,108,126,126,-68,126,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,108,108,-128,126,108,126,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,126,126,247,-119,-120,-121,-122,-123,-124,-125,-126,-115,-110,126,-66,-67,126,126,126,-127,-127,-127,-127,-127,-127,126,-127,-127,126,-127,-127,126,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-118,-95,-103,-107,]),'CTEINT':([52,67,102,108,109,110,112,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,147,148,149,160,161,164,170,171,172,173,174,176,177,178,179,180,185,199,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,238,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,272,273,274,275,],[60,73,120,135,135,135,135,135,135,-53,135,135,-68,135,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,135,194,135,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,135,135,-115,-110,135,-66,-67,135,135,135,-127,-127,-127,-127,-127,-127,135,-127,-127,135,-127,-127,135,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-118,-95,-103,-107,]),'CORDER':([60,73,120,128,130,131,132,133,134,135,136,137,138,139,147,148,162,164,170,173,174,176,177,178,179,180,194,209,210,214,216,246,249,250,251,258,261,272,273,274,275,],[66,80,159,-68,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,198,-128,-116,-94,-102,-111,-112,-113,-114,-117,242,-115,-110,-66,-67,271,-91,-93,-131,-129,-130,-118,-95,-103,-107,]),'PARDER':([62,64,69,70,78,101,108,117,118,119,125,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,151,152,153,154,155,156,157,158,159,164,165,166,167,168,169,170,173,174,176,177,178,179,180,182,183,184,186,187,189,191,193,209,210,211,213,214,215,216,233,234,235,241,242,247,248,249,250,251,258,261,266,268,272,273,274,275,280,281,],[68,-135,76,77,-17,-135,128,-37,-40,-41,-53,-68,-128,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,181,-63,-63,-128,-128,-53,188,-53,-128,-53,192,-85,-86,-87,-88,-89,-53,-17,-128,210,-135,214,-128,216,-116,-94,-102,-111,-112,-113,-114,-117,-135,-135,-61,-65,-62,237,239,-135,-115,-110,-69,-72,-66,-70,-67,-59,-60,-64,-38,-17,272,-71,-91,-93,-131,-129,-130,-80,-135,-118,-95,-103,-107,285,-39,]),'LLAVEDER':([75,81,82,83,84,85,86,87,88,89,90,91,104,105,106,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[-135,104,105,-24,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-23,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'write':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[93,93,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'if':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[94,94,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'while':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[95,95,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'for':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[96,96,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'read':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[97,97,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'return':([75,83,84,85,86,87,88,89,90,91,104,105,128,214,216,232,240,244,264,267,269,270,276,278,279,282,284,286,288,289,],[98,98,-42,-43,-44,-45,-46,-47,-48,-49,-21,-22,-68,-66,-67,-58,-84,-51,-135,-83,-50,-52,-133,-75,-78,-73,-76,-74,-82,-79,]),'ASIGNA':([92,107,122,124,198,271,],[-53,-135,161,-57,-55,-56,]),'else':([104,105,264,],[-21,-22,277,]),'CTEFLOAT':([108,109,110,112,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,147,148,149,161,164,170,171,172,173,174,176,177,178,179,180,185,199,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,238,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,272,273,274,275,],[136,136,136,136,136,136,-53,136,136,-68,136,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,136,136,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,136,136,-115,-110,136,-66,-67,136,136,136,-127,-127,-127,-127,-127,-127,136,-127,-127,136,-127,-127,136,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-118,-95,-103,-107,]),'true':([108,109,110,112,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,147,148,149,161,164,170,171,172,173,174,176,177,178,179,180,185,199,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,238,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,272,273,274,275,],[137,137,137,137,155,137,-53,137,137,-68,137,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,137,137,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,137,137,-115,-110,137,-66,-67,137,137,137,-127,-127,-127,-127,-127,-127,137,-127,-127,137,-127,-127,137,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-118,-95,-103,-107,]),'false':([108,109,110,112,114,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,147,148,149,161,164,170,171,172,173,174,176,177,178,179,180,185,199,209,210,212,214,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,238,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,272,273,274,275,],[138,138,138,138,156,138,-53,138,138,-68,138,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,138,138,-128,-116,-127,-127,-94,-102,-111,-112,-113,-114,-117,138,138,-115,-110,138,-66,-67,138,138,138,-127,-127,-127,-127,-127,-127,138,-127,-127,138,-127,-127,138,-91,-93,-131,-96,-97,-98,-99,-100,-101,-129,-104,-105,-130,-108,-109,-118,-95,-103,-107,]),'CTESTRING':([109,114,161,185,],[142,154,197,142,]),'PUNTO':([125,145,147,158,],[163,163,163,163,]),'MULT':([125,128,129,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,175,176,177,178,179,180,196,209,210,214,216,272,],[-53,-68,-128,-130,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,230,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-118,]),'DIV':([125,128,129,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,175,176,177,178,179,180,196,209,210,214,216,272,],[-53,-68,-128,-130,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,231,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-118,]),'MAS':([125,128,129,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,174,176,177,178,179,180,196,209,210,214,216,261,272,275,],[-53,-68,-128,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,227,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-130,-118,-107,]),'MENOS':([125,128,129,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,174,176,177,178,179,180,196,209,210,214,216,261,272,275,],[-53,-68,-128,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,228,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-130,-118,-107,]),'MAYORQUE':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,220,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'MENORQUE':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,221,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'MAYORIGUAL':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,222,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'MENORIGUAL':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,223,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'EQUALS':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,224,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'DIFERENTE':([125,128,129,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,258,261,272,274,275,],[-53,-68,-128,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,225,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-129,-130,-118,-103,-107,]),'AND':([125,128,129,131,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,251,258,261,272,273,274,275,],[-53,-68,-128,172,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,-94,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-131,-129,-130,-118,-95,-103,-107,]),'OR':([125,128,129,130,131,132,133,134,135,136,137,138,139,143,144,145,147,148,155,156,157,158,164,168,170,173,174,176,177,178,179,180,196,209,210,214,216,250,251,258,261,272,273,274,275,],[-53,-68,-128,171,-92,-131,-129,-106,-128,-128,-128,-128,-128,-128,-128,-53,-53,-128,-128,-128,-128,-53,-128,-128,-116,-94,-102,-111,-112,-113,-114,-117,-128,-115,-110,-66,-67,-93,-131,-129,-130,-118,-95,-103,-107,]),'DOSPUNTOS':([128,130,131,132,133,134,135,136,137,138,139,147,148,150,164,170,173,174,176,177,178,179,180,190,209,210,214,216,249,250,251,258,261,272,273,274,275,],[-68,-90,-92,-131,-129,-106,-128,-128,-128,-128,-128,-53,-128,-80,-128,-116,-94,-102,-111,-112,-113,-114,-117,238,-115,-110,-66,-67,-91,-93,-131,-129,-130,-118,-95,-103,-107,]),'length':([163,],[201,]),'max':([163,],[202,]),'min':([163,],[203,]),'avg':([163,],[204,]),'median':([163,],[205,]),'mode':([163,],[206,]),'variance':([163,],[207,]),'stdev':([163,],[208,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'cuadGotoMain':([2,],[3,]),'auxprograma':([3,4,],[5,6,]),'varsaux':([8,11,76,77,],[10,24,99,100,]),'vars':([8,11,76,77,],[11,11,11,11,]),'empty':([8,9,10,11,16,51,64,72,75,76,77,101,103,107,143,144,166,168,182,183,193,264,268,],[12,14,17,12,17,59,70,59,82,12,12,119,59,124,186,186,213,213,186,186,119,278,119,]),'paux2':([10,16,],[15,33,]),'function':([10,16,],[16,16,]),'ftype':([10,16,],[18,18,]),'type':([13,64,101,193,268,],[25,71,71,71,71,]),'mainfunction':([14,15,],[30,32,]),'guardarTipoFunc':([19,20,21,22,23,],[35,36,37,38,39,]),'vaux':([25,58,],[40,65,]),'guardarTipoVar':([26,27,28,29,],[42,43,44,45,]),'agregaVar':([41,66,78,80,159,242,],[51,72,101,103,193,268,]),'cuadEnd':([46,48,],[53,55,]),'agregaFunc':([47,49,],[54,56,]),'nextvar':([51,72,103,],[57,79,121,]),'funcaux':([64,101,193,268,],[69,118,118,118,]),'bloque':([68,99,100,236,265,283,287,],[74,115,116,264,279,286,288,]),'bloqueaux':([75,83,],[81,106,]),'estatuto':([75,83,],[83,83,]),'asignacion':([75,83,],[84,84,]),'escritura':([75,83,],[85,85,]),'llamada':([75,83,108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,219,226,229,238,],[86,86,139,144,139,139,157,139,139,139,139,139,139,144,139,139,139,139,139,139,139,139,]),'condicion':([75,83,],[87,87,]),'whileloop':([75,83,],[88,88,]),'forloop':([75,83,],[89,89,]),'lectura':([75,83,],[90,90,]),'estReturn':([75,83,],[91,91,]),'checkID':([92,125,145,147,151,158,],[107,164,164,164,191,164,]),'migaja':([95,],[111,]),'masParam':([101,193,268,],[117,241,281,]),'asignaux':([107,],[122,]),'expresion':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,238,],[127,141,146,150,153,162,165,166,166,189,195,141,246,166,266,]),'llamada_esp':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,219,226,229,238,],[129,143,148,148,148,148,148,168,168,148,196,143,148,168,148,148,148,148,148,148,]),'andExpresion':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,238,],[130,130,130,130,130,130,130,130,130,130,130,130,130,130,249,130,]),'relopExpresion':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,238,],[131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,250,131,]),'aritExpresion':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,219,238,],[132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,251,132,]),'term':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,219,226,238,],[133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,258,133,]),'factor':([108,109,110,112,114,123,126,127,129,149,161,185,199,212,217,218,219,226,229,238,],[134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,261,134,]),'escaux':([109,185,],[140,235,]),'retAux':([114,],[152,]),'llamaux':([127,129,212,],[167,169,248,]),'pushOT':([129,135,136,137,138,139,143,144,148,155,156,157,164,168,196,],[170,176,177,178,179,180,170,180,170,178,179,180,209,170,170,]),'cuadArit':([132,251,],[173,273,]),'cuadTerm':([133,258,],[174,274,]),'cuadFactor':([134,261,],[175,275,]),'cuadEsc':([141,142,],[182,183,]),'nextexp':([143,144,182,183,],[184,187,233,234,]),'checkExpFor':([150,266,],[190,280,]),'especiales':([163,],[200,]),'nextparametro':([166,168,],[211,215,]),'pushOper':([171,172,220,221,222,223,224,225,227,228,230,231,],[217,218,252,253,254,255,256,257,259,260,262,263,]),'relopAux':([173,],[219,]),'aritAux':([174,],[226,]),'termAux':([175,],[229,]),'cuadGotof':([188,237,],[236,265,]),'cuadAsignacion':([195,197,],[243,245,]),'condicionAux':([264,],[276,]),'cuadFinIf':([276,],[282,]),'cuadGoto':([277,],[283,]),'cuadFinWhile':([279,],[284,]),'gotoFor':([285,],[287,]),'returnFor':([288,],[289,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC','programa',11,'p_programa','amrlang.py',227),
  ('programa -> program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC','programa',10,'p_programa_vacio','amrlang.py',232),
  ('cuadGotoMain -> <empty>','cuadGotoMain',0,'p_cuadGotoMain','amrlang.py',237),
  ('cuadEnd -> <empty>','cuadEnd',0,'p_cuadEnd','amrlang.py',245),
  ('auxprograma -> <empty>','auxprograma',0,'p_auxprograma','amrlang.py',254),
  ('varsaux -> vars varsaux','varsaux',2,'p_varsaux','amrlang.py',265),
  ('varsaux -> empty','varsaux',1,'p_varsaux','amrlang.py',266),
  ('paux2 -> function paux2','paux2',2,'p_paux2','amrlang.py',271),
  ('paux2 -> empty','paux2',1,'p_paux2','amrlang.py',272),
  ('vars -> var type vaux PYC','vars',4,'p_vars','amrlang.py',277),
  ('vars -> empty','vars',1,'p_vars','amrlang.py',278),
  ('vaux -> ID agregaVar nextvar','vaux',3,'p_vaux','amrlang.py',283),
  ('vaux -> ID CORIZQ CTEINT CORDER agregaVar nextvar','vaux',6,'p_vaux','amrlang.py',284),
  ('vaux -> ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar','vaux',8,'p_vaux','amrlang.py',285),
  ('nextvar -> COMA vaux','nextvar',2,'p_nextvar','amrlang.py',290),
  ('nextvar -> empty','nextvar',1,'p_nextvar','amrlang.py',291),
  ('agregaVar -> <empty>','agregaVar',0,'p_agregaVar','amrlang.py',296),
  ('guardarTipoVar -> <empty>','guardarTipoVar',0,'p_guardarTipoVar','amrlang.py',359),
  ('guardarTipoFunc -> <empty>','guardarTipoFunc',0,'p_guardarTipoFunc','amrlang.py',366),
  ('mainfunction -> func main agregaFunc PARIZQ PARDER bloque','mainfunction',6,'p_mainfunction','amrlang.py',373),
  ('bloque -> LLAVEIZQ bloqueaux LLAVEDER','bloque',3,'p_bloque','amrlang.py',378),
  ('bloque -> LLAVEIZQ empty LLAVEDER','bloque',3,'p_bloque','amrlang.py',379),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','amrlang.py',384),
  ('bloqueaux -> estatuto','bloqueaux',1,'p_bloqueaux','amrlang.py',385),
  ('type -> int guardarTipoVar','type',2,'p_type','amrlang.py',390),
  ('type -> float guardarTipoVar','type',2,'p_type','amrlang.py',391),
  ('type -> string guardarTipoVar','type',2,'p_type','amrlang.py',392),
  ('type -> bool guardarTipoVar','type',2,'p_type','amrlang.py',393),
  ('function -> ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux bloque','function',9,'p_function','amrlang.py',398),
  ('function -> ftype func ID agregaFunc PARIZQ empty PARDER varsaux bloque','function',9,'p_function','amrlang.py',399),
  ('agregaFunc -> <empty>','agregaFunc',0,'p_agregaFunc','amrlang.py',404),
  ('ftype -> int guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',415),
  ('ftype -> float guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',416),
  ('ftype -> string guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',417),
  ('ftype -> bool guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',418),
  ('ftype -> void guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',419),
  ('funcaux -> type ID agregaVar masParam','funcaux',4,'p_funcaux','amrlang.py',424),
  ('funcaux -> type ID CORIZQ CTEINT CORDER agregaVar masParam','funcaux',7,'p_funcaux','amrlang.py',425),
  ('funcaux -> type ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar masParam','funcaux',9,'p_funcaux','amrlang.py',426),
  ('masParam -> funcaux','masParam',1,'p_masParam','amrlang.py',431),
  ('masParam -> empty','masParam',1,'p_masParam','amrlang.py',432),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','amrlang.py',437),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','amrlang.py',438),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','amrlang.py',439),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','amrlang.py',440),
  ('estatuto -> whileloop','estatuto',1,'p_estatuto','amrlang.py',441),
  ('estatuto -> forloop','estatuto',1,'p_estatuto','amrlang.py',442),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','amrlang.py',443),
  ('estatuto -> estReturn','estatuto',1,'p_estatuto','amrlang.py',444),
  ('asignacion -> ID checkID asignaux ASIGNA expresion cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',449),
  ('asignacion -> ID checkID asignaux ASIGNA llamada_esp PYC','asignacion',6,'p_asignacion','amrlang.py',450),
  ('asignacion -> ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',451),
  ('checkID -> <empty>','checkID',0,'p_checkID','amrlang.py',456),
  ('cuadAsignacion -> <empty>','cuadAsignacion',0,'p_cuadAsignacion','amrlang.py',481),
  ('asignaux -> CORIZQ expresion CORDER','asignaux',3,'p_asignaux','amrlang.py',516),
  ('asignaux -> CORIZQ expresion COMA expresion CORDER','asignaux',5,'p_asignaux','amrlang.py',517),
  ('asignaux -> empty','asignaux',1,'p_asignaux','amrlang.py',518),
  ('escritura -> write PARIZQ escaux PARDER PYC','escritura',5,'p_escritura','amrlang.py',523),
  ('escaux -> expresion cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',528),
  ('escaux -> CTESTRING cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',529),
  ('escaux -> llamada_esp nextexp','escaux',2,'p_escaux','amrlang.py',530),
  ('escaux -> llamada nextexp','escaux',2,'p_escaux','amrlang.py',531),
  ('cuadEsc -> <empty>','cuadEsc',0,'p_cuadEsc','amrlang.py',536),
  ('nextexp -> COMA escaux','nextexp',2,'p_nextexp','amrlang.py',555),
  ('nextexp -> empty','nextexp',1,'p_nextexp','amrlang.py',556),
  ('llamada -> ID PARIZQ expresion llamaux PARDER','llamada',5,'p_llamada','amrlang.py',561),
  ('llamada -> ID PARIZQ llamada_esp llamaux PARDER','llamada',5,'p_llamada','amrlang.py',562),
  ('llamada -> ID PARIZQ PARDER','llamada',3,'p_llamada','amrlang.py',563),
  ('llamaux -> expresion nextparametro','llamaux',2,'p_llamaux','amrlang.py',568),
  ('llamaux -> llamada_esp nextparametro','llamaux',2,'p_llamaux','amrlang.py',569),
  ('nextparametro -> COMA llamaux','nextparametro',2,'p_nextparametro','amrlang.py',574),
  ('nextparametro -> empty','nextparametro',1,'p_nextparametro','amrlang.py',575),
  ('condicion -> if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf','condicion',8,'p_condicion','amrlang.py',580),
  ('condicionAux -> else cuadGoto bloque','condicionAux',3,'p_condicionAux','amrlang.py',585),
  ('condicionAux -> empty','condicionAux',1,'p_condicionAux','amrlang.py',586),
  ('whileloop -> while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile','whileloop',8,'p_whileloop','amrlang.py',591),
  ('migaja -> <empty>','migaja',0,'p_migaja','amrlang.py',596),
  ('cuadFinWhile -> <empty>','cuadFinWhile',0,'p_cuadFinWhile','amrlang.py',604),
  ('forloop -> for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor','forloop',11,'p_forloop','amrlang.py',619),
  ('checkExpFor -> <empty>','checkExpFor',0,'p_checkExpFor','amrlang.py',624),
  ('gotoFor -> <empty>','gotoFor',0,'p_gotoFor','amrlang.py',640),
  ('returnFor -> <empty>','returnFor',0,'p_returnFor','amrlang.py',699),
  ('lectura -> read PARIZQ ID checkID PARDER PYC','lectura',6,'p_lectura','amrlang.py',740),
  ('estReturn -> return PARIZQ retAux PARDER PYC','estReturn',5,'p_estReturn','amrlang.py',745),
  ('retAux -> expresion','retAux',1,'p_retAux','amrlang.py',750),
  ('retAux -> CTESTRING','retAux',1,'p_retAux','amrlang.py',751),
  ('retAux -> true','retAux',1,'p_retAux','amrlang.py',752),
  ('retAux -> false','retAux',1,'p_retAux','amrlang.py',753),
  ('retAux -> llamada','retAux',1,'p_retAux','amrlang.py',754),
  ('expresion -> andExpresion','expresion',1,'p_expresion','amrlang.py',759),
  ('expresion -> andExpresion OR pushOper andExpresion','expresion',4,'p_expresion','amrlang.py',760),
  ('andExpresion -> relopExpresion','andExpresion',1,'p_andExpresion','amrlang.py',765),
  ('andExpresion -> relopExpresion AND pushOper relopExpresion','andExpresion',4,'p_andExpresion','amrlang.py',766),
  ('relopExpresion -> aritExpresion cuadArit','relopExpresion',2,'p_relopExpresion','amrlang.py',771),
  ('relopExpresion -> aritExpresion cuadArit relopAux aritExpresion cuadArit','relopExpresion',5,'p_relopExpresion','amrlang.py',772),
  ('relopAux -> MAYORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',777),
  ('relopAux -> MENORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',778),
  ('relopAux -> MAYORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',779),
  ('relopAux -> MENORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',780),
  ('relopAux -> EQUALS pushOper','relopAux',2,'p_relopAux','amrlang.py',781),
  ('relopAux -> DIFERENTE pushOper','relopAux',2,'p_relopAux','amrlang.py',782),
  ('aritExpresion -> term cuadTerm','aritExpresion',2,'p_aritExpresion','amrlang.py',787),
  ('aritExpresion -> term cuadTerm aritAux term cuadTerm','aritExpresion',5,'p_aritExpresion','amrlang.py',788),
  ('aritAux -> MAS pushOper','aritAux',2,'p_aritAux','amrlang.py',793),
  ('aritAux -> MENOS pushOper','aritAux',2,'p_aritAux','amrlang.py',794),
  ('term -> factor','term',1,'p_term','amrlang.py',799),
  ('term -> factor cuadFactor termAux factor cuadFactor','term',5,'p_term','amrlang.py',800),
  ('termAux -> MULT pushOper','termAux',2,'p_termAux','amrlang.py',805),
  ('termAux -> DIV pushOper','termAux',2,'p_termAux','amrlang.py',806),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','amrlang.py',811),
  ('factor -> CTEINT pushOT','factor',2,'p_factor','amrlang.py',812),
  ('factor -> CTEFLOAT pushOT','factor',2,'p_factor','amrlang.py',813),
  ('factor -> true pushOT','factor',2,'p_factor','amrlang.py',814),
  ('factor -> false pushOT','factor',2,'p_factor','amrlang.py',815),
  ('factor -> ID checkID pushOT','factor',3,'p_factor','amrlang.py',816),
  ('factor -> llamada_esp pushOT','factor',2,'p_factor','amrlang.py',817),
  ('factor -> llamada pushOT','factor',2,'p_factor','amrlang.py',818),
  ('llamada_esp -> ID PUNTO especiales PARIZQ PARDER','llamada_esp',5,'p_llamada_esp','amrlang.py',825),
  ('especiales -> length','especiales',1,'p_especiales','amrlang.py',830),
  ('especiales -> max','especiales',1,'p_especiales','amrlang.py',831),
  ('especiales -> min','especiales',1,'p_especiales','amrlang.py',832),
  ('especiales -> avg','especiales',1,'p_especiales','amrlang.py',833),
  ('especiales -> median','especiales',1,'p_especiales','amrlang.py',834),
  ('especiales -> mode','especiales',1,'p_especiales','amrlang.py',835),
  ('especiales -> variance','especiales',1,'p_especiales','amrlang.py',836),
  ('especiales -> stdev','especiales',1,'p_especiales','amrlang.py',837),
  ('pushOper -> <empty>','pushOper',0,'p_pushOper','amrlang.py',842),
  ('pushOT -> <empty>','pushOT',0,'p_pushOT','amrlang.py',849),
  ('cuadTerm -> <empty>','cuadTerm',0,'p_cuadTerm','amrlang.py',903),
  ('cuadFactor -> <empty>','cuadFactor',0,'p_cuadFactor','amrlang.py',940),
  ('cuadArit -> <empty>','cuadArit',0,'p_cuadArit','amrlang.py',980),
  ('cuadGotof -> <empty>','cuadGotof',0,'p_cuadGotof','amrlang.py',1019),
  ('cuadFinIf -> <empty>','cuadFinIf',0,'p_cuadFinIf','amrlang.py',1040),
  ('cuadGoto -> <empty>','cuadGoto',0,'p_cuadGoto','amrlang.py',1049),
  ('empty -> <empty>','empty',0,'p_empty','amrlang.py',1067),
]
