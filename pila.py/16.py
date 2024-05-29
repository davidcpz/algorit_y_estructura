#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
#bos episodios.

from pilas import Stack
def interseccion (p1,p2):
    lista1=[]
    lista2=[]
    while p1.size()>0:
        lista1.append(p1.pop())
    while p2.size()>0:
        lista2.append(p2.pop())
    for element in reversed (lista1):
        p1.push(element)
    for element in reversed(lista2):
        p2.push(element)
    interseccion_pilas= list(set(lista1) & set (lista2))
    return interseccion_pilas

episodio_V_characters= ["Luke Skywalker","Darth Vader","Leia Organa","Han Solo","Chewbacca", "Yoda"]
episodio_VII_characters=["Rey","Finn","Kylo Ren","Laia Organa", "Han Solo","Chewbaca", "Luke Skywalker"]
pila_episodio_V = Stack()
pila_episodio_VII=Stack()

for personajes in episodio_V_characters:
    pila_episodio_V.push(personajes)
for personajes in episodio_VII_characters:
    pila_episodio_VII.push(personajes)
personajes_en_comun=interseccion(pila_episodio_V,pila_episodio_VII)
print ("Los personajes en comun son: ", personajes_en_comun)