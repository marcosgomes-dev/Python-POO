# Python - POO

Repositório de estudos de **Programação Orientada a Objetos (POO)** em Python, organizado em exercícios e desafios progressivos. Cada pasta aprofunda um conceito diferente de POO, desde a declaração básica de classes até o uso de classes abstratas, herança e polimorfismo.

## Objetivo

Praticar e consolidar os fundamentos de POO em Python, incluindo:

- Declaração de classes e objetos
- Atributos e métodos de instância
- Método construtor (`__init__`) parametrizado
- Dunder Methods (`__str__`, `__dict__`, `__class__`)
- Herança simples com `super()`
- Classes Abstratas com `ABC` e `abstractmethod`
- Polimorfismo
- Modularização em múltiplos arquivos
- Uso da biblioteca `rich` para saída estilizada no terminal

## Estrutura do projeto

```text
Python - POO/
├── desafios/
│   ├── desafio001/    # Classe Funcionario com apresentação
│   ├── desafio002/    # Classe Produto com etiqueta formatada
│   ├── desafio003/    # Classe Churrasco com cálculo de kg e preço
│   ├── desafio004/    # Classe Livro com navegação de páginas
│   ├── desafio005/    # Classe Gamer com lista de favoritos
│   ├── desafio006/    # Classes abstratas: Polígono, Quadrado, Círculo
│   ├── desafio007/    # Template Method: BebidaQuente, Café, Chá, Leite
│   ├── desafio008/    # Classes abstratas: Transporte, Moto, Caminhão, Drone
│   ├── desafio009/    # Herça + abstrato: Funcionário, Horista, Mensalista
│   └── desafio010/    # Polimorfismo + rich: Personagem, Guerreiro, Mago
├── exercicios/
│   ├── ex001/         # Introdução: classe Gafanhoto, atributos e métodos
│   ├── ex002/         # Construtores parametrizados e Dunder Methods
│   ├── ex003/         # Classe ContaBancária com saque e depósito
│   ├── ex004/         # Herança: Pessoa, Aluno, Professor, Funcionário (arquivo único)
│   ├── ex005/         # Herança: separando classes em arquivo externo
│   ├── ex006/         # Herança: modularização total (um arquivo por classe)
│   └── ex007/         # Classe abstrata Pessoa com método estudar() polimórfico
└── riich/
    └── rich001.py     # Primeiro teste com a biblioteca rich
```

---

## Exercícios

### ex001 — Introdução à POO

**Conceitos:** Declaração de classe, atributos de instância, métodos, criação de objetos.

Cria a classe `Gafanhoto` com atributos `nome` e `idade` e métodos `aniversario()` e `mensagem()`. Os objetos são instanciados sem parâmetros e os atributos são definidos diretamente após a criação.

```python
g1 = Gafanhoto()
g1.nome = "Marcos"
g1.idade = 29
g1.aniversario()
print(g1.mensagem())  # Marcos é um gafanhoto e tem 30 anos de idade
```

---

### ex002 — Construtores parametrizados e Dunder Methods

**Conceitos:** `__init__` com parâmetros padrão, `__str__`, `__dict__`, `__class__`, `__getstate__`.

Evolução do ex001: o construtor agora aceita `nome` e `idade` diretamente. Implementa `__str__` para impressão amigável e explora outros Dunder Methods para inspecionar o objeto.

```python
g1 = Gafanhoto("Marcos", 29)
print(g1)           # usa __str__
print(g1.__dict__)  # exibe atributos como dicionário
print(g1.__class__) # exibe a classe do objeto
```

---

### ex003 — Conta Bancária

**Conceitos:** Classe com lógica de negócio, validação de saldo, `__str__`.

Modela uma conta bancária com métodos `depositar()` e `sacar()`. O saque é recusado com mensagem de erro se o saldo for insuficiente.

```python
c1 = ContaBancaria(100, "Marcos", 3000)
c1.depositar(500)   # saldo: 3500
c1.sacar(3600)      # SALDO INSUFICIENTE
print(c1)           # exibe saldo atual
```

---

### ex004 — Herança (arquivo único)

**Conceitos:** Herança simples, `super()`, polimorfismo de métodos, biblioteca `rich`.

Cria a hierarquia `Pessoa` → `Aluno`, `Professor`, `Funcionario`. Cada subclasse herda `fazer_aniversario()` e adiciona seus próprios métodos e atributos. Usa `inspect()` da biblioteca `rich` para visualizar objetos.

---

### ex005 — Herança (classes em arquivo externo)

**Conceitos:** Importação de módulos, separação de responsabilidades.

Refatoração do ex004: as classes `Aluno`, `Professor` e `Funcionario` são movidas para `classes.py`, e o `main.py` importa e usa apenas essas classes.

```text
ex005/
├── classes.py   # Pessoa, Aluno, Professor, Funcionario
└── main.py      # Instancia e executa
```

---

### ex006 — Herança (modularização total)

**Conceitos:** Um arquivo por classe, padrão de projeto modular, ponto de entrada com `__main__.py`.

Evolução do ex005: cada classe ganha seu próprio arquivo (`pessoa.py`, `aluno.py`, `professor.py`, `funcionario.py`). O módulo é executado com `python -m ex006`.

```text
ex006/
├── pessoa.py
├── aluno.py
├── professor.py
├── funcionario.py
└── __main__.py
```

---

### ex007 — Classe Abstrata com Polimorfismo

**Conceitos:** `ABC`, `abstractmethod`, polimorfismo via método abstrato `estudar()`.

`Pessoa` se torna uma classe abstrata com o método obrigatório `estudar()`. Cada subclasse implementa esse método de forma diferente, demonstrando polimorfismo.

```python
a1.estudar()  # "Marcos está estudando Sistemas de Informação na turma T0021"
p1.estudar()  # "Daniel é especialista em Banco de Dados no nível Doutorado"
f1.estudar()  # "Cláudia se especializa para a área de Secretaria"
```

---

## Desafios

### Desafio 001 — Funcionário

**Conceitos:** Classe básica, `input()`, `split()`, f-string.

Cria a classe `Funcionario` com atributos `nome`, `setor` e `cargo`. Leitura dos dados via `input()` com `split(",")` e exibe apresentação formatada.

---

### Desafio 002 — Produto

**Conceitos:** Classe básica, método de formatação, `input()`.

Cria a classe `Produto` com atributos `nome` e `preco` e o método `etiqueta()` que formata e exibe as informações do produto.

---

### Desafio 003 — Churrasco

**Conceitos:** Lógica de negócio, métodos encadeados, formatação de float.

Calcula automaticamente a quantidade de carne (0.4kg/pessoa a R$82,40/kg) e o custo total para um churrasco com N convidados.

---

### Desafio 004 — Livro

**Conceitos:** Estado interno do objeto, método com validação de limites.

Simula a passagem de páginas de um livro. O método `avancar_paginas()` valida se o avanço é possível, detecta o fim do livro e informa o restante de páginas se o avanço exceder o limite.

---

### Desafio 005 — Gamer

**Conceitos:** Atributo do tipo lista, método de adição, formatação de ficha.

Cria a classe `Gamer` com nome, nick e lista de jogos favoritos. O método `add_favoritos()` adiciona jogos dinamicamente e `ficha()` exibe o perfil completo do gamer.

---

### Desafio 006 — Polígonos Abstratos

**Conceitos:** `ABC`, `abstractmethod`, herança, cálculos geométricos, biblioteca `math`.

Classe abstrata `Poligono` define os métodos `perimetro()` e `area()` como obrigatórios. `Quadrado` e `Circulo` implementam cada um à sua maneira.

```python
q = Quadrado(20)
# perímetro: 80 cm | área: 400 cm²

c = Circulo(12)
# perímetro: 75.40 cm | área: 452.39 cm²
```

---

### Desafio 007 — Bebidas Quentes (Template Method)

**Conceitos:** `ABC`, Template Method Pattern, método concreto na classe base.

A classe abstrata `BebidaQuente` define o fluxo de preparo em `preparar()` (ferver → misturar → servir). `Cafe`, `Cha` e `Leite` implementam apenas `misturar()` e `servir()`, personalizando o preparo de cada bebida.

---

### Desafio 008 — Cálculo de Frete

**Conceitos:** `ABC`, validação por fator e distância, polimorfismo.

Classe abstrata `Transporte` define `calcular_frete()`. Cada modal tem sua própria regra:
- **Moto:** R$0,50/km (sem restrição)
- **Caminhão:** R$1,20/km (mínimo 50km)
- **Drone:** R$9,50/km (máximo 10km)

---

### Desafio 009 — Cálculo de Salário

**Conceitos:** `ABC`, desconto de INSS (7,5%), comparação com salário mínimo.

Classe abstrata `Funcionario` define `calc_sal()`. `Horista` calcula pelo valor/hora × horas trabalhadas. `Mensalista` calcula pelo salário bruto. Ambos deduzem INSS e informam quantos salários mínimos o líquido representa.

---

### Desafio 010 — Batalha com Personagens

**Conceitos:** `ABC`, polimorfismo, `random`, biblioteca `rich` para saída colorida.

Classe abstrata `Personagem` define `atacar()`, `receber_dano()` e o abstrato `curar()`. `Guerreiro` e `Mago` são subclasses com golpes e curas personalizadas. Os ataques e danos são aleatórios, e a saída é colorida com `rich`.

---

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/marcosgomes-dev/Estudos-de-Python.git
   cd Estudos-de-Python
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install rich
   ```
4. Execute um exercício ou desafio:
   ```bash
   python exercicios/ex001/ex001.py
   python desafios/desafio010/desafio010.py
   ```
5. Para o ex006 (módulo modularizado):
   ```bash
   python -m exercicios/ex006
   ```

## Tecnologias

- **Python 3.x**
- **rich** — saída estilizada e colorida no terminal
- **abc** — módulo nativo para classes abstratas

## Autor

Estudos de POO desenvolvidos durante a graduação em Sistemas de Informação na UFF.
