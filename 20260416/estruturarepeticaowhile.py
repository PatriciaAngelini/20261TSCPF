#estruturas de repeticao em python sao while e for
print('Bom dia')
print('Bom dia')
print('Bom dia')

print('Bom dia 1')
print('Bom dia 2')

#while é muito parecido com o if, só que ele trata parte true
#a repeticao acontece enquanto a condicao (comparacao) for verdadeira


#tabuada
titulo = 'Estrutura Repeticao While - Tabuada'
print(f'{titulo:^60}')

#a nossa tabuada vai de 1 a 10
#n = int(input('Entre com um numero da tabuada: '))
# n = 3
# i = 1 #contadores chamam i, j, c, cont, contador
# while i <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     i += 1 #i = i + 1

#geralmente a gente usa o while qdo precisa da interacao do usuario
#mudar o algoritmo de cima para o usuario ir fazendo a tabuada um a um
#ex
#3 X 1 = 3
#quer calcular + 1
#3 X 2 = 6
#quer calcular + 1
#3 X 3 = 9
# n = 3
# i = 1 #contadores chamam i, j, c, cont, contador
# resp = 's'
# while resp == 's': #i <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     i += 1 #i = i + 1
#     resp = input('Quer calcular +1? ').lower()[0] #sim s=0 i=1 m=2

# #Beatriz Falasca
# n = 3
# i = 1
# while i <= 10:
#     tab = n * i
#     print(f'{n} X {i} = {tab}')
#     segue = str(input('Quer calcular + 1? (S ou N): ')).lower()
#     if segue == 's':
#         i += 1
#     else:
#         print(f'Ok, obrigada por usar nosso código!')
#         i = 11


# #Yasmin
# n = 3
# i = 1
# while n <= 10:
#     tabuada = n*i
#     print(f'{n} X {i} = {tabuada}')
#     validacao = int(input('Quer continuar a tabuada? \n 1 - Sim \n 2 - Não'))
#     i+=1
#     if validacao == 2:
#         break
#     # else:
#     #     continue

# #Lucas Luna
# titulo ="Bem vindo a taboada!"
# num = int(input(f"{titulo} Escolha um número para iniciar a taboada: "))
# i = 1 #contador
#
# while i <= 10:
#     taboada = num * i
#     print(f"{num} x {i} = {taboada}")
#     i += 1
#     pergunta = input(f"{titulo} Deseja continuar? [s/n] ")
#
#     if pergunta == "n":
#         print(f"Obrigado por utilizar o programa!")
#         break
#     else:
#         continue

#misture as duas abordagens
#1a interacao calcular a tabuada completa de 1 a 10
#lancar a pergunta se quer calcular a proxima tabuada
#ex
#3 X 1 = 3
#3 X 2 = 6
#3 X 3 = 9
#...
#3 X 10 = 30
#quer calcular a proxima tabuada
#4 X 1 = 4
#4 x 2 = 8
#...
#4 x 10 = 40
#quer calcular a proxima tabuada

# n = 3
# i = 1
# resp = 's'
# while resp == 's':
#     #print(i)
#     while i <= 10:
#         tabuada = n*i
#         print(f'{n} X {i} = {tabuada}')
#         i += 1
#     resp = input('Quer calcular outra tabuada? ').lower()[0] #sim s=0 i=1 m=2
#     i = 1
#     n += 1
#
#e o while true??? é o loop infinito
n = 3
i = 1
while True:
    while i <= 10:
        tabuada = n*i
        print(f'{n} X {i} = {tabuada}')
        i += 1
    resp = input('Quer calcular outra tabuada? ').lower()[0] #sim s=0 i=1 m=2
    if resp == 'n':
        break
    i = 1
    n += 1

# o uso do while é mais interessante qdo precisamos da acao do usuario
# qdo já sabemos de antemao o numero certo de repeticoes a gente usa o for
