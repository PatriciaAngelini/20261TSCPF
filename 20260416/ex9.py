"""Faça um algoritmo que solicite N números e calcule a média dos números pares e a
média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do
programa)."""
titulo = 'Media de Pares e Impares'
print(f'{titulo:^30}')

q = int(input('Quantos numeros vc deseja para o calculo: '))
i = 1
totalpar, totalimpar, qtp, qti = 0, 0, 0 ,0

while i <= q:
    n = int(input('Entre com o numero: '))
    if n % 2 == 0:
        qtp += 1
        #totalpar = totalpar + n
        totalpar += n
    else:
        qti += 1
        totalimpar +=n
    i += 1

print(f'A média de {qtp} numeros pares é {totalpar/qtp:.2f}')
print(f'A média de {qti} numeros impares é {totalimpar/qti:.2f}')

# #Giovanni
# qtd_numeros = int(input("Digite a quantidade de números que deseja informar: "))
# contador = 0
# soma_pares = 0
# contador_pares = 0
# soma_impares = 0
# contador_impares = 0
#
# while contador < qtd_numeros:
#     numero = int(input(f"Digite o {contador + 1}° número: "))
#     contador += 1
#
#     if numero % 2 == 0:
#         soma_pares += numero
#         contador_pares += 1
#     else:
#         soma_impares += numero
#         contador_impares += 1

media_pares = soma_pares / contador_pares
media_impares = soma_impares / contador_impares

print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")