from grafo import Graph

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
# d)cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey,Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8


starwar=Graph(False)
starwar.insert_vertice("Yoda")
starwar.insert_vertice("Luke Skywalker")
starwar.insert_vertice("Darth Vader")
starwar.insert_vertice("Boba Fett")
starwar.insert_vertice("C-3PO")
starwar.insert_vertice("Leia")
starwar.insert_vertice("Rey")
starwar.insert_vertice("Kylo Ren")
starwar.insert_vertice("Chewbacca")
starwar.insert_vertice("Han Solo")
starwar.insert_vertice("R2_D2")
starwar.insert_vertice("BB-8")

starwar.insert_arista("Yoda","Luke Skywalker",3)
starwar.insert_arista("Yoda","Darth Vader",1)
starwar.insert_arista("Luke Skywalker","Leia Organa",5)
#muestra el grafo
starwar.show_graph()
#arbol expansión minimo y si incluye a yoda

bosque = starwar.kruskal("Yoda")
contiene_a_yoda = False
for arbol in bosque:
    if "Yoda" in arbol:
        contiene_a_yoda = True
        break
print("Arbol de expansión de minimo: ")
print(bosque)
if contiene_a_yoda == False:
    print("el arbol de expansión minimo no contiene a yoda")
else:
    print("el arbol de expansión minimo  contiene a yoda")


#arista con el peso maximo 
maxep = 0
personaje = None
for nodo in starwar.elements:
    for arista in nodo["aristas"]:
        if arista["peso"] > maxep:
            maxep = arista["peso"]
            personaje = (nodo["value"],arista["value"])
print(f"Los personajes que más episodios comparten son {personaje[0]} y {personaje[1]} con {maxep} episodios.")



