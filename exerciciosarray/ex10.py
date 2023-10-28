n=int(input("Digite o número correspondete ao tamanho das listas:"))
vetora=[]
vetorb=[]
vetorsoma=[]
for x in range(n):
    numeroa=float(input("Digite um número para adicionar ao Vetor A:"))
    vetora.append(numeroa)
for g in range(n):
    numerob=float(input("Digite um número para adicionar ao Vetor B:"))
    vetorb.append(numerob)
for y in range(n):
    soma=vetora[y]+vetorb[y]
    vetorsoma.append(soma)
print(vetorsoma)