titulo='Saudavel'
print(f'{titulo:^40}')

#upper() transforma em maiusculo a resposta
#lower() transforma em minusculo
verduras = input('Você come verduras todos os dias? ').upper()
exercicios = input('Você faz exercios 3X na semana? ').lower()

#VERSAO BOAZINHA - PATRICIA - OR
#if verduras == 'SIM' aqui é limitado a um tipo de resposta
if verduras == 'SIM' or exercicios == 'sim':
#if verduras in ('SIM', 'YES') or exercicios in ('SIM', 'YES'):
    print('PAT - Você é saudável')
else:
    print('PAT - Você precisa melhorar ')

#VERSAO MALVADA - NEMEC ALEMAO FALSO- AND
if verduras in ('SIM', 'YES', 'JA') and exercicios in ('sim', 'yes', 'ja'):
    print('NEMEC - Você é saudável')
else:
    print('NEMEC - Você precisa melhorar ')


# Qdo usamos um =, estamos atribuindo um valor, ou seja, estamos
# colocando um valor na memoria
# Qdo usamos dois = (==), estamos comparando o valor
#OPERADORES LOGICOS
#and - operador malvado: so qdo todos respondem sim funciona
#or - operados bonzinho: basta 1 responder sim
#not - do contra: contradiz tudo que falamos