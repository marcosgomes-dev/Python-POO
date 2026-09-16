from desafio010 import *
from rich import inspect

def main():
    p1 = Guerreiro("Pikachu", 4000)
    p2 = Mago("Rorvat", 2000)

    inspect(p1, methods='True')
    p1.atacar(p2, 200)
    p2.atacar(p2, 100)

    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()
