class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.preco = valor

    def etiqueta(self):
        return f"\nProduto\n\n{self.nome}\n\n{self.preco}"

nome, valor = input("Digite o nome do produto e o seu preco: ").split(",")

produto = Produto(nome, valor)

print(produto.etiqueta())
