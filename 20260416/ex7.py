"""Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
deve solicitar os números novamente) e informe a diferença entre o maior e o menor
número."""

#Giovanni
# while True:
#     num1 = int(input("Digite o primeiro número: "))
#     num2 = int(input("Digite o segundo número: "))
#     if num1 == num2:
#         print("Os números são iguais. Por favor, digite novamente")
#     else:
#         break
#
# if num1 > num2:
#     diferenca = num1 - num2
# else:
#     diferenca = num2 - num1
#
# print(f"A diferença entre o maior e o menor número é: {diferenca}")

num1 = num2 = 1
while num1 == num2:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 == num2:
        print("Os números são iguais. Por favor, digite novamente")

if num1 > num2:
    diferenca = num1 - num2
else:
    diferenca = num2 - num1

print(f"A diferença entre o maior e o menor número é: {diferenca}")