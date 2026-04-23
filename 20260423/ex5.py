"""Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada
de cada número (Dica: importe a biblioteca math)."""
# #Mariana Ayumi
# import math
#
# for i in range(3):
#     numero = float(input(f"Digite o {i + 1}º número: "))
#     if numero < 0:
#         print("Não existe raiz quadrada real para número negativo.")
#     else:
#         raiz = math.sqrt(numero)
#         print(f"A raiz quadrada de {numero} é {raiz:.2f}")

#Luana (0.5)
import math

for contador in range(1, 4):
    numero = float(input(f"Digite o {contador}o numero: "))
    raiz_quadrada = math.sqrt(numero)

    print(f"A raiz quadrada de {numero} e {raiz_quadrada}.")