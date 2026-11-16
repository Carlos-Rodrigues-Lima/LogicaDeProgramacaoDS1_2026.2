"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
monitores = ["Ryan Mesquita Damasceno"]
monitores.append("João Silva")
monitores.append("bruna soares")
monitores[0] = "Ryan M. Damasceno vilvu da silva ramos"
print("os classificados para monitores são: ")
print(monitores)