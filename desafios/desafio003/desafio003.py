# Consumo padrão: 400g por pessoa
# Preço: R$82,40/Kg
class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        self.kiloTotal = 0
        self.precoTotal = 0

    def contaKilo(self):
        gramas = self.quantidade * 400
        self.kiloTotal = gramas/1000
        return self.kiloTotal

    def contaPreco(self):
        self.precoTotal = self.kiloTotal * 82.40
        return self.precoTotal

    def analisar(self):
        self.contaKilo()
        self.contaPreco()
        print(self.titulo)
        print(f"\nAnalisando {self.titulo} com {self.quantidade} convidados\nCada participante comerá 0.4Kg e cada Kg custa R$82.40\nRecomendo comprar {self.kiloTotal:.2f}Kg de carne\nO custo total será de R${self.precoTotal:.2f}\nCada pessoa pagará R$32.96 para participar")


c1 = Churrasco("Churras dos amigos", 100)
c1.analisar()
