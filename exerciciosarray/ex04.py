notas = []
soma = 0
for x in range(5):
    nota = float(input("Digite a nota do aluno:"))
    notas.append(nota)
    soma = soma+nota
print(notas)
media=soma/5
alunosaprovados=0
for y in range(5):
    if notas[y] >= media:
        alunosaprovados=alunosaprovados+1
print("A media da turma é:", media,", e a quantidade de alunos aprovados é:", alunosaprovados)