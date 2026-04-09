#Biblioteca
#sao funcoes e codigo em python que fazem "coisas" especializadas
#a gente utitiza bibliotecas qdo precisa de uma funcao especifica

#Para gerar numeros aleatorios temos a bibliotecam random
import random as r
#Exemplo dia da semana
titulo = 'Dia da semana'
print(f'{titulo:^30}')
#n = int(input('Entre com o numero: '))
n = r.randint(1, 7)
print(n)
match n:
    case 6:
        print('Sexta')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 1 | 7: # | equivalente ao or
        print('Fim de semana')
    case _: #equivale ao else
        print('Numero invalido')