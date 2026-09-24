## 🛠️ Prática do Aluno (Mão na Massa)
#Declare variáveis para representar:
#* `media_aluno` (nota de 0 a 10)
#* `frequencia_percentual` (frequência de 0 a 100)

#Crie uma expressão lógica que verifique se o aluno foi aprovado (critério da escola: média maior ou igual a 6.0 **E** frequência maior ou igual a 75%).

media = int(input("qual a media do aluno"))
frequencia_percentual = int(input("qual a frequencia do aluno"))
aprovador_nota = (media>=6) and (frequencia_percentual >= 75) 
print (" o alunor estar aprovado ?", aprovador_nota)
