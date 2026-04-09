"""
Aplicativo que mostre as opcoes de operacoes matematicas (soma, subtracao,
multiplicar, dividir)
e solicite 2 numeros
e faca a operacao matematica
"""

# #Julia
# # Operações matemáticas
# titulo = 'Calculadora'
# print(f'{titulo:^30}')
#
# print("Opções de operações:")
# print("1 - Soma")
# print("2 - Subtração")
# print("3 - Multiplicação")
# print("4 - Divisão")
#
# op = int(input('Escolha a operação (1 a 4): '))
# n1 = float(input('Entre com o primeiro numero: '))
# n2 = float(input('Entre com o segundo numero: '))
#
# if op == 1:
#     print(f'Resultado da soma: {n1 + n2::.4f}')
# elif op == 2:
#     print(f'Resultado da subtração: {n1 - n2:.4f}')
# elif op == 3:
#     print(f'Resultado da multiplicação: {n1 * n2:.2f}')
# elif op == 4:
#     if n2 == 0:
#         print('Erro: Não é possível dividir por zero.')
#     else:
#         print(f'Resultado da divisão: {n1 / n2:.2f}')
# else:
#     print('Opção inválida')

# soma = 22.9+7.5+6.8
# print(f'soma: {soma:.2f}')

#yasmin

"""
Aplicativo que mostre as opcoes de operacoes matematicas
-> Soma, subtracao, multiplicao e divisao
solicite dois numeros
e faca a operacao matematica
"""


# #Soma
# def soma():
#     n1 = float(input('Digite o 1º número:'))
#     n2 = float(input('Digite o 2º número.'))
#     res = 0
#     res = round(n1 + n2, 2)
#     print(f'A soma dos números é igual a {res}')
#
# #Subtracao
# def subtracao():
#     n1 = float(input('Digite o 1º número:'))
#     n2 = float(input('Digite o 2º número.'))
#     res = 0
#     res = round(abs(n2 - n1), 2)
#     print(f'A subtração dos números é igual a {res}')
#
# def divisao():
#     n1 = float(input('Digite o 1º número:'))
#     n2 = float(input('Digite o 2º número.'))
#     res = 0
#     if n1 > n2:
#         res = round((n1 / n2), 2)
#         print(f'A divisão dos números é igual a {res}')
#     else:
#         res = round ((n2/n1), 2)
#         print(f'A divisão dos números é igual a {res}')
# #Multiplicacao
# def multiplicacao():
#     n1 = float(input('Digite o 1º número:'))
#     n2 = float(input('Digite o 2º número.'))
#     res = 0
#     res = round((n2*n1), 1)
#     print(f'A multiplicacao dos números é igual a {res}')
#
# print("**********************************")
# print("OPERAÇÕES MATEMÁTICAS")
# print("**********************************")
# tipo_operacao = int(input('Escolha uma operação matemática. \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n'))
# match tipo_operacao:
#     case 1:
#         soma()
#     case 2:
#         subtracao()
#     case 3:
#         multiplicacao()
#     case 4:
#         divisao()
#     case _:
#         print('Opção Inválida.')

#Joao Guilherme Cavalcante
def soma(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y
def divisao(x, y):
    if y == 0:
        return "divisão por zero."
    else:
        return x / y

continuar = 's'

while continuar.lower() == 's':
    print('\nSelecione a operação:')
    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')

    escolha = input('digite sua escolha (1/2/3/4): ')

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input('digite o primeiro numero: '))
        num2 = float(input('digite o segundo numero: '))

        if escolha == '1':
            print(f'resultado: {num1} + {num2} = {soma(num1, num2)}')
        elif escolha == '2':
            print(f'resultado: {num1} - {num2} = {subtracao(num1, num2)}')
        elif escolha == '3':
            print(f'resultado: {num1} * {num2} = {multiplicacao(num1, num2)}')
        elif escolha == '4':
            print(f'resultado: {num1} / {num2} = {divisao(num1, num2)}')
    else:
        print('selecione de 1 ate 4')

    continuar = input('clique "s" se quiser tentar d novo: ')
