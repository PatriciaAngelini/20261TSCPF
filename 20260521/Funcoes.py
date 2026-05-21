#Funcoes
#Sao pedacos de codigo que visam organizar e fazer o reaproveitamento

#Em algumas linguagens funcoes e procedimentos sao coisas diferentes
#Funcoes retorna valor e procedimento nao retorna valor
#Não é o caso do python, tudo é junto e misturado

#1o passo é a construcao de uma funcao
def saudacao():
    print("Ola Mundo")
#2o passo é a utilizacao
saudacao()

#Escopo
#visibilidade da variavel

#toda variavel criada dentro de uma funcao, só é visivel dentro da funcao
def somaconst ():
    x = 1
    y = 5
    print(x+y)

somaconst()
#print(x)

#2 jeitos de resolver isso
#1o jeito: criar uma variavel global - ela fica no programa principal

z = 8
print(z)
def somaconst2 ():
    print(z+100)
somaconst2()
print(z)

#2o jeito: passar parametro
def soma2(n1, n2):
    print(n1+n2)

soma2(8, 45)
z = 67
soma2(z, 45)

#ate agora passamos os paramentros no uso posicionalmente
#mas podemos passar nomeados, o que nos da uma flexibilidade

soma2(n2=108, n1=67)

#parametros opcionais/default
def somapadrao(n1, n2=90):
    print(n1+n2)
somapadrao(5,6)
somapadrao(7)

#a partir do momento que eu defino um parametro default
#os proximos precisam ter valor default
# def soma3(n1, n2=90, n3): #=> isso nao é permitido
#     print(n1+n2+n3)

def soma3(n1, n2=90, n3=64):
    print(n1+n2+n3)

soma3(4,5)

#transformar em funcao
def soma3(n1, n2=90, n3=64):
    return n1+n2+n3

total = soma3(7,4,-1)
print(total)

#quantidade de paramentros variaveis
#a ideia é que os parametros sao passados como uma colecao
#a colecao é uma tupla
def soma (*colecao):
    total = 0
    for item in colecao:
        total += item
    #print(colecao)
    return total

print(soma(1, 3, 6, 7))
print(soma(8, 7))

#map
#é a possibilidade de aplicar uma funcao em varios elementos de uma colecao
#funciona com colecoes

def dobro(p):
    return p*2
print(dobro(8))
numeros = [3, 4, 6, -1, 45, 9]
#do jeito tradicional
dobros = []
for n in numeros:
    dobros.append(dobro(n))
print(numeros)
print(dobros)

#o map facilita esse processo
# dobrosmap = map(dobro,numeros)
# print(dobrosmap)

dobrosmap = list(map(dobro,numeros))
print(dobrosmap)

def mult (n1, n2):
    return n1*n2
numeros = [3, 4, 6, -1, 45, 9]
#resultado = [9, 16, ...]

#Vitor Matias
numeros = [3,4,5,-1,45,9]
#numeros2 = [3,4,5,-1,45,9]
def multi(v1, v2):
    return v1 * v2

total = list(map(multi,numeros,numeros))
print(total)

#o reduce junta todos os elementos de uma colecao segundo uma funcao

def soma2(n1, n2):
    return n1+n2
print(soma2(8,7))
numeros = [3,4,5,-1,45,9]
#O objetivo é somar todos os numeros dessa lista usando a funcao que soma de 2 em 2 parametros
#do jeito tradicional
total = 0
for n in numeros:
    total = soma2(total,n)
print(numeros)
print(total)

from functools import reduce
print(reduce(soma2,numeros))

def multi(v1, v2):
    return v1 * v2
print(reduce(multi,numeros))