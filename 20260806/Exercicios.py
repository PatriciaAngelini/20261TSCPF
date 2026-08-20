# print('Calculo da media da lista com lambda')
# #Vitor
# listaoriginal = [234,64,13467,45,89,23]
#
# media = lambda m: round(sum(m)/ len(m), 2)
#
# print(media(listaoriginal))
#
# print('\nRetorna o numero em uma lista se ele for par')
# #Luana
# retorna_par = lambda numero: numero if numero % 2 == 0 else None
# print(retorna_par(10))
# print(retorna_par(11))
#
# print(list(map(retorna_par, listaoriginal)))
#
# print('\nRemover Espacos')
# #Luana
# Original = [' vermelho', ' verde', 'azul ', ' amarelo ']
# sem_espacos = [cor.strip() for cor in Original]
# print(sem_espacos)
#
# print('\nPositivos')
# #Vitor
# lNumeros = [-4, -2, 0, 2, 4]
# resultado = [n for n in lNumeros if n >=0]
# print(f'Lista sem os numeros negativos: {resultado }')


#Excecoes
# print('\nFrutas')
# try:
#     letra = input('Entre com uma letra:').upper()[0]
#     match letra:
#         case 'A':
#             print('Abacaxi')
#         case 'B':
#             print('Banana')
#         case 'C':
#             print('Caqui')
#         case 'D':
#             print('Damasco')
#         case _ :
#             raise Exception('Letra Invalida')
# except Exception as e:
#     print(f'Ocorreu uma exceção:{e}')


print('\nSalario Minimo')
#Vitor
try:
    #salario_minimo = 1621.00
    salario_minimo:float = 1621
    salario = float(input('Digite o valor do seu salário:  '))
    if salario <0:
        raise Exception('Salário não pode ser um valor negativo')
    if salario <= salario_minimo:
        #print('Você tem que receber até um salário minimo')
        raise Exception('Você tem que receber até um salário minimo')
    if salario > salario_minimo:
        print(f'Voce recebe {salario/ salario_minimo:.2f} minimos')

except ValueError:
    print('O salario precisa ser um numero')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    #print('O valor do salário não pode ser negativo')