#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#se (MCU), desarrollar un algoritmo que contemple lo siguiente:

#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
#leano que indica si es un héroe o un villano, True y False respectivamente;

#b. listar los villanos ordenados alfabéticamente;

#c. mostrar todos los superhéroes que empiezan con C;

#d. determinar cuántos superhéroes hay el árbol;

#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;

#f. listar los superhéroes ordenados de manera descendente;

#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
                    #I. determinar cuántos nodos tiene cada árbol;
                    #II. realizar un barrido ordenado alfabéticamente de cada árbol.
from arbol_avl import BinaryTree
arbol = BinaryTree()
arbol.insert_node('Iron Man', {'is_hero': True})
arbol.insert_node('Thanos', {'is_hero': False})
arbol.insert_node('Captain America', {'is_hero': True})
arbol.insert_node('Ultron', {'is_hero': False})
arbol.insert_node('Doctor Strang', {'is_hero': True})  # Mal escrito 
arbol.insert_node('Loki', {'is_hero': False})
arbol.insert_node('Scarlet Witch', {'is_hero': True})

#print("Villanos Ordenados Alfabeticamente: ")

#arbol.inorden_villanos()

#print("SuperHeroes que inician con C: ")
#arbol.inorden_superheros_start_with("C")

#print("En el arbol hay : ", arbol.contar_super_heroes(),"SuperHeroes")

#print("SuperHeroes ordenados de manera descendente: ")

#arbol.postorden()
arbol.proximity_search("Doctor")
arbol.delete_node("Doctor Strang")
arbol.insert_node("Doctor Strange",{"is_hero":True})


#arbol_heroes = BinaryTree()
#arbol_villanos = BinaryTree()
#arbol_heroes.insert_node('Iron Man', {'is_hero': True})
#arbol_heroes.insert_node('Captain America', {'is_hero': True})
#arbol_heroes.insert_node('Doctor Strange', {'is_hero': True})
#arbol_heroes.insert_node('Scarlet Witch', {'is_hero': True})
#arbol_villanos.insert_node('Loki', {'is_hero': False})
#arbol_villanos.insert_node('Ultron', {'is_hero': False})
#arbol_villanos.insert_node('Thanos', {'is_hero': False})

#print(arbol_heroes.contar_super_heroes())

#print(arbol_villanos.contar_villanos())

#arbol_heroes.inorden()

#arbol_villanos.inorden()