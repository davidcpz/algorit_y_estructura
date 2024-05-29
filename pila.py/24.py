#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los 
#cuales se dispone de su nombre y la cantidad de películas de la saga en 
#la que participó, implementar las funciones necesarias para resolver 
#las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando
#como posición uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de 
#la saga, además indicar la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
from pilas import Stack

Marvel_Cinematic_universe =[
    ("Iron Man",10),("Capitan America", 9),("Thor",8),
    ("Hulk",7),("Black Widow",8),("Hawkeye",5),("Groot",5),
    ("Rocket Raccoon",6),("Doctor Strange",4),("Black Panter",3),
    ("Spider-Man",5),("Scarlet Witch",4),("Ant-Man",3),("Vision",3),
    ("Falcon",3)
    ]
pila_Marvel_Cinematic_universe=Stack()

for personaje in Marvel_Cinematic_universe:
    pila_Marvel_Cinematic_universe.push(personaje)
#determinar la posicion de raccoon y groot
posicion_groot = -1
posicion_rocket= -1
posicion_actual= 1
pila_temporal= Stack()

while pila_Marvel_Cinematic_universe.size()> 0:
   personaje = pila_Marvel_Cinematic_universe.pop()
   pila_temporal.push(personaje)
   if personaje[0]=="Rocket Raccoon":
       posicion_rocket= posicion_actual
   if personaje[0]=="Groot":
       posicion_groot=posicion_actual 
       posicion_actual += 1

while pila_temporal.size()>0:
    pila_Marvel_Cinematic_universe.push(pila_temporal.pop())

print ("Rocket esta en la posicion: ", posicion_rocket)
print("Groot esta en la posicion: ", posicion_groot)

#determinar participacion
mas_de_5=[]
while pila_Marvel_Cinematic_universe.size()>0:
    personaje = pila_Marvel_Cinematic_universe.pop()
    pila_temporal.push(personaje)
    if personaje[1] > 5:
        mas_de_5.append(personaje)

while pila_temporal.size()>0:
    pila_Marvel_Cinematic_universe.push(pila_temporal.pop())
print("Los personajes que tienen mas de 5 peliculas son: ", mas_de_5)

#determinar en cuantas peliculas participo black
black_widow_peliculas =0
while pila_Marvel_Cinematic_universe.size()>0:
    personaje = pila_Marvel_Cinematic_universe.pop()
    pila_temporal.push(personaje)
    if personaje[0]=="Black Widow":
        black_widow_peliculas=personaje[1]

while pila_temporal.size()> 0:
    pila_Marvel_Cinematic_universe.push(pila_temporal.pop())
print("Black Widow participo en las peliculas: ", black_widow_peliculas)

#mostrar personajes que comienzan con letra cdg
personajes_con_letra_cdg =[]
while pila_Marvel_Cinematic_universe.size()>0:
    personaje=pila_Marvel_Cinematic_universe.pop()
    pila_temporal.push(personaje)
    if personaje[0][0] in "CDG":
        personajes_con_letra_cdg.append(personaje[0])

while pila_temporal.size()>0:
    pila_Marvel_Cinematic_universe.push(pila_temporal.pop())

print("Los personajes que comienzan con C, D, y G son: ", personajes_con_letra_cdg)

       
