"""Exercício 04
Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as
idades em outra lista.
Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual
a 18 anos."""
# #Vitor Matias
# nomes = []
# idades = []
#
# for i in range(1, 5):
#     v1 = (input(f'Digite o nome da pessoa numero: {i}: '))
#     v2 = (int(input(f'Digite a idade da pessoa numero: {i}: ')))
#     nomes.append(v1)
#     idades.append(v2)
#     if v2 >= 18:
#         print(v1)

# #prof Patricia
# nomes = []
# idades = []
#
# for i in range(1, 5):
#     nome = (input(f'Digite o nome da pessoa numero: {i}: '))
#     idade = (int(input(f'Digite a idade da pessoa numero: {i}: ')))
#     nomes.append(nome)
#     idades.append(idade)
#
# print(nomes)
# print(idades)
#
# for i in range(len(nomes)):
#     if idades[i] >= 18:
#         print(nomes[i])

#Luana
# Exercício 04: Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as
# idades em outra lista.
# Na sequência, exiba os nomes de todas as pessoas que
# possuem idade maior ou igual a 18 anos


nomes = []  # Lista para armazenar os nomes
idades = []  # Lista para armazenar as idades

# Solicitar os nomes e idades de 10 pessoas
for i in range(4):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))

    nomes.append(nome)
    idades.append(idade)

# Exibir os nomes das pessoas com idade >= 18 anos
print('\n' + '='*50)
print('Pessoas com 18 anos ou mais:')
print('='*50)

maiores_de_idade = []
for i in range(len(nomes)):
    if idades[i] >= 18:
        maiores_de_idade.append(nomes[i])
        print(f'• {nomes[i]} - {idades[i]} anos')

if len(maiores_de_idade) == 0:
    print('Nenhuma pessoa possui 18 anos ou mais.')

print('='*50)
print(f'Total de maiores de idade: {len(maiores_de_idade)}')
print('='*50)