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
                       'IGUAL', # =
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
t_IGUAL = r'\='
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
    if t.value.upper() in reservadas:
        t.type = t.value
    t.value = t.value.upper()
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


def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
       program ejemplo; 
       var float x, z;

       func main()
       var int y;
       {
        print()
       }
       '''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)