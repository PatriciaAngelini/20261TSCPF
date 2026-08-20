#1. Agenda (pressupoe varias pessoas)
#nome, endereco, telefone, idade

#2. Ja com a agenda montada, acrescenta para todas pessoas a informacao de estado civil

#3. Exclui uma pessoa da agenda pelo nome da pessoa

#4. Ordenar essa agenda pela idade da pessoa (decrescente)

# exemplodic_dic = {
#     'Vitor':{'endereco':'r x 123', 'telefone':134},
#     'Antonio': {'endereco': 'r x 123', 'telefone': 134}
# }
# exemplolista_dic = [
#     {'nome':'Vitor','endereco':'r x 123', 'telefone':134},
#     {'nome':'Antonio', 'endereco': 'r x 123', 'telefone': 134}
# ]

#Vitor
# print(f'{'-' * 30} AGENDA {'-' * 30}')
# resp = 'S'
# agenda = []
# while resp == 's' or resp == 'S':
#     nome = input('Digite o nome: ')
#     endereco = input('Digite o endereço: ')
#     telefone = int(input('Digite o telefone: '))
#     idade = int(input('Digite a sua idade: '))
#     resp = input('Deseja continuar a adicionar pessoas na agenda? (s/n): ')
#
#     pessoa = {'nome': nome, 'endereco': endereco, 'telefone': telefone, 'idade': idade}
#     agenda.append(pessoa)
#
# print(agenda)

##Comentarios da professora
# agenda = []
# while True:
#     nome = input('Digite o nome: ')
#     idade = int(input('Digite a sua idade: '))
#     agenda.append({'nome': nome, 'idade': idade})
#     resp = input('Deseja continuar a adicionar pessoas na agenda? (s/n): ').lower()
#     if resp in ('n', 'nao'):
#         break
# print(agenda)

# #Guilherme Ladeira
# agenda = []
# while True:
#     pessoa = {'nome': input('Digite seu nome: '),
#           'idade': int(input('Digite sua idade: ')),
#           'endereco': input('Digite seu endereco: '),
#           'telefone':input('Digite seu telefone: ')
#           }
#     agenda.append(pessoa)
#     repetir = input('Voce quer repetir?(Digite S/N): ').upper()
#
#     if repetir != 'S' and repetir != 'SIM':
#         break
# print(agenda)

#Comentarios da professora
# agenda = []
# while True:
#     agenda.append({'nome': input('Digite o nome: '), 'idade':  int(input('Digite a sua idade: '))})
#     resp = input('Deseja continuar a adicionar pessoas na agenda? (s/n): ').lower()
#     if resp in ('n', 'nao'):
#         break
# print(agenda)

# agenda = [{'nome': 'Pat', 'endereco': '123', 'telefone': 456, 'idade': 55}, {'nome': 'Antonio', 'endereco': 'rua x 123', 'telefone': 1234, 'idade': 19}]
agenda = [{'nome': 'P', 'idade': 12}, {'nome': 'A', 'idade': 34}, {'nome': 'G', 'idade': 56}]
#print(f'{'-' * 30} Adicinando estado civil {'-' * 30}')

# for pessoa in agenda:
#     pessoa['estado_civil'] = input(f"Qual o estado civil de {pessoa['nome']}? ")
#
# print(agenda)

# #Gui
# #2. Ja com a agenda montada, acrescenta para todas pessoas a informacao de estado civil
#
# for pessoa in agenda:
#     pessoa.update({'estado civil': input('Digite seu estado Civil: ')})
# print(agenda)
#
# agenda = [{'nome': 'P', 'idade': 12}, {'nome': 'A', 'idade': 34}, {'nome': 'G', 'idade': 56}]
#
# del_ = input('Digite o nome da pessoa que voce gostaria de excluir da agenda: ')
#
# for indice, pessoa in enumerate(agenda):
#     print(f'{indice} - {pessoa}')
#     if pessoa['nome'] == del_:
#         del agenda[indice]
#         break

# agenda = [{'nome': 'P', 'idade': 12}, {'nome': 'P', 'idade': 34}, {'nome': 'G', 'idade': 56}]
# print(agenda)
# del_ = input('Digite o nome da pessoa que voce gostaria de excluir da agenda: ')
#
# for indice, pessoa in enumerate(agenda):
#     print(f'{indice} - {pessoa}')
#     if pessoa['nome'] == del_:
#         del agenda[indice]
#
# print(agenda)
#                     #0                          1                         2
#                                             #   0                           1
# agenda = [{'nome': 'P', 'idade': 12}, {'nome': 'G', 'idade': 34}, {'nome': 'P', 'idade': 56}]
# print(agenda)
# del_ = input('Digite o nome da pessoa que voce gostaria de excluir da agenda: ')
#
# for pessoa in agenda:
#     print(f'{pessoa}')
#     if pessoa['nome'] == del_:
#         agenda.remove(pessoa)
#
# print(agenda)
#
# #3. exclui uma pessoa da agenda pelo nome da pessoa
# nome = input('Digite o nome da pessoa para exluir:')
# for pessoa in listaAgenda:
#     if nome == pessoa['nome']:
#      listaAgenda.remove(pessoa)

# agenda_ordenada = sorted(agenda, key=lambda pessoa: pessoa['idade'])
#


print('Obter a idade')
print('def')
def getidade (dicionario:dict) -> int:
    return dicionario['idade']

pessoa = {'nome':'Vitor', 'idade': 23}
pessoa2 = {'nome':'Guilherme', 'idade': 25}

print(getidade(pessoa))
print(getidade(pessoa2))
print('lambda')
lidade = lambda dicionario:dicionario['idade']
print(lidade(pessoa))
print(lidade(pessoa2))

print('aplicando na agenda')
agenda = [{'nome': 'P', 'idade': 12}, {'nome': 'G', 'idade': 34},
          {'nome': 'P', 'idade': 56}, {'nome': 'K', 'idade': 7}]
for pessoa in agenda:
    print(lidade(pessoa))
print('Ordenacao em lista')
lista = [5, 66, 2, 8]
print(lista)
lista.sort()
print(lista)

lista = ['a', 'ka', 'ax', 'po']
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print(agenda)
#agenda.sort(key=getidade, reverse=True)
agenda_ordenada = sorted(agenda, key=lambda pessoa: pessoa['idade'])
agenda.sort(key=(lambda dicionario:dicionario['idade']), reverse=True)
print(agenda)


