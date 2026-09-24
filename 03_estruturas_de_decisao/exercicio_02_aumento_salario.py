"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario =  int(input("quanto voce ganhar "))
if salario < 400:
    bonus=salario * 0.15
    novo = salario + bonus
    print(f"seu novo salario e {novo} ")
elif 400> salario <800:
    bonus=salario * 0.12
    novo = salario + bonus
    print(f"seu novo salario e {novo} ")
elif 800 > salario < 1200:
    bonus=salario * 0.10
    novo = salario + bonus
    print(f"seu novo salario e {novo} ")
elif salario > 2000:
    bonus=salario * 0.15
    novo = salario + bonus
    print(f"seu novo salario e {novo} ")