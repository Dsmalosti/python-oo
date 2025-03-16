from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

P1 = Produto('maça', 2)
P2 = Produto('camisa', 15)
P3 = Produto('abacaxi', 3)
P4 = Produto('tenis', 200)
P5 = Produto('chocolate', 5)

carrinho.inserir_produto(P1)
carrinho.inserir_produto(P2)
carrinho.inserir_produto(P3)
carrinho.inserir_produto(P4)
carrinho.inserir_produto(P5)
carrinho.inserir_produto(P1)
carrinho.inserir_produto(P3)

carrinho.lista_produto()
print(carrinho.soma_produto())