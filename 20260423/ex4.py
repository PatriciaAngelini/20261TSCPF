"""Escreva um algoritmo que exiba 20 números aleatórios sorteados entre 1 e 50 (Dica: importe a
biblioteca random). """
#Joao Guilherme (0.5)
import random

#Lucas Amaral (0.5):
for _ in range(20): #o underline serve para quando
    # nao quisermos utilizar o valor o contador
  print(random.randint(1, 50))

# #Diego
# import random
#
# i = 0
# while i < 20:
#     numero = random.randint(1, 50)
#     print(numero)
#     i = i + 1