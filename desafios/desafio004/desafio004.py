# Crie uma classe Livro que simula a passagem de páginas, verificando se o leitor chegou ao fim.
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginaAtual = 1
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total.\nVocê agora está na página {self.paginaAtual}")

    def avancar_paginas(self, avanco):
        nova_pagina = self.paginaAtual + avanco
        if nova_pagina < self.paginas:
            self.paginaAtual = nova_pagina
            return f"Você avançou {avanco} páginas, e agora está na página {self.paginaAtual}"
        elif nova_pagina == self.paginas:
            self.paginaAtual = nova_pagina
            return f"Parabéns!! Você avançou {avanco} páginas, e acabou de terminar o seu livro"
        else:
            restante = self.paginas - self.paginaAtual
            return f"Você não pode avançar {avanco} páginas, restam apenas {restante} páginas no livro {self.titulo}"


l1 = Livro("Harry potter e a Pedra Filosofal", 264)
print(l1.avancar_paginas(250))
