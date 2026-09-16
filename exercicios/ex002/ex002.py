# Declaracao de Classe com construtores parametrizados e Dunder Methods

class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use: variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome="", idade=0):  # Método construtor parametrizado
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):  # Dunder Method: representacao textual
        return f"{self.nome} é um gafanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# Declaracao de objetos
g1 = Gafanhoto("Marcos", 29)
g1.aniversario()
print(g1)              # usa __str__
print(g1.__dict__)     # Atributos da instância
print(g1.__getstate__())
print(g1.__class__)    # Diz qual a classe do objeto
