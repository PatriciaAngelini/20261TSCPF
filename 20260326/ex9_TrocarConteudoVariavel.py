titulo='Troca de variaves'
print(f'{titulo:^40}')

A = int(input('Entre com um numero: '))
B = int(input('Entre com outro numero numero: '))
print(f'Valores antes A:{A} e B:{B}')
#Versao classica
# TEMP = A
# A = B
# B = TEMP
#teste de atribuicao multipla: com unico =, coloco valores em muitas variaveis
x, y, z = 10, 8, 23
print(f'x:{x} e y:{y} e z:{z}')

#Versao python - aproveitando A ATRIBUICAO MULTIPLA
A, B = B, A
print(f'Valores depois A:{A} e B:{B}')

# #Versao do Filipe
# A = A+B #(7+10=17)
# B = A-B #(17-10=7)
# A = A-B #(17-7=10)
# print(f'Valores depois A:{A} e B:{B}')