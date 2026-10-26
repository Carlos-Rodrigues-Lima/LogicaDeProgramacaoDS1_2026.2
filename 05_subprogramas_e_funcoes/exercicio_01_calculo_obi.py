"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total (fase1, fase2, fase3):
    media = (fase1 + fase2 + fase3)
    return media
fase1 = int(input(" digie sua primeira nota : "))
fase2 = int(input(" digie sua segunda nota : "))
fase3 = int(input(" digie sua terceira nota : "))

media_final = calcular_pontuacao_total(fase1,fase2,fase3)

print(f"sua media final e igual a : {media_final}")