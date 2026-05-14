"""Exercício 02
Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a. A média aritmética dos números armazenados na lista.
b. O somatório dos números pares armazenados na lista.
"""
# #Julia
# # Exercício 2
# numeros = []
#
# for i in range(4):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
#
# media = sum(numeros) / len(numeros)
#
# soma_pares = 0
#
# for numero in numeros:
#     if numero % 2 == 0:
#         soma_pares += numero
#
# print("\nLista:", numeros)
# print("Média aritmética:", media)
# print("Soma dos pares:", soma_pares)

# #Victor
# par = []
# media = []
# for i in range (1,5):
#     v1 = int(input(f'Digite  valor valor. número {i}: '))
#
#     media.append(v1)
#
#     if v1 % 2 ==0:
#        par.append(v1)
#
#
# print(f'A soma dos numeros pares é: {sum(par)}')
# print(f'A média aritimética é: {sum(media) / len(media)}')

# #Vinicius
# print("digite 10 numeros")
# lista = []
# soma = 0
# soma_pares = 0
# for i in range(1, 5):
#     n = int(input("numero: "))
#     lista.append(n)
#     soma += n
#     if n % 2 == 0:
#         soma_pares += n
# media = soma / len(lista)
# print(f"a media dos numeros é {media}")
# print(f"a soma dos pares é {soma_pares}")

# #Giovanni
# numeros = []
#
# for i in range(10):
#     numero = int(input(f"Digite o {i + 1}º número inteiro: "))
#     numeros.append(numero)
#
# media = sum(numeros) / len(numeros)
#
# soma_pares = 0
#
# for numero in numeros:
#     if numero % 2 == 0:
#         soma_pares += numero
#
# print(f"\nMédia aritmética: {media}")
# print(f"Somatório dos números pares: {soma_pares}")


#Prof
numeros = []
soma = 0
qt = 0
soma_pares = 0

for i in range(4):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    soma += numero
    qt += 1
    if numero % 2 == 0:
        soma_pares += numero

print(f"\nMédia aritmética: {soma/qt:.2f}")
print(f"Somatório dos números pares: {soma_pares}")