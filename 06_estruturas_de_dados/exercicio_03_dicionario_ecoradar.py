"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
membros = [
    {"matricula": "1" , "cargo": "coordenador"},
    {"matricula": "2" , "cargo": "vice-coordenador"},
    {"matricula": "3" , "cargo": "secretario"}

]
entrada =  input("Digite a matrícula do membro da equipe EcoRadar: ")
for membros in membros :
    if entrada == membros ["matricula"]:
        print("o cargo do membro de numeração e : ", membros["cargo"])