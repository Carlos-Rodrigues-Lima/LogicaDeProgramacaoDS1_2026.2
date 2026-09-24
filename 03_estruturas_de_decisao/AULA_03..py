## 🛠️ Prática do Aluno (Mão na Massa)
#Construa um menu interativo para o sistema da biblioteca da escola:
#* Opção 1: Consultar livro
#* Opção 2: realiza empretimos
#* Opção 3: Devolver livro
#* Qualquer outra opção: Mensagem de "Opção Não Encontrada".

opcoes = int(input("qoue vc dejeseja  Opção 1: Consultar livro ,Opção 2: realiza empretimos,Opção 3: Devolver livro"))
if opcoes == 1:
    print ("seu livros sao ")
elif opcoes == 2:
    print("opçoes de empretimo")
elif opcoes == 3:
    print (" devolvar seu livro aqui ")
else:
    print("opção indisponivel")