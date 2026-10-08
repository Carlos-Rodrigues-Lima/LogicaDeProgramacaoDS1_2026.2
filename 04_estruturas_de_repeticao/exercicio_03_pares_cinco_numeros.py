"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
a = 0
for i  in range(5):
    num = int(input(' digite seu numero '))
    if num % 2 == 0 :
        a += 1
print(f" a quantidade de numeros pares digitados foram { a }")


