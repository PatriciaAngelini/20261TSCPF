#O for é a segunda maneira de fazermos a repeticao
#Normalmente em todas as linguagens nós temos essas duas maneiras
#Iterativa (for) - usado qdo sabemos de antemao a quantidade de repeticoes
#Interativa (while) - usado qdo esperamos a interferencia do usuario

#O for no python ele é dependente de elementos iteraveis
#Elementos iteraveis sao o que podemos percorrer item a item
#Exemplo: sequencia de numeros, sequencia de letras de uma palavra,
# elementos de uma colecao,
#linhas de um arquivo, palavras de uma frase. Tudo isso o for consegue percorrer

for letra in 'amor':
    print(letra)

#E quando a gente nao tem essa sequencia para percorrer? A gente consegue
#usar o for? Sim, para isso entra o range

#O que o range é?
#Ele é um gerador de numeros
#range(4): 0, 1, 2, 3
#O range comeca do 0
#Podemos pedir para ele comecar de outro numero
#range(1, 4): 1, 2, 3
#ue? o que aconteceu com o numero 4
#o range "come" / desconsidera o ultimo numero
#SINTAXE
#range(INICIO, FIM - 1, PULO)


#a nossa tabuada vai de 1 a 10
#n = int(input('Entre com um numero da tabuada: '))
# n = 3
# i = 1 #contadores chamam i, j, c, cont, contador
# while i <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     i += 1 #i = i + 1

print('Tabuada')
n = 3
for i in range(1, 10 + 1):
    tabuada = n * i
    print(f'{n} X {i} = {tabuada}')
print('\n\n')
n = 8
for i in range(10):
    tabuada = n * (i + 1)
    print(f'{n} X {i + 1} = {tabuada}')
print('\n\n')
n = 10
for i in range(1, 10 + 1, 2):
    tabuada = n * i
    print(f'{n} X {i} = {tabuada}')