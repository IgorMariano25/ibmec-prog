"""
Tipos de dados primitivos

- int
- float
- string
- bool

Operações

- Operações matemáticas

  - +
  - -
  - *
  - /
  - **
  - //
  - %

- Operações lógicas

  - Operações de comparação

    - >
    - <
    - >=
    - <=
    - ==
    - !=

  - Operações booleanas

    - and
    - or
    - not

Funções

- Dois tipos de parâmetros:

  - posicionais
  - chave

- "\" -> escape char
- "\n" -> quebra de linha
- "\t" -> "tab"
- "\"" -> aspas duplas
- "\\" -> uma contrabarra
"""

"""
nome = "Victor"

print("Olá, mundo!")
print("Olá,", nome, "!", end=" ; ")
print("Olá, ", nome, "!", sep="")

nome = input("Informe o nome: ")

print("Olá, ", nome, "!", sep="")

numero = int(input("Informe um número: "))
print("O número informado foi", numero)
outro_numero = int(input("Informe outro número: "))
print(
  "A soma dos dois números é",
  numero + outro_numero
)

nome = input("Informe o nome: ")

print("Olá, ", nome, "!", sep="")

numero = int(input("Informe um número: "))
print("O número informado foi", numero)
outro_numero = int(input("Informe outro número: "))
print(
  "A soma dos dois números é",
  numero + outro_numero
)
"""

# modularização
# encapsulamento

def linha(marc="-", larg=40):
  print(marc * larg)

def cabecalho(titulo, marc="-", larg=40):
  linha(marc, larg)
  print(titulo)
  linha(marc, larg)

def teste_cabecalho():
  cabecalho("Exemplo", marc="=")
  cabecalho("Outro Exemplo", marc="+")
  cabecalho("Mais um exemplo", larg=35)

# teste_cabecalho()

def media(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

def calcula_media():
  nota1 = float(input("Informe a 1a nota: "))
  nota2 = float(input("Informe a 2a nota: "))
  nota3 = float(input("Informe a 3a nota: "))

  print(
    "A média é:",
    round(media(nota1, nota2, nota3), 2)
  )

# calcula_media()

def m_para_cm(comp_m):
  print(comp_m * 100)

m_para_cm(25)