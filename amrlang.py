#Adrián Montemayor Rojas
#A01283139

#Pendiente y cambios
#Pendiente
#Se tiene que agregar asignación de índices de arreglos y matrices
#Guardar el tamaño de listas y matrices cuando se guarda la variable

#Cambios:

import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys

# -1 = error
# 0 = int
# 1 = float
# 2 = string
# 3 = bool

typeList = ['int', 'float', 'string', 'bool']

def cuboSemantico(op1, op2, operador) -> int:
    print("se revisa el tipo {} {} {}".format(op1,operador,op2))
    if operador == '+':
        if op1 == 'int' and op2 == 'int':
            return 0
        elif op1 == 'float' and op2 == 'float':
            return 1
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 1
        else:
            return -1
    elif operador == '-':
        if op1 == 'int' and op2 == 'int':
            return 0
        elif op1 == 'float' and op2 == 'float':
            return 1
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 1
        else:
            return -1
    elif operador == '*':
        if op1 == 'int' and op2 == 'int':
            return 0
        elif op1 == 'float' and op2 == 'float':
            return 1
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 1
        else:
            return -1
    elif operador == '/':
        if op1 == 'int' and op2 == 'int':
            return 1
        elif op1 == 'float' and op2 == 'float':
            return 1
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 1
        else:
            return -1
    elif operador == '>' or operador == '<':
        if op1 == 'int' and op2 == 'int':
            return 3
        elif op1 == 'float' and op2 == 'float':
            return 3
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 3
        else:
            return -1
    elif operador == '==' or operador == '$':
        if op1 == 'int' and op2 == 'int':
            return 3
        elif op1 == 'float' and op2 == 'float':
            return 3
        elif (op1 == 'int' and op2 == 'float') or (op1 == 'float' and op2 == 'int'):
            return 3
        elif op1 == 'string' and op2 == 'string':
            return 3
        elif op1 == 'bool' and op2 == 'bool':
            return 3
        else:
            return -1
    elif operador == '&&' or operador == '||':
        if op1 == 'bool' and op2 == 'bool':
            return 3
        else:
            return -1
    elif operador == '=':
        if op1 != op2:
            return -1
        else:
            return op1;
    else:
        return -1

reservadas = ['program', 'var', 'func', 'main', 'int', 'float', 'string', 'bool',
              'write', 'if', 'else', 'while', 'for', 'read', 'void', 'end', 'length',
              'max', 'min', 'avg', 'median', 'mode', 'variance', 'stdev', 'true', 'false']

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
                       'MAYORIGUAL',
                       'MENORIGUAL',
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

progName = ''
tipoVar = ''
tipoFunc = ''
actualFunc = ''
dirFunc = {}
dirVars = {}
listaCuadruplos = []
poper = []
pilaOperandos = []
pilaTipos = []
avail = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10'
         , 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20']
contAvail = 0

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
    t.value = int(t.value)
    return t

def t_CTESTRING(t):
    # r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
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
program amr;
var int x;
var bool b;

func main()
var float y;
{
    write("Hola");
    y = 2.0;
    y = y + 1;
    b = true;
}

end;

       '''

lexer.input(data)

#varsaux es P
#paux2 es F
def p_programa(p):
    '''
    programa : program ID auxprograma PYC varsaux paux2 mainfunction end PYC
    '''

def p_programa_vacio(p):
    '''
    programa : program auxprograma ID PYC empty mainfunction end PYC
    '''

def p_auxprograma(p):
    '''auxprograma :
    '''
    global progName
    progName = str(p[-1])
    t = 'program'
    dirFunc[progName] = {'type': t, 'vars' : {}}
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
    e = dirFunc.get(actualFunc,0)
    if e!=0:
        #Simple variable
        if p[-1]!=']':
            #Name of var (ID)
            nv = p[-1]
            dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':0}
        else:
            print('p de arreglo o matriz',p)
            #Array
            if p[-3] != ',':
                #Name of var (ID)
                nv = p[-4]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':1}
            #Matrix
            else:
                #Name of var (ID)
                nv = p[-6]
                dirFunc[actualFunc]['vars'][nv] = {'type':tipoVar, 'dimensions':2}

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
    mainfunction : func main agregaFunc PARIZQ PARDER varsaux bloque
                 | func main agregaFunc PARIZQ PARDER bloque
    '''

def p_agregaFunc(p):
    '''
    agregaFunc :
    '''
    global actualFunc
    global tipoFunc
    if p[-1]=='main':
        t = 'void'
        actualFunc = p[-1]
    else:
        t = tipoFunc
        actualFunc = p[-1]
    dirFunc[actualFunc] = {'type': tipoFunc, 'vars' : {}}

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
    function : ftype func ID agregaFunc PARIZQ funcaux PARDER varsaux bloque
             | ftype func ID agregaFunc PARIZQ empty PARDER varsaux bloque
    '''

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
    funcaux : type ID agregaVar masParam
            | type ID CORIZQ CTEINT CORDER agregaVar masParam
            | type ID CORIZQ CTEINT COMA CTEINT CORDER agregaVar masParam
    '''

def p_masParam(p):
    '''
    masParam : funcaux
             | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
             | escritura
             | llamada
             | condicion
             | whileloop
             | forloop
             | lectura
    '''

def p_asignacion(p):
    '''
    asignacion : ID checkID asignaux ASIGNA expresion cuadAsignacion PYC
               | ID checkID asignaux ASIGNA llamada_esp PYC
               | ID checkID asignaux ASIGNA CTESTRING PYC
    '''

def p_checkID(p):
    '''
    checkID :
    '''
    id = p[-1]
    varExists = False
    global dirFunc
    global actualFunc
    global progName
    global reservadas
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


def p_asignaux(p):
    '''
    asignaux : CORIZQ expresion CORDER
             | CORIZQ expresion COMA expresion CORDER
             | empty
    '''

def p_escritura(p):
    '''
    escritura : write PARIZQ escaux PARDER PYC
    '''

def p_escaux(p):
    '''
    escaux : expresion nextexp
           | CTESTRING nextexp
           | llamada_esp nextexp
    '''

#Para poner más de una expresión en un print
def p_nextexp(p):
    '''
    nextexp : COMA escaux
            | empty
    '''

def p_llamada(p):
    '''
    llamada : ID PARIZQ expresion llamaux PARDER
            | ID PARIZQ llamada_esp llamaux PARDER
            | ID PARIZQ PARDER
    '''

def p_llamaux(p):
    '''
    llamaux : expresion nextparametro
            | llamada_esp nextparametro
    '''

def p_nextparametro(p):
    '''
    nextparametro : COMA llamaux
                  | empty
    '''

def p_condicion(p):
    '''
    condicion : if PARIZQ expresion PARDER bloque
              | if PARIZQ expresion PARDER bloque else bloque
    '''

def p_whileloop(p):
    '''
    whileloop : while PARIZQ expresion PARDER bloque
    '''

def p_forloop(p):
    '''
    forloop : for PARIZQ expresion DOSPUNTOS expresion PARDER bloque
    '''

def p_lectura(p):
    '''
    lectura : read PARIZQ ID checkID PARDER PYC
    '''

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
    relopExpresion : aritExpresion
                   | aritExpresion relopAux aritExpresion
    '''

def p_relopAux(p):
    '''
    relopAux : MAYORQUE pushOper 
             | MENORQUE pushOper 
             | MAYORIGUAL pushOper
             | MENORIGUAL pushOper
             | EQUALS pushOper
             | DIFERENTE pushOper
    '''

def p_aritExpresion(p):
    '''
    aritExpresion : term cuadTerm
                  | term cuadTerm aritAux term cuadTerm
    '''

def p_p1(p):
    '''
    p1 : 
    '''
    print("Entrando a cuadTerm 1")

def p_p2(p):
    '''
    p2 : 
    '''
    print("Entrando a cuadTerm 2")

def p_aritAux(p):
    '''
    aritAux : MAS pushOper
            | MENOS pushOper
    '''

def p_term(p):
    '''
    term : factor 
         | factor cuadFactor termAux factor cuadFactor
    '''

def p_termAux(p):
    '''
    termAux : MULT pushOper
            | DIV pushOper
    '''

def p_factor(p):
    '''
    factor : PARIZQ expresion PARDER
           | CTEINT pushOT
           | CTEFLOAT pushOT
           | true pushOT
           | false pushOT
           | ID checkID pushOT
           | llamada_esp pushOT
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
    global pilaOperandos
    global pilaTipos
    global dirFunc
    global actualFunc
    global progName
    # print('p[-1] de factor = {}'.format(p[-1]))
    if p[-1] != None:
        operando = p[-1]
        pilaOperandos.append(operando)
    #Si es un ID porque está el checkID que es None
    else:
        operando = p[-2]
        pilaOperandos.append(operando)
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
    global avail
    global contAvail
    global pilaOperandos
    # print("Poper dentro de cuadTerm",poper)
    # try:
    #     print("Ultimo elemento de poper",poper[-1])
    # except:
    #     print("No hay último elemento", poper)
    hayOp = len(poper) >= 1
    # print(hayOp)
    print(pilaOperandos)
    print(pilaTipos)
    if (hayOp and (poper[-1] == '+' or poper[-1] == '-')):
        rightOp = pilaOperandos.pop()
        right_type = pilaTipos.pop()
        leftOp = pilaOperandos.pop()
        left_type = pilaTipos.pop()
        operator = poper.pop()
        typeResult = cuboSemantico(left_type, right_type, operator)
        if typeResult != -1:
            cuad = [operator, leftOp, rightOp, avail[contAvail]]
            print("Generamos cuadruplo", cuad)
            listaCuadruplos.append(cuad)
            pilaOperandos.append(avail[contAvail])
            pilaTipos.append(typeResult)
            contAvail += 1
        else:
            sys.exit("TypeError : {} and {} cannot use operator {}".format(left_type, right_type, operator))

def p_cuadFactor(p):
    '''
    cuadFactor :
    '''
    global poper
    global listaCuadruplos
    global avail
    global contAvail
    global typeList
    # print("Poper dentro de cuadTerm",poper)
    # try:
    #     print("Ultimo elemento de poper",poper[-1])
    # except:
    #     print("No hay último elemento", poper)
    hayOp = len(poper) >= 1
    # print(hayOp)
    print(pilaOperandos)
    print(pilaTipos)
    if (hayOp and (poper[-1] == '*' or poper[-1] == '/')):
        rightOp = pilaOperandos.pop()
        right_type = pilaTipos.pop()
        leftOp = pilaOperandos.pop()
        left_type = pilaTipos.pop()
        operator = poper.pop()
        typeResult = cuboSemantico(left_type, right_type, operator)
        if typeResult != -1:
            cuad = [operator, leftOp, rightOp, avail[contAvail]]
            print("Generamos cuadruplo", cuad)
            listaCuadruplos.append(cuad)
            pilaOperandos.append(avail[contAvail])
            pilaTipos.append(typeList[typeResult])
            contAvail += 1
        else:
            sys.exit("TypeError : {} and {} cannot use operator {}".format(left_type, right_type, operator))
    else:
        pass

def p_cuadAsignacion(p):
    '''
    cuadAsignacion :
    '''
    global listaCuadruplos
    global avail
    global contAvail
    global pilaOperandos
    print('p[-5]', p[-5])
    cuad = ['=', pilaOperandos.pop(),p[-5]]
    listaCuadruplos.append(cuad)

# def p_expresion(p):
#     '''
#     expresion : term 
#               | term MAS term
#               | term MENOS term
#     '''

# def p_term(p):
#     '''
#     term : fact
#          | fact MULT fact
#          | fact DIV fact
#     '''

# def p_fact(p):
#     '''
#     fact : CTEINT
#          | CTEFLOAT
#          | ID
#          | hyper_exp
#     '''

# def p_hyper_exp(p):
#     '''
#     hyper_exp : super_exp
#               | super_exp AND super_exp
#               | super_exp OR super_exp
#     '''

# def p_super_exp(p):
#     '''
#     super_exp : expresion
#               | expresion MAYORQUE expresion
#               | expresion MENORQUE expresion
#               | expresion EQUALS expresion
#               | expresion DIFERENTE expresion
#     '''

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
    '''


def p_empty(p):
    '''
    empty : 
    '''

def p_error(p):
    # print("Syntax error at '%s'" %p[0])
    print(p)
    print("Syntax error")
    sys.exit()

parser = yacc.yacc()

# parser.parse(data)
# fn = input("Nombre del archivo\n")

try:
    f = open("./ejemplo3.txt", "r")
    fileContent = f.read()
    # print(fileContent)
except:
    print("Hubo un error con el archivo")
    pass

parser.parse(fileContent)

# PRINTS DEBUGGEO ------------------------------------------------

funcs = list(dirFunc)

for f in funcs:
    print(f)
    print(dirFunc[f],'\n')

print('Pila operandos\n',pilaOperandos)
print('Pila Tipos\n', pilaTipos)
print('Pila operadores\n', poper)
for c in listaCuadruplos:
    print(c)
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