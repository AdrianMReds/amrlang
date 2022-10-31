#Adrián Montemayor Rojas
#A01283139

#Pendiente y cambios
#Pendiente
#No se pueden poner arreglos o matrices como parametros de funciones

#Cambios:
# Programa, main y function en grámatica hay que agregarle el regreso de vars --ver nuevos diagramas--

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
    else:
        return -1

reservadas = ['program', 'var', 'func', 'main', 'int', 'float', 'string', 'bool',
              'write', 'if', 'else', 'while', 'for', 'read', 'void', 'end', 'length',
              'max', 'min', 'avg', 'median', 'mode', 'variance', 'stdev']

tokens = reservadas + ['ID', #NOMBRE DE VARIABLE O FUNCIÓN
                       'CTEINT', #CONSTANTE INT
                       'CTEFLOAT', #CONSTANTE FLOAT
                       'CTESTRING', #CONSTANTE STRING
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
        program ejemplo;
var int x, y, z[5];

func main(){
write("Hola");
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
    funcaux : type ID agregaVar
            | type ID agregaVar COMA funcaux
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
    asignacion : ID asignaux ASIGNA expresion PYC
               | ID asignaux ASIGNA llamada_esp PYC
               | ID asignaux ASIGNA CTESTRING PYC
    '''

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
    lectura : read PARIZQ ID PARDER PYC
    '''

def p_expresion(p):
    '''
    expresion : andExpresion
              | andExpresion OR andExpresion
    '''

def p_andExpresion(p):
    '''
    andExpresion : relopExpresion
                 | relopExpresion AND relopExpresion
    '''

def p_relopExpresion(p):
    '''
    relopExpresion : aritExpresion
                   | aritExpresion MAYORQUE aritExpresion
                   | aritExpresion MENORQUE aritExpresion
                   | aritExpresion MAYORIGUAL aritExpresion
                   | aritExpresion MENORIGUAL aritExpresion
                   | aritExpresion EQUALS aritExpresion
                   | aritExpresion DIFERENTE aritExpresion
    '''

def p_aritExpresion(p):
    '''
    aritExpresion : term
                  | term MAS term
                  | term MENOS term
    '''

def p_term(p):
    '''
    term : factor
         | factor MULT factor
         | factor DIV factor
    '''

def p_factor(p):
    '''
    factor : PARIZQ expresion PARDER
           | CTEINT
           | CTEFLOAT
           | ID
           | llamada_esp
    '''

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
    f = open("./ejemplo.txt", "r")
    fileContent = f.read()
    # print(fileContent)
except:
    print("Hubo un error con el archivo")
    pass

parser.parse(fileContent)

funcs = list(dirFunc)

for f in funcs:
    print(f)
    print(dirFunc[f],'\n')

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