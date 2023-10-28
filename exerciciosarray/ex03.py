toatldealunos=int(input("Digite a quantidade de alunos:"))
listadealunos=[]
for x in range (toatldealunos):
    nome=input("Digite o nome do aluno:")
    listadealunos.append(nome)
for i in range (toatldealunos):
    print("Aluno",i+1,":",listadealunos[i])
resp=input("Qual o nome do aluno que deseja pesquisar?")
if resp in listadealunos:
    for y in range (toatldealunos):
        if listadealunos[y]==resp:
            print("Aluno",y+1,":",listadealunos[y])
else:
    print("Aluno não encontrado na lista.")