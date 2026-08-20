#Conjuntos
#Sao colecoes que nao permitem duplicados
#Porque NAO SAO INDEXADOS (posicionais) - NAO TEM ORDEM
#Eh como se tivessemos colocado os itens/elementos numa sacola
#Nao existe ALTERACAO DE ELEMENTO
#Mas podemos incluir e excluir elementos
#O simbolo é do dicionario {}

meujardim = {'rosa', 'camelia', 'geranio'}
print(type(meujardim))
#Ao exibir as informações do conjunto, o Python pode mudar a ordem
print(meujardim)

print('\nAdicionar')
#Nao ha garantias que ira adicionar o novo elemento no final
#Pois nao é posicional
meujardim.add('margarida')
print(meujardim)
#Como nao permite repetidos, se adicionar um item que ja existe, ele ignora
print('\nAdicionando repetidos')
meujardim.add('margarida')
meujardim.add('margarida')
meujardim.add('rosa')
print(meujardim)

#qual o uso em ciencia de dados?
#webscrapping
#varrer um texto e colocar os conectores da lingua portuguesa(e, ou, mas, a, o, os)
#e ir armazendo nessa colecao
#dai vai garantir que nao entra repetidamente esses elementos

print('\nEliminar ou Remover')
meujardim.remove('rosa')
print(meujardim)
meujardim.discard('geranio')
print(meujardim)
#retira um elemento aleatorio
meujardim.pop()
print(meujardim)

print('\nEliminando todos os itens do conjunto')
meujardim.clear()
#o conjunto vazio nao é representado pelo simbolo {} pois esse simbolo
#esta reservado para o dicionario
#o conjunto vazio apresenta-se com a palavra set()
print(meujardim)

print('\nJuntando Conjuntos')
meujardim = {'rosa', 'camelia', 'geranio'}
meuquintal = set(('pinheiro', False, 800, 'camelia'))
print(meujardim)
print(meuquintal)
print('\ne criando um novo conjunto')
# o union é usado para criar um conjunto novo
paisagismo = meuquintal.union(meujardim)
print(paisagismo)

#podemos querer acrescentar um conjunto no outro
print('\ne acrescentando um conjunto no outro')
print(meujardim)
print(meuquintal)
meuquintal.update(meujardim)
print(meuquintal)

print('\nInterseccao de conjuntos')
#elementos que repetem entre os dois conjuntos
meujardim = {'rosa', 'camelia', 'geranio'}
floricultura = {'rosa', 'camelia', 'artemisia', 'cravo', 'margarida'}
print(meujardim)
print(floricultura)
print('\ne criando um novo conjunto')
interseccao = floricultura.intersection(meujardim)
print(interseccao)
print('\ne atualizando o proprio conjunto')
print(meujardim)
print(floricultura)
floricultura.intersection_update(meujardim)
print(floricultura)

print('\nDiferenca de conjuntos')
meujardim = {'rosa', 'camelia', 'geranio','cacto'}
floricultura = {'rosa', 'camelia', 'artemisia', 'cravo', 'margarida'}
print(meujardim)
print(floricultura)
#elementos que sao unicos entre os dois conjuntos
print('\ne criando um novo conjunto')
diferenca = floricultura.symmetric_difference(meujardim)
print(diferenca)
print('\ne atualizando o proprio conjunto mantendo os diferentes')
print(meujardim)
print(floricultura)
floricultura.symmetric_difference_update(meujardim)
print(floricultura)
