#Exceções é o erro que acontece somente na EXECUÇAO de um programa

#1.Identificar e tratar exceções

#2. LANCAR OU LEVANTAR EXCEÇÕES: quando nós como programadores provocamos erro de proposito
#Fazemos isso quando a situacao de negocio necessita que haja erro

#1.
print('Excecoes: identificando e tratando')
# #programa original
# print('\nValor medio de compras')
# valorcompra = float(input('Entre com o valor da compra: '))
# qtditens = int(input('Entre com a quantidade de itens: '))
# media = valorcompra/qtditens
# print(f'O valor medio da compra é R${media:.2f}')


#primeiro nivel de tratamento
# print('\nValor medio de compras')
# try:
#     valorcompra = float(input('Entre com o valor da compra: '))
#     qtditens = int(input('Entre com a quantidade de itens: '))
#     media = valorcompra/qtditens
#     print(f'O valor medio da compra é R${media:.2f}')
# except:
#     print('Ocorreu um erro')

# #segundo nivel de tratamento
# print('\nValor medio de compras')
# try:
#     valorcompra = float(input('Entre com o valor da compra: '))
#     qtditens = int(input('Entre com a quantidade de itens: '))
#     media = valorcompra/qtditens
#     print(f'O valor medio da compra é R${media:.2f}')
# # except ValueError:
# #     print('Letras nao são permitidas')
# except ZeroDivisionError as z:
#     print(f'Quantidade não pode ser zerada: {z}')
# except Exception as e:
#     print(f'Ocorreu um erro:{e}')

#2.
#levantar exceções - situacao inicial
# print('\nValor medio de compras')
# try:
#     valorcompra = float(input('Entre com o valor da compra: '))
#     qtditens = int(input('Entre com a quantidade de itens: '))
#     if valorcompra < 0 or qtditens < 0:
#         print(f'Quantidade ou valor negativos')
#     else:
#         media = valorcompra/qtditens
#         print(f'O valor medio da compra é R${media:.2f}')
# except ValueError:
#     print('Letras nao são permitidas')
# except ZeroDivisionError as z:
#     print(f'Quantidade não pode ser zerada: {z}')
# except Exception as e:
#     print(f'Ocorreu um erro:{e}')

# #levantar exceções
# print('\nValor medio de compras')
# try:
#     valorcompra = float(input('Entre com o valor da compra: '))
#     qtditens = int(input('Entre com a quantidade de itens: '))
#     if valorcompra < 0 or qtditens < 0:
#         raise Exception('Quantidade ou valor negativos')
#     media = valorcompra/qtditens
#     print(f'O valor medio da compra é R${media:.2f}')
# except ValueError:
#     print('\nERRO: Letras nao são permitidas')
# except ZeroDivisionError as z:
#     print(f'\nERRO: Quantidade não pode ser zerada: {z}')
#     #raise
# except Exception as e:
#     print(f'\nERRO: Ocorreu um erro:{e}')

#3.Blocos opcionais
print('\nValor medio de compras')
try:
    valorcompra = float(input('Entre com o valor da compra: '))
    qtditens = int(input('Entre com a quantidade de itens: '))
    if valorcompra < 0 or qtditens < 0:
        raise Exception('Quantidade ou valor negativos')
    media = valorcompra/qtditens
    #print(f'O valor medio da compra é R${media:.2f}')
except ValueError:
    print('\nERRO: Letras nao são permitidas')
except ZeroDivisionError as z:
    print(f'\nERRO: Quantidade não pode ser zerada: {z}')
    #raise
except Exception as e:
    print(f'\nERRO: Ocorreu um erro:{e}')
else: #só é executado quando nao ocorre erro!
    print(f'O valor medio da compra é R${media:.2f}')
    print('---> Voce esta gastando muito')
finally: #bloco que sempre é executado. O uso é para fechar um arquivo, encerrar uma conexao com banco de dados
    print('Obrigada por usar nosso programa')