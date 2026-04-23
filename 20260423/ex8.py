"""Escreva um algoritmo que determine se um número N (informado pelo usuário) é primo ou não. """
#Gabriele
#racional é pegar os numeros entre 1 e o numero escolhido e tentar dividir
#qdo ela encontra um numero divisivel ela soma um no contador de divisiveis

# n = int(input("Digite um número: "))
# divisores = 0
#
# for i in range(1, n + 1):
#
#     if n % i == 0:
#         divisores += 1
#     print(i, 'divisores', divisores)
#
# if divisores == 2:
#     print(f"O número {n} é PRIMO.")
# else:
#     print(f"O número {n} NÃO é primo.")

# #Lucas Lunas
# print("-" * 10, "EX 8", "-" * 10)
# n = int(input("Digite um número inteiro: "))
# primo = True
# #Racional excluir as pontas (1, e o proprio)
# for i in range(2, n):
#     if n % i == 0:
#         primo = False
#         #break
#
# if n < 2:
#     primo = False
#
# if primo:
#     print(f"{n} é primo")
# else:
#     print(f"{n} não é primo")

#Diego Gaspar
numero = int(input("Digite um número inteiro: "))

primo = True

if numero < 2:
    primo = False
else:
    print('ate', int(numero ** 0.5) + 1)
    for i in range(2, int(numero ** 0.5) + 1): #racional é tentar dividir pelos
        #numeros da raiz quadrada inferior, porque mais do que a raiz quadrada
        #sempre vai dar
        #numero quebrado (decimal)
        if numero % i == 0:
            primo = False
            #break
        print(i)
if primo:
    print(numero, "é primo")
else:
    print(numero, "não é primo")