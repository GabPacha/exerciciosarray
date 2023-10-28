vetor=[]
cont=0
for x in range(30):
    numero=float(input("Digite um número:"))
    vetor.append(numero)
numero2=float(input("Digite um número para identificarmos quantas vezes ele aparece na lista:"))
for y in range(30):
    if numero2 == vetor[y]:
        cont += 1
print(cont)