class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Meu nome é {self.nome}, sou do setor de {self.setor} e atuo no cargo de {self.cargo}"

nome, setor, cargo = input("Me informe seu nome, setor e cargo: ").split(",") 

pessoa = Funcionario(nome, setor, cargo )

print(pessoa.apresentacao())
