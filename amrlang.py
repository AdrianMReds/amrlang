#Adrián Montemayor Rojas
#A01283139


#Pendiente y cambios
#Pendiente
#Cuadruplos de llamadas especiales
#Al poner x-y*z+r me marca error en el último +
#También marca error al poner del mismo operador muchas veces

#En la máquina virtual va a haber una pila por cada loc y temp por cada tipo
#Las variables globales se envían como una lista estática
#Las constantes se envían como una lista estática

#Cambios:

import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys
from funcionesCompilacion import *
from linkedListComp import *
from maqvir import *


# -1 = error
# 0 = int
# 1 = float
# 2 = string
# 3 = bool
typeList = ['int', 'float', 'string', 'bool']

progName = ''
tipoVar = ''
tipoFunc = ''
actualFunc = ''
dirFunc = {}
dirVars = {}
listaCuadruplos = []
contCuadruplos = 1
poper = []
pilaOperandos = []
pilaTipos = []
# avail = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10'
#          , 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27']
# contAvail = 0
pilaSaltos = []
listaConstantes = {}
paramCounter = 0
funcACorrer = ''
idParaLista = ''

#Globales
#Int 1000-1999
globIntInf = 1000 #Límite inferior de memoria
globInt = globIntInf
#Float 2000-2999
globFloatInf = 2000
globFloat = globFloatInf
#String 3000-3999
globStringInf = 3000
globString = globStringInf
#Bool 4000-4999
globBoolInf = 4000
globBool = globBoolInf

#  #Global lists
# #ListInt 1000-1999
# globListIntInf = 5000 #Límite inferior de memoria
# globListInt = globIntInf
# #ListFloat 2000-2999
# globListFloatInf = 6000
# globListFloat = globFloatInf
# #ListString 3000-3999
# globListStringInf = 7000
# globListString = globStringInf
# #ListBool 4000-4999
# globListBoolInf = 5000
# globListBool = globBoolInf

#locales
#Int 5000-5999
locIntInf = 5000 #Límite inferior de memoria
locInt = locIntInf
#Float 6000-6999
locFloatInf = 6000
locFloat = locFloatInf
#String 7000-7999
locStringInf = 7000
locString = locStringInf
#Bool 8000-8999
locBoolInf = 8000
locBool = locBoolInf

#Temporales
#Int 5000-5999
tempIntInf = 9000 #Límite inferior de memoria
tempInt = tempIntInf
#Float 6000-6999
tempFloatInf = 10000
tempFloat = tempFloatInf
#String 7000-7999
tempStringInf = 11000
tempString = tempStringInf
#Bool 8000-8999
tempBoolInf = 12000
tempBool = tempBoolInf
#Pointer 9000-9999
tempPointerInf = 13000
tempPointer = tempPointerInf

ctesInf = 14000
ctes = ctesInf

def fill(numCuad, contenido):
    global listaCuadruplos
    listaCuadruplos[numCuad-1].append(contenido)

def checkType(id):
    global actualFunc
    print(actualFunc)
    if(dirFunc[actualFunc]['vars'].get(id,-1)!=-1):
        varsInFunc = dirFunc[actualFunc]['vars']
    else:
        varsInFunc = dirFunc[progName]['vars']
    t = varsInFunc[id]['type']
    print("Type de {}".format(id), t)
    return t

reservadas = ['program', 'var', 'func', 'main', 'int', 'float', 'string', 'bool',
              'write', 'if', 'else', 'while', 'for', 'read', 'void', 'end', 'length',
              'max', 'min', 'avg', 'median', 'mode', 'variance', 'stdev', 'graph','true', 'false', 'return']

tokens = reservadas + ['ID', #NOMBRE DE VARIABLE O FUNCIÓN
                       'CTEINT', #CONSTANTE INT
                       'CTEFLOAT', #CONSTANTE FLOAT
                       'CTESTRING', #CONSTANTE STRING
                       'CTEBOOL',
                       'PYC', #PUNTO Y COMA
                       'CORIZQ', #CORCHETE IZQUIERDO
                       'CORDER', #CORCHETE DERECHO
                       'COMA',
                       'PARIZQ', #PARENTESIS IZQUIERDO
                       'PARDER', #PARENTESIS DERECHO
                       'LLAVEIZQ', #LLAVE IZQUIERDA
                       'LLAVEDER', #LLAVE DERECHA
                       'ASIGNA', # =
                       'DOSPUNTOS', # :
                       'MAS', # +
                       'MENOS', #-
                       'AND', #&&
                       'OR', # ||
                       'MULT', # *
                       'DIV', # /
                       'MAYORQUE', # >
                       'MENORQUE', # <
                       'EQUALS', # ==
                       'DIFERENTE', #$
                       'PUNTO' # .
                       ]

t_ignore = r' '
t_ignore_endline = r'\n'
t_ignore_tab = r'\t'
t_PYC = r'\;'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_COMA = r'\,'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_ASIGNA = r'\='
t_DOSPUNTOS = r'\:'
t_MAS = r'\+'
t_MENOS = r'\-'
t_AND = r'\&\&' 
t_OR = r'\|\|'
t_MULT = r'\*'
t_DIV = r'\/'
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_EQUALS = r'\=\='
t_DIFERENTE = r'\$'
t_PUNTO = r'\.'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = t.value
    t.value = t.value
    return t

def t_CTEFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTEINT(t):
    r'\d+'
    # r'-?[0-9]\d*'
    t.value = int(t.value)
    return t

def t_CTESTRING(t):
    r'\"(\\.|[^"\\])*\"'
    t.value = str(t.value)
    return t

def t_CTEBOOL(t):
    r'true|false'
    t.value = bool(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
program patito;
var int i,j,p;
var int arreglo[10];
var int matriz[2,5];

int func fact(int j)
var int i;
{

    i = p-j*2-j;
    if(j == 1){
        return(j);
    }else{
        return(j*fact(j-1));
    }
}

void func inicia(int y)
var int x;
{
    x = 0;
    while(x<11){
        arreglo[x] = y*x;
        x = x+1;
    }
}

func main(){
    read(p);
    j = p*2;
    i = -1;
    inicia(p*j-5)
}

       '''

lexer.input(data)

#varsaux es P
#paux2 es F
def p_programa(p):
    '''
    programa : program cuadGotoMain ID auxprograma PYC varsaux paux2 mainfunction end cuadEnd PYC
    '''

def p_programa_vacio(p):
    '''
    programa : program cuadGotoMain auxprograma ID PYC empty mainfunction end cuadEnd PYC
    '''

def p_cuadGotoMain(p):
    '''
    cuadGotoMain :
    '''
    global listaCuadruplos
    global contCuadruplos
    cuad = [contCuadruplos, 'goto']
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplo', cuad)
    contCuadruplos += 1

def p_cuadEnd(p):
    '''
    cuadEnd :
    '''
    global listaCuadruplos
    global contCuadruplos
    cuad = [contCuadruplos, 'endprogram']
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplo', cuad)


def p_auxprograma(p):
    '''auxprograma :
    '''
    global progName
    progName = str(p[-1])
    t = 'program'
    dirFunc[progName] = {'type': t, 'globInt':0, 'globFloat':0, 'globString':0, 'globBool':0
                       ,'tempInt':0, 'tempFloat':0, 'tempString':0, 'tempBool':0, 'tempPointer':0
                       , 'vars' : {}}
    global actualFunc
    actualFunc = progName

def p_varsaux(p):
    '''
    varsaux : vars varsaux
            | empty
    '''

def p_paux2(p):
    '''
    paux2 : function paux2
          | empty
    '''

def p_vars(p):
    '''
    vars : var type vaux PYC
         | empty
    '''

def p_vaux(p):
    '''
    vaux : ID agregaVar nextvar
         | ID CORIZQ CTEINT CORDER agregaVar nextvar
         | ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar nextvar
    '''

def p_nextvar(p):
    '''
    nextvar : COMA vaux
            | empty
    '''

def p_agregaVar(p):
    '''
    agregaVar :
    '''
    global locInt
    global locFloat
    global locString
    global locBool
    global globInt
    global globFloat
    global globString
    global globBool

    e = dirFunc.get(actualFunc,0)
    if e!=0:
        direc = None
        if tipoVar == 'int':
            if actualFunc == progName:
                direc = globInt
                globInt += 1
                dirFunc[actualFunc]['globInt'] += 1
            else:
                direc = locInt
                locInt+=1
                dirFunc[actualFunc]['locInt'] += 1
        elif tipoVar == 'float':
            if actualFunc == progName:
                direc = globFloat
                globFloat += 1
                dirFunc[actualFunc]['globFloat'] += 1
            else:
                direc = locFloat
                locFloat+=1
                dirFunc[actualFunc]['locFloat'] += 1
        elif tipoVar == 'string':
            if actualFunc == progName:
                direc = globString
                globString += 1
                dirFunc[actualFunc]['globString'] += 1
            else:
                direc = locString
                locString+=1
                dirFunc[actualFunc]['locString'] += 1
        elif tipoVar == 'bool':
            if actualFunc == progName:
                direc = globBool
                globBool += 1
                dirFunc[actualFunc]['globBool'] += 1
            else:
                direc = locBool
                locBool+=1
                dirFunc[actualFunc]['locBool'] += 1

        #Simple variable
        if p[-1]!=']':
            #Name of var (ID)
            nv = p[-1]
            dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':0, 'dirVar' : direc, 'size':1}
        else:
            # print('p de arreglo o matriz',p)
            #Array
            if p[-3] != ',':
                #Name of var (ID)
                nv = p[-4]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':1, 'dirVar' : direc}
                inf = 0
                sup = p[-2]
                r = 1
                r = (sup+1)*r
                m0 = r
                dirFunc[actualFunc]['vars'][nv]['size'] = m0
                # print('m0',r)
                offset = 0
                n = Node(inf, sup, 0)
                ll = LinkedList(n)
                dirFunc[actualFunc]['vars'][nv]['llDims'] = ll
                dirFunc[actualFunc]['vars'][nv]['llDims'].printList()

                for x in range(m0-1):
                    direc = None
                    if tipoVar == 'int':
                        if actualFunc == progName:
                            direc = globInt
                            globInt += 1
                            dirFunc[actualFunc]['globInt'] += 1
                        else:
                            direc = locInt
                            locInt+=1
                            dirFunc[actualFunc]['locInt'] += 1
                    elif tipoVar == 'float':
                        if actualFunc == progName:
                            direc = globFloat
                            globFloat += 1
                            dirFunc[actualFunc]['globFloat'] += 1
                        else:
                            direc = locFloat
                            locFloat+=1
                            dirFunc[actualFunc]['locFloat'] += 1
                    elif tipoVar == 'string':
                        if actualFunc == progName:
                            direc = globString
                            globString += 1
                            dirFunc[actualFunc]['globString'] += 1
                        else:
                            direc = locString
                            locString+=1
                            dirFunc[actualFunc]['locString'] += 1
                    elif tipoVar == 'bool':
                        if actualFunc == progName:
                            direc = globBool
                            globBool += 1
                            dirFunc[actualFunc]['globBool'] += 1
                        else:
                            direc = locBool
                            locBool+=1
                            dirFunc[actualFunc]['locBool'] += 1
            #Matrix
            else:
                #Name of var (ID)
                nv = p[-6]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':2, 'dirVar' : direc}
                inf = 0
                sup = p[-4]
                sup2 = p[-2]

                r=1
                r = sup+1
                r = r *(sup2 + 1)
                m0 = r
                dirFunc[actualFunc]['vars'][nv]['size'] = r
                # print('m0',m0)
                m1 = m0/(sup+1)
                m1 = int(m1)
                n = Node(inf,sup,m1)
                ll = LinkedList(n)
                m2 = m1/(sup2+1)
                ll.add(inf,sup2,0)
                dirFunc[actualFunc]['vars'][nv]['llDims'] = ll
                dirFunc[actualFunc]['vars'][nv]['llDims'].printList()
                for x in range(m0-1):
                    direc = None
                    if tipoVar == 'int':
                        if actualFunc == progName:
                            direc = globInt
                            globInt += 1
                            dirFunc[actualFunc]['globInt'] += 1
                        else:
                            direc = locInt
                            locInt+=1
                            dirFunc[actualFunc]['locInt'] += 1
                    elif tipoVar == 'float':
                        if actualFunc == progName:
                            direc = globFloat
                            globFloat += 1
                            dirFunc[actualFunc]['globFloat'] += 1
                        else:
                            direc = locFloat
                            locFloat+=1
                            dirFunc[actualFunc]['locFloat'] += 1
                    elif tipoVar == 'string':
                        if actualFunc == progName:
                            direc = globString
                            globString += 1
                            dirFunc[actualFunc]['globString'] += 1
                        else:
                            direc = locString
                            locString+=1
                            dirFunc[actualFunc]['locString'] += 1
                    elif tipoVar == 'bool':
                        if actualFunc == progName:
                            direc = globBool
                            globBool += 1
                            dirFunc[actualFunc]['globBool'] += 1
                        else:
                            direc = locBool
                            locBool+=1
                            dirFunc[actualFunc]['locBool'] += 1

def p_agregaPar(p):
    '''
    agregaPar :
    '''
    global locInt
    global locFloat
    global locString
    global locBool
    global globInt
    global globFloat
    global globString
    global globBool

    e = dirFunc.get(actualFunc,0)
    if e!=0:
        direc = None
        if tipoVar == 'int':
            direc = locInt
            locInt+=1
            dirFunc[actualFunc]['parInt'] += 1
            dirFunc[actualFunc]['locInt'] += 1
            dirFunc[actualFunc]['secPars'] += 'i'
        elif tipoVar == 'float':
            direc = locFloat
            locFloat+=1
            dirFunc[actualFunc]['parFloat'] += 1
            dirFunc[actualFunc]['locFloat'] += 1
            dirFunc[actualFunc]['secPars'] += 'f'
        elif tipoVar == 'string':
            direc = locString
            locString+=1
            dirFunc[actualFunc]['parString'] += 1
            dirFunc[actualFunc]['locString'] += 1
            dirFunc[actualFunc]['secPars'] += 's'
        elif tipoVar == 'bool':
            direc = locBool
            locBool+=1
            dirFunc[actualFunc]['parBool'] += 1
            dirFunc[actualFunc]['locBool'] += 1
            dirFunc[actualFunc]['secPars'] += 'b'

        #Simple variable
        if p[-1]!=']':
            #Name of var (ID)
            nv = p[-1]
            dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':0, 'dirVar' : direc}
        else:
            # print('p de arreglo o matriz',p)
            #Array
            if p[-3] != ',':
                #Name of var (ID)
                nv = p[-4]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':1, 'dirVar' : direc}
                inf = 0
                sup = p[-2]
                dim = 1
                r = 1
                r = (sup+1)*r
                m0 = r
                dirFunc[actualFunc]['vars'][nv]['size'] = m0
                print('m0',m0)
                offset = 0
                n = Node(inf, sup, 0)
                ll = LinkedList(n)
                dirFunc[actualFunc]['vars'][nv]['llDims'] = ll
                dirFunc[actualFunc]['vars'][nv]['llDims'].printList()

                for x in range(m0-1):
                    print('m0',m0)
                    print('actualFunc',actualFunc)
                    direc = None
                    if tipoVar == 'int':
                        direc = locInt
                        locInt+=1
                        dirFunc[actualFunc]['locInt'] += 1
                    elif tipoVar == 'float':
                        direc = locFloat
                        locFloat+=1
                        dirFunc[actualFunc]['locFloat'] += 1
                    elif tipoVar == 'string':
                        direc = locString
                        locString+=1
                        dirFunc[actualFunc]['locString'] += 1
                    elif tipoVar == 'bool':
                        direc = locBool
                        locBool+=1
                        dirFunc[actualFunc]['locBool'] += 1
            #Matrix
            else:
                #Name of var (ID)
                nv = p[-6]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':2, 'dirVar' : direc}
                inf = 0
                sup = p[-4]
                inf2 = 0
                sup2 = p[-2]

                r=1
                dim = 1
                r = sup+1
                r = r *(sup2 + 1)
                m0 = r
                dirFunc[actualFunc]['vars'][nv]['size'] = r
                # print('m0',m0)
                m1 = m0/(sup+1)
                m1 = int(m1)
                n = Node(inf,sup,m1)
                ll = LinkedList(n)
                m2 = m1/(sup2+1)
                ll.add(inf,sup2,0)
                dirFunc[actualFunc]['vars'][nv]['llDims'] = ll
                dirFunc[actualFunc]['vars'][nv]['llDims'].printList()
                for x in range(m0-1):
                    print('m0',m0)
                    print('actualFunc',actualFunc)
                    direc = None
                    if tipoVar == 'int':
                        direc = locInt
                        locInt+=1
                        dirFunc[actualFunc]['locInt'] += 1
                    elif tipoVar == 'float':
                        direc = locFloat
                        locFloat+=1
                        dirFunc[actualFunc]['locFloat'] += 1
                    elif tipoVar == 'string':
                        direc = locString
                        locString+=1
                        dirFunc[actualFunc]['locString'] += 1
                    elif tipoVar == 'bool':
                        direc = locBool
                        locBool+=1
                        dirFunc[actualFunc]['locBool'] += 1

def p_guardarTipoVar(p):
    '''
    guardarTipoVar :
    '''
    global tipoVar
    tipoVar = p[-1]

def p_guardarTipoFunc(p):
    '''
    guardarTipoFunc :
    '''
    global tipoFunc
    tipoFunc = p[-1]

def p_mainfunction(p):
    '''
    mainfunction : func main agregaFunc PARIZQ PARDER fillMain bloque
    '''

def p_fillMain(p):
    '''
    fillMain :
    '''
    fill(1,contCuadruplos)

def p_bloque(p):
    '''
    bloque : LLAVEIZQ bloqueaux LLAVEDER
           | LLAVEIZQ empty LLAVEDER
    '''

def p_bloqueaux(p):
    '''
    bloqueaux : estatuto bloqueaux
              | estatuto
    '''

def p_type(p):
    '''
    type : int guardarTipoVar
         | float guardarTipoVar
         | string guardarTipoVar
         | bool guardarTipoVar
    '''

def p_function(p):
    '''
    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux agregaDir bloque cuadEndf
             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux agregaDir bloque cuadEndf
    '''

def p_agregaDir(p):
    '''
    agregaDir :
    '''
    dirFunc[actualFunc]['dirFunc'] = contCuadruplos

def p_cuadEndf(p):
    '''
    cuadEndf :
    '''
    global contCuadruplos
    global listaCuadruplos
    global locInt
    global locFloat
    global locString
    global locBool
    global tempInt
    global tempFloat
    global tempString
    global tempBool
    cuad = [contCuadruplos, 'endfunc']
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplo', cuad)
    contCuadruplos += 1
    locInt = locIntInf
    locFloat = locFloatInf
    locString = locStringInf
    locBool = locBoolInf
    tempInt = tempIntInf
    tempFloat = tempFloatInf
    tempString = tempStringInf
    tempBool = tempBoolInf
    # dirFunc[actualFunc]['vars'] = {}

def p_agregaFunc(p):
    '''
    agregaFunc :
    '''
    global actualFunc
    global tipoFunc
    if(p[-1]=='main'):
        actualFunc = progName
    else:
        t = tipoFunc
        actualFunc = p[-1]
        dirFunc[actualFunc] = {'type': t, 'dirFunc': None
                             , 'locInt':0, 'locFloat':0, 'locString':0, 'locBool':0
                             , 'parInt':0, 'parFloat':0, 'parString':0, 'parBool':0, 'parListInt':0, 'parListFloat':0, 'parListString':0, 'parListBool':0
                             , 'tempInt':0, 'tempFloat':0, 'tempString':0, 'tempBool':0, 'tempPointer':0
                             , 'secPars':'', 'vars' : {}}

#Function types
def p_ftype(p):
    '''
    ftype : int guardarTipoFunc
          | float guardarTipoFunc
          | string guardarTipoFunc
          | bool guardarTipoFunc
          | void guardarTipoFunc
    '''

def p_funcaux(p):
    '''
    funcaux : type ID agregaPar masParam
            | type ID CORIZQ CTEINT CORDER agregaPar masParam
            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaPar masParam
    '''

def p_masParam(p):
    '''
    masParam : COMA funcaux
             | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
             | escritura
             | llamada PYC
             | condicion
             | whileloop
             | forloop
             | lectura
             | estReturn
    '''

def p_asignacion(p):
    '''
    asignacion : ID checkID asignaux ASIGNA expresion cuadAsignacion PYC
               | ID checkID asignaux ASIGNA llamada_esp PYC
               | ID checkID asignaux ASIGNA CTESTRING cuadAsignacion PYC
    '''

def p_checkID(p):
    '''
    checkID :
    '''
    id = p[-1]
    print('ID EN ASIGNACION',p[-1])
    varExists = False
    global dirFunc
    global actualFunc
    global progName
    global reservadas
    global idParaLista
    if id in reservadas:
        sys.exit("Error: can't use {} as an ID name".format(id))
    varsInFunc = dirFunc[actualFunc]['vars']
    for key in varsInFunc:
        if key == id:
            varExists = True
    if varExists == False:
        varsInFunc = dirFunc[progName]['vars']
        for key in varsInFunc:
            if key == id:
                varExists = True
                break
    if varExists == False:
        sys.exit("Error: ID {} does not exist in the scope".format(id))
    else:
        idParaLista = id

def p_cuadAsignacion(p):
    '''
    cuadAsignacion :
    '''
    global listaCuadruplos
    global pilaOperandos
    global contCuadruplos
    global pilaTipos

    if(type(p[-1]) == str):
        pilaOperandos.append(p[-1].strip('"'))
        pilaTipos.append('string')

    print(p[-5])

    tipoID = checkType(p[-5])
    tipoAsigna = pilaTipos.pop()
    print("Tipo de {}".format(pilaOperandos[-1]), tipoAsigna)
    if(tipoID == tipoAsigna):
        varsInFunc = dirFunc[actualFunc]['vars']
        varLocal = p[-5] in varsInFunc.keys()
        aAsignar = pilaOperandos.pop()
        if varLocal:
            if(dirFunc[actualFunc]['vars'][p[-5]]['size']==1):
                direc = dirFunc[actualFunc]['vars'][p[-5]]['dirVar']
            else:
                try:
                    direc = pilaOperandos.pop()
                    pilaTipos.pop()
                except IndexError:
                    sys.exit('Error: you need to add some [] to {}'.format(p[-5]))
        else:
            if(dirFunc[progName]['vars'][p[-5]]['size']==1):
                direc = dirFunc[progName]['vars'][p[-5]]['dirVar']
            else:
                try:
                    direc = pilaOperandos.pop()
                    pilaTipos.pop()
                except IndexError:
                    sys.exit('Error: you need to add some [] to {}'.format(p[-5]))
        #Si es una expresión
        if(p[-1] is None):
            
            cuad = [contCuadruplos, '=', aAsignar,direc]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            contCuadruplos += 1
        elif(type(p[-1]) == str):
            cuad = [contCuadruplos, '=', aAsignar,direc]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            contCuadruplos += 1
    else:
        sys.exit("TypeMismatch Error: Id \"{}\" is {}, not {}".format(p[-5],tipoID,tipoAsigna))

def p_asignaux(p):
    '''
    asignaux : CORIZQ expresion CORDER pushOTAsig
             | CORIZQ expresion COMA expresion CORDER pushOTAsig
             | empty
    '''

def p_pushOTAsig(p):
    '''
    pushOTAsig :
    '''
    global idParaLista
    global pilaOperandos
    global pilaTipos
    global dirFunc
    global actualFunc
    global progName
    global tempInt
    global contCuadruplos
    global tempPointer
    if(p[-1] == ']'):
        #Array/Lista
        if(p[-3]!=','):
            #Nombre de variable/ID
            operando = idParaLista
            print('operando', operando)
            aVerificar = pilaOperandos.pop()
            pilaTipos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                lilist  = dirFunc[actualFunc]['vars'][operando]['llDims']
            else:
                lilist  = dirFunc[progName]['vars'][operando]['llDims']
            n = lilist.root
            inf = n.get_inf()
            sup = n.get_sup()
            k = n.get_k()
            cuad = [contCuadruplos, 'ver', aVerificar, inf, sup]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1
            
            cuad = [contCuadruplos, '+', aVerificar, (k*-1), tempInt]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplo',cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            tx = pilaOperandos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                dirB = dirFunc[actualFunc]['vars'][operando]['dirVar']
            else:
                dirB = dirFunc[progName]['vars'][operando]['dirVar']

            print('TX AJDKLAJFLAKSDJFÑLSAKDJFLKSDAJF', tx)
            print('DIRB AJASDLKFJSDAÑFLKJASLÑDKF', dirB)


            cuad = [contCuadruplos, '+', tx, dirB, tempPointer]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempPointer)
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                tipoEnElPointer = dirFunc[actualFunc]['vars'][operando]['type']
            else:
                tipoEnElPointer = dirFunc[progName]['vars'][operando]['type']
            print('METO EL TIPO POINTER #######################################', tipoEnElPointer)
            pilaTipos.append(tipoEnElPointer)
            contCuadruplos += 1
            tempPointer += 1
        #Matriz
        else:
            #Nombre de variable/ID
            operando = idParaLista
            aVerificar = pilaOperandos.pop()
            pilaTipos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                lilist  = dirFunc[actualFunc]['vars'][operando]['llDims']
            else:
                lilist  = dirFunc[progName]['vars'][operando]['llDims']
            n1 = lilist.root
            inf = n1.get_inf()
            sup = n1.get_sup()
            k = n1.get_k()
            try:
                sup2 = n1.next_node.get_sup()
            except AttributeError:
                sys.exit('Error: {} has not 2 dimensions'.format(operando))

            cuad = [contCuadruplos, 'ver', aVerificar, inf, sup]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1

            r=1
            r = sup+1
            r = r *(sup2 + 1)
            m0 = r
            m1 = m0/(sup+1)
            m1 = int(m1)

            cuad = [contCuadruplos, '*', aVerificar, m1, tempInt]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            aVerificar2 = pilaOperandos.pop()
            cuad = [contCuadruplos, 'ver', aVerificar2, inf, sup2]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1

            tx = pilaOperandos.pop()

            cuad = [contCuadruplos, '+', tx, aVerificar2, tempInt]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            ty = pilaOperandos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                dirB = dirFunc[actualFunc]['vars'][operando]['dirVar']
            else:
                dirB = dirFunc[progName]['vars'][operando]['dirVar']


            cuad = [contCuadruplos, '+', ty, dirB, tempPointer]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempPointer)
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                tipoEnElPointer = dirFunc[actualFunc]['vars'][operando]['type']
            else:
                tipoEnElPointer = dirFunc[progName]['vars'][operando]['type']
            pilaTipos.append(tipoEnElPointer)
            contCuadruplos += 1
            tempPointer += 1


def p_escritura(p):
    '''
    escritura : write PARIZQ escaux PARDER PYC
    '''

def p_escaux(p):
    '''
    escaux : expresion cuadEsc nextexp
           | CTESTRING cuadEsc nextexp
           | llamada_esp nextexp
           | llamada nextexp
    '''

def p_cuadEsc(p):
    '''
    cuadEsc :
    '''
    global contCuadruplos
    global listaCuadruplos
    global pilaOperandos
    global ctes
    global listaConstantes
    global pilaTipos
    #Lo que se va a escribir
    aesc = None
    # print('En el write',p[-1])
    #Expresion o llamada
    if(p[-1] is None):
        aesc = pilaOperandos.pop()
        pilaTipos.pop()
    #String
    elif(isinstance(p[-1], str)):
        # aesc = p[-1].strip('"')
        aesc = ctes
        listaConstantes[p[-1].strip('"')] = ctes
    cuad = [contCuadruplos, 'write', aesc]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    contCuadruplos += 1
    ctes += 1

#Para poner más de una expresión en un print
def p_nextexp(p):
    '''
    nextexp : COMA escaux
            | empty
    '''

def p_llamada(p):
    '''
    llamada : ID checkFunc cuadEra PARIZQ guardaFondo llamaux verPars PARDER cuadGoSub quitaFondo
            | ID checkFunc cuadEra PARIZQ PARDER
    '''

def p_pycopc(p):
    '''
    pycopc : PYC
           | empty
    '''

def p_llamaux(p):
    '''
    llamaux : expresion cuadPar nextparametro
            | llamada_esp cuadPar nextparametro
            | CTESTRING cuadPar nextparametro
    '''

def p_nextparametro(p):
    '''
    nextparametro : COMA llamaux
                  | empty
    '''

def p_checkFunc(p):
    '''
    checkFunc :
    '''
    print('------------------------', p[-1])
    existe = dirFunc.get(p[-1], -1) != -1
    if existe == False:
        sys.exit('Error: {} is not defined as a function'.format(p[-1]))

def p_cuadEra(p):
    '''
    cuadEra :
    '''
    global listaCuadruplos
    global contCuadruplos
    global funcACorrer
    funcACorrer = p[-2]
    
    numLoci = dirFunc[funcACorrer]['locInt']
    numLocf = dirFunc[funcACorrer]['locFloat']
    numLocs = dirFunc[funcACorrer]['locString']
    numLocb = dirFunc[funcACorrer]['locBool']
    numPari = dirFunc[funcACorrer]['parInt']
    numParf = dirFunc[funcACorrer]['parFloat']
    numPars = dirFunc[funcACorrer]['parString']
    numParb = dirFunc[funcACorrer]['parBool']
    numTempi = dirFunc[funcACorrer]['tempInt']
    numTempf = dirFunc[funcACorrer]['tempFloat']
    numTemps = dirFunc[funcACorrer]['tempString']
    numTempb = dirFunc[funcACorrer]['tempBool']
    
    cuad = [contCuadruplos, 'era', numLoci, numLocf, numLocs, numLocb
                                 , numPari, numParf, numPars, numParb
                                 , numTempi, numTempf, numTemps, numTempb]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    contCuadruplos += 1
    print('Funca',funcACorrer)

def p_cuadPar(p):
    '''
    cuadPar :
    '''
    global listaCuadruplos
    global contCuadruplos
    global pilaOperandos
    global pilaTipos
    global paramCounter
    global funcACorrer
    print('P[-1] de cuadPar',p[-1])
    if p[-1] is None:
        arg = pilaOperandos.pop()
        argType = pilaTipos.pop()
    else:
        if(p[-1] == 'true' or p[-1] == 'false'):
            arg = p[-1]
            argType = 'bool'
        else:
            arg = p[-1]
            argType = 'string'

    # funcACorrer = p[-5]
    secuencia = dirFunc[funcACorrer]['secPars']
    numPars = len(secuencia)
    print('PARAM COUNTER',paramCounter)
    print('NUMPARS',numPars)
    if paramCounter+1 > numPars:
        sys.exit('Error: The number of parameters on the call is incorrect')
    if argType == 'int':
        if secuencia[paramCounter] == 'i':
            paramCounter += 1
        else:
            sys.exit('Error: {}\'s parameter number {} is not int'.format(funcACorrer,paramCounter+1))
    elif argType == 'float':
        if secuencia[paramCounter] == 'f':
            paramCounter += 1
        else:
            sys.exit('Error: {}\'s parameter number {} is not float'.format(funcACorrer,paramCounter+1))
    elif argType == 'string':
        if secuencia[paramCounter] == 's':
            paramCounter += 1
        else:
            sys.exit('Error: {}\'s parameter number {} is not string'.format(funcACorrer,paramCounter+1))
    elif argType == 'bool':
        if secuencia[paramCounter] == 'b':
            paramCounter += 1
        else:
            sys.exit('Error: {}\'s parameter number {} is not bool'.format(funcACorrer,paramCounter+1))
    parNum = 'par'+str(paramCounter)
    cuad = [contCuadruplos, 'par', arg, parNum]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    contCuadruplos += 1


def p_verPars(p):
    '''
    verPars :
    '''
    global paramCounter
    global funcACorrer
    # funcACorrer = p[-7]
    secuencia = dirFunc[funcACorrer]['secPars']
    print('PARAM COUNTER',paramCounter)
    print('NUMPARS', len(secuencia))
    if paramCounter != len(secuencia):
        sys.exit('Error: {} needs to have {} parameters'.format(funcACorrer,len(secuencia)))
    else:
        #Reiniciamos paramCounter para la siguiente llamada
        paramCounter = 0

def p_cuadGoSub(p):
    '''
    cuadGoSub :
    '''
    global listaCuadruplos
    global contCuadruplos
    global funcACorrer
    global globInt
    global globFloat
    global globString
    global globBool
    global tempInt
    global tempFloat
    global tempString
    global tempBool
    # funcACorrer = p[-9]
    dirDeFunc = dirFunc[funcACorrer]['dirFunc']
    cuad = [contCuadruplos, 'gosub', funcACorrer, dirDeFunc]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    contCuadruplos += 1
    #Si la función no es void tiene que guardar lo que retorna en una variable
    if(dirFunc[funcACorrer]['type'] != 'void'):
        tFunc = dirFunc[funcACorrer]['type']
        #Si aún no existe una variable de la función
        #Si ya existe no es necesario crear la variable, solo hacer el cuadruplo
        if(dirFunc[progName]['vars'].get(funcACorrer,-1) == -1):
            #Tipo de la función
            if tFunc == 'int':
                dirFunc[progName]['vars'][funcACorrer] = {'type':tFunc, 'dimensions':0, 'dirVar':globInt}
                dirFunc[progName]['globInt'] += 1
                globInt+=1
            elif tFunc == 'float':
                dirFunc[progName]['vars'][funcACorrer] = {'type':tFunc, 'dimensions':0, 'dirVar':globFloat}
                dirFunc[progName]['globFloat'] += 1
                globFloat+=1
            elif tFunc == 'string':
                dirFunc[progName]['vars'][funcACorrer] = {'type':tFunc, 'dimensions':0, 'dirVar':globString}
                dirFunc[progName]['globString'] += 1
                globString+=1
            elif tFunc == 'bool':
                dirFunc[progName]['vars'][funcACorrer] = {'type':tFunc, 'dimensions':0, 'dirVar':globBool}
                dirFunc[progName]['globBool'] += 1
                globBool+=1
        
        direc = dirFunc[progName]['vars'][funcACorrer]['dirVar']
        if tFunc == 'int':
            cuad = [contCuadruplos, '=', direc, tempInt]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempInt)
            pilaTipos.append('int')
            dirFunc[actualFunc]['tempInt'] += 1
            contCuadruplos += 1
            tempInt += 1
        elif tFunc == 'float':
            cuad = [contCuadruplos, '=', direc, tempFloat]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempFloat)
            pilaTipos.append('float')
            dirFunc[actualFunc]['tempFloat'] += 1
            contCuadruplos += 1
            tempFloat += 1
        elif tFunc == 'string':
            cuad = [contCuadruplos, '=', direc, tempString]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempString)
            pilaTipos.append('string')
            dirFunc[actualFunc]['tempString'] += 1
            contCuadruplos += 1
            tempString += 1
        elif tFunc == 'bool':
            cuad = [contCuadruplos, '=', direc, tempBool]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            pilaOperandos.append(tempBool)
            pilaTipos.append('bool')
            dirFunc[actualFunc]['tempBool'] += 1
            contCuadruplos += 1
            tempBool += 1

def p_condicion(p):
    '''
    condicion : if PARIZQ expresion PARDER cuadGotof bloque condicionAux cuadFinIf
    '''

def p_condicionAux(p):
    '''
    condicionAux : else cuadGoto bloque
                 | empty
    '''

def p_whileloop(p):
    '''
    whileloop : while migaja PARIZQ expresion PARDER cuadGotof bloque cuadFinWhile
    '''

def p_migaja(p):
    '''
    migaja :
    '''
    global pilaSaltos
    global contCuadruplos
    pilaSaltos.append(contCuadruplos)

def p_cuadFinWhile(p):
    '''
    cuadFinWhile :
    '''
    global pilaSaltos
    global listaCuadruplos
    global contCuadruplos
    end = pilaSaltos.pop()
    #Return -> a que cuadruplo tenemos que regresar
    ret = pilaSaltos.pop()
    cuad = [contCuadruplos, 'goto', ret]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    contCuadruplos += 1
    fill(end, contCuadruplos)

def p_forloop(p):
    '''
    forloop : for PARIZQ expresion checkExpFor DOSPUNTOS expresion checkExpFor PARDER gotoFor bloque returnFor
    '''

def p_checkExpFor(p):
    '''
    checkExpFor :
    '''
    global pilaOperandos
    global poper
    global pilaTipos
    # print("PILA OPERANDOS FOR", pilaOperandos)
    # print("POPER EN FOR", poper)
    # print("TIPOS EN FOR", pilaTipos)
    if (pilaTipos[-1] != 'int'):
        sys.exit("TypeMismatch Error: Expresions inside a for loop have to be int")
    else:
        pass

#GotoF del for
def p_gotoFor(p):
    '''
    gotoFor :
    '''
    global listaCuadruplos
    global pilaOperandos
    global pilaTipos
    global contCuadruplos
    global pilaSaltos
    global tempInt
    global tempBool
    rightOp = pilaOperandos.pop()
    rightType = pilaTipos.pop()
    leftOp =  pilaOperandos.pop()
    leftType = pilaTipos.pop()

    #Asignamos el primer valor a un temporal
    cuad = [contCuadruplos, '=', leftOp, tempInt]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    pilaOperandos.append(tempInt)
    dirFunc[actualFunc]['tempInt'] += 1
    contCuadruplos += 1
    tempInt += 1

    #Asignamos el segundo valor a un temporal
    cuad = [contCuadruplos, '=', rightOp, tempInt]
    listaCuadruplos.append(cuad)
    print('Generamos cuadruplos',cuad)
    pilaOperandos.append(tempInt)
    dirFunc[actualFunc]['tempInt'] += 1
    contCuadruplos += 1
    tempInt += 1

    #A este punto tendremos que regresar
    pilaSaltos.append(contCuadruplos)

    # Revisamos si el de la izquierda es menor al de la derecha para el gotof
    rightOp = pilaOperandos.pop()
    leftOp =  pilaOperandos.pop()
    pilaTipos.append('int')
    pilaTipos.append('int')
    typeResult = cuboSemantico(pilaTipos.pop(), pilaTipos.pop(), '<=')
    cuad = [contCuadruplos, '<=', leftOp, rightOp, tempBool]
    pilaOperandos.append(leftOp)
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    pilaOperandos.append(tempBool)
    dirFunc[actualFunc]['tempBool'] += 1
    pilaTipos.append(typeList[typeResult])
    tempBool += 1
    contCuadruplos += 1

    #A este cuadruplo tendremos que llenar el gotof
    pilaSaltos.append(contCuadruplos)

    #Resultado para ver si hace lo del for
    result = pilaOperandos.pop()
    pilaTipos.pop()
    cuad = [contCuadruplos, 'gotof', result]
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    contCuadruplos += 1

def p_returnFor(p):
    '''
    returnFor :
    '''
    global listaCuadruplos
    global pilaOperandos
    global pilaTipos
    global contCuadruplos
    global pilaSaltos
    global tempInt
    #A donde hacemos el goto
    toFill = pilaSaltos.pop()
    ret = pilaSaltos.pop()
    aSumar = pilaOperandos.pop()
    
    cuad = [contCuadruplos, '+', aSumar, 1, tempInt]
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    pilaOperandos.append(tempInt)
    dirFunc[actualFunc]['tempInt'] += 1
    pilaTipos.append('int')
    tempInt += 1
    contCuadruplos += 1

    #Asignamos la suma de 1 al primer valor del for
    cuad = [contCuadruplos, '=', pilaOperandos.pop(), aSumar]
    pilaTipos.pop()
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    contCuadruplos += 1

    #Regresamos y rellenamos el gotof del principio
    
    cuad = [contCuadruplos, 'goto', ret]
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    contCuadruplos += 1
    fill(toFill, contCuadruplos)



def p_lectura(p):
    '''
    lectura : read PARIZQ ID checkID cuadRead PARDER PYC
    '''

def p_cuadRead(p):
    '''
    cuadRead :
    '''
    global listaCuadruplos
    global contCuadruplos
    aleer = p[-2]
    d = dirFunc[actualFunc]['vars'][aleer]['dirVar']
    cuad = [contCuadruplos,'read',d]
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    contCuadruplos += 1

def p_estReturn(p):
    '''
    estReturn : return PARIZQ retAux PARDER PYC
    '''

def p_retAux(p):
    '''
    retAux : expresion cuadRet
           | CTESTRING cuadRet
           | true cuadRet
           | false cuadRet
           | llamada cuadRet
    '''

def p_cuadRet(p):
    '''
    cuadRet :
    '''
    global listaCuadruplos
    global contCuadruplos
    global pilaOperandos
    global pilaTipos
    pasado = p[-1]
    #Es una expresión
    if(pasado is None):
        retVal = pilaOperandos.pop()
        retType = pilaTipos.pop()
    elif(isinstance(pasado, str)):
        if(pasado == 'true' or pasado == 'false'):
            retVal = pasado
            retType = 'bool'
        else:
            retVal = pasado
            retType = 'string'
    if(retType != dirFunc[actualFunc]['type']):
        sys.exit('Error: {} function has to return {} value'.format(actualFunc, dirFunc[actualFunc]['type']))
    else:
        cuad = [contCuadruplos, 'ret', retVal]
        listaCuadruplos.append(cuad)
        print("Generamos cuadruplo", cuad)
        contCuadruplos += 1


def p_expresion(p):
    '''
    expresion : andExpresion
              | andExpresion OR pushOper andExpresion
    '''

def p_andExpresion(p):
    '''
    andExpresion : relopExpresion
                 | relopExpresion AND pushOper relopExpresion
    '''

def p_relopExpresion(p):
    '''
    relopExpresion : aritExpresion cuadArit
                   | aritExpresion cuadArit relopAux aritExpresion cuadArit
    '''

def p_relopAux(p):
    '''
    relopAux : MAYORQUE pushOper 
             | MENORQUE pushOper 
             | EQUALS pushOper
             | DIFERENTE pushOper
    '''

def p_aritExpresion(p):
    '''
    aritExpresion : term
                  | term cuadTerm aritAux aritExpresion cuadTerm
    '''

def p_aritAux(p):
    '''
    aritAux : MAS pushOper
            | MENOS pushOper
    '''

def p_term(p):
    '''
    term : factor 
         | factor cuadFactor termAux term cuadFactor
    '''

def p_termAux(p):
    '''
    termAux : MULT pushOper
            | DIV pushOper
    '''

def p_factor(p):
    #Agregar representante de fondo falso
    #Agregar un operador que no use 
    '''
    factor : PARIZQ guardaFondo expresion PARDER quitaFondo
           | CTEINT pushOT
           | CTEFLOAT pushOT
           | true pushOT
           | false pushOT
           | ID checkIDfac pushOT
           | ID checkIDfac CORIZQ expresion CORDER pushOT
           | ID checkIDfac CORIZQ expresion COMA expresion CORDER pushOT
           | llamada_esp pushOT
           | CTESTRING pushOT
           | llamada
    '''

def p_checkIDfac(p):
    '''
    checkIDfac :
    '''
    id = p[-1]
    print('ID EN FACTOR',p[-1])
    varExists = False
    global dirFunc
    global actualFunc
    global progName
    global reservadas
    global idParaLista
    if id in reservadas:
        sys.exit("Error: can't use {} as an ID name".format(id))
    varsInFunc = dirFunc[actualFunc]['vars']
    for key in varsInFunc:
        if key == id:
            varExists = True
    if varExists == False:
        varsInFunc = dirFunc[progName]['vars']
        for key in varsInFunc:
            if key == id:
                varExists = True
                break
    if varExists == False:
        sys.exit("Error: ID {} does not exist in the scope".format(id))

def p_guardaFondo(p):
    '''
    guardaFondo :
    '''
    global poper
    poper.append('?')

def p_quitaFondo(p):
    '''
    quitaFondo :
    '''
    global poper
    # print('Qutifondo',poper[-1])
    poper.pop()

def p_llamada_esp(p):
    '''
    llamada_esp : ID PUNTO especiales PARIZQ PARDER
    '''

def p_especiales(p):
    '''
    especiales : length
               | max
               | min
               | avg
               | median
               | mode
               | variance
               | stdev
               | graph
    '''

def p_pushOper(p):
    '''
    pushOper :
    '''
    global poper
    poper.append(p[-1])

def p_pushOT(p):
    '''
    pushOT :
    '''
    # | ID checkID CORIZQ CTEINT CORDER pushOT
    # | ID checkID CORIZQ CTEINT COMA CTEINT CORDER pushOT
    global pilaOperandos
    global pilaTipos
    global dirFunc
    global actualFunc
    global progName
    global ctes
    global listaConstantes
    global tempInt
    global contCuadruplos
    global tempPointer
    print('p[-1] de factor = {}'.format(p[-1]))
    #Lista o Matriz
    if(p[-1] == ']'):
        #Array/Lista
        if(p[-3]!=','):
            print('ESTOY EN PUSHOT SIENDO UNA LISTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            #Nombre de variable/ID
            operando = p[-5]
            print('operando', operando)
            aVerificar = pilaOperandos.pop()
            pilaTipos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                lilist  = dirFunc[actualFunc]['vars'][operando]['llDims']
            else:
                lilist  = dirFunc[progName]['vars'][operando]['llDims']
            n = lilist.root
            inf = n.get_inf()
            sup = n.get_sup()
            k = n.get_k()

            cuad = [contCuadruplos, 'ver', aVerificar, inf, sup]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1
            
            #+ S1 (-k) tx -> k siempre es 0 este cuadruplo es innecesario
            cuad = [contCuadruplos, '+', aVerificar, (k*-1), tempInt]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            tx = pilaOperandos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                dirB = dirFunc[actualFunc]['vars'][operando]['dirVar']
            else:
                dirB = dirFunc[progName]['vars'][operando]['dirVar']

            print('TX AJDKLAJFLAKSDJFÑLSAKDJFLKSDAJF', tx)
            print('DIRB AJASDLKFJSDAÑFLKJASLÑDKF', dirB)

            cuad = [contCuadruplos, '+', tx, dirB, tempPointer]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempPointer)
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                tipoEnElPointer = dirFunc[actualFunc]['vars'][operando]['type']
            else:
                tipoEnElPointer = dirFunc[progName]['vars'][operando]['type']
            pilaTipos.append(tipoEnElPointer)
            contCuadruplos += 1
            tempPointer += 1
        #Matriz
        else:
            print('ESTOY EN PUSHOT SIENDO UNA MATRIZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
            #Nombre de variable/ID
            operando = p[-7]
            aVerificar = pilaOperandos.pop()
            pilaTipos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                lilist  = dirFunc[actualFunc]['vars'][operando]['llDims']
            else:
                lilist  = dirFunc[progName]['vars'][operando]['llDims']
            n1 = lilist.root
            inf = n1.get_inf()
            sup = n1.get_sup()
            k = n1.next_node.get_k()
            sup2 = n1.next_node.get_sup()

            cuad = [contCuadruplos, 'ver', aVerificar, inf, sup]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1

            r=1
            r = sup+1
            r = r *(sup2 + 1)
            m0 = r
            m1 = m0/(sup+1)
            m1 = int(m1)

            cuad = [contCuadruplos, '*', aVerificar, m1, tempInt]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            aVerificar2 = pilaOperandos.pop()
            pilaTipos.pop()
            cuad = [contCuadruplos, 'ver', aVerificar2, inf, sup2]
            listaCuadruplos.append(cuad)
            print('Generamos cuadruplos',cuad)
            contCuadruplos += 1

            tx = pilaOperandos.pop()

            cuad = [contCuadruplos, '+', tx, aVerificar2, tempInt]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1


            cuad = [contCuadruplos, '+', aVerificar, (k*-1), tempInt]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempInt)
            contCuadruplos += 1
            tempInt += 1

            ty = pilaOperandos.pop()
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                dirB = dirFunc[actualFunc]['vars'][operando]['dirVar']
            else:
                dirB = dirFunc[progName]['vars'][operando]['dirVar']

            cuad = [contCuadruplos, '+', ty, dirB, tempPointer]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempPointer)
            if(dirFunc[actualFunc]['vars'].get(operando,-1) != -1):
                tipoEnElPointer = dirFunc[actualFunc]['vars'][operando]['type']
            else:
                tipoEnElPointer = dirFunc[progName]['vars'][operando]['type']
            pilaTipos.append(tipoEnElPointer)
            contCuadruplos += 1
            tempPointer += 1

    #Constantes
    elif p[-1] != None:
        operando = p[-1]
        existe = listaConstantes.get(operando,-1)
        if(existe == -1):
            dirConst = ctes
            ctes += 1
            pilaOperandos.append(dirConst)
            if(isinstance(operando,str)):
                listaConstantes[operando.strip('"')] = dirConst
            else:
                listaConstantes[operando] = dirConst
        else:
            pilaOperandos.append(listaConstantes[operando])
        
        #En este if revisamos que tipo es el factor para agregarlo a la pila de tipos
        
        #Si el número es entero
        if(isinstance(operando, int)):
            pilaTipos.append('int')
        elif(isinstance(operando, float)):
            pilaTipos.append('float')
        #Si es un string significa que es un ID (variable)
        elif(isinstance(operando, str)):
            #Si es una constante boolena 'true' o 'false'
            if(operando == 'true' or operando == 'false'):
                pilaTipos.append('bool')
            else:
                #Revisamos si la variable usada es local o global
                varsInFunc = dirFunc[actualFunc]['vars']
                varLocal = operando in varsInFunc.keys()
                if varLocal:
                    pilaTipos.append(dirFunc[actualFunc]['vars'][operando]['type'])
                else:
                    noesconst = dirFunc[progName]['vars'].get(operando,-1)
                    if noesconst!=-1:
                        pilaTipos.append(dirFunc[progName]['vars'][operando]['type'])
                    else:
                        pilaTipos.append('string')



    #Si es un ID porque está el checkID que es None
    else:
        operando = p[-2]
        varsInFunc = dirFunc[actualFunc]['vars']
        varLocal = operando in varsInFunc.keys()
        if varLocal:
            pilaOperandos.append(dirFunc[actualFunc]['vars'][operando]['dirVar'])
        else:
            # for c in listaCuadruplos:
            #     print(c)
            # print(pilaOperandos)
            pilaOperandos.append(dirFunc[progName]['vars'][operando]['dirVar'])
        

        #En este if revisamos que tipo es el factor para agregarlo a la pila de tipos
        
        #Si el número es entero
        if(isinstance(operando, int)):
            pilaTipos.append('int')
        elif(isinstance(operando, float)):
            pilaTipos.append('float')
        #Si es un string significa que es un ID (variable)
        elif(isinstance(operando, str)):
            #Si es una constante boolena 'true' o 'false'
            if(operando == 'true' or operando == 'false'):
                pilaTipos.append('bool')
            #Finalmente si es un ID
            else:
                #Revisamos si la variable usada es local o global
                varsInFunc = dirFunc[actualFunc]['vars']
                varLocal = operando in varsInFunc.keys()
                if varLocal:
                    pilaTipos.append(dirFunc[actualFunc]['vars'][operando]['type'])
                else:
                    pilaTipos.append(dirFunc[progName]['vars'][operando]['type'])

def p_cuadTerm(p):
    '''
    cuadTerm :
    '''
    global poper
    global listaCuadruplos
    global pilaOperandos
    global contCuadruplos
    global tempInt
    global tempFloat
    global pilaTipos
    # print("Poper dentro de cuadTerm",poper)
    # try:
    #     print("Ultimo elemento de poper",poper[-1])
    # except:
    #     print("No hay último elemento", poper)
    hayOp = len(poper) >= 1
    # print(hayOp)
    print('PilaO cuadTerm',pilaOperandos)
    print('PilaT cuadTerm',pilaTipos)
    if (hayOp and (poper[-1] == '+' or poper[-1] == '-')):
        rightOp = pilaOperandos.pop()
        right_type = pilaTipos.pop()
        leftOp = pilaOperandos.pop()
        left_type = pilaTipos.pop()
        operator = poper.pop()
        typeResult = cuboSemantico(left_type, right_type, operator)
        if typeResult != -1:
            #Si el resultado es int usamos el tempInt
            if(typeResult == 0):
                cuad = [contCuadruplos, operator, leftOp, rightOp, tempInt]
                listaCuadruplos.append(cuad)
                print("Generamos cuadruplo", cuad)
                pilaOperandos.append(tempInt)
                dirFunc[actualFunc]['tempInt'] += 1
                pilaTipos.append(typeList[typeResult])
                tempInt += 1
                contCuadruplos += 1
            #El resultado es float
            else:
                cuad = [contCuadruplos, operator, leftOp, rightOp, tempFloat]
                listaCuadruplos.append(cuad)
                print("Generamos cuadruplo", cuad)
                pilaOperandos.append(tempFloat)
                dirFunc[actualFunc]['tempFloat'] += 1
                pilaTipos.append(typeList[typeResult])
                tempFloat += 1
                contCuadruplos += 1
        else:
            sys.exit("TypeError : {} and {} cannot use operator {}".format(left_type, right_type, operator))

def p_cuadFactor(p):
    '''
    cuadFactor :
    '''
    global poper
    global listaCuadruplos
    global typeList
    global contCuadruplos
    global tempInt
    global tempFloat
    # print("Poper dentro de cuadTerm",poper)
    # try:
    #     print("Ultimo elemento de poper",poper[-1])
    # except:
    #     print("No hay último elemento", poper)
    hayOp = len(poper) >= 1
    # print(hayOp)
    print('PilaO cuadFactor',pilaOperandos)
    print('PilaT cuadFactor',pilaTipos)
    if (hayOp and (poper[-1] == '*' or poper[-1] == '/')):
        rightOp = pilaOperandos.pop()
        right_type = pilaTipos.pop()
        leftOp = pilaOperandos.pop()
        left_type = pilaTipos.pop()
        operator = poper.pop()
        typeResult = cuboSemantico(left_type, right_type, operator)
        if typeResult != -1:
            if(typeResult == 0):
                cuad = [contCuadruplos, operator, leftOp, rightOp, tempInt]
                listaCuadruplos.append(cuad)
                print("Generamos cuadruplo", cuad)
                pilaOperandos.append(tempInt)
                dirFunc[actualFunc]['tempInt'] += 1
                pilaTipos.append(typeList[typeResult])
                tempInt += 1
                contCuadruplos += 1
            else:
                cuad = [contCuadruplos, operator, leftOp, rightOp, tempFloat]
                listaCuadruplos.append(cuad)
                print("Generamos cuadruplo", cuad)
                pilaOperandos.append(tempFloat)
                dirFunc[actualFunc]['tempFloat'] += 1
                pilaTipos.append(typeList[typeResult])
                tempFloat += 1
                contCuadruplos += 1
        else:
            sys.exit("TypeError : {} and {} cannot use operator {}".format(left_type, right_type, operator))
    else:
        pass


def p_cuadArit(p):
    '''
    cuadArit :
    '''
    global poper
    global listaCuadruplos
    global pilaOperandos
    global contCuadruplos
    global tempBool
    # print("Poper dentro de cuadTerm",poper)
    # try:
    #     print("Ultimo elemento de poper",poper[-1])
    # except:
    #     print("No hay último elemento", poper)
    hayOp = len(poper) >= 1
    # print(hayOp)
    print(pilaOperandos)
    print(pilaTipos)
    if (hayOp and (poper[-1] == '<' or poper[-1] == '>'
                or poper[-1] == '<=' or poper[-1] == '>='
                or poper[-1] == '==' or poper[-1] == '$')):
        rightOp = pilaOperandos.pop()
        right_type = pilaTipos.pop()
        leftOp = pilaOperandos.pop()
        left_type = pilaTipos.pop()
        operator = poper.pop()
        typeResult = cuboSemantico(left_type, right_type, operator)
        if typeResult != -1:
            cuad = [contCuadruplos, operator, leftOp, rightOp, tempBool]
            listaCuadruplos.append(cuad)
            print("Generamos cuadruplo", cuad)
            pilaOperandos.append(tempBool)
            dirFunc[actualFunc]['tempBool'] += 1
            pilaTipos.append(typeList[typeResult])
            tempBool += 1
            contCuadruplos += 1
        else:
            sys.exit("TypeError : {} and {} cannot use operator {}".format(left_type, right_type, operator))

def p_cuadGotof(p):
    '''
    cuadGotof : 
    '''
    global pilaTipos
    global pilaOperandos
    global contCuadruplos
    global listaCuadruplos
    global pilaSaltos
    exp_type = pilaTipos.pop()
    # print(exp_type)
    if(exp_type != 'bool'):
        sys.exit("Type-mismatch Error: expression inside the if has to be bool")
    else:
        result = pilaOperandos.pop()
        cuad = [contCuadruplos, 'gotof', result]
        listaCuadruplos.append(cuad)
        print("Generamos cuadruplo", cuad)
        pilaSaltos.append(contCuadruplos)
        contCuadruplos += 1

def p_cuadFinIf(p):
    '''
    cuadFinIf :
    '''
    global pilaSaltos
    global contCuadruplos
    end = pilaSaltos.pop()
    fill(end, contCuadruplos)

def p_cuadGoto(p):
    '''
    cuadGoto :
    '''
    global listaCuadruplos
    global contCuadruplos
    global pilaSaltos
    cuad = [contCuadruplos, 'goto']
    listaCuadruplos.append(cuad)
    print("Generamos cuadruplo", cuad)
    contCuadruplos += 1
    #False -> la expresión del if fue falsa
    fal = pilaSaltos.pop()
    pilaSaltos.append(contCuadruplos-1)
    fill(fal, contCuadruplos)



def p_empty(p):
    '''
    empty : 
    '''

def p_error(p):
    print(p)
    print("Syntax error")
    sys.exit()

parser = yacc.yacc()

# parser.parse(data)
# fn = input("Nombre del archivo\n")

arch = input('¿Qué archivo quieres abrir?\n')
arch = './' + arch
try:
    f = open(arch, "r")
    fileContent = f.read()
    # print(fileContent)
except:
    print("Hubo un error con el archivo")
    pass

parser.parse(fileContent)

# PRINTS DEBUGGEO ------------------------------------------------

funcs = list(dirFunc)

for f in funcs:
    attrs = list(dirFunc[f])
    print(f)
    # print(dirFunc[f],'\n')
    for a in attrs:
        print('    ',a,dirFunc[f][a])

print('Pila operandos\n',pilaOperandos)
print('Pila Tipos\n', pilaTipos)
print('Pila operadores\n', poper)
print('Pila de saltos\n', pilaSaltos)
print('Lista de constantes')
consts = list(listaConstantes)
# print('list(constantes)',consts)
for co in consts:
    print(co,listaConstantes[co])
print()
for c in listaCuadruplos:
    print(c)
tempi = dirFunc[progName]['tempInt']
tempf = dirFunc[progName]['tempFloat']
temps = dirFunc[progName]['tempString']
tempb = dirFunc[progName]['tempBool']
maq(listaCuadruplos,dirFunc[progName]['vars'],listaConstantes,tempi,tempf,temps,tempb)

# -----------------------------------------------------------------

# while True:
#     try:
#         s = input()
#     except EOFError:
#         break
#     parser.parse(s)
#     # print(result)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
