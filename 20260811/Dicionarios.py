#Dicionario
#Colecao do tipo chave e valor
#mutaveis
#tipos de dados diferentes

print('Dicionarios')
meuDicionario:dict = {'nome':'Patricia', 'sexo':'feminino', 'idade':54}
print(type(meuDicionario))
print(meuDicionario)

outroDic = dict((('nome','Patricia'), ('sexo','feminino'), ('idade', 54)))
print(outroDic)

print('\nAcessando um valor')
meuNome = meuDicionario['nome']
print(meuNome)
print(meuDicionario['idade'])

print('\nRecuperando as chaves')
chaves = meuDicionario.keys()
print(chaves)

print('\nRecuperando os valores')
valores = meuDicionario.values()
print(valores)

print('\nRecuperando os itens')
itens = meuDicionario.items()
print(itens)

print('\nRecuperando as chaves uma a uma')
for chave in meuDicionario.keys():
    print(chave)

print('\nRecuperando os valores um a um')
for valor in meuDicionario.values():
    print(valor)

print('\nRecuperando os itens um a um')
for item in meuDicionario.items():
    print(item)

#tirando vantagem da atribuicao multipla
print('\nRecuperando os itens um a um com atribuicao multipla')
for chave, valor in meuDicionario.items():
    print(f'Chave:{chave} e o valor:{valor}')

print('\nPausa para relembrar o enumerate com lista')
#pausa para o list
x, y = 0, 0
print(x)
print(y)
minhaLista = ['domingo', 'segunda', 'terca']
for indice, item in enumerate(minhaLista):
    #print(item)
    print(f'{indice+1}:{item}')

print('\nTruque para recuperar o valor qdo eu esqueci como trazer os valores')
for chave in meuDicionario:
    #print(chave)
    print(meuDicionario[chave])

print('\nAlterando valores')
print(meuDicionario)
meuDicionario['idade'] = 55
print(meuDicionario)

print('\nAlterando valores com update')
print(meuDicionario)
meuDicionario.update({'idade':17})
print(meuDicionario)
print('\no update acrescenta um par chave e valor se ele nao estiver originalmente no dicionario')
meuDicionario.update({'estado civil':'casada'})
print(meuDicionario)

print('\nApagando itens')
print('del')
del meuDicionario['estado civil']
print(meuDicionario)

print('popitem')
meuDicionario.popitem()
print(meuDicionario)

print('pop com escolha')
meuDicionario.pop('nome')
print(meuDicionario)

meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'estado civil': 'casada', 'tipo sanguineo':'Orh-'}
print('\nLocalizando itens')
if 'idade' in meuDicionario:
    print(f'Tem idade e ela é {meuDicionario['idade']}')
if 'Patricia' in meuDicionario.values():
    print('Patricia esta no dicionario')

#ATENCAO SITUACAO DE PERIGO
print('\nSituacao Perigo')
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'estado civil': 'casada', 'tipo sanguineo':'Orh-'}
print('Situacao Inicial')
print(meuDicionario)
#ATENCAO QUANDO IGUALAMOS DOIS DICIONARIOS NAO ESTAMOS FAZENDO A COPIA
#ESTAMOS APONTANDO PARA O MESMO ENDERECO DE MEMORIOA
copiafake = meuDicionario
print(copiafake)

print('Situacao removendo o tipo sanguineo')
copiafake.pop('tipo sanguineo')
print(meuDicionario)
print(copiafake)

# e como copiamos?
meuDicionario = {'nome': 'Patricia', 'sexo': 'feminino',
                 'idade': 17, 'estado civil': 'casada', 'tipo sanguineo':'Orh-'}
copia = meuDicionario.copy()
print('Situacao removendo o tipo sanguineo da copia real')
copia.pop('tipo sanguineo')
print(meuDicionario)
print(copia)
