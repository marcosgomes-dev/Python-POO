from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(4)
        self.lados = lados

    def perimetro(self):
        return self.lados * 4

    def area(self):
        return self.lados ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2


q = Quadrado(20)
print(f"Um quadrado com lado {q.lados} tem perímetro de {q.perimetro()} cm")
print(f"Um quadrado com lado {q.lados} tem área de {q.area()} cm²")

c = Circulo(12)
print(f"Um círculo com raio {c.raio} tem perímetro de {c.perimetro():.2f} cm")
print(f"Um círculo com raio {c.raio} tem área de {c.area():.2f} cm²")
