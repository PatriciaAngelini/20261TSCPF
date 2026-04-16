"""8. Escreva um algoritmo que solicite 10 números e informe qual foi o menor número
digitado."""
#vamos fazer usando o i <= 10
#o racional é comparar o numero que esta sendo digitado com o numero anterior
#mas no primeiro caso que a gente nao tem numero anterior??? como fazemos??
#sabemos que dentro do while, vai ter que ter uma condicao especial quando for a
#primeira vez
# i = 1
#
# while i <= 3:
#     n = int(input(f'Entre com o {i}º número:'))
#     if i == 1:
#         anterior = menor = n
#     if n < anterior:
#         menor = n
#     i += 1
#     anterior = n
# print(f'O menor numero da sequencia é {menor}')

#Giovanni
# contador = 0
# menor = 0
# while contador < 5:
#     numero = int(input(f"Digite o {contador + 1}° número: "))
#     contador += 1
#     if menor == 0 or numero < menor:
#         menor = numero
# print(f"O menor número digitado foi: {menor}")

contador = 0
menor = 0
while contador < 5:
    numero = int(input(f"Digite o {contador + 1}° número: "))
    if contador == 0 or numero < menor:
        menor = numero
    contador += 1
print(f"O menor número digitado foi: {menor}")