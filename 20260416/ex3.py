"""
Escreva um algoritmo que solicite a idade de 15 pessoas e informe a quantidade de
pessoas com idade inferior a 18 anos.
"""
#Giovanni Pascon
# pessoas = 0
# menores = 0
# qtpessoas = 3
# while True:
#     idade = int(input(f"Digite a idade da pessoa {pessoas + 1}: "))
#     if idade < 18:
#         menores += 1
#     pessoas += 1
#     if pessoas == qtpessoas:
#         break
# print(f"Quantidade de pessoas menores de idade: {menores}")

pessoas = 1
menores = 0
qtpessoas = 3
while True:
    idade = int(input(f"Digite a idade da pessoa {pessoas}: "))
    if idade < 18:
        menores += 1
    pessoas += 1
    if pessoas > qtpessoas:
        break
print(f"Quantidade de pessoas menores de idade: {menores}")