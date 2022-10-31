# amrlang
Adrián Montemayor Rojas
A01283139

Proyecto para la clase de diseño de compiladores

El lenguaje para el cual estamos creando un compilador tiene como nombre amrlang. 

Para el primer avance se desarrolló todo el análisis léxico y sintáctico. Para se esto se definieron las palabras reservadas y los tokens que se usaran para el resto del proyecto:

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

Después implementamos la gramática previamente desarrollada para el lenguaje.

El compilador ya detecta errores de sintaxis al escribir líneas de código incorrectas.


-- AVANCE 2 --

Para este avance ya se tiene la tabla de funciones con sus respectivas tablas de variables funcionando, también se desarrollo una función como cubo semántico pero aún no se ha probado, existe un bug al momento de poner expresiones en el código.