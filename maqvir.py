
pointer = 0
globales = None

constantes = []
cuadruplos = None

globInt = []
globFloat = []
globString = []
globBool = []

dic = {

      }

def isBetween(num, a, b) -> bool:
    return (num>=a) and (num<=b)

def checkDir(dir:int):
    if(isBetween(dir,1000,1999)):
        return 'globInt'
    elif(isBetween(dir,2000,2999)):
        return 'globFloat'
    elif(isBetween(dir,3000,3999)):
        return 'globString'
    elif(isBetween(dir,4000,4999)):
        return 'globBool'
    elif(isBetween(dir,5000,5999)):
        return 'locInt'
    elif(isBetween(dir,6000,6999)):
        return 'locFloat'
    elif(isBetween(dir,7000,7999)):
        return 'locString'
    elif(isBetween(dir,8000,8999)):
        return 'locBool'
    elif(isBetween(dir,9000,9999)):
        return 'locPointer'
    elif(isBetween(dir,10000,10999)):
        return 'tempInt'
    elif(isBetween(dir,11000,11999)):
        return 'tempFloat'
    elif(isBetween(dir,12000,12999)):
        return 'tempString'
    elif(isBetween(dir,13000,13999)):
        return 'tempBool'
    elif(isBetween(dir,14000,14999)):
        return 'locPointer'
    elif(isBetween(dir,15000,15999)):
        return 'constante'
    

def ejecucion(pointer):
    # while True:
    cuadruplo = cuadruplos[pointer]
    operador = cuadruplo[1]
    if operador == 'goto':
        # print(cuadruplos[cuadruplo[2]-1])
        adonde = cuadruplo[2]
        ejecucion(adonde)
    if operador == '=':
        asigna = cuadruplo[2]
        adonde = cuadruplo[3]
        
    return


def maq(listaCuad : list, glob, ctes):
    global cuadruplos
    global globales
    global constantes
    global globInt
    global globFloat
    global globString
    global globBool
    cuadruplos = listaCuad
    globales = glob
    constants = ctes
    # print('Desde la máquina virtual')
    # for c in cuadruplos:
    #     print(c)

    globs = list(globales)
    contGlobs = 0
    contGlobint = 0
    contGlobfloat = 0
    contGlobstring = 0
    contGlobbool = 0
    # print('list(constantes)',consts)
    for g in globs:
        print(g,globales[g])
        if(globales[g]['type']=='int'):
            globInt.append(None)
            contGlobint += 1
        elif(globales[g]['type']=='float'):
            globFloat.append(None)
            contGlobfloat += 1
        elif(globales[g]['type']=='string'):
            globString.append(None)
            contGlobstring += 1
        elif(globales[g]['type']=='bool'):
            globBool.append(None)
            contGlobbool += 1
        contGlobs += 1
    print('Hay {} globales'.format(contGlobs))
    print('Hay {} globales enteras'.format(contGlobint))
    #Declaramos memoria global
    globales = []
    for g in range(contGlobs):
        globales.append(None)
    print(globInt)
    print(globFloat)
    print(globString)
    print(globBool)

    #Declaramos la memoria de constantess
    consts = list(constants)
    for co in consts:
        print(co,constants[co])
        constantes.append(co)
    
    print(constantes)
    

    ejecucion(0)