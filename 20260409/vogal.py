"""
Escreva um programa que peça uma letra e mostre se é uma vogal
ou se é uma consoante
Use o que aprendeu hoje
"""
#
# #Diego
# letra = input("Digite uma letra: ").lower()
#
# if letra == 'a':
#     print("É uma vogal")
# elif letra == 'e':
#     print("É uma vogal")
# elif letra == 'i':
#     print("É uma vogal")
# elif letra == 'o':
#     print("É uma vogal")
# elif letra == 'u':
#     print("É uma vogal")
# else:
#     print("É uma consoante")

# #Guilherme Ladeira
# titulo = 'consoante ou vogal?'
# print(f'{titulo:^40}')
#
# l = input('Digite uma letra:').lower().strip()
# if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
#     print(f'A letra {l} é uma vogal!')
# else: print(f'A letra {l} é uma consoante!')

#Beatriz
# titulo= 'Vogal ou cnsoante?'
# print(f'{titulo:^30}')
#
# n= str(input('Digite uma letra: ')).lower()
#
# match n:
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print ('Essa letra é uma vogal!')
#     case _: #o _ indica como se fosse else
#         print ('Essa letra é uma consoante!')

# #João Marcos
# letra = input("Digite uma letra: ")
# if letra in "aeiouAEIOU": #toda string é um elemento iteravel
# #elemento iteravel é que eu posso percorrer um a um
# #if letra in ('a', 'e', 'i', 'o', 'u'):
#     print("Vogal")
# else:
#     print("Consoante")
#
#João Cavalcanti
letra = input('digite uma letra: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print(f'a letra {letra} é uma vogal.')
else:
    print(f'a letra {letra} é uma consoante.')
