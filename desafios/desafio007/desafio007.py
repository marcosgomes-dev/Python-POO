from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print("\n--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()

    def ferver_agua(self):
        print("1. Fervendo a água a 100 graus celsius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo pó moído")
    def servir(self):
        print("3. Servindo em xícara pequena.\n--- Bebida Pronta ---")

class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água")
    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.\n--- Bebida Pronta ---")

class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite")
    def servir(self):
        print("3. Servindo na caneca grande, já com o café.\n--- Bebida Pronta ---")


bebida = Leite()
bebida.preparar()
