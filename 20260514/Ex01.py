"""Exercício 01
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e
os números ímpares em outra lista. Exiba as duas listas ao usuário.
"""
print('Pares e Impares')
# numeros = [] #lista vazia
# numeros = list() #lista vazia
pares, impares, numeros = [], [], []
for i in range(5):
    n = int(input('Entre com um numero: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'todos: {sorted(numeros)}')
impares.sort()
pares.sort()
print(f'impares: {impares}')
print(f'pares: {pares}')


