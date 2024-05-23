#Desarrollar un algoritmo que permita calcular la 
#siguiente serie:h(n)=1 + 1/2 + 1/3 +...+1/n..
def sumatoria_serie(numero):
    if numero==1:
        return 1
    else:
        return 1/numero+sumatoria_serie(numero-1)
print(sumatoria_serie(99))