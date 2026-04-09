titulo='Inversao de Números'
print(f'{titulo:^40}')


n = int(input('Entre com um numero inteiro de 3 digitos: '))
print(f'Numero antes:{n}')

c = n // 100
resto = n % 100
d = resto // 10
u = resto % 10
print('A ilusao')
print(f'Numero depois - exibindo os digitos 3 numeros separados:{u}**{d}**{c}')
numerofinal = u*100 + d*10 +c
print('O real')
print(f'Numero final calculado:{numerofinal}')
