"""
Estrutura de Decisao
Serve para dividir o fluxo do programa
Comparacoes com decisões binaria (0,1 - true or false, sim ou nao)
Estrutura if (then) : else:
Comparacoes relacionais >, <, >=, <=, ==, !=
Operadores logico aqueles que juntam duas ou mais comparacoes no mesmo if
and - malvado, or - bonzinho, not - do contra
"""
#Exemplo dia da semana
#Dica de performance coloque a ocorrencia que o mais ocorre nas primeiras comparacoes,
#para economizar instrucoes
titulo = 'Dia da semana'
print(f'{titulo:^30}')
n = int(input('Entre com o numero: '))
if n == 6:
    print('Sexta')
elif n == 2:
    print('Segunda')
elif n == 3:
    print('Terça')
elif n == 4:
    print('Quarta')
elif n == 5:
    print('Quinta')
elif n == 1:
    print('Domingo')
elif n == 7:
    print('Sabado')
else:
    print('Numero invalido')