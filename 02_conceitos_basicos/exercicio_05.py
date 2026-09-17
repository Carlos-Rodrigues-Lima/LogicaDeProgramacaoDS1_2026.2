"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("qual a primeira nota"))
nota2 = float(input("qual a segunda nota"))
nota3 = float(input("qual a terceira nota"))
nota_bruta = nota1*2+nota2*3+nota3*5
nota_final = nota_bruta/10
print(f"sua nota final e {nota_bruta}")