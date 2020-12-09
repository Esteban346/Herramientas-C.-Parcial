# Herramientas-C.-Parcial
Este repositorio contiene el control de versiones del parcial de herramientas computacionales.

Se agregó el código con la solución a la primera parte del parcial y se agrego un archivo de Word con los errores que aparecieron a la hora de ejecutar y realizar el código.

## ¿Qué problema es?
Este es un problema que busca realizar descuentos dependiendo del rol de la persona, si es estudiante tiene un descuento del 50% y si es profeso un descuento del 20%.

## ¿Qué recibe como entrada?
Como entrada recibe:
<p>Un <strong>entero</strong> que es la cédula de la persona.</p>
<p>Una <strong>cadena</strong> que es el rol de la persona(<strong>estudiante</strong>, <strong>profesor</strong>).</p>
<p>Un <strong>eval</strong> que es el valor del producto que la persona tiene que pagar.</p>
<p>Una <strong>cadena</strong> que es el código del producto.</p>
<p> Un <strong>entero</strong> que es la cantidad de unidades.

## ¿Cual sería la salida?
La salida sería:
<p>El <strong>Rol</strong> con cédula <strong>Numero</strong>, debe pagar <strong>Valor</strong> por el producto <strong>Codigo</strong>.
 
## ¿Cómo se cálcula?
Se calcula por medio de dos funciones, una que resuelve el problema y otra que lee la entrada e imprime la salida. Para calcular el descuento realicé dos if, uno por si el rol es estudiante y el otro por si el rol es profesor, luego de esto realice el proceso matematico, el cual es (valor - (valor por 0.5)) por cantidad de unidades, esto para estudiante y (valor - (valor por 0.2)) por cantidad de unidades; luego en la función que imprime se llama a la función que resuelve el problema y se imprime con la estructura de la salida, que es <strong>print("El " + rol + " con cédula " + str(cedula) + "," + " debe pagar " + "$" + str(descuento(rol,valor, cantidad)) + " por el producto " + codigo)</strong>.
