
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNA COMA CORDER CORIZQ CTEBOOL CTEFLOAT CTEINT CTESTRING DIFERENTE DIV DOSPUNTOS EQUALS ID LLAVEDER LLAVEIZQ MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MULT OR PARDER PARIZQ PUNTO PYC avg bool else end false float for func if int length main max median min mode program read return stdev string true var variance void while write\n    programa : program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC\n    \n    programa : program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC\n    \n    cuadGotoMain :\n    \n    cuadEnd :\n    auxprograma :\n    \n    varsaux : vars varsaux\n            | empty\n    \n    paux2 : function paux2\n          | empty\n    \n    vars : var type vaux PYC\n         | empty\n    \n    vaux : ID agregaVar nextvar\n         | ID CORIZQ CTEINT CORDER agregaVar nextvar\n         | ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar\n    \n    nextvar : COMA vaux\n            | empty\n    \n    agregaVar :\n    \n    agregaPar :\n    \n    guardarTipoVar :\n    \n    guardarTipoFunc :\n    \n    mainfunction : func main agregaFunc PARIZQ PARDER fillMain bloque\n    \n    fillMain :\n    \n    bloque : LLAVEIZQ bloqueaux LLAVEDER\n           | LLAVEIZQ empty LLAVEDER\n    \n    bloqueaux : estatuto bloqueaux\n              | estatuto\n    \n    type : int guardarTipoVar\n         | float guardarTipoVar\n         | string guardarTipoVar\n         | bool guardarTipoVar\n    \n    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux agregaDir bloque cuadEndf\n             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux agregaDir bloque cuadEndf\n    \n    agregaDir :\n    \n    cuadEndf :\n    \n    agregaFunc :\n    \n    ftype : int guardarTipoFunc\n          | float guardarTipoFunc\n          | string guardarTipoFunc\n          | bool guardarTipoFunc\n          | void guardarTipoFunc\n    \n    funcaux : type ID agregaPar masParam\n            | type ID CORIZQ CTEINT CORDER agregaPar masParam\n            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaPar masParam\n    \n    masParam : COMA funcaux\n             | empty\n    \n    estatuto : asignacion\n             | escritura\n             | llamada\n             | condicion\n             | whileloop\n             | forloop\n             | lectura\n             | estReturn\n    \n    asignacion : ID checkID asignaux ASIGNA expresion cuadAsignacion PYC\n               | ID checkID asignaux ASIGNA llamada_esp PYC\n               | ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC\n    \n    checkID :\n    \n    cuadAsignacion :\n    \n    asignaux : CORIZQ expresion CORDER\n             | CORIZQ expresion COMA expresion CORDER\n             | empty\n    \n    escritura : write PARIZQ escaux PARDER PYC\n    \n    escaux : expresion cuadEsc nextexp\n           | CTESTRING cuadEsc nextexp\n           | llamada_esp nextexp\n           | llamada nextexp\n    \n    cuadEsc :\n    \n    nextexp : COMA escaux\n            | empty\n    \n    llamada : ID checkFunc cuadEra PARIZQ expresion llamaux PARDER PYC\n            | ID checkFunc cuadEra PARIZQ CTESTRING llamaux PARDER PYC\n            | ID checkFunc cuadEra PARIZQ llamada_esp llamaux PARDER PYC\n            | ID checkFunc cuadEra PARIZQ PARDER PYC\n    \n    checkFunc :\n    \n    cuadEra :\n    \n    llamaux : COMA expresion nextparametro\n            | COMA llamada_esp nextparametro\n            | COMA CTESTRING nextparametro\n            | empty\n    \n    nextparametro : llamaux\n                  | empty\n    \n    condicion : if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf\n    \n    condicionAux : else cuadGoto bloque\n                 | empty\n    \n    whileloop : while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile\n    \n    migaja :\n    \n    cuadFinWhile :\n    \n    forloop : for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor\n    \n    checkExpFor :\n    \n    gotoFor :\n    \n    returnFor :\n    \n    lectura : read PARIZQ ID checkID cuadRead PARDER PYC\n    \n    cuadRead :\n    \n    estReturn : return PARIZQ retAux PARDER PYC\n    \n    retAux : expresion\n           | CTESTRING\n           | true\n           | false\n           | llamada\n    \n    expresion : andExpresion\n              | andExpresion OR pushOper andExpresion\n    \n    andExpresion : relopExpresion\n                 | relopExpresion AND pushOper relopExpresion\n    \n    relopExpresion : aritExpresion cuadArit\n                   | aritExpresion cuadArit relopAux aritExpresion cuadArit\n    \n    relopAux : MAYORQUE pushOper \n             | MENORQUE pushOper \n             | MAYORIGUAL pushOper\n             | MENORIGUAL pushOper\n             | EQUALS pushOper\n             | DIFERENTE pushOper\n    \n    aritExpresion : term cuadTerm\n                  | term cuadTerm aritAux term cuadTerm\n    \n    aritAux : MAS pushOper\n            | MENOS pushOper\n    \n    term : factor \n         | factor cuadFactor termAux factor cuadFactor\n    \n    termAux : MULT pushOper\n            | DIV pushOper\n    \n    factor : PARIZQ guardaFondo expresion PARDER quitaFondo\n           | CTEINT pushOT\n           | CTEFLOAT pushOT\n           | true pushOT\n           | false pushOT\n           | ID checkID pushOT\n           | llamada_esp pushOT\n           | llamada pushOT\n    \n    guardaFondo :\n    \n    quitaFondo :\n    \n    llamada_esp : ID PUNTO especiales PARIZQ PARDER\n    \n    especiales : length\n               | max\n               | min\n               | avg\n               | median\n               | mode\n               | variance\n               | stdev\n    \n    pushOper :\n    \n    pushOT :\n    \n    cuadTerm :\n    \n    cuadFactor :\n    \n    cuadArit :\n    \n    cuadGotof : \n    \n    cuadFinIf :\n    \n    cuadGoto :\n    \n    empty : \n    '
    
_lr_action_items = {'program':([0,],[2,]),'$end':([1,61,63,],[0,-2,-1,]),'ID':([2,3,5,25,26,27,28,29,34,42,43,44,45,58,71,81,89,90,91,92,93,94,95,96,97,112,113,117,118,120,121,122,129,132,152,166,168,169,175,179,182,202,208,212,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,241,244,248,250,258,259,260,261,262,263,265,266,268,269,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[-3,4,7,41,-19,-19,-19,-19,49,-27,-28,-29,-30,41,77,98,98,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,139,149,149,154,161,149,-128,149,197,197,149,139,-139,-139,149,-62,149,149,149,-139,-139,-139,-139,-139,-139,149,-139,-139,149,-139,-139,149,-94,-55,197,-73,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'PYC':([4,6,7,40,41,46,48,51,53,55,57,59,65,66,72,78,79,86,111,138,140,141,142,143,144,145,146,147,149,150,151,170,174,178,181,183,184,186,187,188,189,194,197,198,199,200,204,222,243,245,250,253,254,256,257,264,267,273,278,282,283,284,285,286,287,288,295,301,302,],[-5,8,9,50,-17,-4,-4,-147,61,63,-12,-16,-15,-17,-147,-13,-17,-147,-14,-100,-102,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,208,-126,-127,-140,-104,-112,-121,-122,-123,-124,241,-57,-58,244,-58,250,-125,275,276,-73,-129,-101,-103,-143,-141,-142,294,295,301,302,-120,-130,-105,-113,-117,-70,-71,-72,]),'var':([8,11,12,50,75,76,],[13,13,-11,-10,13,13,]),'int':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-147,19,-147,-7,26,19,-6,-10,26,26,-23,-24,-34,-34,-31,-32,]),'float':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-147,20,-147,-7,27,20,-6,-10,27,27,-23,-24,-34,-34,-31,-32,]),'string':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-147,21,-147,-7,28,21,-6,-10,28,28,-23,-24,-34,-34,-31,-32,]),'bool':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-147,22,-147,-7,29,22,-6,-10,29,29,-23,-24,-34,-34,-31,-32,]),'void':([8,10,11,12,16,24,50,112,113,123,124,162,163,],[-147,23,-147,-7,23,-6,-10,-23,-24,-34,-34,-31,-32,]),'func':([8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,33,35,36,37,38,39,50,112,113,123,124,162,163,],[-147,-147,-147,-147,-7,31,31,-147,-9,34,-20,-20,-20,-20,-20,-6,-8,-36,-37,-38,-39,-40,-10,-23,-24,-34,-34,-31,-32,]),'LLAVEIZQ':([11,12,24,50,68,74,75,76,82,83,105,106,190,237,238,271,290,304,306,308,],[-147,-7,-6,-10,-22,81,-147,-147,-33,-33,81,81,-144,81,-144,81,-146,81,-90,81,]),'end':([30,32,80,112,113,],[46,48,-21,-23,-24,]),'main':([31,],[47,]),'CORIZQ':([41,77,98,115,],[52,85,-57,129,]),'COMA':([41,51,60,66,72,77,79,84,86,110,126,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,151,164,167,171,172,174,178,181,183,184,186,187,188,189,196,197,203,205,206,222,242,250,253,254,256,257,264,267,279,280,281,284,285,286,287,288,295,301,302,],[-17,58,67,-17,58,-18,-17,108,58,127,-18,-67,-67,175,175,-100,-57,-102,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,108,202,175,175,-126,-127,-140,-104,-112,-121,-122,-123,-124,-18,-57,248,248,248,-125,108,-73,-129,-101,-103,-143,-141,-142,248,248,248,-120,-130,-105,-113,-117,-70,-71,-72,]),'PARIZQ':([47,49,54,56,98,99,100,101,102,103,104,116,117,118,119,120,122,129,131,132,139,149,152,161,166,168,169,175,179,182,197,202,212,213,214,215,216,217,218,219,220,221,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,248,258,259,260,261,262,263,265,266,268,269,],[-35,-35,62,64,-74,117,118,-86,120,121,122,-75,132,132,152,132,132,132,168,-128,-74,-74,132,-74,132,132,132,132,-139,-139,-74,132,132,255,-131,-132,-133,-134,-135,-136,-137,-138,132,132,-139,-139,-139,-139,-139,-139,132,-139,-139,132,-139,-139,132,132,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,]),'CTEINT':([52,67,85,117,118,120,122,127,129,132,152,166,168,169,175,179,182,202,212,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,248,258,259,260,261,262,263,265,266,268,269,],[60,73,110,144,144,144,144,165,144,-128,144,144,144,144,144,-139,-139,144,144,144,144,-139,-139,-139,-139,-139,-139,144,-139,-139,144,-139,-139,144,144,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,]),'CORDER':([60,73,110,138,140,141,142,143,144,145,146,147,149,150,151,165,167,174,178,181,183,184,186,187,188,189,222,246,250,253,254,256,257,264,267,284,285,286,287,288,295,301,302,],[66,79,126,-100,-102,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,196,201,-126,-127,-140,-104,-112,-121,-122,-123,-124,-125,277,-73,-129,-101,-103,-143,-141,-142,-120,-130,-105,-113,-117,-70,-71,-72,]),'PARDER':([62,64,69,70,77,84,107,109,125,126,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,154,155,156,157,158,159,160,161,164,168,171,172,173,174,176,177,178,181,183,184,186,187,188,189,191,193,195,196,197,203,205,206,207,209,210,211,222,240,242,247,249,250,251,252,253,254,255,256,257,264,267,272,274,279,280,281,284,285,286,287,288,293,295,296,297,298,299,300,301,302,],[68,-147,75,76,-18,-147,-41,-45,-44,-18,170,-67,-67,-140,-140,-100,-57,-102,-143,-141,-116,-140,-140,-140,-140,190,-57,-140,-140,-57,194,-95,-96,-97,-98,-99,-57,-147,204,-147,-147,-65,-126,-69,-66,-127,-140,-104,-112,-121,-122,-123,-124,238,-93,-42,-18,-57,-147,-147,-140,253,-63,-64,-68,-125,273,-147,278,-79,-73,282,283,-129,-101,285,-103,-143,-141,-142,-89,-43,-147,-140,-147,-120,-130,-105,-113,-117,306,-70,-76,-80,-79,-77,-78,-71,-72,]),'LLAVEDER':([81,87,88,89,90,91,92,93,94,95,96,97,112,113,114,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[-147,112,113,-26,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-25,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'write':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[99,99,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'if':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[100,100,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'while':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[101,101,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'for':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[102,102,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'read':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[103,103,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'return':([81,89,90,91,92,93,94,95,96,97,112,113,208,241,244,250,270,275,276,289,291,292,294,295,301,302,303,305,307,309,310,],[104,104,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-62,-94,-55,-73,-147,-54,-56,-145,-84,-87,-92,-70,-71,-72,-82,-85,-83,-91,-88,]),'ASIGNA':([98,115,128,130,201,277,],[-57,-147,166,-61,-59,-60,]),'else':([112,113,270,],[-23,-24,290,]),'CTESTRING':([117,122,166,168,175,248,],[135,157,200,205,135,281,]),'CTEFLOAT':([117,118,120,122,129,132,152,166,168,169,175,179,182,202,212,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,248,258,259,260,261,262,263,265,266,268,269,],[145,145,145,145,145,-128,145,145,145,145,145,-139,-139,145,145,145,145,-139,-139,-139,-139,-139,-139,145,-139,-139,145,-139,-139,145,145,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,]),'true':([117,118,120,122,129,132,152,166,168,169,175,179,182,202,212,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,248,258,259,260,261,262,263,265,266,268,269,],[146,146,146,158,146,-128,146,146,146,146,146,-139,-139,146,146,146,146,-139,-139,-139,-139,-139,-139,146,-139,-139,146,-139,-139,146,146,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,]),'false':([117,118,120,122,129,132,152,166,168,169,175,179,182,202,212,223,224,225,226,227,228,229,230,231,232,233,234,235,236,239,248,258,259,260,261,262,263,265,266,268,269,],[147,147,147,159,147,-128,147,147,147,147,147,-139,-139,147,147,147,147,-139,-139,-139,-139,-139,-139,147,-139,-139,147,-139,-139,147,147,-106,-107,-108,-109,-110,-111,-114,-115,-118,-119,]),'MULT':([136,137,139,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,185,186,187,188,189,197,199,206,222,250,253,280,284,285,295,301,302,],[-140,-140,-57,-142,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,235,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-140,-120,-130,-70,-71,-72,]),'DIV':([136,137,139,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,185,186,187,188,189,197,199,206,222,250,253,280,284,285,295,301,302,],[-140,-140,-57,-142,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,236,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-140,-120,-130,-70,-71,-72,]),'MAS':([136,137,139,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,184,186,187,188,189,197,199,206,222,250,253,267,280,284,285,288,295,301,302,],[-140,-140,-57,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,232,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-142,-140,-120,-130,-117,-70,-71,-72,]),'MENOS':([136,137,139,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,184,186,187,188,189,197,199,206,222,250,253,267,280,284,285,288,295,301,302,],[-140,-140,-57,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,233,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-142,-140,-120,-130,-117,-70,-71,-72,]),'MAYORQUE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,225,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'MENORQUE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,226,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'MAYORIGUAL':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,227,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'MENORIGUAL':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,228,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'EQUALS':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,229,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'DIFERENTE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,264,267,280,284,285,287,288,295,301,302,],[-140,-140,-57,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,230,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-141,-142,-140,-120,-130,-113,-117,-70,-71,-72,]),'AND':([136,137,139,140,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,257,264,267,280,284,285,286,287,288,295,301,302,],[-140,-140,-57,182,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,-104,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-143,-141,-142,-140,-120,-130,-105,-113,-117,-70,-71,-72,]),'OR':([136,137,138,139,140,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,197,199,206,222,250,253,256,257,264,267,280,284,285,286,287,288,295,301,302,],[-140,-140,179,-57,-102,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-140,-140,-140,-57,-126,-127,-140,-104,-112,-121,-122,-123,-124,-57,-140,-140,-125,-73,-129,-103,-143,-141,-142,-140,-120,-130,-105,-113,-117,-70,-71,-72,]),'DOSPUNTOS':([138,140,141,142,143,144,145,146,147,149,150,151,153,174,178,181,183,184,186,187,188,189,192,222,250,253,254,256,257,264,267,284,285,286,287,288,295,301,302,],[-100,-102,-143,-141,-116,-140,-140,-140,-140,-57,-140,-140,-89,-126,-127,-140,-104,-112,-121,-122,-123,-124,239,-125,-73,-129,-101,-103,-143,-141,-142,-120,-130,-105,-113,-117,-70,-71,-72,]),'PUNTO':([139,149,161,197,],[180,180,180,180,]),'length':([180,],[214,]),'max':([180,],[215,]),'min':([180,],[216,]),'avg':([180,],[217,]),'median':([180,],[218,]),'mode':([180,],[219,]),'variance':([180,],[220,]),'stdev':([180,],[221,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'cuadGotoMain':([2,],[3,]),'auxprograma':([3,4,],[5,6,]),'varsaux':([8,11,75,76,],[10,24,82,83,]),'vars':([8,11,75,76,],[11,11,11,11,]),'empty':([8,9,10,11,16,51,64,72,75,76,81,84,86,115,136,137,164,171,172,203,205,206,242,270,279,280,281,],[12,14,17,12,17,59,70,59,12,12,88,109,59,130,176,176,109,176,176,249,249,249,109,291,298,298,298,]),'paux2':([10,16,],[15,33,]),'function':([10,16,],[16,16,]),'ftype':([10,16,],[18,18,]),'type':([13,64,108,],[25,71,71,]),'mainfunction':([14,15,],[30,32,]),'guardarTipoFunc':([19,20,21,22,23,],[35,36,37,38,39,]),'vaux':([25,58,],[40,65,]),'guardarTipoVar':([26,27,28,29,],[42,43,44,45,]),'agregaVar':([41,66,79,],[51,72,86,]),'cuadEnd':([46,48,],[53,55,]),'agregaFunc':([47,49,],[54,56,]),'nextvar':([51,72,86,],[57,78,111,]),'funcaux':([64,108,],[69,125,]),'fillMain':([68,],[74,]),'bloque':([74,105,106,237,271,304,308,],[80,123,124,270,292,307,309,]),'agregaPar':([77,126,196,],[84,164,242,]),'bloqueaux':([81,89,],[87,114,]),'estatuto':([81,89,],[89,89,]),'asignacion':([81,89,],[90,90,]),'escritura':([81,89,],[91,91,]),'llamada':([81,89,117,118,120,122,129,152,166,168,169,175,202,212,223,224,231,234,239,248,],[92,92,137,151,151,160,151,151,151,151,151,137,151,151,151,151,151,151,151,151,]),'condicion':([81,89,],[93,93,]),'whileloop':([81,89,],[94,94,]),'forloop':([81,89,],[95,95,]),'lectura':([81,89,],[96,96,]),'estReturn':([81,89,],[97,97,]),'agregaDir':([82,83,],[105,106,]),'masParam':([84,164,242,],[107,195,274,]),'checkID':([98,139,149,154,161,197,],[115,181,181,193,181,181,]),'checkFunc':([98,139,149,161,197,],[116,116,116,116,116,]),'migaja':([101,],[119,]),'asignaux':([115,],[128,]),'cuadEra':([116,],[131,]),'escaux':([117,175,],[133,211,]),'expresion':([117,118,120,122,129,152,166,168,169,175,202,239,248,],[134,148,153,156,167,191,198,203,207,134,246,272,279,]),'llamada_esp':([117,118,120,122,129,152,166,168,169,175,202,212,223,224,231,234,239,248,],[136,150,150,150,150,150,199,206,150,136,150,150,150,150,150,150,150,280,]),'andExpresion':([117,118,120,122,129,152,166,168,169,175,202,212,239,248,],[138,138,138,138,138,138,138,138,138,138,138,254,138,138,]),'relopExpresion':([117,118,120,122,129,152,166,168,169,175,202,212,223,239,248,],[140,140,140,140,140,140,140,140,140,140,140,140,256,140,140,]),'aritExpresion':([117,118,120,122,129,152,166,168,169,175,202,212,223,224,239,248,],[141,141,141,141,141,141,141,141,141,141,141,141,141,257,141,141,]),'term':([117,118,120,122,129,152,166,168,169,175,202,212,223,224,231,239,248,],[142,142,142,142,142,142,142,142,142,142,142,142,142,142,264,142,142,]),'factor':([117,118,120,122,129,152,166,168,169,175,202,212,223,224,231,234,239,248,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,267,143,143,]),'retAux':([122,],[155,]),'cuadEndf':([123,124,],[162,163,]),'guardaFondo':([132,],[169,]),'cuadEsc':([134,135,],[171,172,]),'nextexp':([136,137,171,172,],[173,177,209,210,]),'pushOT':([136,137,144,145,146,147,150,151,158,159,160,181,199,206,280,],[174,178,186,187,188,189,174,178,188,189,178,222,174,174,174,]),'cuadArit':([141,257,],[183,286,]),'cuadTerm':([142,264,],[184,287,]),'cuadFactor':([143,267,],[185,288,]),'checkExpFor':([153,272,],[192,293,]),'pushOper':([179,182,225,226,227,228,229,230,232,233,235,236,],[212,223,258,259,260,261,262,263,265,266,268,269,]),'especiales':([180,],[213,]),'relopAux':([183,],[224,]),'aritAux':([184,],[231,]),'termAux':([185,],[234,]),'cuadGotof':([190,238,],[237,271,]),'cuadRead':([193,],[240,]),'cuadAsignacion':([198,200,],[243,245,]),'llamaux':([203,205,206,279,280,281,],[247,251,252,297,297,297,]),'quitaFondo':([253,],[284,]),'condicionAux':([270,],[289,]),'nextparametro':([279,280,281,],[296,299,300,]),'cuadFinIf':([289,],[303,]),'cuadGoto':([290,],[304,]),'cuadFinWhile':([292,],[305,]),'gotoFor':([306,],[308,]),'returnFor':([309,],[310,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC','programa',11,'p_programa','amrlang.py',240),
  ('programa -> program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC','programa',10,'p_programa_vacio','amrlang.py',245),
  ('cuadGotoMain -> <empty>','cuadGotoMain',0,'p_cuadGotoMain','amrlang.py',250),
  ('cuadEnd -> <empty>','cuadEnd',0,'p_cuadEnd','amrlang.py',260),
  ('auxprograma -> <empty>','auxprograma',0,'p_auxprograma','amrlang.py',269),
  ('varsaux -> vars varsaux','varsaux',2,'p_varsaux','amrlang.py',282),
  ('varsaux -> empty','varsaux',1,'p_varsaux','amrlang.py',283),
  ('paux2 -> function paux2','paux2',2,'p_paux2','amrlang.py',288),
  ('paux2 -> empty','paux2',1,'p_paux2','amrlang.py',289),
  ('vars -> var type vaux PYC','vars',4,'p_vars','amrlang.py',294),
  ('vars -> empty','vars',1,'p_vars','amrlang.py',295),
  ('vaux -> ID agregaVar nextvar','vaux',3,'p_vaux','amrlang.py',300),
  ('vaux -> ID CORIZQ CTEINT CORDER agregaVar nextvar','vaux',6,'p_vaux','amrlang.py',301),
  ('vaux -> ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar','vaux',8,'p_vaux','amrlang.py',302),
  ('nextvar -> COMA vaux','nextvar',2,'p_nextvar','amrlang.py',307),
  ('nextvar -> empty','nextvar',1,'p_nextvar','amrlang.py',308),
  ('agregaVar -> <empty>','agregaVar',0,'p_agregaVar','amrlang.py',313),
  ('agregaPar -> <empty>','agregaPar',0,'p_agregaPar','amrlang.py',384),
  ('guardarTipoVar -> <empty>','guardarTipoVar',0,'p_guardarTipoVar','amrlang.py',439),
  ('guardarTipoFunc -> <empty>','guardarTipoFunc',0,'p_guardarTipoFunc','amrlang.py',446),
  ('mainfunction -> func main agregaFunc PARIZQ PARDER fillMain bloque','mainfunction',7,'p_mainfunction','amrlang.py',453),
  ('fillMain -> <empty>','fillMain',0,'p_fillMain','amrlang.py',458),
  ('bloque -> LLAVEIZQ bloqueaux LLAVEDER','bloque',3,'p_bloque','amrlang.py',464),
  ('bloque -> LLAVEIZQ empty LLAVEDER','bloque',3,'p_bloque','amrlang.py',465),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','amrlang.py',470),
  ('bloqueaux -> estatuto','bloqueaux',1,'p_bloqueaux','amrlang.py',471),
  ('type -> int guardarTipoVar','type',2,'p_type','amrlang.py',476),
  ('type -> float guardarTipoVar','type',2,'p_type','amrlang.py',477),
  ('type -> string guardarTipoVar','type',2,'p_type','amrlang.py',478),
  ('type -> bool guardarTipoVar','type',2,'p_type','amrlang.py',479),
  ('function -> ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux agregaDir bloque cuadEndf','function',11,'p_function','amrlang.py',484),
  ('function -> ftype func ID agregaFunc PARIZQ empty PARDER varsaux agregaDir bloque cuadEndf','function',11,'p_function','amrlang.py',485),
  ('agregaDir -> <empty>','agregaDir',0,'p_agregaDir','amrlang.py',490),
  ('cuadEndf -> <empty>','cuadEndf',0,'p_cuadEndf','amrlang.py',496),
  ('agregaFunc -> <empty>','agregaFunc',0,'p_agregaFunc','amrlang.py',506),
  ('ftype -> int guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',524),
  ('ftype -> float guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',525),
  ('ftype -> string guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',526),
  ('ftype -> bool guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',527),
  ('ftype -> void guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',528),
  ('funcaux -> type ID agregaPar masParam','funcaux',4,'p_funcaux','amrlang.py',533),
  ('funcaux -> type ID CORIZQ CTEINT CORDER agregaPar masParam','funcaux',7,'p_funcaux','amrlang.py',534),
  ('funcaux -> type ID CORIZQ CTEINT COMA CTEINT CORDER agregaPar masParam','funcaux',9,'p_funcaux','amrlang.py',535),
  ('masParam -> COMA funcaux','masParam',2,'p_masParam','amrlang.py',540),
  ('masParam -> empty','masParam',1,'p_masParam','amrlang.py',541),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','amrlang.py',546),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','amrlang.py',547),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','amrlang.py',548),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','amrlang.py',549),
  ('estatuto -> whileloop','estatuto',1,'p_estatuto','amrlang.py',550),
  ('estatuto -> forloop','estatuto',1,'p_estatuto','amrlang.py',551),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','amrlang.py',552),
  ('estatuto -> estReturn','estatuto',1,'p_estatuto','amrlang.py',553),
  ('asignacion -> ID checkID asignaux ASIGNA expresion cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',558),
  ('asignacion -> ID checkID asignaux ASIGNA llamada_esp PYC','asignacion',6,'p_asignacion','amrlang.py',559),
  ('asignacion -> ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',560),
  ('checkID -> <empty>','checkID',0,'p_checkID','amrlang.py',565),
  ('cuadAsignacion -> <empty>','cuadAsignacion',0,'p_cuadAsignacion','amrlang.py',590),
  ('asignaux -> CORIZQ expresion CORDER','asignaux',3,'p_asignaux','amrlang.py',630),
  ('asignaux -> CORIZQ expresion COMA expresion CORDER','asignaux',5,'p_asignaux','amrlang.py',631),
  ('asignaux -> empty','asignaux',1,'p_asignaux','amrlang.py',632),
  ('escritura -> write PARIZQ escaux PARDER PYC','escritura',5,'p_escritura','amrlang.py',637),
  ('escaux -> expresion cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',642),
  ('escaux -> CTESTRING cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',643),
  ('escaux -> llamada_esp nextexp','escaux',2,'p_escaux','amrlang.py',644),
  ('escaux -> llamada nextexp','escaux',2,'p_escaux','amrlang.py',645),
  ('cuadEsc -> <empty>','cuadEsc',0,'p_cuadEsc','amrlang.py',650),
  ('nextexp -> COMA escaux','nextexp',2,'p_nextexp','amrlang.py',678),
  ('nextexp -> empty','nextexp',1,'p_nextexp','amrlang.py',679),
  ('llamada -> ID checkFunc cuadEra PARIZQ expresion llamaux PARDER PYC','llamada',8,'p_llamada','amrlang.py',684),
  ('llamada -> ID checkFunc cuadEra PARIZQ CTESTRING llamaux PARDER PYC','llamada',8,'p_llamada','amrlang.py',685),
  ('llamada -> ID checkFunc cuadEra PARIZQ llamada_esp llamaux PARDER PYC','llamada',8,'p_llamada','amrlang.py',686),
  ('llamada -> ID checkFunc cuadEra PARIZQ PARDER PYC','llamada',6,'p_llamada','amrlang.py',687),
  ('checkFunc -> <empty>','checkFunc',0,'p_checkFunc','amrlang.py',692),
  ('cuadEra -> <empty>','cuadEra',0,'p_cuadEra','amrlang.py',703),
  ('llamaux -> COMA expresion nextparametro','llamaux',3,'p_llamaux','amrlang.py',711),
  ('llamaux -> COMA llamada_esp nextparametro','llamaux',3,'p_llamaux','amrlang.py',712),
  ('llamaux -> COMA CTESTRING nextparametro','llamaux',3,'p_llamaux','amrlang.py',713),
  ('llamaux -> empty','llamaux',1,'p_llamaux','amrlang.py',714),
  ('nextparametro -> llamaux','nextparametro',1,'p_nextparametro','amrlang.py',719),
  ('nextparametro -> empty','nextparametro',1,'p_nextparametro','amrlang.py',720),
  ('condicion -> if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf','condicion',8,'p_condicion','amrlang.py',725),
  ('condicionAux -> else cuadGoto bloque','condicionAux',3,'p_condicionAux','amrlang.py',730),
  ('condicionAux -> empty','condicionAux',1,'p_condicionAux','amrlang.py',731),
  ('whileloop -> while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile','whileloop',8,'p_whileloop','amrlang.py',736),
  ('migaja -> <empty>','migaja',0,'p_migaja','amrlang.py',741),
  ('cuadFinWhile -> <empty>','cuadFinWhile',0,'p_cuadFinWhile','amrlang.py',749),
  ('forloop -> for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor','forloop',11,'p_forloop','amrlang.py',764),
  ('checkExpFor -> <empty>','checkExpFor',0,'p_checkExpFor','amrlang.py',769),
  ('gotoFor -> <empty>','gotoFor',0,'p_gotoFor','amrlang.py',785),
  ('returnFor -> <empty>','returnFor',0,'p_returnFor','amrlang.py',847),
  ('lectura -> read PARIZQ ID checkID cuadRead PARDER PYC','lectura',7,'p_lectura','amrlang.py',888),
  ('cuadRead -> <empty>','cuadRead',0,'p_cuadRead','amrlang.py',893),
  ('estReturn -> return PARIZQ retAux PARDER PYC','estReturn',5,'p_estReturn','amrlang.py',905),
  ('retAux -> expresion','retAux',1,'p_retAux','amrlang.py',910),
  ('retAux -> CTESTRING','retAux',1,'p_retAux','amrlang.py',911),
  ('retAux -> true','retAux',1,'p_retAux','amrlang.py',912),
  ('retAux -> false','retAux',1,'p_retAux','amrlang.py',913),
  ('retAux -> llamada','retAux',1,'p_retAux','amrlang.py',914),
  ('expresion -> andExpresion','expresion',1,'p_expresion','amrlang.py',919),
  ('expresion -> andExpresion OR pushOper andExpresion','expresion',4,'p_expresion','amrlang.py',920),
  ('andExpresion -> relopExpresion','andExpresion',1,'p_andExpresion','amrlang.py',925),
  ('andExpresion -> relopExpresion AND pushOper relopExpresion','andExpresion',4,'p_andExpresion','amrlang.py',926),
  ('relopExpresion -> aritExpresion cuadArit','relopExpresion',2,'p_relopExpresion','amrlang.py',931),
  ('relopExpresion -> aritExpresion cuadArit relopAux aritExpresion cuadArit','relopExpresion',5,'p_relopExpresion','amrlang.py',932),
  ('relopAux -> MAYORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',937),
  ('relopAux -> MENORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',938),
  ('relopAux -> MAYORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',939),
  ('relopAux -> MENORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',940),
  ('relopAux -> EQUALS pushOper','relopAux',2,'p_relopAux','amrlang.py',941),
  ('relopAux -> DIFERENTE pushOper','relopAux',2,'p_relopAux','amrlang.py',942),
  ('aritExpresion -> term cuadTerm','aritExpresion',2,'p_aritExpresion','amrlang.py',947),
  ('aritExpresion -> term cuadTerm aritAux term cuadTerm','aritExpresion',5,'p_aritExpresion','amrlang.py',948),
  ('aritAux -> MAS pushOper','aritAux',2,'p_aritAux','amrlang.py',953),
  ('aritAux -> MENOS pushOper','aritAux',2,'p_aritAux','amrlang.py',954),
  ('term -> factor','term',1,'p_term','amrlang.py',959),
  ('term -> factor cuadFactor termAux factor cuadFactor','term',5,'p_term','amrlang.py',960),
  ('termAux -> MULT pushOper','termAux',2,'p_termAux','amrlang.py',965),
  ('termAux -> DIV pushOper','termAux',2,'p_termAux','amrlang.py',966),
  ('factor -> PARIZQ guardaFondo expresion PARDER quitaFondo','factor',5,'p_factor','amrlang.py',971),
  ('factor -> CTEINT pushOT','factor',2,'p_factor','amrlang.py',972),
  ('factor -> CTEFLOAT pushOT','factor',2,'p_factor','amrlang.py',973),
  ('factor -> true pushOT','factor',2,'p_factor','amrlang.py',974),
  ('factor -> false pushOT','factor',2,'p_factor','amrlang.py',975),
  ('factor -> ID checkID pushOT','factor',3,'p_factor','amrlang.py',976),
  ('factor -> llamada_esp pushOT','factor',2,'p_factor','amrlang.py',977),
  ('factor -> llamada pushOT','factor',2,'p_factor','amrlang.py',978),
  ('guardaFondo -> <empty>','guardaFondo',0,'p_guardaFondo','amrlang.py',985),
  ('quitaFondo -> <empty>','quitaFondo',0,'p_quitaFondo','amrlang.py',992),
  ('llamada_esp -> ID PUNTO especiales PARIZQ PARDER','llamada_esp',5,'p_llamada_esp','amrlang.py',1000),
  ('especiales -> length','especiales',1,'p_especiales','amrlang.py',1005),
  ('especiales -> max','especiales',1,'p_especiales','amrlang.py',1006),
  ('especiales -> min','especiales',1,'p_especiales','amrlang.py',1007),
  ('especiales -> avg','especiales',1,'p_especiales','amrlang.py',1008),
  ('especiales -> median','especiales',1,'p_especiales','amrlang.py',1009),
  ('especiales -> mode','especiales',1,'p_especiales','amrlang.py',1010),
  ('especiales -> variance','especiales',1,'p_especiales','amrlang.py',1011),
  ('especiales -> stdev','especiales',1,'p_especiales','amrlang.py',1012),
  ('pushOper -> <empty>','pushOper',0,'p_pushOper','amrlang.py',1017),
  ('pushOT -> <empty>','pushOT',0,'p_pushOT','amrlang.py',1024),
  ('cuadTerm -> <empty>','cuadTerm',0,'p_cuadTerm','amrlang.py',1081),
  ('cuadFactor -> <empty>','cuadFactor',0,'p_cuadFactor','amrlang.py',1131),
  ('cuadArit -> <empty>','cuadArit',0,'p_cuadArit','amrlang.py',1182),
  ('cuadGotof -> <empty>','cuadGotof',0,'p_cuadGotof','amrlang.py',1221),
  ('cuadFinIf -> <empty>','cuadFinIf',0,'p_cuadFinIf','amrlang.py',1242),
  ('cuadGoto -> <empty>','cuadGoto',0,'p_cuadGoto','amrlang.py',1251),
  ('empty -> <empty>','empty',0,'p_empty','amrlang.py',1269),
]
