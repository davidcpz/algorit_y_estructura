#Dada una secuencia de caracteres, obtener dicha
#secuencia invertida.
def secuencia_invertida(palabra):
    if len(palabra)==0:
        return palabra 
    else:
        return palabra[-1]+ secuencia_invertida(palabra[:-1])
palabra="catastrofe"
print(secuencia_invertida(palabra))