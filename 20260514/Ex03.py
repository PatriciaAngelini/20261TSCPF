"""Exercício 03
Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
a. a lista com todos os itens armazenados.
b. o somatório de todos os números contidos na lista.
c. o maior número da lista.
d. o menor número da lista.
"""
#usar random e randint
#Luana
# Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
# a. a lista com todos os itens armazenados.
# b. o somatório de todos os números contidos na lista.
# c. o maior número da lista.
# d. o menor número da lista.

import random

numeros = []  # Lista para armazenar os números

# Preencher a lista com 20 números aleatórios entre 1 e 50
for i in range(20):
    numero = random.randint(1, 50)
    numeros.append(numero)

# Calcular os resultados
somatoria = sum(numeros)
maior = max(numeros)
menor = min(numeros)

# Exibir resultados
print('\n' + '=' * 60)
print('a. Lista com todos os números armazenados:')
print(numeros)
print('=' * 60)
print(f'b. Somatório de todos os números: {somatoria}')
print(f'c. Maior número da lista: {maior}')
print(f'd. Menor número da lista: {menor}')
print('=' * 60)
