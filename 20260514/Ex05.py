"""Exercício 05
Preencha a lista com 10 números aleatórios. Na sequência, solicite um número ao
usuário e informe quantas vezes esse número aparece na lista."""
import random

numeros = []  # Lista para armazenar os números

# Preencher a lista com 10 números aleatórios
for i in range(10):
    numero = random.randint(1, 6) # diminui o range para aumentar a chance de repetidos
    numeros.append(numero)

print(numeros)
numero = int(input('Entre com um numero de 1 a 6: '))
print(f'O numero {numero} aparece {numeros.count(numero)} vezes')