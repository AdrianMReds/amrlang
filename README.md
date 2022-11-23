# amrlang
Adrián Montemayor Rojas
A01283139

Proyecto para la clase de diseño de compiladores

## Descripción

El lenguaje para el cual estamos creando un compilador tiene como nombre amrlang. 

El propósito de este proyecto, desarrollado para la clase de Desarrollo de compiladores, fue diseñar un nuevo lenguaje de programación que sea usado para manipular listas y matrices y se le puedan aplicar funciones estadísticas y matemáticas, así como las funciones básicas de cualquier lenguaje de programación, uso de variables, uso de funciones y uso de ciclos. El lenguaje está enfocado a gente que está aprendiendo o sabe lo básico de programación que quiera entrar al mundo de la ciencia de datos y que pueda ver un poco de ambos mundos.

## Características 

El lenguaje amrlang contiene las siguientes características:

- Variables: Se permite declararlas y llamar el valor que tengas después
Estructura de arreglos y matrices: Se permite crear arreglos y matrices así como acceder a sus índices
- Estructuras condicionales (if): Se permite hacer condiciones, validarlas y ejecutar bloques dependiendo del resultado
- Ciclos: Se permite generar estructuras para repetir la ejecución de bloques
Expresiones matemáticas y lógicas: Se permita generar expresiones matemáticas con sumas, restas, multiplicaciones y divisiones, así como expresiones lógicas con resultado booleano
- Asignaciones: Se permite asignarle a una variable un valor del tipo de la variable
- Módulos: Se permite declarar módulos void o que retornen un valor y usarlos en cualquier lugar del código, ya sea en el main u otros módulos. 
- Funciones estadísticas para listas: Se permite sacar ciertos valores estadísticos de listas numéricas como el promedio, mediana, moda, varianza y desviación estándar.

## Tokens y palabras reservadas

Palabras reservadas: 
'program'
'var'
'func'
'main'
'int'
'float'
'string'
'print'
'if'
'else'
'while'
'for'
'input'

Tokens:
'ID' NOMBRE DE VARIABLE O FUNCIÓN
'CTEINT' CONSTANTE INT
'CTEFLOAT' CONSTANTE FLOAT
'CTESTRING' CONSTANTE STRING
'PYC' PUNTO Y COMA
'CORIZQ' CORCHETE IZQUIERDO
'CORDER' CORCHETE DERECHO
'COMA' ,
'PARIZQ' PARENTESIS IZQUIERDO
'PARDER' PARENTESIS DERECHO
'LLAVEIZQ' LLAVE IZQUIERDA
'LLAVEDER' LLAVE DERECHA
'ASIGNA' =
'DOSPUNTOS' :
'MAS' +
'MENOS' -
'AND' &&
'OR' ||
'MULT' *
'DIV' /
'MAYORQUE' >
'MENORQUE' <
'EQUALS' ==
'DIFERENTE' $

## Uso de características 

### Asignación de variables

x = 5;
st = "Hola";
y = 2.5 + 9;

### Lectura
read(x);

### Escritura
write("Hola");
write(x,y,z);
write(5*x, "Adios");

### Funciones

void func nombre(){
    write("Algo");
}

void func suma(int a, int b){
    return(a+b);
}

### Llamadas

num = suma(8,x);
nombre();

### While

while(x$0){
    write("X no es 0");
}

### For 

for(0:5){
    write("Algo");
}

## Llamadas especiales (solo para listas numéricas)

l = arr.length();
x = arr.avg() + 5;

## Ejemplos de código

### Ejemplo 1
En este programa podemos ver uso de variables globales y locales, lectura y escritura, if else y asignación de variables.

program e;
var int a, b;

void func algo(string s)
var int x;{
    x = 8 + 9;
    write(s);
}

func main(){
    read(a);
    if(a>10){
        b = 5;
    }else{
        b = 3;
    }
    write(b);
    algo("Adios!");
}
end;

### Ejemplo 2
program factorial;
var int num, res;


func main(){
    write("Escriba un valor");
    read(num);
    res = 1;
    if(num<0){
        write("No existe factorial para numeros negativos");
    }
    if(num==0){
        write(1);
    }
    if(num>0){
        write("El factorial de ese numero es");
        while(num>0){
            res = res * num;
            num = num - 1;
        }
        write(res);
    }
    write("Hasta luego!");
}

end;

## Lista de errores

- Al comparar dos índices de listas o arreglos no detecta siempre que sea una expresión booleana

- Al usar muchas funciones de recursión en un programa se sobrecarga la memoria y marca un error de ejecución

- Al usar dos for anidados, a veces hace la suma de la variable de control mal

## Reflexión

Este fue un proyecto muy retador y divertido de realizar, no pienso darle seguimiento por el momento, pero espero algún día poder modificarlo o agregarle algo.