#Dicionario
#colecao do tipo chave valor (formulario)
#Nome = Patricia (onde chave nome, valor é Patricia)
#mutaveis: consigo alterar, incluir, excluir
#tipos de dados diferentes
#(str, int, float, bool, list, dict, tuple, etc) -> object (tipo de mais generico)

#dicionarios sao tao poderosos qto listas

print('Dicionarios')
meuDicionario:dict = {'nome':'Patricia', 'sexo':'feminino', 'idade':54}
print(type(meuDicionario))
print(meuDicionario)

outroDic = dict((('nome','Patricia'), ('sexo','feminino')))
print(outroDic)

print('\nAcessando um valor')
meuNome = meuDicionario['nome']
print(meuNome)
print(meuDicionario['idade'])

print('\nRecuperando as chaves')
chaves = meuDicionario.keys()
print(chaves)

print('\nRecuperando Valores')
valores = meuDicionario.values()
print(valores)

print('\nRecuperando itens')
itens = meuDicionario.items()
print(itens)

print('\nRecuperando as chaves um a um')
chaves = meuDicionario.keys()
for chave in chaves:
    print(chave)

print('\nRecuperando Valores')
valores = meuDicionario.values()
for valor in valores:
    print(valor)

print('\nAtribuicao multipla')
#pausa para atribuicao multipla
x, y, nome = 0, 0, 'Carlos'
print(x)
print(y)
print(nome)
                # 0         1           2
semanacurta = ['domingo', 'segunda', 'terca']
for indice, item in enumerate(semanacurta):
    print (f'{indice+1}o dia -> {item}')

print('\nRecuperando itens')
for chave, valor in meuDicionario.items():
    print(f'Chave:{chave} e valor {valor}')

#quando esquecemos de referenciar o metodo apropriado
#na chamada de um dicionario dentro do for
#o dicionario naturalmente nos devolve a chave
print('\nPonto de atencao - chave no for')
for xpto in meuDicionario:
    print(xpto)

print('\ntruque para acessar o valor no for - ineficiente')
for coxinha in meuDicionario:
    print(meuDicionario[coxinha])

print('\nAlterando os valores')
print(meuDicionario)
meuDicionario['idade']=55
print(meuDicionario)

print('\nAlterando os valores com o update')
meuDicionario.update({'idade':17})
print(meuDicionario)
print('\nquando nos referimos a uma chave que nao existe no update, ela cria')
meuDicionario.update({'estado civil':'casada'})
print(meuDicionario)

print('\nApagando itens')
print('del')
del meuDicionario['estado civil']
print(meuDicionario)
print('popitem - apaga o ultimo item')
meuDicionario.popitem()
print(meuDicionario)
print('pop - item especifico')
meuDicionario.pop('nome')
print(meuDicionario)

#para localizar um item especifico nao precisamos usar o for
#da para usar o if
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'tipo sanguineo':'ORh-'}
print('\nLocalizando itens')
if 'tipo sanguineo' in meuDicionario:
    print(f'O tipo sanguineo é {meuDicionario['tipo sanguineo']}')
if 'ORh-' in meuDicionario.values():
    print(f'Há pessoa com Rh- na base')

#ATENCAO SITUACAO DE PERIGO!!!!!
print('\n\nPERIGO')
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'tipo sanguineo':'ORh-'}
print('original')
print(meuDicionario)
#ATENCAO QUANDO IGUALAMOS DOIS DICIONARIOS NAO ESTAMOS FAZENDO A COPIA
#ESTAMOS APONTANDO PARA O MESMO ENDERECO DE MEMORIA
#O QUE ACONTECE EM 1, ESTA NA REAL, ACONTECENDO NO ORIGINAL E NA COPIA
copiafake = meuDicionario
print('copia')
print(copiafake)

print('tirando o tipo sanguineo')
copiafake.popitem()
print('copia')
print(copiafake)
print('original')
print(meuDicionario)

#E SE EU QUISER COPIAR?
print('\n\nCopiando de verdade')
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'tipo sanguineo':'ORh-'}
print('original')
print(meuDicionario)
copia = meuDicionario.copy()
print('copia')
print(copia)

print('tirando o tipo sanguineo')
copia.popitem()
print('copia')
print(copia)
print('original')
print(meuDicionario)