#Manipulacao de arquivos
#podem bibliotecas especializadas como JSON e CSV
#mas no arquivo .txt a gente usa o python nativo

print('Arquivos')
#Para ler ou escrever um arquivo, precisamos informar ao sistema operacional (S.O.)
#A operacao que faz isso é o open
#Mas to do open tem um close associado
print('\nAbrindo arquivo')
arqAlunos = open("C:\\Projetos\\1TSCPF2026\\Python\\20260820\\alunos.txt", encoding = 'UTF-8')
print('\nLendo linha a linha')
linha=arqAlunos.readline()
print(linha)
linha=arqAlunos.readline()
print(linha, end='')
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

print('\nLendo de maneira natural')
#texto é um elemento iteravel

for linha in arqAlunos:
    print(linha, end='')

#qdo chega no fim do arquivo ele nao le nenhuma linha
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

print('\nVoltando ao inicio do arquivo')
arqAlunos.seek(0)
#Cabeçalho
print(arqAlunos.readline(), end='')
#Dados
for linha in arqAlunos:
    print(linha, end='')

print('\nLendo como listas de linhas')
arqAlunos.seek(0)
linhas = arqAlunos.readlines()
print(linhas)

#desafio: utilize list comprehension para tirar o \n da colecao de linhas
linhas = ['nome sobrenome idade\n', 'Patricia Angelini 55\n', 'Angelo Lima 17\n', 'Antonio Santo 78\n', 'Bruno Paes 34\n', 'Felipe Lorandi 23\n', 'Eduardo Bambulim 22\n', 'Maria Eduarda 19\n']

print('\nPosicao do cursor no arquivo')
print(f'Posicao cursor:{arqAlunos.tell()}')

print('\nSe o cursor é tao flexivel podemos ler a partir de uma posicao escolhida')
arqAlunos.seek(101)
print(arqAlunos.readline(), end='')

print('\nLer o arquivo todo de uma vez')
#cuidado com arquivos grandes demais
arqAlunos.seek(0)
print(arqAlunos.read())

print('\nTexto Completo e slicing')
arqAlunos.seek(0)
textoCompleto = arqAlunos.read()
trecho = textoCompleto[56:112:2]
print(trecho)

print('\nLer ate uma de uma posicao')
arqAlunos.seek(0)
pedaco = arqAlunos.read(111)
print(pedaco)
print('\n')
arqAlunos.seek(45)
pedaco = arqAlunos.read(100)
print(pedaco)


print('\nToda vez que eu abro um arquivo, eu preciso fechar')
if arqAlunos.closed:
    print('Fechado')
else:
    print('Fechando arquivo')
    arqAlunos.close()

# if arqAlunos.closed:
#     print('Fechado')
# else:
#     print('Ainda aberto')

print('\n\nEscrita de arquivos')
arqOlaMundo = open('olamundo.txt', mode = 'w', encoding = 'UTF-8')
arqOlaMundo.write('Ola Mundo')
arqOlaMundo.write('Bom dia\n\n\n')
arqOlaMundo.write('Como esta')
arqOlaMundo.close()

print('\nEscrevendo um arquivo a partir de uma lista')
floricultura = ['rosa', 'camelia', 'artemisia', 'cravo', 'margarida']
floricultura2 = [flor+'\n' for flor in floricultura]
arqFloricultura = open('floricultura.txt', mode = 'w', encoding = 'UTF-8')
arqFloricultura.writelines(floricultura2)

arqFloricultura.close()


