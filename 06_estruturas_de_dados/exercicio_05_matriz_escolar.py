"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos = [
    ['carlos', 8.6 , 9.6],
    ['lv' , 0.8 ,0.5],
    ['vivian', 10.0 , 9.5]  
]
print("\nlista das medias ")
for linha in alunos:
    nome = linha[0]
    nota_1 = linha[1]
    nota_2 = linha[2]
    media = (nota_1 + nota_2 ) / 2
    print(f" aluno: {nome} media do alunos { media}")