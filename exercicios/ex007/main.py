from rich import print, inspect
from classes import Aluno, Professor, Funcionario


def main():
    a1 = Aluno("Marcos", 29, "Sistemas de Informação", "T0021")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Daniel", 42, "Banco de Dados", "Doutorado")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Cláudia", 55, "Secretária", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == "__main__":
    main()
