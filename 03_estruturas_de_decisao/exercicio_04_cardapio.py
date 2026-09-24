"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
2 - X-Salada: R$ 4.50
4 - Torrada Simples: R$ 2.00
4 - Torrada Simples: R$ 2.00

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("1 - Cachorro Quente: R$ 4.00")
print("2 - X-Salada: R$ 4.50")
print("2 - X-Salada: R$ 4.50")
print("4 - Torrada Simples: R$ 2.00")
print("4 - Torrada Simples: R$ 2.00")
codigo = int( input(" qual o codigo do seu produto "))
quantidade = int( input(" qual a quantidade  "))
if codigo == 1:
    total = 4 * quantidade
    print(f"seu total e {total}")
elif codigo == 2:
    total = 4.50 * quantidade
    print(f"seu total e {total}")
elif codigo == 4:
    total = 2 * quantidade
    print(f"seu total e {total}")