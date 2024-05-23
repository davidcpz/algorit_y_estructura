#Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
#matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
#y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
#avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.