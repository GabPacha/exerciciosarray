listadenome=[]
listadesenha=[]
for x in range(5):
    nome=input("Digite seu nome:")
    listadenome.append(nome)
    senha=input("Digite sua senha:")
    listadesenha.append(senha)
for y in range(5):
    print("Aluno",y+1,". Nome:",listadenome[y],".Senha:",listadesenha[y])
