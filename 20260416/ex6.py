"""Solicite vários números ao usuário (até que ele digite o número zero) e informe o
somatório dos números digitados. """

#Giovanni Pascon
# soma = 0
# while True:
#     numero = int(input("Digite um número (0 para sair): "))
#     if numero == 0:
#         break
#     soma += numero
# print(f"Somatório dos números digitados: {soma}")


soma = 0
numero = 1
while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    soma += numero
print(f"Somatório dos números digitados: {soma}")
