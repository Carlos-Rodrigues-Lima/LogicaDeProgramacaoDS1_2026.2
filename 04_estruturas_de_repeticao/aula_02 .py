# TODO: Desenvolva o acumulador com parada no 0
# Escreva a estrutura de repetição while
res_final = 0
while True:
    numero = int(input(" digite seu numero "))
    if numero == 0 :
        break
    res_final+=numero
print (f" seu resultado final e {res_final}")