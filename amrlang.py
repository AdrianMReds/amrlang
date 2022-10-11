#Adrián Montemayor Rojas
#A01283139

#Pendiente y cambios
#Pendiente:
#Agregar llamadas especiales
#Agregar llamadas especiales a asignación y escritura?
#Checar si la parte de expresiones está bien
#Agregar void a palabras reservadas y a gramática de function
#Cambios:
# Programa, main y function en grámatica hay que agregarle el regreso de vars --ver nuevos diagramas--


import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys

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
    vars : var type guardarTipo vaux PYC
         | empty
    '''

def p_vaux(p):
    '''
    vaux : ID crearVar nextvar
         | ID CORIZQ CTEINT CORDER crearVar nextvar
         | ID CORIZQ CTEINT COMA CTEINT CORDER crearVar nextvar
    '''

def p_nextvar(p):
    '''
    nextvar : COMA vaux
            | empty
    '''

def p_crearVar(p):
    '''
    crearVar :
    '''
    print(p[-3])
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

def p_guardarTipo(p):
    '''
    guardarTipo :
    '''
    global tipoVar
    tipoVar = p[-1]

def p_mainfunction(p):
    '''
    mainfunction : func main agregaMain PARIZQ PARDER varsaux bloque
                 | func main agregaMain PARIZQ PARDER bloque
    '''

def p_agregaMain(p):
    '''
    agregaMain :
    '''
    t = 'main'
    global actualFunc
    actualFunc = p[-1]
    dirFunc[actualFunc] = {'type': t, 'vars' : {}}


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
    type : int
         | float
         | string
         | bool
    '''

def p_function(p):
    '''
    function : ftype func ID PARIZQ funcaux PARDER varsaux bloque
             | ftype func ID PARIZQ empty PARDER varsaux bloque
    '''

#Function types
def p_ftype(p):
    '''
    ftype : type
          | void
    '''

def p_funcaux(p):
    '''
    funcaux : type ID 
            | type ID COMA funcaux
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
    asignacion : ID asignaux ASIGNA hyper_exp PYC
               | ID asignaux ASIGNA llamada_esp PYC
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
    expresion : term 
              | term MAS term
              | term MENOS term
    '''

def p_term(p):
    '''
    term : fact
         | fact MULT fact
         | fact DIV fact
    '''

def p_fact(p):
    '''
    fact : CTEINT
         | CTEFLOAT
         | ID
         | hyper_exp
    '''

def p_hyper_exp(p):
    '''
    hyper_exp : super_exp
              | super_exp AND super_exp
              | super_exp OR super_exp
    '''

def p_super_exp(p):
    '''
    super_exp : expresion
              | expresion MAYORQUE expresion
              | expresion MENORQUE expresion
              | expresion EQUALS expresion
              | expresion DIFERENTE expresion
    '''

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
    print("Syntax error bro")

parser = yacc.yacc()

# parser.parse(data)
# fn = input("Nombre del archivo\n")
try:
    f = open("./ejemplo.txt", "r")
    fileContent = f.read()
    # print(fileContent)
    parser.parse(fileContent)
except:
    print("Hubo un error con el archivo")
    pass

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