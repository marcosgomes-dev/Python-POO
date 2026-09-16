# Declaracao de Classe

class Gafanhoto:
    def __init__(self):  # Método construtor
        # Atributos de instância
        self.nome = " "
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um gafanhoto e tem {self.idade} anos de idade"


# Declaracao de objetos
g1 = Gafanhoto()
g1.nome = "Marcos"
g1.idade = 29
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Bruno"
g2.idade = 27
print(g2.mensagem())
