
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNA COMA CORDER CORIZQ CTEBOOL CTEFLOAT CTEINT CTESTRING DIFERENTE DIV DOSPUNTOS EQUALS ID LLAVEDER LLAVEIZQ MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MULT OR PARDER PARIZQ PUNTO PYC avg bool else end false float for func if int length main max median min mode program read return stdev string true var variance void while write\n    programa : program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC\n    \n    programa : program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC\n    \n    cuadGotoMain :\n    \n    cuadEnd :\n    auxprograma :\n    \n    varsaux : vars varsaux\n            | empty\n    \n    paux2 : function paux2\n          | empty\n    \n    vars : var type vaux PYC\n         | empty\n    \n    vaux : ID agregaVar nextvar\n         | ID CORIZQ CTEINT CORDER agregaVar nextvar\n         | ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar\n    \n    nextvar : COMA vaux\n            | empty\n    \n    agregaVar :\n    \n    agregaPar :\n    \n    guardarTipoVar :\n    \n    guardarTipoFunc :\n    \n    mainfunction : func main agregaFunc PARIZQ PARDER fillMain bloque\n    \n    fillMain :\n    \n    bloque : LLAVEIZQ bloqueaux LLAVEDER\n           | LLAVEIZQ empty LLAVEDER\n    \n    bloqueaux : estatuto bloqueaux\n              | estatuto\n    \n    type : int guardarTipoVar\n         | float guardarTipoVar\n         | string guardarTipoVar\n         | bool guardarTipoVar\n    \n    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux agregaDir bloque cuadEndf\n             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux agregaDir bloque cuadEndf\n    \n    agregaDir :\n    \n    cuadEndf :\n    \n    agregaFunc :\n    \n    ftype : int guardarTipoFunc\n          | float guardarTipoFunc\n          | string guardarTipoFunc\n          | bool guardarTipoFunc\n          | void guardarTipoFunc\n    \n    funcaux : type ID agregaPar masParam\n            | type ID CORIZQ CTEINT CORDER agregaPar masParam\n            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaPar masParam\n    \n    masParam : COMA funcaux\n             | empty\n    \n    estatuto : asignacion\n             | escritura\n             | llamada\n             | condicion\n             | whileloop\n             | forloop\n             | lectura\n             | estReturn\n    \n    asignacion : ID checkID asignaux ASIGNA expresion cuadAsignacion PYC\n               | ID checkID asignaux ASIGNA llamada_esp PYC\n               | ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC\n    \n    aaa :\n    \n    bbb :\n    \n    ccc :\n    \n    checkID :\n    \n    cuadAsignacion :\n    \n    asignaux : CORIZQ expresion CORDER\n             | CORIZQ expresion COMA expresion CORDER\n             | empty\n    \n    escritura : write PARIZQ escaux PARDER PYC\n    \n    escaux : expresion cuadEsc nextexp\n           | CTESTRING cuadEsc nextexp\n           | llamada_esp nextexp\n           | llamada nextexp\n    \n    cuadEsc :\n    \n    nextexp : COMA escaux\n            | empty\n    \n    llamada : ID checkFunc cuadEra PARIZQ guardaFondo llamaux verPars PARDER cuadGoSub quitaFondo PYC\n            | ID checkFunc cuadEra PARIZQ PARDER PYC\n    \n    pycopc : PYC\n           | empty\n    \n    llamaux : expresion cuadPar nextparametro\n            | llamada_esp cuadPar nextparametro\n            | CTESTRING cuadPar nextparametro\n    \n    nextparametro : COMA llamaux\n                  | empty\n    \n    checkFunc :\n    \n    cuadEra :\n    \n    cuadPar :\n    \n    verPars :\n    \n    cuadGoSub :\n    \n    condicion : if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf\n    \n    condicionAux : else cuadGoto bloque\n                 | empty\n    \n    whileloop : while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile\n    \n    migaja :\n    \n    cuadFinWhile :\n    \n    forloop : for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor\n    \n    checkExpFor :\n    \n    gotoFor :\n    \n    returnFor :\n    \n    lectura : read PARIZQ ID checkID cuadRead PARDER PYC\n    \n    cuadRead :\n    \n    estReturn : return PARIZQ retAux PARDER PYC\n    \n    retAux : expresion cuadRet\n           | CTESTRING cuadRet\n           | true cuadRet\n           | false cuadRet\n           | llamada cuadRet\n    \n    cuadRet :\n    \n    expresion : andExpresion\n              | andExpresion OR pushOper andExpresion\n    \n    andExpresion : relopExpresion\n                 | relopExpresion AND pushOper relopExpresion\n    \n    relopExpresion : aritExpresion cuadArit\n                   | aritExpresion cuadArit relopAux aritExpresion cuadArit\n    \n    relopAux : MAYORQUE pushOper \n             | MENORQUE pushOper \n             | MAYORIGUAL pushOper\n             | MENORIGUAL pushOper\n             | EQUALS pushOper\n             | DIFERENTE pushOper\n    \n    aritExpresion : term cuadTerm\n                  | term cuadTerm aritAux term cuadTerm\n    \n    aritAux : MAS pushOper\n            | MENOS pushOper\n    \n    term : factor \n         | factor cuadFactor termAux factor cuadFactor\n    \n    termAux : MULT pushOper\n            | DIV pushOper\n    \n    factor : PARIZQ guardaFondo expresion PARDER quitaFondo\n           | CTEINT pushOT\n           | CTEFLOAT pushOT\n           | true pushOT\n           | false pushOT\n           | ID checkID pushOT\n           | llamada_esp pushOT\n           | llamada pushOTLlam\n    \n    guardaFondo :\n    \n    quitaFondo :\n    \n    llamada_esp : ID PUNTO especiales PARIZQ PARDER\n    \n    especiales : length\n               | max\n               | min\n               | avg\n               | median\n               | mode\n               | variance\n               | stdev\n    \n    pushOper :\n    \n    pushOT :\n    \n    pushOTLlam :\n    \n    cuadTerm :\n    \n    cuadFactor :\n    \n    cuadArit :\n    \n    cuadGotof : \n    \n    cuadFinIf :\n    \n    cuadGoto :\n    \n    empty : \n    '
    
_lr_action_items = {'program':([0,],[2,]),'$end':([1,61,63,],[0,-2,-1,]),'ID':([2,3,5,25,26,27,28,29,34,42,43,44,45,58,71,81,89,90,91,92,93,94,95,96,97,112,113,117,118,120,121,122,129,132,152,166,168,169,175,179,182,207,208,211,215,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,244,247,254,260,261,262,263,264,265,267,268,270,271,272,277,278,289,291,292,294,297,301,303,307,310,311,312,],[-3,4,7,41,-19,-19,-19,-19,49,-27,-28,-29,-30,41,77,98,98,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,139,149,149,154,161,149,-134,149,202,-134,149,139,-145,-145,149,202,-65,149,149,149,-145,-145,-145,-145,-145,-145,149,-145,-145,149,-145,-145,149,-99,-55,-74,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,-154,-54,-56,-152,-89,-92,-97,202,-87,-90,-88,-96,-73,-93,]),'PYC':([4,6,7,40,41,46,48,51,53,55,57,59,65,66,72,78,79,86,111,138,140,141,142,143,144,145,146,147,149,150,151,170,174,178,181,183,184,186,187,188,189,194,202,203,204,205,209,225,246,248,254,255,256,258,259,266,269,275,284,285,286,287,288,295,305,309,311,],[-5,8,9,50,-17,-4,-4,-154,61,63,-12,-16,-15,-17,-154,-13,-17,-154,-14,-106,-108,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,211,-132,-133,-146,-110,-118,-127,-128,-129,-130,244,-60,-61,247,-61,254,-131,277,278,-74,-135,-107,-109,-150,-148,-149,294,-126,-136,-111,-119,-123,-86,-135,311,-73,]),'var':([8,11,12,50,75,76,],[13,13,-11,-10,13,13,]),'int':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-154,19,-154,-7,26,19,-6,-10,26,26,-23,-24,-34,-34,-31,-32,]),'float':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-154,20,-154,-7,27,20,-6,-10,27,27,-23,-24,-34,-34,-31,-32,]),'string':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-154,21,-154,-7,28,21,-6,-10,28,28,-23,-24,-34,-34,-31,-32,]),'bool':([8,10,11,12,13,16,24,50,64,108,112,113,123,124,162,163,],[-154,22,-154,-7,29,22,-6,-10,29,29,-23,-24,-34,-34,-31,-32,]),'void':([8,10,11,12,16,24,50,112,113,123,124,162,163,],[-154,23,-154,-7,23,-6,-10,-23,-24,-34,-34,-31,-32,]),'func':([8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,33,35,36,37,38,39,50,112,113,123,124,162,163,],[-154,-154,-154,-154,-7,31,31,-154,-9,34,-20,-20,-20,-20,-20,-6,-8,-36,-37,-38,-39,-40,-10,-23,-24,-34,-34,-31,-32,]),'LLAVEIZQ':([11,12,24,50,68,74,75,76,82,83,105,106,190,240,241,273,290,302,304,308,],[-154,-7,-6,-10,-22,81,-154,-154,-33,-33,81,81,-151,81,-151,81,-153,81,-95,81,]),'end':([30,32,80,112,113,],[46,48,-21,-23,-24,]),'main':([31,],[47,]),'CORIZQ':([41,77,98,115,],[52,85,-60,129,]),'COMA':([41,51,60,66,72,77,79,84,86,110,126,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,151,164,167,171,172,174,178,181,183,184,186,187,188,189,201,202,225,245,251,252,253,254,255,256,258,259,266,269,281,282,283,284,285,286,287,288,311,],[-17,58,67,-17,58,-18,-17,108,58,127,-18,-70,-70,175,175,-106,-60,-108,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,108,207,175,175,-132,-133,-146,-110,-118,-127,-128,-129,-130,-18,-60,-131,108,-84,-84,-84,-74,-135,-107,-109,-150,-148,-149,297,297,297,-126,-136,-111,-119,-123,-73,]),'PARIZQ':([47,49,54,56,98,99,100,101,102,103,104,116,117,118,119,120,122,129,131,132,139,149,152,161,166,168,169,175,179,182,202,207,208,215,216,217,218,219,220,221,222,223,224,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,260,261,262,263,264,265,267,268,270,271,297,],[-35,-35,62,64,-82,117,118,-91,120,121,122,-83,132,132,152,132,132,132,168,-134,-82,-82,132,-82,132,-134,132,132,-145,-145,-82,132,132,132,257,-137,-138,-139,-140,-141,-142,-143,-144,132,132,-145,-145,-145,-145,-145,-145,132,-145,-145,132,-145,-145,132,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,132,]),'CTEINT':([52,67,85,117,118,120,122,127,129,132,152,166,168,169,175,179,182,207,208,215,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,260,261,262,263,264,265,267,268,270,271,297,],[60,73,110,144,144,144,144,165,144,-134,144,144,-134,144,144,-145,-145,144,144,144,144,144,-145,-145,-145,-145,-145,-145,144,-145,-145,144,-145,-145,144,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,144,]),'CORDER':([60,73,110,138,140,141,142,143,144,145,146,147,149,150,151,165,167,174,178,181,183,184,186,187,188,189,225,249,254,255,256,258,259,266,269,284,285,286,287,288,311,],[66,79,126,-106,-108,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,201,206,-132,-133,-146,-110,-118,-127,-128,-129,-130,-131,279,-74,-135,-107,-109,-150,-148,-149,-126,-136,-111,-119,-123,-73,]),'PARDER':([62,64,69,70,77,84,107,109,125,126,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,154,155,156,157,158,159,160,161,164,168,171,172,173,174,176,177,178,181,183,184,186,187,188,189,191,193,195,196,197,198,199,200,201,202,210,212,213,214,225,243,245,250,251,252,253,254,255,256,257,258,259,266,269,274,276,280,281,282,283,284,285,286,287,288,293,296,298,299,300,306,311,],[68,-154,75,76,-18,-154,-41,-45,-44,-18,170,-70,-70,-146,-147,-106,-60,-108,-150,-148,-122,-146,-146,-146,-146,190,-60,-146,-147,-60,194,-105,-105,-105,-105,-105,-60,-154,209,-154,-154,-68,-132,-72,-69,-133,-146,-110,-118,-127,-128,-129,-130,241,-98,-100,-101,-102,-103,-104,-42,-18,-60,255,-66,-67,-71,-131,275,-154,-85,-84,-84,-84,-74,-135,-107,285,-109,-150,-148,-149,-94,-43,295,-154,-154,-154,-126,-136,-111,-119,-123,304,-77,-81,-78,-79,-80,-73,]),'LLAVEDER':([81,87,88,89,90,91,92,93,94,95,96,97,112,113,114,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[-154,112,113,-26,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-25,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'write':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[99,99,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'if':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[100,100,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'while':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[101,101,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'for':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[102,102,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'read':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[103,103,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'return':([81,89,90,91,92,93,94,95,96,97,112,113,211,244,247,254,272,277,278,289,291,292,294,301,303,307,310,311,312,],[104,104,-46,-47,-48,-49,-50,-51,-52,-53,-23,-24,-65,-99,-55,-74,-154,-54,-56,-152,-89,-92,-97,-87,-90,-88,-96,-73,-93,]),'ASIGNA':([98,115,128,130,206,279,],[-60,-154,166,-64,-62,-63,]),'else':([112,113,272,],[-23,-24,290,]),'CTESTRING':([117,122,166,168,175,208,297,],[135,157,205,-134,135,253,253,]),'CTEFLOAT':([117,118,120,122,129,132,152,166,168,169,175,179,182,207,208,215,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,260,261,262,263,264,265,267,268,270,271,297,],[145,145,145,145,145,-134,145,145,-134,145,145,-145,-145,145,145,145,145,145,-145,-145,-145,-145,-145,-145,145,-145,-145,145,-145,-145,145,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,145,]),'true':([117,118,120,122,129,132,152,166,168,169,175,179,182,207,208,215,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,260,261,262,263,264,265,267,268,270,271,297,],[146,146,146,158,146,-134,146,146,-134,146,146,-145,-145,146,146,146,146,146,-145,-145,-145,-145,-145,-145,146,-145,-145,146,-145,-145,146,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,146,]),'false':([117,118,120,122,129,132,152,166,168,169,175,179,182,207,208,215,226,227,228,229,230,231,232,233,234,235,236,237,238,239,242,260,261,262,263,264,265,267,268,270,271,297,],[147,147,147,159,147,-134,147,147,-134,147,147,-145,-145,147,147,147,147,147,-145,-145,-145,-145,-145,-145,147,-145,-145,147,-145,-145,147,-112,-113,-114,-115,-116,-117,-120,-121,-124,-125,147,]),'MULT':([136,137,139,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,185,186,187,188,189,202,204,225,252,254,255,284,285,311,],[-146,-147,-60,-149,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,238,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-126,-136,-73,]),'DIV':([136,137,139,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,185,186,187,188,189,202,204,225,252,254,255,284,285,311,],[-146,-147,-60,-149,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,239,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-126,-136,-73,]),'MAS':([136,137,139,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,184,186,187,188,189,202,204,225,252,254,255,269,284,285,288,311,],[-146,-147,-60,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,235,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-149,-126,-136,-123,-73,]),'MENOS':([136,137,139,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,184,186,187,188,189,202,204,225,252,254,255,269,284,285,288,311,],[-146,-147,-60,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,236,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-149,-126,-136,-123,-73,]),'MAYORQUE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,228,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'MENORQUE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,229,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'MAYORIGUAL':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,230,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'MENORIGUAL':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,231,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'EQUALS':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,232,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'DIFERENTE':([136,137,139,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,266,269,284,285,287,288,311,],[-146,-147,-60,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,233,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-148,-149,-126,-136,-119,-123,-73,]),'AND':([136,137,139,140,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,259,266,269,284,285,286,287,288,311,],[-146,-147,-60,182,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,-110,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-150,-148,-149,-126,-136,-111,-119,-123,-73,]),'OR':([136,137,138,139,140,141,142,143,144,145,146,147,149,150,151,158,159,160,161,174,178,181,183,184,186,187,188,189,202,204,225,252,254,255,258,259,266,269,284,285,286,287,288,311,],[-146,-147,179,-60,-108,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-146,-146,-147,-60,-132,-133,-146,-110,-118,-127,-128,-129,-130,-60,-146,-131,-146,-74,-135,-109,-150,-148,-149,-126,-136,-111,-119,-123,-73,]),'DOSPUNTOS':([138,140,141,142,143,144,145,146,147,149,150,151,153,174,178,181,183,184,186,187,188,189,192,225,254,255,256,258,259,266,269,284,285,286,287,288,311,],[-106,-108,-150,-148,-122,-146,-146,-146,-146,-60,-146,-147,-94,-132,-133,-146,-110,-118,-127,-128,-129,-130,242,-131,-74,-135,-107,-109,-150,-148,-149,-126,-136,-111,-119,-123,-73,]),'PUNTO':([139,149,161,202,],[180,180,180,180,]),'length':([180,],[217,]),'max':([180,],[218,]),'min':([180,],[219,]),'avg':([180,],[220,]),'median':([180,],[221,]),'mode':([180,],[222,]),'variance':([180,],[223,]),'stdev':([180,],[224,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'cuadGotoMain':([2,],[3,]),'auxprograma':([3,4,],[5,6,]),'varsaux':([8,11,75,76,],[10,24,82,83,]),'vars':([8,11,75,76,],[11,11,11,11,]),'empty':([8,9,10,11,16,51,64,72,75,76,81,84,86,115,136,137,164,171,172,245,272,281,282,283,],[12,14,17,12,17,59,70,59,12,12,88,109,59,130,176,176,109,176,176,109,291,298,298,298,]),'paux2':([10,16,],[15,33,]),'function':([10,16,],[16,16,]),'ftype':([10,16,],[18,18,]),'type':([13,64,108,],[25,71,71,]),'mainfunction':([14,15,],[30,32,]),'guardarTipoFunc':([19,20,21,22,23,],[35,36,37,38,39,]),'vaux':([25,58,],[40,65,]),'guardarTipoVar':([26,27,28,29,],[42,43,44,45,]),'agregaVar':([41,66,79,],[51,72,86,]),'cuadEnd':([46,48,],[53,55,]),'agregaFunc':([47,49,],[54,56,]),'nextvar':([51,72,86,],[57,78,111,]),'funcaux':([64,108,],[69,125,]),'fillMain':([68,],[74,]),'bloque':([74,105,106,240,273,302,308,],[80,123,124,272,292,307,310,]),'agregaPar':([77,126,201,],[84,164,245,]),'bloqueaux':([81,89,],[87,114,]),'estatuto':([81,89,],[89,89,]),'asignacion':([81,89,],[90,90,]),'escritura':([81,89,],[91,91,]),'llamada':([81,89,117,118,120,122,129,152,166,169,175,207,208,215,226,227,234,237,242,297,],[92,92,137,151,151,160,151,151,151,151,137,151,151,151,151,151,151,151,151,151,]),'condicion':([81,89,],[93,93,]),'whileloop':([81,89,],[94,94,]),'forloop':([81,89,],[95,95,]),'lectura':([81,89,],[96,96,]),'estReturn':([81,89,],[97,97,]),'agregaDir':([82,83,],[105,106,]),'masParam':([84,164,245,],[107,200,276,]),'checkID':([98,139,149,154,161,202,],[115,181,181,193,181,181,]),'checkFunc':([98,139,149,161,202,],[116,116,116,116,116,]),'migaja':([101,],[119,]),'asignaux':([115,],[128,]),'cuadEra':([116,],[131,]),'escaux':([117,175,],[133,214,]),'expresion':([117,118,120,122,129,152,166,169,175,207,208,242,297,],[134,148,153,156,167,191,203,210,134,249,251,274,251,]),'llamada_esp':([117,118,120,122,129,152,166,169,175,207,208,215,226,227,234,237,242,297,],[136,150,150,150,150,150,204,150,136,150,252,150,150,150,150,150,150,252,]),'andExpresion':([117,118,120,122,129,152,166,169,175,207,208,215,242,297,],[138,138,138,138,138,138,138,138,138,138,138,256,138,138,]),'relopExpresion':([117,118,120,122,129,152,166,169,175,207,208,215,226,242,297,],[140,140,140,140,140,140,140,140,140,140,140,140,258,140,140,]),'aritExpresion':([117,118,120,122,129,152,166,169,175,207,208,215,226,227,242,297,],[141,141,141,141,141,141,141,141,141,141,141,141,141,259,141,141,]),'term':([117,118,120,122,129,152,166,169,175,207,208,215,226,227,234,242,297,],[142,142,142,142,142,142,142,142,142,142,142,142,142,142,266,142,142,]),'factor':([117,118,120,122,129,152,166,169,175,207,208,215,226,227,234,237,242,297,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,269,143,143,]),'retAux':([122,],[155,]),'cuadEndf':([123,124,],[162,163,]),'guardaFondo':([132,168,],[169,208,]),'cuadEsc':([134,135,],[171,172,]),'nextexp':([136,137,171,172,],[173,177,212,213,]),'pushOT':([136,144,145,146,147,150,158,159,181,204,252,],[174,186,187,188,189,174,188,189,225,174,174,]),'pushOTLlam':([137,151,160,],[178,178,178,]),'cuadArit':([141,259,],[183,286,]),'cuadTerm':([142,266,],[184,287,]),'cuadFactor':([143,269,],[185,288,]),'checkExpFor':([153,274,],[192,293,]),'cuadRet':([156,157,158,159,160,],[195,196,197,198,199,]),'pushOper':([179,182,228,229,230,231,232,233,235,236,238,239,],[215,226,260,261,262,263,264,265,267,268,270,271,]),'especiales':([180,],[216,]),'relopAux':([183,],[227,]),'aritAux':([184,],[234,]),'termAux':([185,],[237,]),'cuadGotof':([190,241,],[240,273,]),'cuadRead':([193,],[243,]),'cuadAsignacion':([203,205,],[246,248,]),'llamaux':([208,297,],[250,306,]),'verPars':([250,],[280,]),'cuadPar':([251,252,253,],[281,282,283,]),'quitaFondo':([255,305,],[284,309,]),'condicionAux':([272,],[289,]),'nextparametro':([281,282,283,],[296,299,300,]),'cuadFinIf':([289,],[301,]),'cuadGoto':([290,],[302,]),'cuadFinWhile':([292,],[303,]),'cuadGoSub':([295,],[305,]),'gotoFor':([304,],[308,]),'returnFor':([310,],[312,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC','programa',11,'p_programa','amrlang.py',253),
  ('programa -> program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC','programa',10,'p_programa_vacio','amrlang.py',258),
  ('cuadGotoMain -> <empty>','cuadGotoMain',0,'p_cuadGotoMain','amrlang.py',263),
  ('cuadEnd -> <empty>','cuadEnd',0,'p_cuadEnd','amrlang.py',273),
  ('auxprograma -> <empty>','auxprograma',0,'p_auxprograma','amrlang.py',282),
  ('varsaux -> vars varsaux','varsaux',2,'p_varsaux','amrlang.py',295),
  ('varsaux -> empty','varsaux',1,'p_varsaux','amrlang.py',296),
  ('paux2 -> function paux2','paux2',2,'p_paux2','amrlang.py',301),
  ('paux2 -> empty','paux2',1,'p_paux2','amrlang.py',302),
  ('vars -> var type vaux PYC','vars',4,'p_vars','amrlang.py',307),
  ('vars -> empty','vars',1,'p_vars','amrlang.py',308),
  ('vaux -> ID agregaVar nextvar','vaux',3,'p_vaux','amrlang.py',313),
  ('vaux -> ID CORIZQ CTEINT CORDER agregaVar nextvar','vaux',6,'p_vaux','amrlang.py',314),
  ('vaux -> ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar','vaux',8,'p_vaux','amrlang.py',315),
  ('nextvar -> COMA vaux','nextvar',2,'p_nextvar','amrlang.py',320),
  ('nextvar -> empty','nextvar',1,'p_nextvar','amrlang.py',321),
  ('agregaVar -> <empty>','agregaVar',0,'p_agregaVar','amrlang.py',326),
  ('agregaPar -> <empty>','agregaPar',0,'p_agregaPar','amrlang.py',397),
  ('guardarTipoVar -> <empty>','guardarTipoVar',0,'p_guardarTipoVar','amrlang.py',452),
  ('guardarTipoFunc -> <empty>','guardarTipoFunc',0,'p_guardarTipoFunc','amrlang.py',459),
  ('mainfunction -> func main agregaFunc PARIZQ PARDER fillMain bloque','mainfunction',7,'p_mainfunction','amrlang.py',466),
  ('fillMain -> <empty>','fillMain',0,'p_fillMain','amrlang.py',471),
  ('bloque -> LLAVEIZQ bloqueaux LLAVEDER','bloque',3,'p_bloque','amrlang.py',477),
  ('bloque -> LLAVEIZQ empty LLAVEDER','bloque',3,'p_bloque','amrlang.py',478),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','amrlang.py',483),
  ('bloqueaux -> estatuto','bloqueaux',1,'p_bloqueaux','amrlang.py',484),
  ('type -> int guardarTipoVar','type',2,'p_type','amrlang.py',489),
  ('type -> float guardarTipoVar','type',2,'p_type','amrlang.py',490),
  ('type -> string guardarTipoVar','type',2,'p_type','amrlang.py',491),
  ('type -> bool guardarTipoVar','type',2,'p_type','amrlang.py',492),
  ('function -> ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux agregaDir bloque cuadEndf','function',11,'p_function','amrlang.py',497),
  ('function -> ftype func ID agregaFunc PARIZQ empty PARDER varsaux agregaDir bloque cuadEndf','function',11,'p_function','amrlang.py',498),
  ('agregaDir -> <empty>','agregaDir',0,'p_agregaDir','amrlang.py',503),
  ('cuadEndf -> <empty>','cuadEndf',0,'p_cuadEndf','amrlang.py',509),
  ('agregaFunc -> <empty>','agregaFunc',0,'p_agregaFunc','amrlang.py',536),
  ('ftype -> int guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',554),
  ('ftype -> float guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',555),
  ('ftype -> string guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',556),
  ('ftype -> bool guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',557),
  ('ftype -> void guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',558),
  ('funcaux -> type ID agregaPar masParam','funcaux',4,'p_funcaux','amrlang.py',563),
  ('funcaux -> type ID CORIZQ CTEINT CORDER agregaPar masParam','funcaux',7,'p_funcaux','amrlang.py',564),
  ('funcaux -> type ID CORIZQ CTEINT COMA CTEINT CORDER agregaPar masParam','funcaux',9,'p_funcaux','amrlang.py',565),
  ('masParam -> COMA funcaux','masParam',2,'p_masParam','amrlang.py',570),
  ('masParam -> empty','masParam',1,'p_masParam','amrlang.py',571),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','amrlang.py',576),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','amrlang.py',577),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','amrlang.py',578),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','amrlang.py',579),
  ('estatuto -> whileloop','estatuto',1,'p_estatuto','amrlang.py',580),
  ('estatuto -> forloop','estatuto',1,'p_estatuto','amrlang.py',581),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','amrlang.py',582),
  ('estatuto -> estReturn','estatuto',1,'p_estatuto','amrlang.py',583),
  ('asignacion -> ID checkID asignaux ASIGNA expresion cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',588),
  ('asignacion -> ID checkID asignaux ASIGNA llamada_esp PYC','asignacion',6,'p_asignacion','amrlang.py',589),
  ('asignacion -> ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC','asignacion',7,'p_asignacion','amrlang.py',590),
  ('aaa -> <empty>','aaa',0,'p_aaa','amrlang.py',595),
  ('bbb -> <empty>','bbb',0,'p_bbb','amrlang.py',601),
  ('ccc -> <empty>','ccc',0,'p_ccc','amrlang.py',607),
  ('checkID -> <empty>','checkID',0,'p_checkID','amrlang.py',613),
  ('cuadAsignacion -> <empty>','cuadAsignacion',0,'p_cuadAsignacion','amrlang.py',639),
  ('asignaux -> CORIZQ expresion CORDER','asignaux',3,'p_asignaux','amrlang.py',679),
  ('asignaux -> CORIZQ expresion COMA expresion CORDER','asignaux',5,'p_asignaux','amrlang.py',680),
  ('asignaux -> empty','asignaux',1,'p_asignaux','amrlang.py',681),
  ('escritura -> write PARIZQ escaux PARDER PYC','escritura',5,'p_escritura','amrlang.py',686),
  ('escaux -> expresion cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',691),
  ('escaux -> CTESTRING cuadEsc nextexp','escaux',3,'p_escaux','amrlang.py',692),
  ('escaux -> llamada_esp nextexp','escaux',2,'p_escaux','amrlang.py',693),
  ('escaux -> llamada nextexp','escaux',2,'p_escaux','amrlang.py',694),
  ('cuadEsc -> <empty>','cuadEsc',0,'p_cuadEsc','amrlang.py',699),
  ('nextexp -> COMA escaux','nextexp',2,'p_nextexp','amrlang.py',727),
  ('nextexp -> empty','nextexp',1,'p_nextexp','amrlang.py',728),
  ('llamada -> ID checkFunc cuadEra PARIZQ guardaFondo llamaux verPars PARDER cuadGoSub quitaFondo PYC','llamada',11,'p_llamada','amrlang.py',733),
  ('llamada -> ID checkFunc cuadEra PARIZQ PARDER PYC','llamada',6,'p_llamada','amrlang.py',734),
  ('pycopc -> PYC','pycopc',1,'p_pycopc','amrlang.py',739),
  ('pycopc -> empty','pycopc',1,'p_pycopc','amrlang.py',740),
  ('llamaux -> expresion cuadPar nextparametro','llamaux',3,'p_llamaux','amrlang.py',745),
  ('llamaux -> llamada_esp cuadPar nextparametro','llamaux',3,'p_llamaux','amrlang.py',746),
  ('llamaux -> CTESTRING cuadPar nextparametro','llamaux',3,'p_llamaux','amrlang.py',747),
  ('nextparametro -> COMA llamaux','nextparametro',2,'p_nextparametro','amrlang.py',752),
  ('nextparametro -> empty','nextparametro',1,'p_nextparametro','amrlang.py',753),
  ('checkFunc -> <empty>','checkFunc',0,'p_checkFunc','amrlang.py',758),
  ('cuadEra -> <empty>','cuadEra',0,'p_cuadEra','amrlang.py',767),
  ('cuadPar -> <empty>','cuadPar',0,'p_cuadPar','amrlang.py',796),
  ('verPars -> <empty>','verPars',0,'p_verPars','amrlang.py',851),
  ('cuadGoSub -> <empty>','cuadGoSub',0,'p_cuadGoSub','amrlang.py',867),
  ('condicion -> if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf','condicion',8,'p_condicion','amrlang.py',945),
  ('condicionAux -> else cuadGoto bloque','condicionAux',3,'p_condicionAux','amrlang.py',950),
  ('condicionAux -> empty','condicionAux',1,'p_condicionAux','amrlang.py',951),
  ('whileloop -> while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile','whileloop',8,'p_whileloop','amrlang.py',956),
  ('migaja -> <empty>','migaja',0,'p_migaja','amrlang.py',961),
  ('cuadFinWhile -> <empty>','cuadFinWhile',0,'p_cuadFinWhile','amrlang.py',969),
  ('forloop -> for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor','forloop',11,'p_forloop','amrlang.py',984),
  ('checkExpFor -> <empty>','checkExpFor',0,'p_checkExpFor','amrlang.py',989),
  ('gotoFor -> <empty>','gotoFor',0,'p_gotoFor','amrlang.py',1005),
  ('returnFor -> <empty>','returnFor',0,'p_returnFor','amrlang.py',1067),
  ('lectura -> read PARIZQ ID checkID cuadRead PARDER PYC','lectura',7,'p_lectura','amrlang.py',1108),
  ('cuadRead -> <empty>','cuadRead',0,'p_cuadRead','amrlang.py',1113),
  ('estReturn -> return PARIZQ retAux PARDER PYC','estReturn',5,'p_estReturn','amrlang.py',1125),
  ('retAux -> expresion cuadRet','retAux',2,'p_retAux','amrlang.py',1130),
  ('retAux -> CTESTRING cuadRet','retAux',2,'p_retAux','amrlang.py',1131),
  ('retAux -> true cuadRet','retAux',2,'p_retAux','amrlang.py',1132),
  ('retAux -> false cuadRet','retAux',2,'p_retAux','amrlang.py',1133),
  ('retAux -> llamada cuadRet','retAux',2,'p_retAux','amrlang.py',1134),
  ('cuadRet -> <empty>','cuadRet',0,'p_cuadRet','amrlang.py',1139),
  ('expresion -> andExpresion','expresion',1,'p_expresion','amrlang.py',1167),
  ('expresion -> andExpresion OR pushOper andExpresion','expresion',4,'p_expresion','amrlang.py',1168),
  ('andExpresion -> relopExpresion','andExpresion',1,'p_andExpresion','amrlang.py',1173),
  ('andExpresion -> relopExpresion AND pushOper relopExpresion','andExpresion',4,'p_andExpresion','amrlang.py',1174),
  ('relopExpresion -> aritExpresion cuadArit','relopExpresion',2,'p_relopExpresion','amrlang.py',1179),
  ('relopExpresion -> aritExpresion cuadArit relopAux aritExpresion cuadArit','relopExpresion',5,'p_relopExpresion','amrlang.py',1180),
  ('relopAux -> MAYORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',1185),
  ('relopAux -> MENORQUE pushOper','relopAux',2,'p_relopAux','amrlang.py',1186),
  ('relopAux -> MAYORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',1187),
  ('relopAux -> MENORIGUAL pushOper','relopAux',2,'p_relopAux','amrlang.py',1188),
  ('relopAux -> EQUALS pushOper','relopAux',2,'p_relopAux','amrlang.py',1189),
  ('relopAux -> DIFERENTE pushOper','relopAux',2,'p_relopAux','amrlang.py',1190),
  ('aritExpresion -> term cuadTerm','aritExpresion',2,'p_aritExpresion','amrlang.py',1195),
  ('aritExpresion -> term cuadTerm aritAux term cuadTerm','aritExpresion',5,'p_aritExpresion','amrlang.py',1196),
  ('aritAux -> MAS pushOper','aritAux',2,'p_aritAux','amrlang.py',1201),
  ('aritAux -> MENOS pushOper','aritAux',2,'p_aritAux','amrlang.py',1202),
  ('term -> factor','term',1,'p_term','amrlang.py',1207),
  ('term -> factor cuadFactor termAux factor cuadFactor','term',5,'p_term','amrlang.py',1208),
  ('termAux -> MULT pushOper','termAux',2,'p_termAux','amrlang.py',1213),
  ('termAux -> DIV pushOper','termAux',2,'p_termAux','amrlang.py',1214),
  ('factor -> PARIZQ guardaFondo expresion PARDER quitaFondo','factor',5,'p_factor','amrlang.py',1219),
  ('factor -> CTEINT pushOT','factor',2,'p_factor','amrlang.py',1220),
  ('factor -> CTEFLOAT pushOT','factor',2,'p_factor','amrlang.py',1221),
  ('factor -> true pushOT','factor',2,'p_factor','amrlang.py',1222),
  ('factor -> false pushOT','factor',2,'p_factor','amrlang.py',1223),
  ('factor -> ID checkID pushOT','factor',3,'p_factor','amrlang.py',1224),
  ('factor -> llamada_esp pushOT','factor',2,'p_factor','amrlang.py',1225),
  ('factor -> llamada pushOTLlam','factor',2,'p_factor','amrlang.py',1226),
  ('guardaFondo -> <empty>','guardaFondo',0,'p_guardaFondo','amrlang.py',1233),
  ('quitaFondo -> <empty>','quitaFondo',0,'p_quitaFondo','amrlang.py',1240),
  ('llamada_esp -> ID PUNTO especiales PARIZQ PARDER','llamada_esp',5,'p_llamada_esp','amrlang.py',1248),
  ('especiales -> length','especiales',1,'p_especiales','amrlang.py',1253),
  ('especiales -> max','especiales',1,'p_especiales','amrlang.py',1254),
  ('especiales -> min','especiales',1,'p_especiales','amrlang.py',1255),
  ('especiales -> avg','especiales',1,'p_especiales','amrlang.py',1256),
  ('especiales -> median','especiales',1,'p_especiales','amrlang.py',1257),
  ('especiales -> mode','especiales',1,'p_especiales','amrlang.py',1258),
  ('especiales -> variance','especiales',1,'p_especiales','amrlang.py',1259),
  ('especiales -> stdev','especiales',1,'p_especiales','amrlang.py',1260),
  ('pushOper -> <empty>','pushOper',0,'p_pushOper','amrlang.py',1265),
  ('pushOT -> <empty>','pushOT',0,'p_pushOT','amrlang.py',1272),
  ('pushOTLlam -> <empty>','pushOTLlam',0,'p_pushOTLlam','amrlang.py',1332),
  ('cuadTerm -> <empty>','cuadTerm',0,'p_cuadTerm','amrlang.py',1337),
  ('cuadFactor -> <empty>','cuadFactor',0,'p_cuadFactor','amrlang.py',1388),
  ('cuadArit -> <empty>','cuadArit',0,'p_cuadArit','amrlang.py',1439),
  ('cuadGotof -> <empty>','cuadGotof',0,'p_cuadGotof','amrlang.py',1478),
  ('cuadFinIf -> <empty>','cuadFinIf',0,'p_cuadFinIf','amrlang.py',1499),
  ('cuadGoto -> <empty>','cuadGoto',0,'p_cuadGoto','amrlang.py',1508),
  ('empty -> <empty>','empty',0,'p_empty','amrlang.py',1526),
]
