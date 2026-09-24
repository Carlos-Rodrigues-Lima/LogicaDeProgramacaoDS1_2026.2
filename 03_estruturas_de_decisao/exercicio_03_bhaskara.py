"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
a = float(input(" digite os valores de a "))
b = float(input(" digite os valores de b "))
c = float(input(" digite os valores de c "))
delta = (b ** 2) - (4 * a * c)
if a == 0 or delta <0 :
    print ("impossivel de calcular")
else:
    raiz_de_delta = math.sqrt(delta)
    raiz01 = (-b + raiz_de_delta ) / (2*a)
    raaiz02 =  (-b - raiz_de_delta ) / (2*a)
    print(f"suas raizes são R1 = {raiz01:.5f} R2 = {raaiz02:.5f}")