# TODO: Defina a função calcular_media e teste-a abaixo
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media
nota1 = int(input(" digie sua primeira nota : "))
nota2 = int(input(" digie sua segunda nota : "))
nota3 = int(input(" digie sua terceira nota : "))

media_final = calcular_media(nota1,nota2,nota3)

print(f"sua media final e igual a : {media_final}")