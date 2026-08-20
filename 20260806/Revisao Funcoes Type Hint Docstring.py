def dobro(num:int) -> int:
    """
    funcao que calcula o dobro de um numero
    :param num: numero inteiro
    :return: o dobro do numero
    """
    return num * 2


print(dobro(5))
print(dobro(9.3))
help(dobro)

#type hint - boa pratica para assinatura de funcoes
#indica o tipo de dado esperado, mas nao impede o uso com outros tipos de dados
#type hint nao é muito utilizado para declaracao de variaveis simples, mas é muito
#usado com funcoes
nom = 'Daniela'
#com type hint
nome:str = 'Patricia'
print(nome)
nome = 23
print(nome)

listahomegenea:list[int] = [5, 4, 34]
listaheterogenea:list[object] = [3, 4, 'amor', 6.90, True, ['cafe', 'chocolate']]

def positvo (num:int) -> object:
    if num > 0:
        return num
    else:
        return "erro"


#docstring para documentacao de funcoes
#para uso no help

#Lambda é uma pequena funcao para uso imediato
#Voce atribuir a lambda criada para uma variavel se vc for usar algumas vezes
#em lugares proximos na hora de codar
print('\nLambda')
ldobro = lambda num:num*2
print(ldobro(7))

print((lambda num:round(num/2,2))(9))
print((lambda num:round(num/2,2))(76))

#lambda condicional é o lambda com o if interno
def aumento_salario(salario:float) -> float:
    if salario > 15000:
        return salario * 1.07
    elif salario > 10000:
        return salario * 1.10
    else:
        return salario * 1.15
print(f'Meu salario reajustado R${aumento_salario(10000):.2f}')

lreajuste_salarial = lambda salario:salario*1.07 if salario > 15000 else salario*1.15
print(f'Meu salario reajustado R${lreajuste_salarial(10000):.2f}')
print(f'Meu salario reajustado R${(lambda salario: 
                                   round(salario*1.07, 2) if salario > 15000 else 
                                   (round(salario*1.10, 2) 
                         if salario > 10000 else round(salario*1.15, 2)))(9000):.2f}')

#lambda e map sao um bom casamento
#o map aplica uma funcao em todos os elementos de uma lista

def triplo(num:int) -> int:
    """
    Funcao que calcula o triplo de um numero
    :param num: numero inteiro
    :return: o triplo do numero
    """
    return num * 3

print(f'Triplo:{triplo(3)}')
variosnumeros = [5, 4, 78, -9]

#sem map e roots
triplos = []
for num in variosnumeros:
    triplos.append(triplo(num))
print(variosnumeros)
print(triplos)

#com map
triplos2 = list(map(triplo, variosnumeros))
print(triplos2)

#exercicio: criar uma funcao lambda quintuplo e aplicar com map em uma lista de numeros.
#faca numa linha so, usando o print para exibicao

#Felipe Lessa
print('\nExercicio')
variosnumeros = [2, 5, 4, 78, -9]
def triplo(num:int) -> int:
    """
    Funcao que calcula o triplo de um numero
    :param num: numero inteiro
    :return: o triplo do numero
    """
    return num * 3
quintuplo = []
for num in variosnumeros:
    quintuplo.append(triplo(triplo(num)))
print(quintuplo)

quintuplo2 = list(map(triplo, map(triplo, variosnumeros)))


#Vitor

listanum = [5,4,78,-9]

lquintoplo = lambda num: num*5

lquintuplos2 =  list(map(lquintoplo, listanum))
print(listanum)
print(lquintuplos2)

print(list(map((lambda num:num*5),[5, 65, 78, -9])))

#Joao Guilherme
print('\n')
print(list(map(lambda num: num * 5, variosnumeros)))

#List Comprehension
#é a maneira de gerar uma lista a partir de uma regra/funcao
print('\nList Comprehension')
variosnumeros = [2, 5, 4, 78, -9]
quintuplos=[n * 5 for n in variosnumeros]
print(variosnumeros)
print(quintuplos)

print(f'{[n * 5 for n in variosnumeros]}')

quintuplosmenorq5=[n * 5 for n in variosnumeros if n < 5]
print('\n')
print(variosnumeros)
print(quintuplosmenorq5)