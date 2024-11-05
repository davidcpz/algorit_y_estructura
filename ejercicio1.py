#Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;
#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Ivysaur", "numero": 2, "tipo": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipo": ["eléctrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]},
    {"nombre": "Gardevoir", "numero": 282, "tipo": ["psíquico", "hada"]},
    {"nombre": "Greninja", "numero": 658, "tipo": ["agua", "siniestro"]},
    {"nombre": "Eevee", "numero": 133, "tipo": ["normal"]},
    {"nombre": "Gyarados", "numero": 130, "tipo": ["agua", "volador"]},
]


from arbol_avl import BinaryTree
tree_nombre=BinaryTree()
tree_numero=BinaryTree()
tree_tipo=BinaryTree()

#punto a 

for pokemon in pokemons:
    tree_nombre.insert_node(pokemon["nombre"], pokemon)
    tree_numero.insert_node(pokemon["numero"],pokemon)
    for tipo in pokemon["tipo"]:
        nodo=tree_tipo.search(tipo)
        if nodo:
            nodo.other_value.append(pokemon)
        else:
            tree_tipo.insert_node(tipo,pokemon)

#punto b
buscar=input("ingrese el pokemon que buscas:")
resultado=tree_nombre.proximity_search(buscar)
if resultado is not None:
    print (resultado.other_value)
else:
    print("no esta el pokemon")

nombre_buscado= input("ingrese el nombre del pokemon a buscar")
print(f"Búsqueda por proximidad con '{nombre_buscado}':")
tree_nombre.proximity_search(nombre_buscado)

#punto c

tipo = input("ingrese el tipo de pokemon: ")
print(f"Búsqueda por proximidad con '{tipo}':")
tree_tipo.proximity_search(tipo)

#punto d

tree_numero.inorden()
tree_nombre.inorden()


tree_nombre.by_level()

# punto e) mostrar los datos de jolteon , lycanroc y Tyrantrum
nombres= ["Jolteon", "Lycanroc","Tyrantrum"]
for nombre in nombres:
    resultado = tree_nombre.search(nombre)
    if resultado:
        print(resultado.other_value)
    else:
        print(f"{nombre}no fue encontrado")

# punto f  tipo eléctrico y acero
tipo_a_buscar = input("ingrese el tipo de pokemon que desea buscar: ")
nodo = tree_tipo.search(tipo_a_buscar)
if nodo and nodo.other_value:
    contador = len(nodo.other_value)
else:
    contador = 0
print(f"Total de Pokémon de tipo {tipo_a_buscar}: {contador}")















