"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    desconto = preco_base * taxa_desc
    taxa_de_imp = taxa_imp * preco_base
    preco_final = preco_base - desconto + taxa_de_imp 
    return preco_final
def exibir_relatorio_item(numero_item, preco_final):
    print(f"o valor do item {numero_item} e igual a R$ {preco_final} ")
preco_base = float(input("digite o preco base do item: "))
taxa_desc = float(input("digite a taxa de desconto: "))
taxa_imp = float(input("digite a taxa de imposto: "))
numero_item = int(input("digite o número do item: "))
preco_final = calcular_preco_final(preco_base, taxa_desc, taxa_imp)
exibir_relatorio_item(numero_item, preco_final)