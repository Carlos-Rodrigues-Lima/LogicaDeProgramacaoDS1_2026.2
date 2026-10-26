"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
desconto = lambda valor: valor - (valor * 0.15)
n = float(input("qual o valor do produto "))
print(" O valor com desconto é: R$ ", desconto(n))