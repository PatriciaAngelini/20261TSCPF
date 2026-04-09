# # #Gabrielle
#
# blococond = int(input("Em qual bloco você mora (1 a 20)? "))
# if blococond >=1 and blococond <= 10:
# #if 1 <= blococond <= 10:
#     print("O síndico responsável pelo seu bloco é o Sr. José.")
# else:
#      print("O síndico responsável pelo seu bloco é o Sr. Hamilton.")

#Igor
# titulo = 'Blocos'
# print(f'{titulo:^40}')
#
# bloco = int(input('Em qual bloco voce mora? '))
#
# if 0 < bloco <= 10:
#     print('O sindico responsavel pelo seu bloco é o Sr. José')
# elif 10 < bloco <= 20:
#     print('O sindico responsavel pelo seu bloco é o Sr. Hamilton')
# else:
#     print('Informe um bloco existente')

# #Felipe
# bloco = int(input("Digite o número do seu bloco (1 a 20): "))
#
# if bloco >= 1 and bloco <= 10:
#     print("O síndico responsável é o Sr. José")
# elif bloco >= 11 and bloco <= 20:
#     print("O síndico responsável é o Sr. Hamilton")
# else:
#     print("Bloco inválido")

# #Vitor Matias
# bloco = int(input('Digite o número do bloco em que você mora: '))
#
# if bloco in (1,2,3,4,5,6,7,8,9,10):
#     print('O sindico responsavel pelo seu bloco é o Sr. José')
#
# if bloco in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
#     print('O sindico responsavel pelo seu bloco é o Sr. Hamilton ')
#
# if bloco == 0 or bloco >20:
#     print('esse número não corresponde a nenhum bloco do condominio')

# #Lucas
# bloco = int(input('Qual bloco entre o 1º e 20º você mora? '))
#
# if 1 <= bloco <= 10:
#     print("O síndico que administrador seu bloco é o José!")
# elif 11 <= bloco <= 20:
#     print("O síndico que administra seu bloco é o Hamilton")
# else:
#     print('Bloco invalido')
#
# #Giovanni
# bloco = int(input("Digite o numero do bloco: "))
# if bloco >= 1 and bloco <= 10:
#     print(f"O sindico do bloco {bloco} é o sr José")
# elif bloco >= 11 and bloco <= 20:
#     print(f"O sindico do bloco {bloco} é o sr Hamilton")
# else:
#     print('Bloco invalido')

#Daniel
sindico_1 = 'José'
sindico_2 = 'Hamilton'

pergunta = int(input('\nInforme sua torre: '))

if 1 < pergunta <= 10:
    print(f'\nSeu síndico é o {sindico_1}')

elif 11 < pergunta <= 20:
    print(f'\nSeu síndico é o {sindico_2}')

else:
    print('\nNúmero inválido')

#Felipe Lessa
bloco = int(input("Bloco (1–20): "))

if 1 <= bloco <= 20:
    if bloco <= 10:
        sindico = "Sr. José"
    else:
        sindico = "Sr. Hamilton"
    print(f"Responsável: {sindico}")
else:
    print("Bloco inválido")