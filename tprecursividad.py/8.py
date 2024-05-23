#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
#ma binario.
def convert_to_binary(numero):
    if numero<=1:
        return str(numero)
    else:
        return convert_to_binary(numero//2)+str(numero%2)
print(convert_to_binary(8))