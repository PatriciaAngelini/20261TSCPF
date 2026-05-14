#Colecoes
#Estruturas de dados dentro do python que armazenam varios valores numa unica variavel
#Sao varias
#LISTAS - combinam com arquivos .CSV ou .TXT
#DICIONARIOS - combinam com arquivos .JSON
#TUPLAS
#SETS (conjuntos)

#Listas
#sao as mais comuns, poderosas, flexiveis, completas
#MUTAVEIS: depois de criadas, permite que se acrescente, modifique ou exclua itens
#INDEXADAS: ou seja, cada item/elemento dentro da lista tem uma posição
#PERMITE DUPLICADOS
#EXPANSIVEL: concatenar duas listas
#ACEITA DIFERENTES TIPOS DE DADOS (heterogena)
#ORDENAVEIS **> SOMENTE SE OS ELEMENTOS(itens) FOREM DO MESMO TIPO DE DADOS

print('Listas')
#construtor de uma lista é [] ou a proprio list
minhaLista = ['café', 'água', 'acúcar']
print(minhaLista)

#toda colecao indexada, vc consegue acessar o elemento a partir da sua posicao
#toda colecao começa no zero

print(f'primeiro elemento: {minhaLista[0]}')
print(f'segundo elemento:  {minhaLista[1]}')

#   0       1        2       ==> indices positivos
#  -3      -2       -1       ==> indices negativos
#['café', 'água', 'acúcar']

print(f'primeiro elemento pelo indice negativo: {minhaLista[-3]}')
print(f'segundo elemento pelo indice negativo:  {minhaLista[-2]}')

minhaLista = ['café', 'água', 'acúcar', 'café', 'café']
print(minhaLista)
print(f'ultimo elemento pelo indice positivo: {minhaLista[4]}')
print(f'ultimo elemento pelo indice negativo: {minhaLista[-1]}')

print('\nSlicing')

minhaLista = ['café', 'água', 'acúcar', 'café', 'café', 'canela', 'chantilly']
#   0       1        2        3       4        5         6          ==> indices positivos
#  -7      -6       -5       -4      -3       -2        -1          ==> indices negativos
#['café', 'água', 'acúcar', 'café', 'café', 'canela', 'chantilly']
#o mesmo racional do range, ou seja, no final tem que acrescentar 1
print(f'parte da lista:{minhaLista[1:2+1]}')
print(f'parte da lista:{minhaLista[4:6+1]}')
print(f'parte da lista:{minhaLista[-3:]}')
#a representacao do final da lista pode ser feita com : apenas

#o ultimo parametro é o pulo e funciona como funciona no range
print(f'parte da lista invertida pelo positivo:{minhaLista[3::-1]}')
print(f'parte da lista invertida pelo negativo:{minhaLista[-4:-8:-1]}')
print(f'parte da lista invertida pelo negativo 2a versao:{minhaLista[-4::-1]}')
print(f'parte da lista invertida pelo negativo:{minhaLista[-1::-2]}')

print('\nSlicing em frases')
frase = 'O mundo é bom'
print(frase)
palavras = frase.split() #transforma a frase em uma lista de palavras
print(palavras)
print(f'frase inversa:{palavras[::-1]}')
print(f'pegando o mundo é {palavras[1:3]}')

print('\nSlicing em palavras')
palavra = 'Transeunte'
print(palavra)
#no caso da palavra não precisamos converter em letras
#basta usar o conceito, que o python entende que estamos fazendo da palavra uma colecao
print(f'pegando anse {palavra[2:6]}')
print(f'palavra inversa:{palavra[::-1]}')

#Operacoes em lista
print('\nOperacoes em Lista')
minhaLista = ['café', 'água', 'acúcar', 'café', 'café', 'canela', 'chantilly']
print(minhaLista)
print(f'tamanho da lista: {len(minhaLista)}') #quantidade de itens
print('Substituindo valor')
minhaLista[3] = 'raspas de limao'
print(minhaLista)
print('Acrescentando um item no final')
minhaLista.append('baunilha')
print(minhaLista)
print('Acrescentando um item numa determinada posicao')
minhaLista.insert(4,'nibs de chocolate')
print(minhaLista)
print('Eliminar elementos - do final')
minhaLista.pop()
print(minhaLista)
print('Eliminar elementos - de uma posicao')
minhaLista.pop(5)
print(minhaLista)
print('Eliminar elementos pelo proprio elemento')
minhaLista.remove('nibs de chocolate')
print(minhaLista)
print('Limpar a lista')
minhaLista.clear()
print(minhaLista)
print('Apagando a lista')
del minhaLista
#print(minhaLista)

print('\nConcatenar a lista')
print('Listas individuais')
minhaLista = ['café', 'água', 'acúcar', 'raspas de limao', 'canela', 'chantilly']
complementos = ['pimenta', 'gengibre']
print(minhaLista)
print(complementos)
print('Lista concatenada do café perfeito')
cafeperfeito = minhaLista + complementos
#cafeperfeito = complementos + minhaLista
print(cafeperfeito)
print('Extendendo uma lista - a lista modifica para todo sempre')
minhaLista.extend(complementos)
print(minhaLista)

#a principal diferenca entre concatenar e extender, é que a extensão muda para to do
#sempre a lista orginal

print('\nVarrendo uma lista')
#toda colecao é um elemento iteravel - usamos o for para passar elemento a elemento
for item in minhaLista:
    print(item)

print('\nVarrendo uma lista pelo indice')
for i in range(len(minhaLista)): #o i representa o indice
    print(minhaLista[i])
print('\nVarrendo uma lista pelo indice versao 2')
for i in range(len(minhaLista)): #o i representa o indice
    print(f'elemento {i+1}: {minhaLista[i]}')

print('\nEncontrando um elemento na lista')
if 'pimenta' in minhaLista:
    print('eita café apimentado')
if 'gelo' in minhaLista:
    print('cafe gelado')

#desafio: descobrir se tem chantilly e gengibre na minha lista
print('\nDescobrindo a posicao de um elemento')
print(minhaLista)
print(f'posicao da raspas de limao: {minhaLista.index('raspas de limao')}')

print('\nEstudo de ordenacao SORT x SORTED')
print('SORTED - nativo do python - ordena TEMPORARIAMENTE a lista')
print(f'Original =>{minhaLista}')
print(f'Ordenada =>{sorted(minhaLista)}')
print(f'Depois   =>{minhaLista}')

print('SORT - metodo da classe list - ordena PERMANENTEMENTE a lista')
print(f'Original =>{minhaLista}')
minhaLista.sort()
print(f'Ordenada =>{minhaLista}')

print('\nLista de dados de tipos diferentes')
listaHeterogenea = ['Katia', 45, True, ['Puppy', 'Aurora']]
print(listaHeterogenea)
# listaHeterogenea.sort()
# print(listaHeterogenea)
#print(sorted(listaHeterogenea))