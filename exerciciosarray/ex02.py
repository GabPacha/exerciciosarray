totaldealunos=int(input("Digite a quantidade de alunos:"))
listadealunos=[]
for x in range (totaldealunos):
    nome=input("Digite o nome do aluno:")
    listadealunos.append(nome)
for i in range (totaldealunos):
    print("Aluno",i+1,":",listadealunos[i])