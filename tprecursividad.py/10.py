#Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contar_digitos(numero):
    if numero < 10 :
        return 1
    else:
        return 1+contar_digitos(numero//10)
print(contar_digitos(562396488334981655151))