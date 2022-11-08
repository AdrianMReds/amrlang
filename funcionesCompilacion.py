#Funciones para compilacion

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