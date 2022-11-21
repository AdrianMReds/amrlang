import sys


pointer = 0
globales = None

constantes = [[]]
cuadruplos = None

globInt = [[]]
globFloat = [[]]
globString = [[]]
globBool = [[]]

locInt = []
locFloat = []
locString = []
locBool = []

tempInt = [[]]
tempFloat = [[]]
tempString = [[]]
tempBool = [[]]
tempPointer = [[]]

# localIntSize = 0
# localFloatSize = 0
# localStringSize = 0
# localBoolSize = 0

# tempIntSize = 0
# tempFloatSize = 0
# tempStringSize = 0
# tempBoolSize = 0
# tempPointerSize = 0

auxlocInt = []
auxlocFloat = []
auxlocString = []
auxlocBool = []

auxtempInt = []
auxtempFloat = []
auxtempString = []
auxtempBool = []
auxtempPointer = []

comeBack = []

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

dicAux = {
        1000:auxlocInt,
        2000:auxlocFloat,
        3000:auxlocString,
        4000:auxlocBool,
        5000:auxlocInt,
        6000:auxlocFloat,
        7000:auxlocString,
        8000:auxlocBool,
        9000:auxlocInt,
        10000:auxlocFloat,
        11000:auxlocString,
        12000:auxlocBool,
        13000:tempPointer,
        14000:constantes
      }    

def getDirBase(dir):
    return (dir//1000)*1000

def ejecucion(pointer):
    global comeBack
    global locInt
    global locFloat
    global locString
    global locBool
    global tempInt
    global tempFloat
    global tempString
    global tempBool
    global tempPointer
    global auxlocInt
    global auxlocFloat
    global auxlocString
    global auxlocBool
    global auxtempInt
    global auxtempFloat
    global auxtempString
    global auxtempBool
    global auxtempPointer

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
            if(dirAsigna!=13000):
                asigna = dicDir[dirAsigna][-1][asigna-dirAsigna]
            else:
                indice = dicDir[dirAsigna][-1][asigna-dirAsigna]
                dirIndice = (indice//1000)*1000
                asigna = dicDir[dirIndice][-1][indice-dirIndice]
            l = dicDir[dirAdonde]
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
            
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
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
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
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
            # dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 + op2
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]

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
            # print('op1 {} op2 {} adonde {}'.format(op1,op2,adonde))
            # print(tempInt)
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
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
            if(dirop1!=13000):
                op1 = dicDir[dirop1][-1][op1-dirop1]
            else:
                indice = dicDir[dirop1][-1][op1-dirop1]
                dirIndice = (indice//1000)*1000
                op1 = dicDir[dirIndice][-1][indice-dirIndice]
            # print(dicDir[dirop2][-1])
            if(dirop2!=13000):
                op2 = dicDir[dirop2][-1][op2-dirop2]
            else:
                indice = dicDir[dirop2][-1][op2-dirop2]
                dirIndice = (indice//1000)*1000
                op2 = dicDir[dirIndice][-1][indice-dirIndice]
            dicDir[dirAdonde][-1][adonde-dirAdonde] = op1 / op2
            pointer += 1
        # ERA -------------------------------------------------------
        elif operador == 'era':
            # cuad = [contCuadruplos, 'era', numLoci, numLocf, numLocs, numLocb
            #                      , numPari, numParf, numPars, numParb
            #                      , numTempi, numTempf, numTemps, numTempb]
            
            localIntSize = cuadruplo[2]
            localFloatSize = cuadruplo[3]
            localStringSize = cuadruplo[4]
            localBoolSize = cuadruplo[5]
            numParInt = cuadruplo[6]
            numParFloat = cuadruplo[7]
            numParString = cuadruplo[8]
            numParBool = cuadruplo[9]
            tempIntSize = cuadruplo[10]
            tempFloatSize = cuadruplo[11]
            tempStringSize = cuadruplo[12]
            tempBoolSize = cuadruplo[13]
            tempPointerSize = cuadruplo[14]

            # auxlocInt.append([])
            for i in range(localIntSize):
                auxlocInt.append(None)

            # auxlocFloat.append([])
            for i in range(localFloatSize):
                auxlocFloat.append(None)

            # locString.append([])
            for i in range(localStringSize):
                auxlocString.append(None)

            # locBool.append([])
            for i in range(localBoolSize):
                auxlocBool.append(None)

            # tempInt.append([])
            for i in range(tempIntSize):
                auxtempInt.append(None)

            # tempFloat.append([])
            for i in range(tempFloatSize):
                auxtempFloat.append(None)

            # tempString.append([])
            for i in range(tempStringSize):
                auxtempString.append(None)

            # tempBool.append([])
            for i in range(tempBoolSize):
                auxtempBool.append(None)

            # tempPointer.append([])
            for i in range(tempPointerSize):
                auxtempPointer.append(None)

            # if(len(cuadruplo)>15):
            #     dirs = cuadruplo[15:]
            #     for d in dirs:
            #         if(d==1000 or d==5000 or d==9000):
            #             auxlocInt[adonde-1] = parametro
            #         elif(d==2000 or d==6000 or d==10000):
            #             auxlocFloat[adonde-1] = parametro
            #         elif(d==3000 or d==7000 or d==11000):
            #             auxlocString[adonde-1] = parametro
            #         elif(d==4000 or d==8000 or d==12000):
            #             auxlocBool[adonde-1] = parametro

            # print(cuadruplo)
            # print('Era, auxtempint ->', auxtempInt)

            # print(pointer)
            # print(auxlocInt)
            # print(auxlocFloat)
            # print(auxlocString)
            # print(auxlocBool)
            # print(auxtempInt)
            # print(auxtempFloat)
            # print(auxtempString)
            # print(auxtempBool)
            # print(auxtempPointer)


            pointer += 1
        # PARAMETRO -------------------------------------------------------
        elif operador == 'par':
            # 1000:auxlocInt,
            # 2000:auxlocFloat,
            # 3000:auxlocString,
            # 4000:auxlocBool,
            # 5000:auxlocInt,
            # 6000:auxlocFloat,
            # 7000:auxlocString,
            # 8000:auxlocBool,
            # 9000:auxlocInt,
            # 10000:auxlocFloat,
            # 11000:auxlocString,
            # 12000:auxlocBool,
            # 13000:tempPointer,
            # 14000:constantes
            # print(cuadruplo)
            parametro = cuadruplo[2]
            dirPar = (parametro//1000)*1000
            parametro = dicDir[dirPar][-1][parametro-dirPar]
            # print('Lista del parametro', dicDir[dirPar])
            # print('dirPar',dirPar)
            # print('par',parametro)
            adonde = cuadruplo[3]
            adonde = int(adonde[-1])
            # print('adonde',adonde)
            dirAdonde = dirPar
            # print('diradonde',dirAdonde)
            
            if(dirAdonde!=14000):
                if(dirAdonde==1000 or dirAdonde==5000 or dirAdonde==9000):
                    for i in range(len(auxlocInt)):
                        if(auxlocInt[i] is None):
                            auxlocInt[i] = parametro
                            break
                    # auxlocInt[adonde-1] = parametro
                elif(dirAdonde==2000 or dirAdonde==6000 or dirAdonde==10000):
                    auxlocFloat[adonde-1] = parametro
                elif(dirAdonde==3000 or dirAdonde==7000 or dirAdonde==11000):
                    auxlocString[adonde-1] = parametro
                elif(dirAdonde==4000 or dirAdonde==8000 or dirAdonde==12000):
                    auxlocBool[adonde-1] = parametro
            else:
                if isinstance(parametro,int):
                    auxlocInt[adonde-1] = parametro
                elif isinstance(parametro,float):
                    auxlocFloat[adonde-1] = parametro
                elif isinstance(parametro,str):
                    if parametro=='true' or parametro=='false':
                        auxlocBool[adonde-1] = parametro
                    else:
                        auxlocString[adonde-1] = parametro
            # print(auxlocInt)
            # print(globInt)
            if len(cuadruplo) == 5:
                d = cuadruplo[2]
                for i in range(cuadruplo[4]-cuadruplo[2]+1):
                    
                    # print('d',d)
                    
                    dirD = (d//1000)*1000
                    # print('dirD',dirD)
                    if(dirD==1000 or dirD==5000 or dirD==9000):
                        auxlocInt[d-dirD] = dicDir[dirD][-1][d-dirD]
                    elif(dirD==2000 or dirD==6000 or dirD==10000):
                        auxlocFloat[d-dirD] = dicDir[dirD][-1][d-dirD]
                    elif(dirD==3000 or dirD==7000 or dirD==11000):
                        auxlocString[d-dirD] = dicDir[dirD][-1][d-dirD]
                    elif(dirD==4000 or dirD==8000 or dirD==12000):
                        auxlocBool[d-dirD] = dicDir[dirD][-1][d-dirD]
                    d+=1
            # print(auxlocInt)
            pointer += 1
        # GOSUB -------------------------------------------------------
        elif operador == 'gosub':
            locInt.append(auxlocInt)
            locFloat.append(auxlocFloat)
            locString.append(auxlocString)
            locBool.append(auxlocBool)

            tempInt.append(auxtempInt)
            tempFloat.append(auxtempFloat)
            tempString.append(auxtempString)
            tempBool.append(auxtempBool)
            tempPointer.append(auxtempPointer)

            auxlocInt = []
            auxlocFloat = []
            auxlocString = []
            auxlocBool = []

            auxtempInt = []
            auxtempFloat = []
            auxtempString = []
            auxtempBool = []
            auxtempPointer = []

            # print('LOCALES ->', locInt, locFloat, locString, locBool)
            # print('TEMPORALES ->', tempInt, tempFloat, tempString, tempBool)
            # print('gosub, tempint ->', tempInt)
            comeBack.append(pointer+1)
            nuevoPointer = cuadruplo[3]
            ejecucion(nuevoPointer)

            pointer += 1
        # RETURN -------------------------------------------------------
        elif operador == 'ret':
            # print(locInt)
            regresa = cuadruplo[2]
            # print('regresa',regresa)
            adond = cuadruplo[3]
            if(regresa=='true' or regresa=='false'):
                dirAdond = (adond//1000)*1000
                dicDir[dirAdond][-1][adond-dirAdond] = regresa
            else:
                dirRegresa = (regresa//1000)*1000
                dirAdond = (adond//1000)*1000
                # print('dirRegresa',dirRegresa)
                regresa = dicDir[dirRegresa][-1][regresa-dirRegresa]
                if(dirRegresa!=13000):
                    dicDir[dirAdond][-1][adond-dirAdond] = regresa
                else:
                    dirRegresa = (regresa//1000)*1000
                    # print('regresa en else',regresa)
                    # print('dirRegresa en else',dirRegresa)
                    indice = dicDir[dirRegresa][-1][regresa-dirRegresa]
                    # print('indice', indice)
                    # print('adonde',adond)
                    # print(dicDir[dirAdond])
                    dicDir[dirAdond][-1][adond-dirAdond] = indice

                    # dirIndice = (indice//1000)*1000
                    # l = dicDir[dirIndice]
                    # # print(globInt[-1])
                    # # print(l[-1][indice-dirIndice])
                    # l[-1][indice-dirIndice] = regresa
            

            locInt.pop()
            locFloat.pop()
            locString.pop()
            locBool.pop()

            tempInt.pop()
            tempFloat.pop()
            tempString.pop()
            tempBool.pop()
            tempPointer.pop()

            ejecucion(comeBack.pop())

            pointer += 1
        # ENDFUNC -------------------------------------------------------
        elif operador == 'endfunc':
            locInt.pop()
            locFloat.pop()
            locString.pop()
            locBool.pop()

            tempInt.pop()
            tempFloat.pop()
            tempString.pop()
            tempBool.pop()
            tempPointer.pop()

            # print('LOCALES ->', locInt, locFloat, locString, locBool)
            # print('TEMPORALES ->', tempInt, tempFloat, tempString, tempBool)

            ejecucion(comeBack.pop())
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
        contGlobstring += 1
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