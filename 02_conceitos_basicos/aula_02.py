# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor = float(input("qual o valor da conta "))
amigos = int(input("quantos pessoas a na mesa ? "))
valor_individual = valor/amigos
print( f" cada um davem pagar , {valor_individual:.2f}")