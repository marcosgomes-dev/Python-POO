from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


def main():
    a1 = Aluno("Marcos", 29, "Sistemas de Informação", "T0021")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Daniel", 42, "Banco de Dados", "Doutor")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Cláudia", 55, "Secretária", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == "__main__":
    main()
