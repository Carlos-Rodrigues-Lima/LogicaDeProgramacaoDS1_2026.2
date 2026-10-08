"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x = int(input(" digite o valor de x "))
y = int(input(" digite o valor de y "))
if x < y :
    for sequencia in range (x + 1, y) :
        if sequencia % 5 == 2 or sequencia % 5 == 3 :
            print (f" seus numeros com resto de divisão 2 e 3 sao")
            print(f"{sequencia}")
elif x == y:
    print(" digite valores diferentes")
elif y > x :
    for sequencia in (y + 1, x) :
        if sequencia % 5 == 2 or sequencia % 5 == 3 :
            print (f" seus numeros com resto de divisão 2 e 3 sao")
            print(f"{sequencia}")
else:
    print("Não a nenhum numero para essa cobinação")