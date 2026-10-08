"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Inicialização dos contadores e acumuladores
a = 0
b = 0
m = 0
for i in range(6):
    valor = int(input( "digite seu valor " ))
    if valor > 0:
        a += 1
        b += valor
m = b / a
print(f"{a} valores positivos")
print(f"{m:.1f}")