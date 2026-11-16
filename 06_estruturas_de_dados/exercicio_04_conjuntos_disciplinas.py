"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
from calendar import different_locale


alulnos_web = {"Carlos", "João", "Maria", "Ana" ,"lv" ,"vivian" , 'sarvioBonitinho'}
alunos_banco = {"Carlos", "Maria", "manel", "sarvioBonitinho", "coisa_1", "coisa_2"}

escolha = int(input(""" 
digite 1 para ver a Interseção (&)
digite 2 para ver a Diferença (-) 
"""))
if escolha == 1:
    intersecao = alulnos_web & alunos_banco
    print(f" a interseção e igual a {intersecao}")

elif escolha == 2 :
    diferenca = alunos_banco - alulnos_web
    print(f"a diferença e igual a{diferenca}")

else:
    print("por favor digite 1 ou 2")