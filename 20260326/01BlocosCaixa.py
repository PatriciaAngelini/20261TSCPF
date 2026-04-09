#Luana
#exercicio 01 ler bloco
#SE bloco é par   mostrar "Caixa A"
#SENAO            mostrar "Caixa B"
#FIM

# bloco = int(input("Digite o número do bloco (1-4): "))
#
# if bloco % 2 == 0:
#     print("Seu bloco é abastecido pela caixa A")
# else:
#     print("Seu bloco é abastecido pela caixa B")
#
# #Yasmim
# bloco_morador = int(input('Em qual bloco você mora? 1-4 '))
# if bloco_morador % 2 == 0:
#   print(f'A caixa A pertence ao seu bloco {bloco_morador}')
# else:
#   print(f'A caixa B pertence ao seu bloco {bloco_morador}')
#
# #Ana Julia
# bloco = int(input("Digite o número do bloco (1 a 4): "))
#
# if bloco % 2 == 0:
#     print("Seu bloco é abastecido pela caixa A")
# else:
#     print("Seu bloco é abastecido pela caixa B")

# #Vinicius Barreto
# bloco = int(input("digite o numero do bloco: "))
# if bloco >= 1 and bloco <= 4:
#     if bloco == 1 or bloco == 3:
#         print(f"a caixa que abastece o seu bloco({bloco}) é a caixa B")
#     else:
#         print(f"a caixa que abastece o seu bloco({bloco}) é a caixa A")
#     # if bloco == 2 or bloco == 4:
#     #     print(f"a caixa que abastece o seu bloco({bloco}) é a caixa A")

#João Guilherme
bloco = int(input("numero do bloco (1 a 4): "))

if bloco < 1 or bloco > 4:
    print("invalido")
elif bloco % 2 == 0: #elif = else + if
    print("caixa A")
else:
    print("caixa B")

# #Gabrielle
#
# blococond = int(input("Em qual bloco você mora (1 a 20)? "))
# if 1 <= blococond <= 10:
#     print("O síndico responsável pelo seu bloco é o Sr. José.")
# else:
#      print("O síndico responsável pelo seu bloco é o Sr. Hamilton.")