#Desarrollar una función que permita convertir un 
#número romano en un número decimal.
def romano_a_decimal(romano):
    #diccionario con los romanos
    romano_a_decimal={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#funcion recursiva
    def convertir(romano):
# si la cadena romano esta vacia el valor es cero
        if not romano:
            return 0
#si la longitud de la cadena es 1 devolvemos su valor decimal directamente
        if len(romano)==1:
            return romano_a_decimal[romano[0]]
#si el valor decimal del primer simbolo es menor que el del siguiente , restamos
        if romano_a_decimal[romano[0]]< romano_a_decimal[romano[1]]:
            return romano_a_decimal[romano[1]]-romano_a_decimal[romano[0]]+convertir(romano[2:])
#si el valor decimal del primer simbolo es mayor o igual al del siguiente, sumamos 
    
        else:
            return romano_a_decimal[romano[0]] + convertir [1:]
    
    return convertir(romano)


numero_romano="L"
print(f"el numero romano {numero_romano} es equivalente a {romano_a_decimal(numero_romano)} en decimal")