vetor=[]
numerospares=[]
soma=0
acimadamedia=0
for x in range(30):
    numero=float(input("Digite um número:"))
    vetor.append(numero)
numeromenor=vetor[0]
numeromaior=vetor[0]
for i in range(30):
    if vetor[i] % 2 == 0:
        numerospares.append(vetor[i])
    if vetor[i] > numeromaior:
        numeromaior=vetor[i]
    if vetor[i] < numeromenor:
        numeromenor = vetor[i]
    soma=soma+vetor[i]
media=soma/30
for g in range(30):
    if vetor[g] > media:
        acimadamedia=acimadamedia+1
print("Os números pares são:",numerospares)
print(f"O número maior é {numeromaior},e o número menor é {numeromenor}.A quantidade de alunos acima da média é {acimadamedia}")