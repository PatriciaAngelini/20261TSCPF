#CRIAR UMA AGENDA COM O NOME DA PESSOA E O TELEFONE DESTA
#Racional criar uma lista e para cada uma das pessoas solicitar a informacao nome e telefone

#O usuario pede informacoes para montar agenda

# resp = 's'
# while resp in ('s', 'sim'):
#     nome = input('qual seu nome?: ')
#
#     resp = input('Quer cadastrar mais uma pessoa?').lower()


# agenda = []
# while True:
#     nome = input('qual seu nome?: ')
#     telefone = int(input('qual seu telefone?: '))
#     info = {'nome':nome, 'telefone':telefone}
#     agenda.append(info)
#     resp = input('Quer cadastrar mais uma pessoa?').lower()
#     if resp in ('n', 'nao'):
#         break
#
# print(agenda)

# #maneira resumida
# agenda = []
# while True:
#     # nome = input('qual seu nome?: ')
#     # telefone = int(input('qual seu telefone?: '))
#     # agenda.append({'nome':nome, 'telefone':telefone})
#     agenda.append({'nome':input('qual seu nome?: '), 'telefone':int(input('qual seu telefone?:'))})
#     resp = input('Quer cadastrar mais uma pessoa?: ').lower()
#     if resp in ('n', 'nao'):
#         break
#
# print(agenda)

agenda= [{'nome': 'Pat', 'telefone': 1234}, {'nome': 'Antonia', 'telefone': 567}]
#Agora você quer acrescentar o estado civil da pessoa
#agenda= [{'nome': 'Pat', 'telefone': 1234, 'estado civil': 'casada'},
#{'nome': 'Antonia', 'telefone': 567, 'estado civil': 'solteira'}]
for pessoa in agenda:
    estado_civil = input(f'Entre com o estado civil de {pessoa['nome']}: ')
    pessoa.update({'estado civil':estado_civil})
print(agenda)

#maneira resumida
for pessoa in agenda:
    pessoa['estado civil'] = input(f'Entre com o estado civil de {pessoa['nome']}: ')
print(agenda)