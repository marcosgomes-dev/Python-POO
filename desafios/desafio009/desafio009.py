from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0
        self.sal_min = 1612.00
        self.inss = 0.075

    def analisar_salario(self):
        analise = self.salario / self.sal_min
        return f"{analise:.1f} salários mínimos"

    @abstractmethod
    def calc_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario_bruto = self.valor_hora * self.horas_trab
        self.salario = self.salario_bruto - self.salario_bruto * self.inss
        return f"R${self.salario:.2f}"

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.salario_bruto - self.salario_bruto * self.inss
        return f"R${self.salario:.2f}"


H = Horista("Marcos", 12, 200)
print(f"\nO funcionário {H.nome} ({type(H).__name__}) trabalhando {H.horas_trab}h receberá {H.calc_sal()}")
print(f"o que corresponde a {H.analisar_salario()}")

M = Mensalista("Rafaela", 9500)
print(f"\nO funcionário {M.nome} ({type(M).__name__}) receberá {M.calc_sal()}")
print(f"o que corresponde a {M.analisar_salario()}")
