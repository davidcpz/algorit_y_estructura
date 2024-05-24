#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila,posicion=0,objetos=0):
    if posicion>=len(mochila):
        return print("mochila vacia/ya revisaste toda la mochila")
    if mochila[posicion]=="sable de luz":
        return print ("en horabuena encontraste el sable de luz! despues de haber sacado", objetos +1, "objetos")
    else:
        return usar_la_fuerza(mochila,posicion+1, objetos+1)
mochila = ["comida", "agua", "medkit","ropa", "sable de luz","viajes"]
usar_la_fuerza(mochila)
