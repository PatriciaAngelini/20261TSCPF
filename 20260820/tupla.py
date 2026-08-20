#Tuplas sao colecoes simples
#Tem algumas caracteristicas da lista
#indexadas, permite duplicados
#permite tipos de dados diferentes
#IMUTAVEIS!!! do jeito que ela nasceu, ela continua ate o fim da vida dela
#Nao é possivel nem acrescentar, nem remover, nem alterar elementos

necessidades = ('sono', 'comida', 'sol', 'sol', 'sol')
print(type(necessidades))
print(necessidades)

print(necessidades[2])

#como é imutavel, nao tem jeito de acrescentar elementos,
# nao tem varios metodos de manipulacao de itens: nao tem add, nao tem append, remove

print('\nTupla vazia faz sentido? Não')
vazia = ()
print(vazia)
#nao faz sentido criar uma tupla vazia para depois acrescentar elementos dentro um for, pq
#nao tem metodo para fazer isso

print('\nPodemos ter uma tupla de um unico elemento? sim')
#Examinando em detalhes
print('tupla falsa de um elemento')
um_falso = ('elemento')
print(um_falso)
print(type(um_falso))

print('tupla verdadeira de um elemento')
um = ('elemento',)
print(um)
print(type(um))

frase = 'meu cachorro é alegre e animado'
print(frase)
frase_semantica = []
for palavra in frase.split():
    if palavra not in ('meu', 'minha', 'ou', 'é', 'ser', 'e', 'mas'):
        frase_semantica.append(palavra)
print(frase_semantica)

print('\nAcrescentando um elemento na tupla - gambiarra')
#se a precisarmos acrescentar um elemento numa tupla
#GAMBIARRA
conectores = ('meu', 'minha', 'ou', 'é', 'ser', 'e', 'mas')
print(conectores)
lista_conectores = list(conectores)
lista_conectores.append('porém')
conectores = tuple(lista_conectores)
del lista_conectores
print(conectores)

print('\nOperacao aritmetica com tuple')
necessidades = ('sono', 'comida', 'sol', 'sol', 'sol')
print(necessidades)
cansada = necessidades * 2
print(cansada)