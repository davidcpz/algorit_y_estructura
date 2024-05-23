#Desarrollar un algoritmo que permita implementar la
# búsqueda secuencial con centinela de manera 
#recursiva, y permita determinar si un valor dado 
#está o no en dicha lista.
numeros =[5,8,9,4,3,6,23,55,44,82]
def bb_recursiva(lista,buscado,primero,ultimo):
    medio= (primero+ultimo)//2
    if primero > ultimo:
        return None
    elif buscado==lista [medio]:
        return medio 
    else:
        if buscado < lista[medio]:
            return bb_recursiva(lista,buscado,primero,medio-1)
        else:
            return bb_recursiva(lista,buscado,medio+1,ultimo)

pos= bb_recursiva(numeros, 3,0,len(numeros)-1)
print(pos)