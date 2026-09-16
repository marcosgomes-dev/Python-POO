class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"\nConta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}\n")

    def __str__(self):
        return f"\nA conta {self.id} de {self.titular} tem {self.saldo:.2f} reais de saldo\n"

    def depositar(self, valor):
        self.saldo += valor
        print(f"\nDepósito de R${valor:.2f} autorizado")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\nSaque de R${valor:.2f} não autorizado. SALDO INSUFICIENTE!")
        else:
            self.saldo -= valor
            print(f"\nSaque de R${valor:.2f} autorizado")


c1 = ContaBancaria(100, "Marcos", 3000)
c1.depositar(500)
c1.sacar(3600)
print(c1)
