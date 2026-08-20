#estado inicial
# catalogo = [
#     ["Camiseta Azul", 59.90, 120]
# ]

# #aonde eu quero chegar
# catalogo = [
# ["Camiseta Azul", 59.90, 120],
# ["Tênis Runner", 199.90, 40],
# ]
NOME = 0
PRECO = 1
ESTOQUE = 2
def cadastrar_produto(catalogo:list[list[object]], nome:str, preco:float, estoque:int) -> list[list[object]]:
    """
    Cadastra um novo produto ao catalogo
    :param catalogo: matriz (lista de lista) com os produtos do e-commerce
    :param nome: nome do produto
    :param preco: preço unitário do produto
    :param estoque: quantidade disponível em estoque
    :return: catalogo atualizado com novo produto
    """
    produto:list[object] = [nome, preco, estoque]
    catalogo.append(produto)
    return (catalogo)

#testando
catalogo = [
    ["Camiseta Azul", 59.90, 120]
]
print(catalogo)
cadastrar_produto(catalogo, 'Tenis Runner', 199.90, 40)
print(catalogo)


catalogo_tech = []
print(catalogo_tech)
cadastrar_produto(catalogo_tech, nome="iphone", preco=8.900, estoque=100)
print(catalogo_tech)

def exibir_catalogo(catalogo:list[list[object]]) -> None:
    """
    Exibe todos os produtos do catalogo
    :param catalogo: matriz (lista de lista) com os produtos do e-commerce
    :return: nao ha retorno porque imprime dentro da funcao
    """
    for produto in catalogo:
        print(f'{produto[NOME]} - R$ {produto[PRECO]:.2f} (estoque: {produto[ESTOQUE]})')

exibir_catalogo(catalogo)

