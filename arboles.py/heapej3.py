

#El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
#ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
#se realizan, contemplando lo siguiente:

#a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
#te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma

#nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;

#b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
#mente la cantidad de Stormtroopers requeridos;

#c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
#menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;

#d. opcionalmente se podrán agregar operaciones luego de atender una;

#e. realizar la atención de las operaciones de la cola;

#f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
#para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;

#g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
#Snoke para destruir el planeta Takodana.
from heap import HeapMax
from heap import HeapMin

heap = HeapMax()

actividades = [
    (3, ("Líder Supremo Snoke", "Destruir la resistencia en Jakku", "10:00", 50)),
    (3, ("Kylo Ren", "Buscar mapa de Skywalker", "11:00", None)),
    (2, ("Capitán Phasma", "Revisión de disciplina", "12:00", 10)),
    (2, ("Capitán Phasma", "Inspeccionar armas", "13:00", 5)),
    (2, ("Capitán Phasma", "Organizar patrullas", "14:00", 15)),
    (2, ("Capitán Phasma", "Entrenamiento de Stormtroopers", "15:00", 20)),
    (1, ("General Hux", "Revisión de sistemas", "16:00", None)),
    (1, ("General Hux", "Supervisión de prisioneros", "17:00", None))
]

#PUNTO A
for actividad in actividades:
    heap.add(actividad)

#PUNTO B
def mostrar_actividad(actividad):
    encargado, descripcion, hora, stormtroopers = actividad
    stormtroopers_str = f", Stormtroopers: {stormtroopers}" if stormtroopers else ", Stormtroopers: No requeridos"
    return f"Encargado: {encargado}, Descripción: {descripcion}, Hora: {hora}{stormtroopers_str}"

#PUNTO E y F
for i in range(5):
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {i+1}: {mostrar_actividad(actividad_atendida)}")


heap.add((2, ("Capitán Phasma", "Revisión de intrusos en el hangar B7", "18:00", 25)))

#PUNTO G
actividad_atendida = heap.remove()[1]
print(f"Atendiendo operación 6: {mostrar_actividad(actividad_atendida)}")


heap.add((3, ("Líder Supremo Snoke", "Destruir el planeta Takodana", "19:00", None)))


contador = 7
while heap.elements:
    actividad_atendida = heap.remove()[1]
    print(f"Atendiendo operación {contador}: {mostrar_actividad(actividad_atendida)}")
    contador += 1






