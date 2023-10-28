vetora=[]
multiplicacao=[]
for a in range (11):
    numero=float(input("Digite um número:"))
    vetora.append(numero)
x=float(input("Digite um número para fazer a multiplicação:"))
for g in range (11):
    resultado=vetora[g]*x
    multiplicacao.append(resultado)
print(multiplicacao)