titulo='Dirigir'
print(f'{titulo:^40}')

idade = int(input("Qual a idade q vc tem? "))
habilitacao = input("Você tem habilitacao? ").lower()
#metodos se diferenciam de funcoes por varios motivos
#mas um deles é que chamada (ou uso) é diferente
#enquanto funcao a gente coloca com parametros
#f(x) ou f(x, y, z, k)
#metodos usamos assim
#objeto.f()

if idade >= 18 and habilitacao in ('sim', 'yes', 'si'):
#if idade >= 18 and habilitacao == 'sim':
    print('Você pode dirigir')
else:
    print('Você não pode dirigir')

print('Obrigado por responder a pesquisa!')
