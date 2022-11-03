
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNA COMA CORDER CORIZQ CTEBOOL CTEFLOAT CTEINT CTESTRING DIFERENTE DIV DOSPUNTOS EQUALS ID LLAVEDER LLAVEIZQ MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MULT OR PARDER PARIZQ PUNTO PYC avg bool else end false float for func if int length main max median min mode program read stdev string true var variance void while write\n    programa : program ID auxprograma PYC varsaux paux2 mainfunction end PYC\n    \n    programa : program auxprograma ID PYC empty mainfunction end PYC\n    auxprograma :\n    \n    varsaux : vars varsaux\n            | empty\n    \n    paux2 : function paux2\n          | empty\n    \n    vars : var type vaux PYC\n         | empty\n    \n    vaux : ID agregaVar nextvar\n         | ID CORIZQ CTEINT CORDER agregaVar nextvar\n         | ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar\n    \n    nextvar : COMA vaux\n            | empty\n    \n    agregaVar :\n    \n    guardarTipoVar :\n    \n    guardarTipoFunc :\n    \n    mainfunction : func main agregaFunc PARIZQ PARDER varsaux bloque\n                 | func main agregaFunc PARIZQ PARDER bloque\n    \n    agregaFunc :\n    \n    bloque : LLAVEIZQ bloqueaux LLAVEDER\n           | LLAVEIZQ empty LLAVEDER\n    \n    bloqueaux : estatuto bloqueaux\n              | estatuto\n    \n    type : int guardarTipoVar\n         | float guardarTipoVar\n         | string guardarTipoVar\n         | bool guardarTipoVar\n    \n    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux bloque\n             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux bloque\n    \n    ftype : int guardarTipoFunc\n          | float guardarTipoFunc\n          | string guardarTipoFunc\n          | bool guardarTipoFunc\n          | void guardarTipoFunc\n    \n    funcaux : type ID agregaVar masParam\n            | type ID CORIZQ CTEINT CORDER agregaVar masParam\n            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar masParam\n    \n    masParam : funcaux\n             | empty\n    \n    estatuto : asignacion\n             | escritura\n             | llamada\n             | condicion\n             | whileloop\n             | forloop\n             | lectura\n    \n    asignacion : ID checkID asignaux ASIGNA expresion PYC\n               | ID checkID asignaux ASIGNA llamada_esp PYC\n               | ID checkID asignaux ASIGNA CTESTRING PYC\n    \n    checkID :\n    \n    asignaux : CORIZQ expresion CORDER\n             | CORIZQ expresion COMA expresion CORDER\n             | empty\n    \n    escritura : write PARIZQ escaux PARDER PYC\n    \n    escaux : expresion nextexp\n           | CTESTRING nextexp\n           | llamada_esp nextexp\n    \n    nextexp : COMA escaux\n            | empty\n    \n    llamada : ID PARIZQ expresion llamaux PARDER\n            | ID PARIZQ llamada_esp llamaux PARDER\n            | ID PARIZQ PARDER\n    \n    llamaux : expresion nextparametro\n            | llamada_esp nextparametro\n    \n    nextparametro : COMA llamaux\n                  | empty\n    \n    condicion : if PARIZQ expresion PARDER bloque\n              | if PARIZQ expresion PARDER bloque else bloque\n    \n    whileloop : while PARIZQ expresion PARDER bloque\n    \n    forloop : for PARIZQ expresion DOSPUNTOS expresion PARDER bloque\n    \n    lectura : read PARIZQ ID checkID PARDER PYC\n    \n    expresion : andExpresion\n              | andExpresion OR andExpresion\n    \n    andExpresion : relopExpresion\n                 | relopExpresion AND relopExpresion\n    \n    relopExpresion : aritExpresion\n                   | aritExpresion MAYORQUE aritExpresion\n                   | aritExpresion MENORQUE aritExpresion\n                   | aritExpresion MAYORIGUAL aritExpresion\n                   | aritExpresion MENORIGUAL aritExpresion\n                   | aritExpresion EQUALS aritExpresion\n                   | aritExpresion DIFERENTE aritExpresion\n    \n    aritExpresion : term\n                  | term MAS term\n                  | term MENOS term\n    \n    term : factor \n         | factor MULT factor\n         | factor DIV factor\n    \n    factor : PARIZQ expresion PARDER\n           | CTEINT pushOT\n           | CTEFLOAT pushOT\n           | true pushOT\n           | false pushOT\n           | ID checkID pushOT\n           | llamada_esp pushOT\n    \n    pushOT :\n    \n    llamada_esp : ID PUNTO especiales PARIZQ PARDER\n    \n    especiales : length\n               | max\n               | min\n               | avg\n               | median\n               | mode\n               | variance\n               | stdev\n    \n    empty : \n    '
    
_lr_action_items = {'program':([0,],[2,]),'$end':([1,52,54,],[0,-2,-1,]),'ID':([2,4,24,25,26,27,28,33,41,42,43,44,57,68,73,82,83,84,85,86,87,88,89,101,102,105,106,107,108,109,110,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,140,141,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,199,200,202,204,206,207,208,209,210,211,212,213,214,215,216,217,218,219,221,222,227,228,229,235,238,239,240,],[3,6,40,-16,-16,-16,-16,48,-25,-26,-27,-28,40,76,90,90,-41,-42,-43,-44,-45,-46,-47,-21,-22,121,121,140,140,140,144,140,-51,140,121,-63,121,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,121,-97,-96,140,140,140,140,140,140,140,140,140,140,140,140,-91,-92,-93,-94,121,140,140,-95,-90,121,-61,-62,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-55,-68,-70,-48,-49,-50,-72,-98,-69,-71,]),'PYC':([3,5,6,39,40,45,47,50,56,58,62,63,69,77,78,100,117,121,126,127,128,129,130,131,132,133,134,140,141,150,156,169,170,171,172,173,185,186,187,199,200,207,208,209,210,211,212,213,214,215,216,217,218,224,238,],[-3,7,8,49,-15,52,54,-107,-10,-14,-13,-15,-107,-11,-15,-107,-12,-51,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,-97,-96,-91,-92,-93,-94,219,227,228,229,-95,-90,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,235,-98,]),'var':([7,10,11,49,65,74,75,],[12,12,-9,-8,12,12,12,]),'int':([7,9,10,11,12,15,23,49,61,76,98,101,102,111,112,145,183,226,236,],[-107,18,-107,-5,25,18,-4,-8,25,-15,25,-21,-22,-29,-30,-15,25,-15,25,]),'float':([7,9,10,11,12,15,23,49,61,76,98,101,102,111,112,145,183,226,236,],[-107,19,-107,-5,26,19,-4,-8,26,-15,26,-21,-22,-29,-30,-15,26,-15,26,]),'string':([7,9,10,11,12,15,23,49,61,76,98,101,102,111,112,145,183,226,236,],[-107,20,-107,-5,27,20,-4,-8,27,-15,27,-21,-22,-29,-30,-15,27,-15,27,]),'bool':([7,9,10,11,12,15,23,49,61,76,98,101,102,111,112,145,183,226,236,],[-107,21,-107,-5,28,21,-4,-8,28,-15,28,-21,-22,-29,-30,-15,28,-15,28,]),'void':([7,9,10,11,15,23,49,101,102,111,112,],[-107,22,-107,-5,22,-4,-8,-21,-22,-29,-30,]),'func':([7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,32,34,35,36,37,38,49,101,102,111,112,],[-107,-107,-107,-107,-5,30,30,-107,-7,33,-17,-17,-17,-17,-17,-4,-6,-31,-32,-33,-34,-35,-8,-21,-22,-29,-30,]),'LLAVEIZQ':([10,11,23,49,65,71,74,75,96,97,179,180,233,234,],[-107,-5,-4,-8,73,73,-107,-107,73,73,73,73,73,73,]),'end':([29,31,72,79,101,102,],[45,47,-19,-18,-21,-22,]),'main':([30,],[46,]),'CORIZQ':([40,76,90,104,],[51,99,-51,119,]),'COMA':([40,50,59,63,69,78,100,116,121,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,148,150,152,154,156,169,170,171,172,199,200,207,208,209,210,211,212,213,214,215,216,217,218,238,],[-15,57,64,-15,57,-15,57,146,-51,-97,-73,-75,-77,-84,-87,-97,-97,-97,-97,175,175,175,-51,-97,189,-97,202,202,-96,-91,-92,-93,-94,-95,-90,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'PARIZQ':([46,48,53,55,90,91,92,93,94,95,105,106,107,108,109,119,121,122,123,125,126,127,128,129,130,131,132,133,134,140,141,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,190,191,192,193,194,195,196,197,198,199,200,202,207,208,209,210,211,212,213,214,215,216,217,218,238,],[-20,-20,60,61,105,106,107,108,109,110,122,122,122,122,122,122,-51,122,122,122,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,122,-97,-96,122,122,122,122,122,122,122,122,122,122,122,122,-91,-92,-93,-94,122,122,122,231,-99,-100,-101,-102,-103,-104,-105,-106,-95,-90,122,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'CTEINT':([51,64,99,105,106,107,108,109,119,121,122,123,125,126,127,128,129,130,131,132,133,134,140,141,146,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,199,200,202,207,208,209,210,211,212,213,214,215,216,217,218,238,],[59,70,116,131,131,131,131,131,131,-51,131,131,131,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,184,131,-97,-96,131,131,131,131,131,131,131,131,131,131,131,131,-91,-92,-93,-94,131,131,131,-95,-90,131,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'CORDER':([59,70,116,126,127,128,129,130,131,132,133,134,140,141,148,150,156,169,170,171,172,184,199,200,207,208,209,210,211,212,213,214,215,216,217,218,230,238,],[63,78,145,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,188,-97,-96,-91,-92,-93,-94,226,-95,-90,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,237,-98,]),'PARDER':([60,61,66,67,76,98,105,113,114,115,121,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,150,151,152,153,154,155,156,169,170,171,172,174,176,177,178,182,183,199,200,201,203,205,207,208,209,210,211,212,213,214,215,216,217,218,220,223,225,226,231,232,236,238,241,],[65,-107,74,75,-15,-107,124,-36,-39,-40,-51,-97,-73,-75,-77,-84,-87,-97,-97,-97,-97,173,-107,-107,-97,179,-51,-97,180,-51,-15,-97,200,-107,204,-97,206,-96,-91,-92,-93,-94,-56,-60,-57,-58,224,-107,-95,-90,-64,-67,-65,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-59,234,-37,-15,238,-66,-107,-98,-38,]),'LLAVEDER':([73,80,81,82,83,84,85,86,87,88,89,101,102,103,124,204,206,219,221,222,227,228,229,235,239,240,],[-107,101,102,-24,-41,-42,-43,-44,-45,-46,-47,-21,-22,-23,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'write':([73,82,83,84,85,86,87,88,89,101,102,124,204,206,219,221,222,227,228,229,235,239,240,],[91,91,-41,-42,-43,-44,-45,-46,-47,-21,-22,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'if':([73,82,83,84,85,86,87,88,89,101,102,124,204,206,219,221,222,227,228,229,235,239,240,],[92,92,-41,-42,-43,-44,-45,-46,-47,-21,-22,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'while':([73,82,83,84,85,86,87,88,89,101,102,124,204,206,219,221,222,227,228,229,235,239,240,],[93,93,-41,-42,-43,-44,-45,-46,-47,-21,-22,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'for':([73,82,83,84,85,86,87,88,89,101,102,124,204,206,219,221,222,227,228,229,235,239,240,],[94,94,-41,-42,-43,-44,-45,-46,-47,-21,-22,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'read':([73,82,83,84,85,86,87,88,89,101,102,124,204,206,219,221,222,227,228,229,235,239,240,],[95,95,-41,-42,-43,-44,-45,-46,-47,-21,-22,-63,-61,-62,-55,-68,-70,-48,-49,-50,-72,-69,-71,]),'ASIGNA':([90,104,118,120,188,237,],[-51,-107,147,-54,-52,-53,]),'else':([101,102,221,],[-21,-22,233,]),'CTEFLOAT':([105,106,107,108,109,119,121,122,123,125,126,127,128,129,130,131,132,133,134,140,141,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,199,200,202,207,208,209,210,211,212,213,214,215,216,217,218,238,],[132,132,132,132,132,132,-51,132,132,132,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,132,-97,-96,132,132,132,132,132,132,132,132,132,132,132,132,-91,-92,-93,-94,132,132,132,-95,-90,132,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'true':([105,106,107,108,109,119,121,122,123,125,126,127,128,129,130,131,132,133,134,140,141,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,199,200,202,207,208,209,210,211,212,213,214,215,216,217,218,238,],[133,133,133,133,133,133,-51,133,133,133,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,133,-97,-96,133,133,133,133,133,133,133,133,133,133,133,133,-91,-92,-93,-94,133,133,133,-95,-90,133,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'false':([105,106,107,108,109,119,121,122,123,125,126,127,128,129,130,131,132,133,134,140,141,147,150,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,175,181,189,199,200,202,207,208,209,210,211,212,213,214,215,216,217,218,238,],[134,134,134,134,134,134,-51,134,134,134,-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,134,-97,-96,134,134,134,134,134,134,134,134,134,134,134,134,-91,-92,-93,-94,134,134,134,-95,-90,134,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'CTESTRING':([106,147,175,],[137,187,137,]),'PUNTO':([121,140,],[149,149,]),'MULT':([121,125,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,238,],[-51,-97,167,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-98,]),'DIV':([121,125,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,238,],[-51,-97,168,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-98,]),'MAS':([121,125,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,217,218,238,],[-51,-97,165,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-88,-89,-98,]),'MENOS':([121,125,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,217,218,238,],[-51,-97,166,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-88,-89,-98,]),'MAYORQUE':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,159,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'MENORQUE':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,160,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'MAYORIGUAL':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,161,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'MENORIGUAL':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,162,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'EQUALS':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,163,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'DIFERENTE':([121,125,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,215,216,217,218,238,],[-51,-97,164,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-85,-86,-88,-89,-98,]),'AND':([121,125,127,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,209,210,211,212,213,214,215,216,217,218,238,],[-51,-97,158,-77,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'OR':([121,125,126,127,128,129,130,131,132,133,134,138,140,141,150,154,156,169,170,171,172,186,199,200,208,209,210,211,212,213,214,215,216,217,218,238,],[-51,-97,157,-75,-77,-84,-87,-97,-97,-97,-97,-97,-51,-97,-97,-97,-96,-91,-92,-93,-94,-97,-95,-90,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'DOSPUNTOS':([126,127,128,129,130,131,132,133,134,140,141,143,150,156,169,170,171,172,199,200,207,208,209,210,211,212,213,214,215,216,217,218,238,],[-73,-75,-77,-84,-87,-97,-97,-97,-97,-51,-97,181,-97,-96,-91,-92,-93,-94,-95,-90,-74,-76,-78,-79,-80,-81,-82,-83,-85,-86,-88,-89,-98,]),'length':([149,],[191,]),'max':([149,],[192,]),'min':([149,],[193,]),'avg':([149,],[194,]),'median':([149,],[195,]),'mode':([149,],[196,]),'variance':([149,],[197,]),'stdev':([149,],[198,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'auxprograma':([2,3,],[4,5,]),'varsaux':([7,10,65,74,75,],[9,23,71,96,97,]),'vars':([7,10,65,74,75,],[10,10,10,10,10,]),'empty':([7,8,9,10,15,50,61,65,69,73,74,75,98,100,104,136,137,138,152,154,183,236,],[11,13,16,11,16,58,67,11,58,81,11,11,115,58,120,176,176,176,203,203,115,115,]),'paux2':([9,15,],[14,32,]),'function':([9,15,],[15,15,]),'ftype':([9,15,],[17,17,]),'type':([12,61,98,183,236,],[24,68,68,68,68,]),'mainfunction':([13,14,],[29,31,]),'guardarTipoFunc':([18,19,20,21,22,],[34,35,36,37,38,]),'vaux':([24,57,],[39,62,]),'guardarTipoVar':([25,26,27,28,],[41,42,43,44,]),'agregaVar':([40,63,76,78,145,226,],[50,69,98,100,183,236,]),'agregaFunc':([46,48,],[53,55,]),'nextvar':([50,69,100,],[56,77,117,]),'funcaux':([61,98,183,236,],[66,114,114,114,]),'bloque':([65,71,96,97,179,180,233,234,],[72,79,111,112,221,222,239,240,]),'bloqueaux':([73,82,],[80,103,]),'estatuto':([73,82,],[82,82,]),'asignacion':([73,82,],[83,83,]),'escritura':([73,82,],[84,84,]),'llamada':([73,82,],[85,85,]),'condicion':([73,82,],[86,86,]),'whileloop':([73,82,],[87,87,]),'forloop':([73,82,],[88,88,]),'lectura':([73,82,],[89,89,]),'checkID':([90,121,140,144,],[104,150,150,182,]),'masParam':([98,183,236,],[113,225,241,]),'asignaux':([104,],[118,]),'expresion':([105,106,107,108,109,119,122,123,125,147,175,181,189,202,],[123,136,139,142,143,148,151,152,152,185,136,223,230,152,]),'llamada_esp':([105,106,107,108,109,119,122,123,125,147,157,158,159,160,161,162,163,164,165,166,167,168,175,181,189,202,],[125,138,141,141,141,141,141,154,154,186,141,141,141,141,141,141,141,141,141,141,141,141,138,141,141,154,]),'andExpresion':([105,106,107,108,109,119,122,123,125,147,157,175,181,189,202,],[126,126,126,126,126,126,126,126,126,126,207,126,126,126,126,]),'relopExpresion':([105,106,107,108,109,119,122,123,125,147,157,158,175,181,189,202,],[127,127,127,127,127,127,127,127,127,127,127,208,127,127,127,127,]),'aritExpresion':([105,106,107,108,109,119,122,123,125,147,157,158,159,160,161,162,163,164,175,181,189,202,],[128,128,128,128,128,128,128,128,128,128,128,128,209,210,211,212,213,214,128,128,128,128,]),'term':([105,106,107,108,109,119,122,123,125,147,157,158,159,160,161,162,163,164,165,166,175,181,189,202,],[129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,215,216,129,129,129,129,]),'factor':([105,106,107,108,109,119,122,123,125,147,157,158,159,160,161,162,163,164,165,166,167,168,175,181,189,202,],[130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,217,218,130,130,130,130,]),'escaux':([106,175,],[135,220,]),'llamaux':([123,125,202,],[153,155,232,]),'pushOT':([125,131,132,133,134,138,141,150,154,186,],[156,169,170,171,172,156,156,199,156,156,]),'nextexp':([136,137,138,],[174,177,178,]),'especiales':([149,],[190,]),'nextparametro':([152,154,],[201,205,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> program ID auxprograma PYC varsaux paux2 mainfunction end PYC','programa',9,'p_programa','amrlang.py',230),
  ('programa -> program auxprograma ID PYC empty mainfunction end PYC','programa',8,'p_programa_vacio','amrlang.py',235),
  ('auxprograma -> <empty>','auxprograma',0,'p_auxprograma','amrlang.py',239),
  ('varsaux -> vars varsaux','varsaux',2,'p_varsaux','amrlang.py',250),
  ('varsaux -> empty','varsaux',1,'p_varsaux','amrlang.py',251),
  ('paux2 -> function paux2','paux2',2,'p_paux2','amrlang.py',256),
  ('paux2 -> empty','paux2',1,'p_paux2','amrlang.py',257),
  ('vars -> var type vaux PYC','vars',4,'p_vars','amrlang.py',262),
  ('vars -> empty','vars',1,'p_vars','amrlang.py',263),
  ('vaux -> ID agregaVar nextvar','vaux',3,'p_vaux','amrlang.py',268),
  ('vaux -> ID CORIZQ CTEINT CORDER agregaVar nextvar','vaux',6,'p_vaux','amrlang.py',269),
  ('vaux -> ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar','vaux',8,'p_vaux','amrlang.py',270),
  ('nextvar -> COMA vaux','nextvar',2,'p_nextvar','amrlang.py',275),
  ('nextvar -> empty','nextvar',1,'p_nextvar','amrlang.py',276),
  ('agregaVar -> <empty>','agregaVar',0,'p_agregaVar','amrlang.py',281),
  ('guardarTipoVar -> <empty>','guardarTipoVar',0,'p_guardarTipoVar','amrlang.py',304),
  ('guardarTipoFunc -> <empty>','guardarTipoFunc',0,'p_guardarTipoFunc','amrlang.py',311),
  ('mainfunction -> func main agregaFunc PARIZQ PARDER varsaux bloque','mainfunction',7,'p_mainfunction','amrlang.py',318),
  ('mainfunction -> func main agregaFunc PARIZQ PARDER bloque','mainfunction',6,'p_mainfunction','amrlang.py',319),
  ('agregaFunc -> <empty>','agregaFunc',0,'p_agregaFunc','amrlang.py',324),
  ('bloque -> LLAVEIZQ bloqueaux LLAVEDER','bloque',3,'p_bloque','amrlang.py',338),
  ('bloque -> LLAVEIZQ empty LLAVEDER','bloque',3,'p_bloque','amrlang.py',339),
  ('bloqueaux -> estatuto bloqueaux','bloqueaux',2,'p_bloqueaux','amrlang.py',344),
  ('bloqueaux -> estatuto','bloqueaux',1,'p_bloqueaux','amrlang.py',345),
  ('type -> int guardarTipoVar','type',2,'p_type','amrlang.py',350),
  ('type -> float guardarTipoVar','type',2,'p_type','amrlang.py',351),
  ('type -> string guardarTipoVar','type',2,'p_type','amrlang.py',352),
  ('type -> bool guardarTipoVar','type',2,'p_type','amrlang.py',353),
  ('function -> ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux bloque','function',9,'p_function','amrlang.py',358),
  ('function -> ftype func ID agregaFunc PARIZQ empty PARDER varsaux bloque','function',9,'p_function','amrlang.py',359),
  ('ftype -> int guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',365),
  ('ftype -> float guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',366),
  ('ftype -> string guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',367),
  ('ftype -> bool guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',368),
  ('ftype -> void guardarTipoFunc','ftype',2,'p_ftype','amrlang.py',369),
  ('funcaux -> type ID agregaVar masParam','funcaux',4,'p_funcaux','amrlang.py',374),
  ('funcaux -> type ID CORIZQ CTEINT CORDER agregaVar masParam','funcaux',7,'p_funcaux','amrlang.py',375),
  ('funcaux -> type ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar masParam','funcaux',9,'p_funcaux','amrlang.py',376),
  ('masParam -> funcaux','masParam',1,'p_masParam','amrlang.py',381),
  ('masParam -> empty','masParam',1,'p_masParam','amrlang.py',382),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','amrlang.py',387),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','amrlang.py',388),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','amrlang.py',389),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','amrlang.py',390),
  ('estatuto -> whileloop','estatuto',1,'p_estatuto','amrlang.py',391),
  ('estatuto -> forloop','estatuto',1,'p_estatuto','amrlang.py',392),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','amrlang.py',393),
  ('asignacion -> ID checkID asignaux ASIGNA expresion PYC','asignacion',6,'p_asignacion','amrlang.py',398),
  ('asignacion -> ID checkID asignaux ASIGNA llamada_esp PYC','asignacion',6,'p_asignacion','amrlang.py',399),
  ('asignacion -> ID checkID asignaux ASIGNA CTESTRING PYC','asignacion',6,'p_asignacion','amrlang.py',400),
  ('checkID -> <empty>','checkID',0,'p_checkID','amrlang.py',405),
  ('asignaux -> CORIZQ expresion CORDER','asignaux',3,'p_asignaux','amrlang.py',428),
  ('asignaux -> CORIZQ expresion COMA expresion CORDER','asignaux',5,'p_asignaux','amrlang.py',429),
  ('asignaux -> empty','asignaux',1,'p_asignaux','amrlang.py',430),
  ('escritura -> write PARIZQ escaux PARDER PYC','escritura',5,'p_escritura','amrlang.py',435),
  ('escaux -> expresion nextexp','escaux',2,'p_escaux','amrlang.py',440),
  ('escaux -> CTESTRING nextexp','escaux',2,'p_escaux','amrlang.py',441),
  ('escaux -> llamada_esp nextexp','escaux',2,'p_escaux','amrlang.py',442),
  ('nextexp -> COMA escaux','nextexp',2,'p_nextexp','amrlang.py',448),
  ('nextexp -> empty','nextexp',1,'p_nextexp','amrlang.py',449),
  ('llamada -> ID PARIZQ expresion llamaux PARDER','llamada',5,'p_llamada','amrlang.py',454),
  ('llamada -> ID PARIZQ llamada_esp llamaux PARDER','llamada',5,'p_llamada','amrlang.py',455),
  ('llamada -> ID PARIZQ PARDER','llamada',3,'p_llamada','amrlang.py',456),
  ('llamaux -> expresion nextparametro','llamaux',2,'p_llamaux','amrlang.py',461),
  ('llamaux -> llamada_esp nextparametro','llamaux',2,'p_llamaux','amrlang.py',462),
  ('nextparametro -> COMA llamaux','nextparametro',2,'p_nextparametro','amrlang.py',467),
  ('nextparametro -> empty','nextparametro',1,'p_nextparametro','amrlang.py',468),
  ('condicion -> if PARIZQ expresion PARDER bloque','condicion',5,'p_condicion','amrlang.py',473),
  ('condicion -> if PARIZQ expresion PARDER bloque else bloque','condicion',7,'p_condicion','amrlang.py',474),
  ('whileloop -> while PARIZQ expresion PARDER bloque','whileloop',5,'p_whileloop','amrlang.py',479),
  ('forloop -> for PARIZQ expresion DOSPUNTOS expresion PARDER bloque','forloop',7,'p_forloop','amrlang.py',484),
  ('lectura -> read PARIZQ ID checkID PARDER PYC','lectura',6,'p_lectura','amrlang.py',489),
  ('expresion -> andExpresion','expresion',1,'p_expresion','amrlang.py',494),
  ('expresion -> andExpresion OR andExpresion','expresion',3,'p_expresion','amrlang.py',495),
  ('andExpresion -> relopExpresion','andExpresion',1,'p_andExpresion','amrlang.py',500),
  ('andExpresion -> relopExpresion AND relopExpresion','andExpresion',3,'p_andExpresion','amrlang.py',501),
  ('relopExpresion -> aritExpresion','relopExpresion',1,'p_relopExpresion','amrlang.py',506),
  ('relopExpresion -> aritExpresion MAYORQUE aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',507),
  ('relopExpresion -> aritExpresion MENORQUE aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',508),
  ('relopExpresion -> aritExpresion MAYORIGUAL aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',509),
  ('relopExpresion -> aritExpresion MENORIGUAL aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',510),
  ('relopExpresion -> aritExpresion EQUALS aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',511),
  ('relopExpresion -> aritExpresion DIFERENTE aritExpresion','relopExpresion',3,'p_relopExpresion','amrlang.py',512),
  ('aritExpresion -> term','aritExpresion',1,'p_aritExpresion','amrlang.py',517),
  ('aritExpresion -> term MAS term','aritExpresion',3,'p_aritExpresion','amrlang.py',518),
  ('aritExpresion -> term MENOS term','aritExpresion',3,'p_aritExpresion','amrlang.py',519),
  ('term -> factor','term',1,'p_term','amrlang.py',524),
  ('term -> factor MULT factor','term',3,'p_term','amrlang.py',525),
  ('term -> factor DIV factor','term',3,'p_term','amrlang.py',526),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','amrlang.py',531),
  ('factor -> CTEINT pushOT','factor',2,'p_factor','amrlang.py',532),
  ('factor -> CTEFLOAT pushOT','factor',2,'p_factor','amrlang.py',533),
  ('factor -> true pushOT','factor',2,'p_factor','amrlang.py',534),
  ('factor -> false pushOT','factor',2,'p_factor','amrlang.py',535),
  ('factor -> ID checkID pushOT','factor',3,'p_factor','amrlang.py',536),
  ('factor -> llamada_esp pushOT','factor',2,'p_factor','amrlang.py',537),
  ('pushOT -> <empty>','pushOT',0,'p_pushOT','amrlang.py',542),
  ('llamada_esp -> ID PUNTO especiales PARIZQ PARDER','llamada_esp',5,'p_llamada_esp','amrlang.py',617),
  ('especiales -> length','especiales',1,'p_especiales','amrlang.py',622),
  ('especiales -> max','especiales',1,'p_especiales','amrlang.py',623),
  ('especiales -> min','especiales',1,'p_especiales','amrlang.py',624),
  ('especiales -> avg','especiales',1,'p_especiales','amrlang.py',625),
  ('especiales -> median','especiales',1,'p_especiales','amrlang.py',626),
  ('especiales -> mode','especiales',1,'p_especiales','amrlang.py',627),
  ('especiales -> variance','especiales',1,'p_especiales','amrlang.py',628),
  ('especiales -> stdev','especiales',1,'p_especiales','amrlang.py',629),
  ('empty -> <empty>','empty',0,'p_empty','amrlang.py',635),
]
