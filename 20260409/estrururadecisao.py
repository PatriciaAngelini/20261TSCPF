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
titulo = 'Dia da semana'
print(f'{titulo:^30}')
n = int(input('Entre com o numero: '))
if n == 1:
    print('Domingo')
else:
    if n == 2:
        print('Segunda')
    else:
        if n == 3:
            print('Terça')
        else:
            if n == 4:
                print('Quarta')
            else:
                if n == 5:
                    print('Quinta')
                else:
                    if n == 6:
                        print('Sexta')
                    else:
                        if n == 7:
                            print('Sabado')
                        else:
                            print('Numero invalido')