"""
Aplicativo que mostre as opcoes de operacoes matematicas (soma, subtracao,
multiplicar, dividir)
e solicite 2 numeros
e faca a operacao matematica
"""

#Julia
# Operações matemáticas
titulo = 'Calculadora'
print(f'{titulo:^30}')

print("""
Opções de operações:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
""")
op = int(input('Escolha a operação (1 a 4): '))
if op < 1 or op > 4:
    print('Opcao invalida')
else:
    n1 = int(input('Informe o primeiro numero: '))
    n2 = float(input('Entre com o segundo numero: '))
    match op:
        case 1:
            print(f'Resultado da soma: {n1 + n2::.4f}')
        case 2:
            print(f'Resultado da subtração: {n1 - n2:.4f}')
        case 3:
            print(f'Resultado da multiplicação: {n1 * n2:.2f}')
        case 4:
            if n2 == 0:
                print('Erro: Não é possível dividir por zero.')
            else:
                print(f'Resultado da divisão: {n1 / n2:.2f}')


# soma = 22.9+7.5+6.8
# print(f'soma: {soma:.2f}')