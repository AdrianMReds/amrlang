#Adrián Montemayor Rojas
#A01283139

import ply.lex as lex
import ply.yacc as yacc
import numpy as np
import sys

reservadas = ['program', 'var', 'func', 'main', 'int', 'float', 'string',
              'print', 'if', 'else', 'while', 'for', 'input']

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
                       'DIFERENTE' #$
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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    if t.value in reservadas:
        t.type = t.value
    t.value = t.value
    return t

def t_CTEFLOAT(t):
    r'\d+\.\d+'
    t.type = 'FLOAT'
    t.value = float(t.value)
    return t

def t_CTEINT(t):
    r'\d+'
    t.type = 'INT'
    t.value = int(t.value)
    return t

def t_CTESTRING(t):
    r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
    t.type = 'STRING'
    t.value = str(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
        program ejemplo;

        func main(){
            Sprint()
        }
       '''

lexer.input(data)

def p_programa(p):
    '''
    programa : program ID PYC paux paux2 mainfunction
    '''

def p_programa_vacio(p):
    '''
    programa : program ID PYC empty mainfunction
    '''

def p_paux(p):
    '''
    paux : vars
         | empty
    '''

def p_paux2(p):
    '''
    paux2 : function
          | empty
    '''

def p_vars(p):
    '''
    vars : var type vaux PYC vars
         | empty
    '''

def p_vaux(p):
    '''
    vaux : ID
         | ID CORIZQ CTEINT CORDER nextvar
         | ID CORIZQ CTEINT COMA CTEINT CORDER nextvar
    '''

def p_nextvar(p):
    '''
    nextvar : COMA vaux
            | empty
    '''

def p_mainfunction(p):
    '''
    mainfunction : func main PARIZQ PARDER vars bloque
                 | func main PARIZQ PARDER bloque
    '''

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
    '''

def p_function(p):
    '''
    function : type ID PARIZQ funcaux PARDER vars bloque
             | type ID PARIZQ empty PARDER vars bloque
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
    '''

def p_asignaux(p):
    '''
    asignaux : CORIZQ expresion CORDER
             | CORIZQ expresion COMA expresion CORDER
             | empty
    '''

def p_escritura(p):
    '''
    escritura : print PARIZQ escaux PARDER PYC
    '''

def p_escaux(p):
    '''
    escaux : expresion nextexp
           | CTESTRING nextexp
    '''

#Para poner más de una expresión en un print
def p_nextexp(p):
    '''
    nextexp : COMA expresion
            | empty
    '''

def p_llamada(p):
    '''
    llamada : ID PARIZQ expresion nextexp PARDER
            | ID PARIZQ PARDER
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
    forloop : for PARIZQ CTEINT DOSPUNTOS CTEINT PARDER bloque
    '''

def p_lectura(p):
    '''
    lectura : input PARIZQ ID PARDER PYC
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
    fact : varcte 
         | varcte PARIZQ hyper_exp PARDER fact
    '''

def p_varcte(p):
    '''
    varcte : CTEINT
           | CTEFLOAT
           | ID
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

def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()

# parser.parse(data)

try:
    f = open("./ejemplo2.txt", "r")
    fileContent = f.read()
    print(fileContent)
    parser.parse(fileContent)
except EOFError:
    print("Hubo un error con el archivo")
    pass
    

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