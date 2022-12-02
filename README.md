# Ejercicios-tema-4

Ejercicio 1

Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular primero las frecuencias de cada carácter a partir de la can- tidad de apariciones del mismo–, para resolver las siguientes actividades:
la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último respectivamente en el orden alfabético;
descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
 

I.   Mensaje  1:  “100010111010110000101110100011100000110110000001111001111010010110
0001101001110011010001011101011111110100001111001111110011110100011000110000
00101101011110111111101110101101101110011101101111001111111001010010100101000001
011010110001011001101000111001001011000011001000110101101010111111111110110111
0111001000010010101100011111110001000111011001100101101000110111110101101000
1101110000000111001001010100011111100001100101101011100110011110100011000110
000001011010111110011100”

II. Mensaje 2: “01101010110111001010001111010111001101110101101101000010001110101001
011110100111111101110010100011110101110011011101011000011000100110100011100100
10001100010110011001110010010000111101111010”

finalmente, calcule el espacio de memoria requerido por el mensaje original y el comprimido.
 
Ejercicio 2

El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asigna- ciones de vehículos y Stromtroopers a las distintas misiones que parten desde la estrella de la muerte, para facilitar esta tarea nos encomienda desarrollar las funciones necesarias para gestionar esto mediante prioridades de la siguiente manera:
de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
si la misión fue pedida por Palpatine o Darth Vader estas tendrán alta prioridad, sino su prioridad será baja;
si la misión es de prioridad alta los recursos se asignarán manualmente independiente- mente de su tipo;
si la misión es de baja prioridad se asignarán los recursos de la siguiente manera depen- diendo de su tipo:
exploración: 15 Scout Troopers y 2 speeder bike,
contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),
realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, per- mitiendo agregar nuevos pedidos de misiones durante la atención;
indicar la cantidad total de recursos asignados a las misiones.

Ejercicio 3

Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las siguientes consideraciones:
cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número –estos estarán numerados de manera consecutiva–; cada desvío puede tener múltiples puntos de entrada y salida; se deben cargar seis estaciones de trenes y doce cambios de agujas; cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes; y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente;
encontrar el camino más corto desde:

la estación King's Cross hasta la estación Waterloo,
la estación Victoria Train Station hasta la estación Liverpool Street Station,
la estación St. Pancras hasta la estación King's Cross;


Ejercicio 4
Desarrollar un algoritmo numérico iterativo que permita calcular el método de la bisección de una función f(x).
Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).
Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).
Comparar los tres algoritmos anteriores para resolver la siguiente función: x3 + x +16 = 0, respecto de la cantidad de iteraciones necesarias por cada método para converger. ¿Cuánto es la diferencia en decimales entre las distintas soluciones?

 
