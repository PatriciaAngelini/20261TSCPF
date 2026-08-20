#1. Crie um conjunto com os nomes da agenda a partir do dicionario abaixo
#agenda= [{'nome': 'Pat', 'telefone': 1234},
#{'nome': 'Antonia', 'telefone': 567},{'nome': 'Maria', 'telefone': 1940309238}]

# #Vitor Matias
# agenda= [{'nome': 'Pat', 'telefone' : 1234},
# {'nome': 'Antonia', 'telefone': 567},{'nome' : 'Maria', 'telefone' : 1940309238}]
#
# print(f'{'-'*30} AGENDA {'-'*30}')
# print('')
# print(agenda)
#
# #perconrrendo a lsita de conjunto e separando os nomes com for e .add
# nomes = set()
# for pessoa in agenda:
#     nomes.add(pessoa['nome'])
#
# print('')
# print(f'{'-'*30}Lista de nomes a partir da agenda: {'-'*30}')
# print('')
# print(nomes)

#Ana Julia - set comprehension
agenda = [{'nome': 'Pat', 'telefone': 1234},
          {'nome': 'Antonia', 'telefone': 567},
          {'nome': 'Maria', 'telefone': 1940309238}]

print(agenda)
nomes = set()
print(nomes)
for pessoa in agenda:
    nomes.add(pessoa['nome'])

print(nomes)
print(type(nomes))
nomes_comprehension = {pessoa['nome'] for pessoa in agenda}
print(nomes_comprehension)

#2
# usuarios_ativos = {
#     'Ana', 'Bruno', 'Carlos',
#     'Daniela', 'Eduardo',
#     'Fernanda', 'Gabriel'
# }
# usuarios_bloqueados = {
#     'Carlos', 'Fernanda'
# }
# usuarios_admin = {
#     'Ana', 'Carlos', 'Gabriel'
# }

# Quais usuários estão ativos?
# Quais usuários estão bloqueados?
# Quais administradores estão ativos?
# Quais administradores estão bloqueados?
# Quais usuários ativos não são administradores?
# Quais usuários são administradores e não estão bloqueados?
# Quais usuários estão ativos e bloqueados simultaneamente?

# #Vitor Matias
# usuarios_ativos = {
#     'Ana', 'Bruno', 'Carlos',
#     'Daniela', 'Eduardo',
#     'Fernanda', 'Gabriel'
# }
#
# usuarios_bloqueados = {
#     'Carlos', 'Fernanda'
# }
#
# usuarios_admin = {
#     'Ana', 'Carlos', 'Gabriel'
# }
#
# print(f'{'-' * 30} Quais usuários estão ativos? {'-' * 30}')
# print('')
# print(usuarios_ativos)
# print('')
#
# print(f'{'-' * 30} Quais usuários estão bloqueados? {'-' * 30}')
# print('')
# print(usuarios_bloqueados)
#
# # Quais administradores estão ativos? ATIVOS E ADMIN
# print(f'{'-' * 30} # Quais administradores estão ativos? {'-' * 30}')
# print('')
# adm_ativo = usuarios_admin.intersection(usuarios_ativos)
#
# print(adm_ativo)
# print('')
# # Quais administradores estão bloqueados? ADMIN E BLOQUEADOS
# print(f'{'-' * 30} Quais administradores estão bloqueados?  {'-' * 30}')
# print('')
# bloqu = usuarios_admin.intersection(usuarios_bloqueados)
# print(bloqu)
#
# # Quais usuários ativos não são administradores? ATIVOS - ADMIN
# print(f'{'-' * 30} Quais usuários ativos não são administradores?  {'-' * 30}')
# print('')
# adm_ativo = usuarios_admin.intersection(usuarios_ativos)
# usu_n_adm = usuarios_ativos.symmetric_difference(adm_ativo)
#
# usu_n_adm1 = usuarios_ativos.difference(usuarios_admin)
# print(usu_n_adm)
# print(usu_n_adm1)
# print('')
# # Quais usuários são administradores e não estão bloqueados?
# print(f'{'-' * 30} Quais usuários são administradores e não estão bloqueados?  {'-' * 30}')
# print('')
# usu_bloq = usuarios_admin.intersection(usuarios_bloqueados)
# usu_adm_n_bloq = usuarios_admin.symmetric_difference(usu_bloq)
# print(usu_adm_n_bloq)
# print('')
# # Quais usuários estão ativos e bloqueados simultaneamente?
# print(f'{'-' * 30} Quais usuários estão ativos e bloqueados simultaneamente?  {'-' * 30}')
# ativ_bloq = usuarios_ativos.intersection(usuarios_bloqueados)
# print(ativ_bloq)
# print('')
# #

# #Ana Julia
# # 7. Exercicio: usuarios ativos/bloqueados/admin
# # -----------------------------------------------------------
# usuarios_ativos = {
#     'Ana', 'Bruno', 'Carlos',
#     'Daniela', 'Eduardo',
#     'Fernanda', 'Gabriel'
# }
# usuarios_bloqueados = {
#     'Carlos', 'Fernanda'
# }
# usuarios_admin = {
#     'Ana', 'Carlos', 'Gabriel', 'Joaquim'
# }
#
# print('\nQuais usuarios estao ativos?')
# print(usuarios_ativos)
#
# print('\nQuais usuarios estao bloqueados?')
# print(usuarios_bloqueados)
#
# print('\nQuais administradores estao ativos?')
# admins_ativos = usuarios_admin.intersection(usuarios_ativos)
# print(admins_ativos)
#
# print('\nQuais administradores estao bloqueados?')
# admins_bloqueados = usuarios_admin.intersection(usuarios_bloqueados)
# print(admins_bloqueados)
#
# print('\nQuais usuarios ativos nao sao administradores?')
# ativos_nao_admin = usuarios_ativos.difference(usuarios_admin)
# print(ativos_nao_admin)
#
# print('\nQuais usuarios sao administradores e nao estao bloqueados?')
# admins_nao_bloqueados = usuarios_admin.difference(usuarios_bloqueados)
# print(admins_nao_bloqueados)
#
# print('\nQuais usuarios estao ativos e bloqueados simultaneamente?')
# ativos_e_bloqueados = usuarios_ativos.intersection(usuarios_bloqueados)
# print(ativos_e_bloqueados)
#
# print('\nBonus: quem esta em SO UM dos dois (ativos ou admin, nunca os dois)')
# so_um_dos_dois = usuarios_ativos.symmetric_difference(usuarios_admin)
# print(so_um_dos_dois)

#Guilherme Ladeira
usuarios_ativos = {
    'Ana', 'Bruno', 'Carlos',
    'Daniela', 'Eduardo',
    'Fernanda', 'Gabriel'
}

usuarios_bloqueados = {
    'Carlos', 'Fernanda'
}

usuarios_admin = {
    'Ana', 'Carlos', 'Gabriel'
}

print('\nQuais usuários estão ativos?')
print(usuarios_ativos)

print('\nQuais usuários estão bloqueados?')
print(usuarios_bloqueados)

print('\nQuais administradores estão ativos?')
print(usuarios_admin & usuarios_ativos)

print('\nQuais administradores estão bloqueados?')
print(usuarios_admin & usuarios_bloqueados)

print('\nQuais usuários ativos não são administradores?')
print(usuarios_ativos - usuarios_admin)

print('\nQuais usuários são administradores e não estão bloqueados?')
print(usuarios_admin - usuarios_bloqueados)

print('\nQuais usuários estão ativos e bloqueados simultaneamente?')
print(usuarios_ativos & usuarios_bloqueados)

print('\nBonus: quem esta em SO UM dos dois (ativos ou admin, nunca os dois)')
print( usuarios_ativos^usuarios_admin)
#os simbolos funcionam e equivalem
#& intersection
#| union
#- difference
#^ symmetric_difference

