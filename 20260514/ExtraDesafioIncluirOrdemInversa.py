#desafio é ir acrescentando sempre no inicio
#exemplo: se eu digitar 5, 6, 7, 8
#incluir na lista 8, 7, 6, 5
numeros = []
for i in range(4):
    n = int(input('Entre com um numero: '))
    numeros.insert(0,n)
print(numeros)