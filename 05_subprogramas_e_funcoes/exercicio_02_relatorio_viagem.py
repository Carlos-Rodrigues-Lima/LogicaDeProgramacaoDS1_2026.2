"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo_1 = (distancia_km / consumo_kml) * preco_combustivel
    return custo_1
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo_2 = (qtd_pessoas / diaria_alimentacao) * dias
    return custo_2
distancia = int(input(' qual a disntacia da viagen  '))
consumo = int(input(' qual consumo da sua marquina por litros da viagen : '))
preco_do_gas= float(input(' qual p preço atual da gasolina :  '))
pessoas = int(input(' qual a quantidades de pessoas na viagen  '))
diaria_ali = int(input(' qual a quantidades que cada  pessoas vai consumir na viagen '))
dia = int(input(' qual a quantidades de dias da viagen '))
custo_1 = calcular_custo_transporte(distancia, consumo, preco_do_gas)
custo_2 = calcular_custo_alimentacao(pessoas, dia, diaria_ali)
print(f' o custo total da viagen é de : {custo_1 + custo_2}  ')