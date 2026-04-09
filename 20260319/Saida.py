#Saida de dados
#print aceita varios argumentos/parametros
#ex: print('Olá "', nome, '"')
#Ha outras maneira de fazermos isso
#CONCATENACAO
#ex: print('Olá "'+ nome +'"') # + é a concatenação de strings
#FORMATACOES
#f-strings frases formatadas
#misturar texto e variavel
nome = 'Ana Julia'
print(f'Olá "{nome}"!')

#um jeito mais antigo .format
#vão encontrar no mercado de trabalho, codigos escritos desse jeito
print('Olá "{}"'.format(nome))
print('Olá "{nome}"'.format(nome=nome))
print('Olá "{nome}"'.format(nome='Karla'))
print('Olá "{0} e {1}"'.format('Ana', 'Karla'))
print('Olá "{1} e {0}"'.format('Ana', 'Karla'))

#formatacoes da f-strings
#texto
texto = 'De tudo ao meu amor serei atento'
print(f'\n{texto:>60}')
print(f'{texto:^60}')

numero=0.8789
print(f'{numero:.0%}')
print(f'{numero:.2f}')
numero=78
print(f'{numero:05d}')
#o python aceita cores
texto = f'\nDe tudo ao meu \n\t\033[1;31mamor\033[0;0m\nserei atento'
print(texto)
vermelha = '\033[1;31m'
reset = '\033[0;0m'
amarelo = '\033[1;93m'
texto = (f'\nDe tudo ao meu \n\t{vermelha}amor{reset}\nserei '
         f'{amarelo}atento{reset}')
print(texto)