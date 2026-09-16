from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calcular_frete(self):
        self.frete = self.fator * self.distancia
        return f"R${self.frete:.2f}"

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calcular_frete(self):
        if self.distancia >= 50:
            self.frete = self.fator * self.distancia
            return f"R${self.frete:.2f}"
        else:
            return "Distância não permitida, somente a partir de 50KM"

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calcular_frete(self):
        if self.distancia <= 10:
            self.frete = self.fator * self.distancia
            return f"R${self.frete:.2f}"
        else:
            return "Distância não permitida, somente até 10KM"


dist = 7
entrega = Drone(dist)
print(f"\nFrete de {type(entrega).__name__} em {dist}KM = {entrega.calcular_frete()}")
