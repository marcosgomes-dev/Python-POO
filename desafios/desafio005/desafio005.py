# Crie uma classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos.
# Crie também um método que permita mostrar a ficha desse gamer.
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        lista_favoritos = "\n".join(self.favoritos)
        return f"\nJogador <{self.nick}>\n\nNome real: {self.nome}\n\nJogos favoritos:\n\n{lista_favoritos}"


j1 = Gamer("Marcos Vinicius Gomes da Costa", "Rorvat")
j1.add_favoritos("Red Dead Redemption")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
print(j1.ficha())
