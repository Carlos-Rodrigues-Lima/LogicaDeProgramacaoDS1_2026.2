"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade = int(input("qual sua idade "))
if idade < 12:
    print(" voce obtever 50 % de desconto vc pagara R$50 ")
elif idade >= 60 :
    print(" voce obtever 100 % de desconto vc nao pagara nada")
else:
    print(" voce pagara o preço cheio de  R100 ")