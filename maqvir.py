import sys


pointer = 0
globales = None

constantes = [[]]
cuadruplos = None

globInt = [[]]
globFloat = [[]]
globString = [[]]
globBool = [[]]

locInt = [[]]
locFloat = [[]]
locString = [[]]
locBool = [[]]

tempInt = [[]]
tempFloat = [[]]
tempString = [[]]
tempBool = [[]]
tempPointer = [[]]

dicDir = {
        1000:globInt,
        2000:globFloat,
        3000:globString,
        4000:globBool,
        5000:locInt,
        6000:locFloat,
        7000:locString,
        8000:locBool,
        9000:tempInt,
        10000:tempFloat,
        11000:tempString,
        12000:tempBool,
        13000:tempPointer,
        14000:constantes
      }

# def isBetween(num, a, b) -> bool:
#     return (num>=a) and (num<=b)

# def checkDir(dir:int):
#     if(isBetween(dir,1000,1999)):
#         return 'globInt'
#     elif(isBetween(dir,2000,2999)):
#         return 'globFloat'
#     elif(isBetween(dir,3000,3999)):
#         return 'globString'
#     elif(isBetween(dir,4000,4999)):
#         return 'globBool'
#     elif(isBetween(dir,5000,5999)):
#         return 'locInt'
#     elif(isBetween(dir,6000,6999)):
#         return 'locFloat'
#     elif(isBetween(dir,7000,7999)):
#         return 'locString'
#     elif(isBetween(dir,8000,8999)):
#         return 'locBool'
#     elif(isBetween(dir,9000,9999)):
#         return 'locPointer'
#     elif(isBetween(dir,10000,10999)):
#         return 'tempInt'
#     elif(isBetween(dir,11000,11999)):
#         return 'tempFloat'
#     elif(isBetween(dir,12000,12999)):
#         return 'tempString'
#     elif(isBetween(dir,13000,13999)):
#         return 'tempBool'
#     elif(isBetween(dir,14000,14999)):
#         return 'locPointer'
#     elif(isBetween(dir,15000,15999)):
#         return 'constante'
    

def getDirBase(dir):
    return (dir//1000)*1000

def ejecucion(pointer):
    
    while True:
        cuadruplo = cuadruplos[pointer-1]
        # print('Ejecutamos cuadruplo {}'.format(cuadruplo))
        operador = cuadruplo[1]
        # print('Operador: ',operador)
        # GOTO -------------------------------------------------------
        if operador == 'goto':
            adonde = cuadruplo[2]
            ejecucion(adonde)
        # GOTOF -------------------------------------------------------
        elif operador == 'gotof':
            cond = cuadruplo[2]
            dirCond = (cond//1000)*1000
            cond = dicDir[dirCond][-1][cond-dirCond]
            adonde = cuadruplo[3]
            if(cond=='false'):
                ejecucion(adonde)
            else:
                pointer += 1
        # ASIGNA -------------------------------------------------------
        elif operador == '=':
            asigna = cuadruplo[2]
            adonde = cuadruplo[3]
            dirAsigna = (asigna//1000)*1000
            dirAdonde = (adonde//1000)*1000
            asigna = dicDir[dirAsigna][-1][asigna-dirAsigna]
            l = dicDir[dirAdonde]
            #Tengo que hacer esto pero en suma, resta, etc para que se escriba lo que están en el indice que tiene el pointer
            if(dirAdonde!=13000):
                l[-1][adonde-dirAdonde] = asigna
            else:
                indice = l[-1][adonde-dirAdonde]
                # print('indice', indice)
                dirIndice = (indice//1000)*1000
                l = dicDir[dirIndice]
                # print(globInt[-1])
                # print(l[-1][indice-dirIndice])
                l[-1][indice-dirIndice] = asigna
            pointer += 1
        # ENDFUNC -------------------------------------------------------
        elif operador == 'endfunc':
            pointer +=1
            pass
        # VERIFICAR -------------------------------------------------------
        elif operador == 'ver':
            aVerificar = cuadruplo[2]
            dirAVerificar = (aVerificar//1000)*1000
            aVerificar = dicDir[dirAVerificar][-1][aVerificar-dirAVerificar]
            # print('Hay que verificar {} en {}'.format(aVerificar,pointer))
            inf = cuadruplo[3]
            sup = cuadruplo[4]
            if(aVerificar<inf or aVerificar>sup):
                sys.exit('ExecutionError: The list you\'re trying to access has indexes from {} to {}'.format(inf,sup))
            pointer +=1
            pass
        # READ -------------------------------------------------------
        elif operador == 'read':
            dedonde = cuadruplo[2]
            dirDedonde = (dedonde//1000)*1000
            l = dicDir[dirDedonde]
            if(dirDedonde == 1000 or dirDedonde == 5000):
                try:
                    l[-1][dedonde-dirDedonde] = int(input())
                except ValueError:
                    sys.exit('ValueError: The variable you are trying to read is int')
            elif(dirDedonde == 2000 or dirDedonde == 6000):
                try:
                    l[-1][dedonde-dirDedonde] = float(input())
                except ValueError:
                    sys.exit('ValueError: The variable you are trying to read is float')
            elif(dirDedonde == 3000 or dirDedonde == 7000):
                try:
                    l[-1][dedonde-dirDedonde] = input()
                except ValueError:
                    sys.exit('ValueError: The variable you are trying to read is string')
            elif(dirDedonde == 4000 or dirDedonde == 8000):
                try:
                    l[-1][dedonde-dirDedonde] = bool(input())
                except ValueError:
                    sys.exit('ValueError: The variable you are trying to read is bool')
            pointer +=1
        # WRITE -------------------------------------------------------
        elif operador == 'write':
            dedonde = cuadruplo[2]
            dirDedonde = (dedonde//1000)*1000
            l = dicDir[dirDedonde]
            if(dirDedonde!=13000):
                print(l[-1][dedonde-dirDedonde])
            else:
                indice = l[-1][adonde-dirAdonde]
                # print('indice', indice)
                dirIndice = (indice//1000)*1000
                l = dicDir[dirIndice]
                print(l[-1][indice-dirIndice])
            pointer +=1
        # MENORQUE -------------------------------------------------------
        elif operador == '<':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1<op2):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}<{} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}<{} false'.format(op1,op2))
            
            pointer += 1
        # MAYORQUE -------------------------------------------------------
        elif operador == '>':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1>op2):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}>{} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}>{} false'.format(op1,op2))

            pointer += 1
        # IGUALQUE -------------------------------------------------------
        elif operador == '==':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1==op2):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}=={} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}=={} false'.format(op1,op2))
            
            pointer += 1
        # DIFERENTEDE -------------------------------------------------------
        elif operador == '$':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1!=op2):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}${} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}${} false'.format(op1,op2))

            pointer += 1
        # AND -------------------------------------------------------
        elif operador == '&&':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1=='true' and op2=='true'):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}&&{} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}&&{} false'.format(op1,op2))
            
            pointer += 1
        # OR -------------------------------------------------------
        elif operador == '||':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            if(op1=='true' or op2=='true'):
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'true'
                # print('{}||{} true'.format(op1,op2))
            else:
                dicDir[dirAdonde][-1][adonde-dirAdonde] = 'false'
                # print('{}||{} false'.format(op1,op2))
            
            pointer += 1
        # SUMA -------------------------------------------------------
        elif operador == '+':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            # print('op1 {} op2 {} adonde {}'.format(op1,op2,adonde))
            # print('dirop1 {} dirop2 {} dirAdonde {}'.format(dirop1,dirop2, dirAdonde))
            op1 = dicDir[dirop1][-1][op1-dirop1]
            # print(dicDir[dirop2][-1])
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            # print('temppointer',tempPointer)
            pointer += 1
        # RESTA -------------------------------------------------------
        elif operador == '-':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 - op2
            pointer +=1
        # MULTIPLICACIÓN -------------------------------------------------------
        elif operador == '*':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 * op2
            pointer += 1
        # DIVISIÓN -------------------------------------------------------
        elif operador == '/':
            op1 = cuadruplo[2]
            op2 = cuadruplo[3]
            adonde = cuadruplo[4]
            dirop1 = (op1//1000)*1000
            dirop2 = (op2//1000)*1000
            dirAdonde = (adonde//1000)*1000
            op1 = dicDir[dirop1][-1][op1-dirop1]
            op2 = dicDir[dirop2][-1][op2-dirop2]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 / op2
            pointer += 1
        # ENDPROGRAM -------------------------------------------------------
        elif operador == 'endprogram':
            # print(tempPointer)
            sys.exit('Termino ejecución')
        else:
            print('Aún no programo eso :p')
            pointer += 1


def maq(listaCuad : list, glob, ctes, tempiglob, tempfglob, tempsglob, tempbglob, temppglob, globi, globf, globs, globb):
    global cuadruplos
    global globales
    global constantes
    global globInt
    global globFloat
    global globString
    global globBool
    global tempInt
    global tempFloat
    global tempString
    global tempBool
    cuadruplos = listaCuad
    globales = glob
    constants = ctes
    # print('Desde la máquina virtual')
    # for c in cuadruplos:
    #     print(c)

    # globs = list(globales)
    contGlobs = 0
    contGlobint = 0
    contGlobfloat = 0
    contGlobstring = 0
    contGlobbool = 0
    for i in range(globi):
        globInt[-1].append(None)
        contGlobint += 1
    for i in range(globf):
        globFloat[-1].append(None)
        contGlobfloat += 1
    for i in range(globs):
        globString[-1].append(None)
        contGlobint += 1
    for i in range(globb):
        globBool[-1].append(None)
        contGlobbool += 1

    contGlobs = globi+globf+globs+globb
    print('Hay {} globales'.format(contGlobs))
    print('Hay {} globales enteras'.format(contGlobint))
    #Declaramos memoria global
    globales = []
    for g in range(contGlobs):
        globales.append(None)
    # print(globInt)
    # print(globFloat)
    # print(globString)
    # print(globBool)

    #Declaramos la memoria de constantess
    consts = list(constants)
    for co in consts:
        print(co,constants[co])
        constantes[-1].append(co)
    
    # print(constantes)

    for i in range(tempiglob):
        tempInt[-1].append(None)
    for i in range(tempfglob):
        tempFloat[-1].append(None)
    for i in range(tempsglob):
        tempString[-1].append(None)
    for i in range(tempbglob):
        tempBool[-1].append(None)
    for i in range(temppglob):
        tempPointer[-1].append(None)
    

    print('-----------EMPIEZA EJECUCIÓN-----------')
    ejecucion(1)